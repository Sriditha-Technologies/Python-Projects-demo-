def log(message):
    with open('log.txt', 'a') as file:
        file.write(message + '\n')
print("This is a log message.")
print("This is another log message.")