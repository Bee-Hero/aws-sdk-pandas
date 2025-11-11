"""Initial Module.

Source repository: https://github.com/aws/aws-sdk-pandas
Documentation: https://aws-sdk-pandas.readthedocs.io/

"""

import logging as _logging

from beehero_awswrangler import (
    athena,
    catalog,
    chime,
    cleanrooms,
    cloudwatch,
    data_api,
    data_quality,
    dynamodb,
    emr,
    emr_serverless,
    exceptions,
    mysql,
    neptune,
    opensearch,
    oracle,
    postgresql,
    quicksight,
    redshift,
    s3,
    secretsmanager,
    sqlserver,
    sts,
    timestream,
    typing,
)
from beehero_awswrangler.__metadata__ import __description__, __license__, __title__, __version__
from beehero_awswrangler._config import config
from beehero_awswrangler._distributed import EngineEnum, MemoryFormatEnum, engine, memory_format

engine.register()

__all__ = [
    "athena",
    "catalog",
    "chime",
    "cleanrooms",
    "cloudwatch",
    "emr",
    "emr_serverless",
    "data_api",
    "data_quality",
    "dynamodb",
    "exceptions",
    "opensearch",
    "oracle",
    "quicksight",
    "s3",
    "sts",
    "redshift",
    "mysql",
    "neptune",
    "postgresql",
    "secretsmanager",
    "sqlserver",
    "config",
    "engine",
    "memory_format",
    "timestream",
    "typing",
    "__description__",
    "__license__",
    "__title__",
    "__version__",
    "EngineEnum",
    "MemoryFormatEnum",
]


_logging.getLogger("beehero_awswrangler").addHandler(_logging.NullHandler())
