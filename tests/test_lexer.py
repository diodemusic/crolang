import pytest

from crolang.lexer import scanner, token_classes
from crolang.source import SourceFile


@pytest.mark.parametrize(
    argnames="test_input, expected", argvalues=[("42", 42), ("0", 0), ("12345", 12345)]
)
def test_int_literal(test_input: str, expected: int) -> None:
    tokens: list[token_classes.Token] = scanner.lex(
        source=SourceFile(name="bird.cro", text=test_input)
    )

    assert len(tokens) == 1
    assert type(tokens[0]) is token_classes.IntLiteral
    assert tokens[0].value == expected
