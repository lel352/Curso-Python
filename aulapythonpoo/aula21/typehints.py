""" Descrição rápida e simples - Documentação referente ao módulo

Ele não faz nada, mas é só um exemplo para você
typing - https://docs.python.org/3/library/typing.html
"""

x: int = 10
y: float = 10.5


def funcao(p1: float, p2: str, p3: dict) -> float:
    return 10.10


from typing import Union


def funcao2() ->  Union[list, dict]:
    return {}