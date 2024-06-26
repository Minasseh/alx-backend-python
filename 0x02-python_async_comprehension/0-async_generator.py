#!/usr/bin/env python3
""" A coroutine called async_generator """
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """ This coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10 """

    for i in range(10):
        await asyncio.sleep(1)
        rn = random.uniform(0, 10)
        yield rn
