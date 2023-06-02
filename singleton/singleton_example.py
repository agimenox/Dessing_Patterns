class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def log(self, message):
        print("Log:", message)


# Usage example
logger1 = Logger()
logger1.log("This is a log message from logger1")

logger2 = Logger()
logger2.log("This is a log message from logger2")

