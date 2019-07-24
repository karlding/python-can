"""Types for mypy type-checking
"""
import typing

import mypy_extensions

CanFilter = mypy_extensions.TypedDict(
    "CanFilter", {"can_id": int, "can_mask": int, "extended": bool}, total=False
)
CanFilters = typing.Collection[CanFilter]

CanData = typing.Union[bytes, bytearray]

#
Channel = typing.Union[int, str]
