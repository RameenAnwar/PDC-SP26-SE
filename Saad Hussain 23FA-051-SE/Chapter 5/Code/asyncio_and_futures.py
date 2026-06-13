import asyncio
import sys


async def first_coroutine(future, num):
    count = 0
    for i in range(1, num + 1):
        count += 1
    await asyncio.sleep(4)
    future.set_result('First coroutine (sum of N ints) result = %s' % count)


async def second_coroutine(future, num):
    count = 1
    for i in range(2, num + 1):
        count *= i
    await asyncio.sleep(4)
    future.set_result('Second coroutine (factorial) result = %s' % count)


def got_result(future):
    print(future.result())


async def main(num1, num2):
    loop = asyncio.get_running_loop()
    future1 = loop.create_future()
    future2 = loop.create_future()

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    await asyncio.gather(
        first_coroutine(future1, num1),
        second_coroutine(future2, num2),
    )


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python asyncio_and_futures.py <count> <factorial_number>")

    asyncio.run(main(int(sys.argv[1]), int(sys.argv[2])))
