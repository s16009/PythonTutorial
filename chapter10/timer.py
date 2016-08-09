class Timer(object):
    def __init__(self):
        self.start_time = 0

    def __enter__(self):
            self.start_time = chapter10.timer()
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = chapter10.timer()
        self.secs = self.end_time - self.start_time
        self.millis = self.secs * 1000
        if self.verboose:
            print('elapsed time: {0:f} ms'.format(self.millis))