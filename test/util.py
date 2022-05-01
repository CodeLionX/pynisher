from __future__ import annotations

from typing import Type

import os
import time

from pynisher.util import memconvert


def return_none() -> None:
    """Just returns None"""
    return None


def raises_error(exception: Type[Exception] | Exception | None = None) -> None:
    """Raise `exception` or RuntimeError if None provided"""
    exception = exception if exception is not None else RuntimeError
    if isinstance(exception, Exception):
        raise exception
    else:
        raise exception("RAISED")


def get_process_id() -> int:
    """Get the id of the process running this functions"""
    return os.getpid()


def walltime_sleep(sleep: float) -> float:
    """Sleeps for `sleep` seconds"""
    time.sleep(sleep)
    return sleep


def cputime_sleep(sleep: float) -> tuple[float, int]:
    """Keeps cpu busy for `sleep` seconds"""
    start = time.process_time()
    x = 0
    while True:
        x = x + 1
        duration = time.process_time() - start
        if duration > sleep:
            break

    return (duration, x)


def usememory(x: int | tuple[int, str]) -> int:
    """Use a certain amount of memory in B"""
    if isinstance(x, tuple):
        amount, unit = x
        x = round(memconvert(amount, frm=unit))

    bytearray(int(x))
    return x
