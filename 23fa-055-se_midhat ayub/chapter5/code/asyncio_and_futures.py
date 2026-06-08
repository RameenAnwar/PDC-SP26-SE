import asyncio


async def first_coroutine(future, num):
    count = 0

    for i in range(1, num + 1):
        count += i

    await asyncio.sleep(4)

    future.set_result(
        f"First coroutine (sum of first {num} integers) = {count}"
    )


async def second_coroutine(future, num):
    count = 1

    for i in range(2, num + 1):
        count *= i

    await asyncio.sleep(4)

    future.set_result(
        f"Second coroutine (factorial of {num}) = {count}"
    )


def got_result(future):
    print(future.result())


async def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    future1 = asyncio.Future()
    future2 = asyncio.Future()

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    await asyncio.gather(
        first_coroutine(future1, num1),
        second_coroutine(future2, num2)
    )


if __name__ == "__main__":
    asyncio.run(main())