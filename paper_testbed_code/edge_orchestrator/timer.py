#timer.py
import time

class TimerError(Exception):
    """Exception"""

class Timer:

    def __init__(self):
        self._start_time = None

    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it.")

        self._start_time = time.perf_counter()
        print(f"timer start at : {self._start_time}")

    def get_elapsed(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        elapsed_time = time.perf_counter() - self._start_time

        return elapsed_time

    def re_start(self):
        self._start_time = time.perf_counter()

    def stop(self):

        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        return elapsed_time
