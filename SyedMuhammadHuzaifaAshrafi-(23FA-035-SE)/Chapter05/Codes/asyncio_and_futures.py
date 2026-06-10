import asyncio
import sys
async def first_coroutine(num):
    count = 0
    for i in range(1, num + 1):
        count += 1
    await asyncio.sleep(4)
    return f'First coroutine (sum of N ints) result = {count}'
async def second_coroutine(num):
    count = 1
    for i in range(2, num + 1):
        count *= i
    await asyncio.sleep(4)

    return f'Second coroutine (factorial) result = {count}'


async def main():
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    task1 = asyncio.create_task(first_coroutine(num1))
    task2 = asyncio.create_task(second_coroutine(num2))

    result1 = await task1
    result2 = await task2

    print(result1)
    print(result2)


if __name__ == '__main__':
    asyncio.run(main())