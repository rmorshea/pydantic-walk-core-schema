from importlib.metadata import PackageNotFoundError
from importlib.metadata import version

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # nocov
    __version__ = "0.0.0"

from pydantic_walk_core_schema.walk_core_schema import walk_core_schema

__all__ = ["walk_core_schema"]
