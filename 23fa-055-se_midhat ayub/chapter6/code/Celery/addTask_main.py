import addTask

if __name__ == '__main__':
    print("Sending task add(5, 5) to Celery worker...")
    result = addTask.add.delay(5,5)
    print("Task sent! Task ID:", result.id)
    try:
        print("Waiting for task result...")
        val = result.get(timeout=3)
        print("Result received from worker:", val)
    except Exception:
        print("\n[INFO] Task sent successfully to the queue, but did not receive a result.")
        print("To process the task and see the result, please start a Celery worker in another terminal:")
        print("    cd Chapter06/Celery")
        print("    celery -A addTask worker --loglevel=info --pool=solo\n")


    
