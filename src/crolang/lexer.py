import abc
from dataclasses import dataclass

from crolang.source import SourceFile, Span


@dataclass(frozen=True)
class Token(abc.ABC):
    span: Span


class Scanner:
    def __init__(self, source: SourceFile) -> None:
        self.source: SourceFile = source
        self.tokens: list[Token] = []
        self.start: int = 0
        self.current: int = 0

    def at_end(self) -> bool:
        return self.current >= len(self.source.text)

    def advance(self) -> str:
        if self.at_end():
            raise IndexError

        char: str = self.source.text[self.current]
        self.current += 1

        return char

    def peek(self) -> str:
        if self.at_end():
            return "\0"

        return self.source.text[self.current]

    def scan_token(self) -> None: ...

    def scan_tokens(self) -> None:
        while not self.at_end():
            self.start = self.current
            self.scan_token()


def lex(source: SourceFile) -> list[Token]:
    scanner: Scanner = Scanner(source=source)
    scanner.scan_tokens()

    return scanner.tokens


@dataclass(frozen=True)
class LeftBrace(Token): ...


@dataclass(frozen=True)
class IntLiteral(Token):
    value: int


@dataclass(frozen=True)
class Identifier(Token):
    name: str
