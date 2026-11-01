"""Comparacao entre deteccao de duplicatas por pares e por hashing."""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def tem_duplicata_original(lista: Sequence[T]) -> bool:
    """Versao de referencia do enunciado: compara todos os pares."""
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False


def tem_duplicata_otimizada(lista: Sequence[T]) -> bool:
    """Detecta repeticoes com set; faz fallback para valores nao-hashable.

    Para elementos hashable, a busca/insercao no set tem custo esperado O(1),
    resultando em O(n) no total. Se algum elemento nao puder ser hasheado,
    usa a implementacao original para preservar a compatibilidade com listas
    como [[1, 2], [3], [1, 2]].
    """
    vistos: set[object] = set()

    for item in lista:
        try:
            if item in vistos:
                return True
            vistos.add(item)
        except TypeError:
            return tem_duplicata_original(lista)

    return False
