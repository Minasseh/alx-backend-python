#!/usr/bin/env python3
""" An asynchronous function """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ An asynchronous coroutine that takes in an integer argument
    named wait_random that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    delay = await wait_random()
