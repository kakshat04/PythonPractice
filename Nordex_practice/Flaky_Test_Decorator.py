"""
Problem:
Write a Python decorator @retry(times=3) that retries a test function up to 3 times if it raises an exception.

Example Usage:
@retry(times=3)
def test_sensor_connection():
    # Simulated flaky test
    ...

"""
def decorator(func):
    def newfn():
        attempt = 0
        while attempt < 3:
            try:
                return func()
            except Exception as e:
                print('Retrying...')
                attempt += 1
        return func()
    return newfn


@decorator
def sample_func(abc=1):
    print(f'Sample Function: {abc}')
    raise ValueError('Sample Function')

sample_func()