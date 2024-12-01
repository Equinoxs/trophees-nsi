from src.classes import DEBUG

class LogHandler:
    _instance = None

    # singleton
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.log = []
            self.length = 10

    def add(self, log: str):
        if DEBUG:
            print(log)
        self.log.append(log)

    def set_length(self, length):
        self.length = length

    def get_log(self):
        return ['==== Log ===='] + self.log[-self.length:]