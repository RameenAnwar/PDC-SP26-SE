import asyncio
import sys


async def first_coroutine(future, num):

    total = 0

    for i in range(1, num + 1):
        total += i

    await asyncio.sleep(4)

    future.set_result(
        f'First coroutine (sum) result = {total}'
    )


async def second_coroutine(future, num):

    factorial = 1

    for i in range(2, num + 1):
        factorial *= i

    await asyncio.sleep(4)

    future.set_result(
        f'Second coroutine (factorial) result = {factorial}'
    )


def got_result(future):
    print(future.result())


async def main():

    if len(sys.argv) < 3:
        print("Usage: python asyncio_and_futures.py num1 num2")
        return

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    future1 = asyncio.Future()
    future2 = asyncio.Future()

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    task1 = asyncio.create_task(
        first_coroutine(future1, num1)
    )

    task2 = asyncio.create_task(
        second_coroutine(future2, num2)
    )

    await asyncio.wait([task1, task2])


asyncio.run(main())