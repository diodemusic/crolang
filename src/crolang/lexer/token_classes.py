from abc import ABC
from dataclasses import dataclass

from crolang.source import Span


@dataclass(frozen=True)
class Token(ABC):
    span: Span


@dataclass(frozen=True)
class LeftBrace(Token): ...


@dataclass(frozen=True)
class RightBrace(Token): ...


@dataclass(frozen=True)
class LeftParenthesis(Token): ...


@dataclass(frozen=True)
class RightParenthesis(Token): ...


@dataclass(frozen=True)
class Comma(Token): ...


@dataclass(frozen=True)
class Dot(Token): ...


@dataclass(frozen=True)
class Colon(Token): ...


@dataclass(frozen=True)
class IntLiteral(Token):
    value: int


@dataclass(frozen=True)
class Identifier(Token):
    name: str


@dataclass(frozen=True)
class Bang(Token): ...


@dataclass(frozen=True)
class NotEquals(Token): ...


@dataclass(frozen=True)
class Equals(Token): ...


@dataclass(frozen=True)
class EqualsEquals(Token): ...


@dataclass(frozen=True)
class EqualsEqualsEquals(Token): ...
