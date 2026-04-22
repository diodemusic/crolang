import abc
from dataclasses import dataclass

from crolang.source import Span


@dataclass(frozen=True)
class Token(abc.ABC):
    span: Span
