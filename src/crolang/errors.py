from crolang.source import Span


class CrolangError(Exception):
    def __init__(self, message: str, span: Span) -> None:
        super().__init__(message)
        self.message: str = message
        self.span: Span = span
