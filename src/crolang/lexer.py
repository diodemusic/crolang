import abc
from dataclasses import dataclass

from crolang.source import Span


@dataclass(frozen=True)
class Token(abc.ABC):
    span: Span


@dataclass(frozen=True)
class LeftBrace(Token): ...


@dataclass(frozen=True)
class IntLiteral(Token):
    value: int


@dataclass(frozen=True)
class Identifier(Token):
    name: str
