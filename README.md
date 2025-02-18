# Pydantic Walk Core Schema

[![PyPI - Version](https://img.shields.io/pypi/v/pydantic_walk_core_schema.svg)](https://pypi.org/project/pydantic_walk_core_schema)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pydantic_walk_core_schema.svg)](https://pypi.org/project/pydantic_walk_core_schema)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A PyPI package containing a previously private, and [now removed](https://github.com/pydantic/pydantic/issues/10297#issuecomment-2653873464), function for recursively walking a Pydantic schema.

Specifically [`walk_core_schema`](https://github.com/pydantic/pydantic/blob/df05e69a8a3fb37628a0e3a33518ca0425334bc9/pydantic/_internal/_core_utils.py#L424).

I've been using this function to create [custom type adapters](https://github.com/pydantic/pydantic/issues/8279#issuecomment-2080327559) for Pydantic while waiting for [more official support](https://github.com/pydantic/pydantic/issues/10706).
