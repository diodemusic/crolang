from crolang.lexer import scanner, token_classes
from crolang.source import SourceFile

tokens: list[token_classes.Token] = scanner.lex(
    source=SourceFile(name="bird.cro", text="+ * % ^ - -> ? ?. < <= > >=")
)

for i in range(len(tokens)):
    print(f"Token {i}: {tokens[i]}")
