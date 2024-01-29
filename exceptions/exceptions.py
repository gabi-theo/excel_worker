class BaseTaskException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class NotImplemented(BaseTaskException):
    pass


class ColumnNotFound(BaseTaskException):
    pass


class FilterError(BaseTaskException):
    pass


class OtherExceptions(BaseTaskException):
    pass


class AggregationException(BaseTaskException):
    pass


class ReadWriteException(BaseTaskException):
    pass
