import concurrent.futures
import time

number_list = list(range(1, 11))


def count(number):
    for i in range(0, 10000000):
        i += 1
    return i * number


def evaluate(item):
    result_item = count(item)
    print('Item %s, result %s' % (item, result_item))


if __name__ == '__main__':

    # Sequential Execution
    start_time = time.perf_counter()

    for item in number_list:
        evaluate(item)

    print('Sequential Execution in %.4f seconds'
          % (time.perf_counter() - start_time))

    # Thread Pool Execution
    start_time = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate, item)
                   for item in number_list]

        concurrent.futures.wait(futures)

    print('Thread Pool Execution in %.4f seconds'
          % (time.perf_counter() - start_time))

    # Process Pool Execution
    start_time = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate, item)
                   for item in number_list]

        concurrent.futures.wait(futures)

    print('Process Pool Execution in %.4f seconds'
          % (time.perf_counter() - start_time))