"""Primeira otimizacao da AV2: deteccao de duplicatas com hashing."""

from versao_original import tem_duplicata as tem_duplicata_original


def tem_duplicata(lista):
    vistos = set()
    for item in lista:
        try:
            if item in vistos:
                return True
            vistos.add(item)
        except TypeError:
            return tem_duplicata_original(lista)
    return False


if __name__ == "__main__":
    exemplo = [8, 3, 12, 8, 5]
    print(tem_duplicata(exemplo))
