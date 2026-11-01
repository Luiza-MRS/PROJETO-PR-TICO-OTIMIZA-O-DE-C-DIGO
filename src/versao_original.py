"""Codigo-base da AV2: deteccao de duplicatas por comparacao de pares."""


def tem_duplicata(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False


if __name__ == "__main__":
    exemplo = [8, 3, 12, 8, 5]
    print(tem_duplicata(exemplo))
