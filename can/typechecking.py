"""Types for mypy type-checking
"""
import typing

import mypy_extensions

import os

import can.bit_timing

CanFilter = mypy_extensions.TypedDict(
    "CanFilter", {"can_id": int, "can_mask": int, "extended": bool}, total=False
)
CanFilters = typing.Collection[CanFilter]

CanData = typing.Union[bytes, bytearray]

#
Channel = typing.Union[int, str]

BusConfig = mypy_extensions.TypedDict(
    "BusConfig",
    {
        "interface": str,
        "channel": str,
        "bitrate": int,
        "data_bitrate": int,
        "fd": bool,
        "timing": can.bit_timing.BitTiming,
    },
    total=False,
)

Openable = typing.Union[str, "os.PathLike[typing.Any]"]
