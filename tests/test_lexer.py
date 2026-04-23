from crolang.lexer import Token, lex
from crolang.source import SourceFile

tokens: list[Token] = lex(source=SourceFile(name="bird.cro", text="!= ! , . {} ()"))

for i in range(len(tokens)):
    print(f"Token {i}: {tokens[i]}")
