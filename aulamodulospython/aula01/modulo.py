def soma(x: float, y: float) -> float:
    return x + y


def main() -> None:
    print(soma(10, 30)) # somente executa se o main foi o módulo
    print(soma(20, 20)) # somente executa se o main foi o módulo


if __name__ == '__main__':
    main() # somente executa se o main foi o módulo