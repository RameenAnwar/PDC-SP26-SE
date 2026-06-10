import concurrent.futures
import time

number_list = list(range(1, 11))


def count(number):
    for i in range(0, 10_000_000):
        i += 1
    return i * number


def evaluate(item):
    result_item = count(item)
    print(f'Item {item}, result {result_item}')
    return result_item


if __name__ == '__main__':

    # -------------------------
    # Sequential Execution
    # -------------------------
    start_time = time.perf_counter()

    for item in number_list:
        evaluate(item)

    print('Sequential Execution in', time.perf_counter() - start_time, 'seconds')


    # -------------------------
    # Thread Pool Execution
    # -------------------------
    start_time = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate, item) for item in number_list]

        for f in concurrent.futures.as_completed(futures):
            f.result()

    print('Thread Pool Execution in', time.perf_counter() - start_time, 'seconds')


    # -------------------------
    # Process Pool Execution
    # -------------------------
    start_time = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate, item) for item in number_list]

        for f in concurrent.futures.as_completed(futures):
            f.result()

    print('Process Pool Execution in', time.perf_counter() - start_time, 'seconds')