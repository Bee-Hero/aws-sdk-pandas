"""Ray and Modin registered methods (PRIVATE)."""
# ruff: noqa: PLC0415

from beehero_awswrangler._data_types import pyarrow_types_from_pandas
from beehero_awswrangler._distributed import MemoryFormatEnum, engine, memory_format
from beehero_awswrangler._executor import _get_executor
from beehero_awswrangler._utils import (
    copy_df_shallow,
    ensure_worker_or_thread_count,
    is_pandas_frame,
    split_pandas_frame,
    table_refs_to_df,
)
from beehero_awswrangler.distributed.ray import ray_remote
from beehero_awswrangler.distributed.ray._executor import _get_ray_executor
from beehero_awswrangler.distributed.ray._utils import ensure_worker_count
from beehero_awswrangler.distributed.ray.s3._list import _list_objects_s3fs
from beehero_awswrangler.distributed.ray.s3._read_orc import _read_orc_metadata_file_distributed
from beehero_awswrangler.distributed.ray.s3._read_parquet import _read_parquet_metadata_file_distributed
from beehero_awswrangler.dynamodb._read import _read_scan
from beehero_awswrangler.dynamodb._write import _put_df, _put_items
from beehero_awswrangler.s3._copy import _copy_objects
from beehero_awswrangler.s3._delete import _delete_objects
from beehero_awswrangler.s3._describe import _describe_object
from beehero_awswrangler.s3._list import _list_objects_paginate
from beehero_awswrangler.s3._read_orc import _read_orc, _read_orc_metadata_file
from beehero_awswrangler.s3._read_parquet import _read_parquet, _read_parquet_metadata_file
from beehero_awswrangler.s3._read_text import _read_text
from beehero_awswrangler.s3._select import _select_object_content, _select_query
from beehero_awswrangler.s3._wait import _wait_object_batch
from beehero_awswrangler.s3._write_dataset import _to_buckets, _to_partitions
from beehero_awswrangler.s3._write_orc import _to_orc
from beehero_awswrangler.s3._write_parquet import _to_parquet
from beehero_awswrangler.s3._write_text import _to_text
from beehero_awswrangler.timestream._write import _write_batch, _write_df


def register_ray() -> None:
    """Register dispatched Ray and Modin (on Ray) methods."""
    for func in [
        _copy_objects,
        _describe_object,
        _delete_objects,
        _read_scan,
        _select_query,
        _select_object_content,
        _wait_object_batch,
    ]:
        # Schedule for maximum concurrency
        engine.register_func(func, ray_remote(scheduling_strategy="SPREAD")(func))

    for func in [
        _put_df,
        _put_items,
        _write_batch,
        _write_df,
    ]:
        engine.register_func(func, ray_remote()(func))

    # Register dispatch methods for Ray
    engine.register_func(_get_executor, _get_ray_executor)
    engine.register_func(_list_objects_paginate, _list_objects_s3fs)
    engine.register_func(_read_parquet_metadata_file, ray_remote()(_read_parquet_metadata_file_distributed))
    engine.register_func(_read_orc_metadata_file, ray_remote()(_read_orc_metadata_file_distributed))
    engine.register_func(ensure_worker_or_thread_count, ensure_worker_count)

    if memory_format.get() == MemoryFormatEnum.MODIN:
        from beehero_awswrangler.distributed.ray.modin._data_types import pyarrow_types_from_pandas_distributed
        from beehero_awswrangler.distributed.ray.modin._utils import (
            _arrow_refs_to_df,
            _copy_modin_df_shallow,
            _is_pandas_or_modin_frame,
            _split_modin_frame,
        )
        from beehero_awswrangler.distributed.ray.modin.s3._read_orc import _read_orc_distributed
        from beehero_awswrangler.distributed.ray.modin.s3._read_parquet import _read_parquet_distributed
        from beehero_awswrangler.distributed.ray.modin.s3._read_text import _read_text_distributed
        from beehero_awswrangler.distributed.ray.modin.s3._write_dataset import (
            _to_buckets_distributed,
            _to_partitions_distributed,
        )
        from beehero_awswrangler.distributed.ray.modin.s3._write_orc import _to_orc_distributed
        from beehero_awswrangler.distributed.ray.modin.s3._write_parquet import _to_parquet_distributed
        from beehero_awswrangler.distributed.ray.modin.s3._write_text import _to_text_distributed

        # Register dispatch methods for Modin
        engine.register_func(pyarrow_types_from_pandas, pyarrow_types_from_pandas_distributed)
        engine.register_func(_read_parquet, _read_parquet_distributed)
        engine.register_func(_read_text, _read_text_distributed)
        engine.register_func(_to_buckets, _to_buckets_distributed)
        engine.register_func(_to_parquet, _to_parquet_distributed)
        engine.register_func(_to_partitions, _to_partitions_distributed)
        engine.register_func(_to_text, _to_text_distributed)
        engine.register_func(_read_orc, _read_orc_distributed)
        engine.register_func(_to_orc, _to_orc_distributed)
        engine.register_func(copy_df_shallow, _copy_modin_df_shallow)
        engine.register_func(is_pandas_frame, _is_pandas_or_modin_frame)
        engine.register_func(split_pandas_frame, _split_modin_frame)
        engine.register_func(table_refs_to_df, _arrow_refs_to_df)
