from dataclasses import dataclass


@dataclass(frozen=True)
class SourceFile:
    name: str
    text: str


@dataclass(frozen=True)
class Span:
    start: int
    end: int
    source: SourceFile


source_file: SourceFile = SourceFile(name="bird.cro", text='bird: String = "cro"')
