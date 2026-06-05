"""Asyncio using Asyncio.Task to execute three math functions in parallel"""

import asyncio


async def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        print('Asyncio.Task: Compute factorial(%s)' % i)
        await asyncio.sleep(1)
        fact *= i
    print('Asyncio.Task - factorial(%s) = %s' % (number, fact))


async def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print('Asyncio.Task: Compute fibonacci(%s)' % i)
        await asyncio.sleep(1)
        a, b = b, a + b
    print('Asyncio.Task - fibonacci(%s) = %s' % (number, a))


async def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result*(n - i + 1)/i
        print('Asyncio.Task: Compute binomial_coefficient(%s)' % i)
        await asyncio.sleep(1)
    print('Asyncio.Task - binomial_coefficient(%s, %s) = %s' % (n, k, result))


async def main():
    task_list = [asyncio.create_task(factorial(10)),
                 asyncio.create_task(fibonacci(10)),
                 asyncio.create_task(binomial_coefficient(20, 10))]
    await asyncio.wait(task_list)

if __name__ == '__main__':
    asyncio.run(main())
