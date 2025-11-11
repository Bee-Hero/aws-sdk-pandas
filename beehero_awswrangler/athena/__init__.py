"""Amazon Athena Module."""

from beehero_awswrangler.athena._executions import (  # noqa
    get_query_execution,
    stop_query_execution,
    start_query_execution,
    wait_query,
)
from beehero_awswrangler.athena._spark import create_spark_session, run_spark_calculation
from beehero_awswrangler.athena._statements import (
    create_prepared_statement,
    delete_prepared_statement,
    list_prepared_statements,
)
from beehero_awswrangler.athena._read import (
    get_query_results,
    read_sql_query,
    read_sql_table,
    unload,
)
from beehero_awswrangler.athena._utils import (
    create_athena_bucket,
    create_ctas_table,
    describe_table,
    generate_create_query,
    get_named_query_statement,
    get_query_columns_types,
    get_query_executions,
    get_work_group,
    list_query_executions,
    repair_table,
    show_create_table,
)
from beehero_awswrangler.athena._write_iceberg import to_iceberg, delete_from_iceberg_table


__all__ = [
    "read_sql_query",
    "read_sql_table",
    "create_athena_bucket",
    "describe_table",
    "get_query_columns_types",
    "get_query_execution",
    "get_query_executions",
    "get_query_results",
    "get_named_query_statement",
    "get_work_group",
    "generate_create_query",
    "list_query_executions",
    "repair_table",
    "create_spark_session",
    "run_spark_calculation",
    "create_ctas_table",
    "show_create_table",
    "start_query_execution",
    "stop_query_execution",
    "unload",
    "wait_query",
    "create_prepared_statement",
    "list_prepared_statements",
    "delete_prepared_statement",
    "to_iceberg",
    "delete_from_iceberg_table",
]
