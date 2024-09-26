import time


class FileHandling:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file_obj = open(self.file_path, mode=self.mode)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()


with FileHandling('hello.txt', 'w') as file:
    file.write('tessssstttttttttt')


def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(start - finish)
        return result
    return wrapper


@log_execution_time
def sleep_func():
    print('hey')
    time.sleep(5)
    print('hey again')


sleep_func()