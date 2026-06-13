from addTask import add


if __name__ == '__main__':
    result = add.delay(5, 5)
    print("Task submitted:", result.id)
    
