import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from versao_original import tem_duplicata as original_isolada  # noqa: E402
from versao_otimizada import tem_duplicata as otimizada_isolada  # noqa: E402
from otimizacao_duplicatas import (  # noqa: E402
    tem_duplicata_original,
    tem_duplicata_otimizada,
)


class TestDeteccaoDeDuplicatas(unittest.TestCase):
    def assert_equivalentes(self, valores):
        self.assertEqual(
            tem_duplicata_original(valores),
            tem_duplicata_otimizada(valores),
        )

    def test_lista_vazia(self):
        self.assert_equivalentes([])
        self.assertFalse(tem_duplicata_otimizada([]))

    def test_lista_com_um_elemento(self):
        self.assert_equivalentes([42])
        self.assertFalse(tem_duplicata_otimizada([42]))

    def test_lista_sem_duplicatas(self):
        valores = [10, -3, 0, 8, 22, 91]
        self.assert_equivalentes(valores)
        self.assertFalse(tem_duplicata_otimizada(valores))

    def test_duplicata_no_inicio(self):
        valores = [5, 5, 8, 9]
        self.assert_equivalentes(valores)
        self.assertTrue(tem_duplicata_otimizada(valores))

    def test_duplicata_no_final(self):
        valores = [1, 2, 3, 4, 5, 1]
        self.assert_equivalentes(valores)
        self.assertTrue(tem_duplicata_otimizada(valores))

    def test_elementos_nao_hashable(self):
        valores = [[1, 2], [3], [1, 2]]
        self.assert_equivalentes(valores)
        self.assertTrue(tem_duplicata_otimizada(valores))

    def test_arquivos_de_versao_isolados(self):
        casos = [[], [1], [1, 2, 3], [4, 2, 4], [[1], [2], [1]]]
        for valores in casos:
            self.assertEqual(original_isolada(valores), otimizada_isolada(valores))

    def test_dados_aleatorios_reprodutiveis(self):
        gerador = random.Random(20261031)
        for _ in range(300):
            valores = [gerador.randint(-20, 20) for _ in range(gerador.randint(0, 80))]
            self.assert_equivalentes(valores)


if __name__ == "__main__":
    unittest.main()
