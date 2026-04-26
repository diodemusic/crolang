from crolang.lexer import token_classes
from crolang.source import SourceFile, Span


class Scanner:
    def __init__(self, source: SourceFile) -> None:
        self.source: SourceFile = source
        self.tokens: list[token_classes.Token] = []
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

    def construct_span(self) -> Span:
        return Span(start=self.start, end=self.current, source=self.source)

    def ahead_matches(self, expected: str) -> bool:
        if self.peek() == expected:
            _ = self.advance()
            return True
        else:
            return False

    def scan_token(self) -> None:
        char: str = self.advance()

        match char:
            case "{":
                self.tokens.append(token_classes.LeftBrace(span=self.construct_span()))
            case "}":
                self.tokens.append(token_classes.RightBrace(span=self.construct_span()))
            case "(":
                self.tokens.append(
                    token_classes.LeftParenthesis(span=self.construct_span())
                )
            case ")":
                self.tokens.append(
                    token_classes.RightParenthesis(span=self.construct_span())
                )
            case ",":
                self.tokens.append(token_classes.Comma(span=self.construct_span()))
            case ".":
                self.tokens.append(token_classes.Dot(span=self.construct_span()))
            case ":":
                self.tokens.append(token_classes.Colon(span=self.construct_span()))
            case "!":
                if self.ahead_matches(expected="="):
                    self.tokens.append(
                        token_classes.NotEquals(span=self.construct_span())
                    )
                else:
                    self.tokens.append(token_classes.Bang(span=self.construct_span()))
            case "=":
                if self.ahead_matches(expected="="):
                    if self.ahead_matches(expected="="):
                        self.tokens.append(
                            token_classes.EqualsEqualsEquals(span=self.construct_span())
                        )
                    else:
                        self.tokens.append(
                            token_classes.EqualsEquals(span=self.construct_span())
                        )
                else:
                    self.tokens.append(token_classes.Equals(span=self.construct_span()))
            case "+":
                self.tokens.append(token_classes.Plus(span=self.construct_span()))
            case "*":
                self.tokens.append(token_classes.Star(span=self.construct_span()))
            case "%":
                self.tokens.append(token_classes.Percent(span=self.construct_span()))
            case "^":
                self.tokens.append(token_classes.Caret(span=self.construct_span()))
            case "-":
                if self.ahead_matches(expected=">"):
                    self.tokens.append(token_classes.Arrow(span=self.construct_span()))
                else:
                    self.tokens.append(token_classes.Minus(span=self.construct_span()))
            case "?":
                if self.ahead_matches(expected="."):
                    self.tokens.append(
                        token_classes.QuestionDot(span=self.construct_span())
                    )
                else:
                    self.tokens.append(
                        token_classes.Question(span=self.construct_span())
                    )
            case "<":
                if self.ahead_matches(expected="="):
                    self.tokens.append(
                        token_classes.LessThanEquals(span=self.construct_span())
                    )
                else:
                    self.tokens.append(
                        token_classes.LessThan(span=self.construct_span())
                    )
            case ">":
                if self.ahead_matches(expected="="):
                    self.tokens.append(
                        token_classes.GreaterThanEquals(span=self.construct_span())
                    )
                else:
                    self.tokens.append(
                        token_classes.GreaterThan(span=self.construct_span())
                    )
            case c if c.isdigit():
                while self.peek().isdigit():
                    _ = self.advance()

                self.tokens.append(
                    token_classes.IntLiteral(
                        span=self.construct_span(),
                        value=int(self.source.text[self.start : self.current]),
                    )
                )
            case _:
                ...

    def scan_tokens(self) -> None:
        while not self.at_end():
            self.start = self.current
            self.scan_token()


def lex(source: SourceFile) -> list[token_classes.Token]:
    scanner_instance: Scanner = Scanner(source=source)
    scanner_instance.scan_tokens()

    return scanner_instance.tokens
