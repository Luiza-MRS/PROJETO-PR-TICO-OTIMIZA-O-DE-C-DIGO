"""Benchmark reproduzivel das duas implementacoes de deteccao de duplicatas."""

import csv
import json
import random
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from otimizacao_duplicatas import (  # noqa: E402
    tem_duplicata_original,
    tem_duplicata_otimizada,
)

TAMANHOS = [500, 1_000, 2_000, 4_000, 8_000]
REPETICOES = 5
SEMENTE_BASE = 20261031


def medir(funcao, entrada, repeticoes=REPETICOES):
    tempos = []
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        resultado = funcao(entrada)
        tempos.append(time.perf_counter() - inicio)
        if resultado is not False:
            raise AssertionError("O conjunto de benchmark deveria nao conter duplicatas.")
    return {
        "minimo_s": min(tempos),
        "mediana_s": statistics.median(tempos),
        "tempos_s": tempos,
    }


def executar():
    resultados = []

    for n in TAMANHOS:
        dados = random.Random(SEMENTE_BASE + n).sample(range(n * 10), n)
        original = medir(tem_duplicata_original, dados)
        otimizada = medir(tem_duplicata_otimizada, dados)
        resultados.append({
            "n": n,
            "original_minimo_s": original["minimo_s"],
            "original_mediana_s": original["mediana_s"],
            "otimizada_minimo_s": otimizada["minimo_s"],
            "otimizada_mediana_s": otimizada["mediana_s"],
            "ganho_mediana_x": original["mediana_s"] / otimizada["mediana_s"],
        })

    pasta_resultados = ROOT / "results"
    pasta_resultados.mkdir(exist_ok=True)
    with (pasta_resultados / "benchmark.csv").open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=resultados[0].keys())
        escritor.writeheader()
        escritor.writerows(resultados)

    metadados = {
        "python": sys.version.split()[0],
        "plataforma": sys.platform,
        "semente_base": SEMENTE_BASE,
        "repeticoes": REPETICOES,
        "tamanhos": TAMANHOS,
        "caso": "listas sem duplicatas (pior caso para a implementacao original)",
        "resultados": resultados,
    }
    (pasta_resultados / "benchmark.json").write_text(
        json.dumps(metadados, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("n, original mediana (ms), otimizada mediana (ms), ganho (x)")
    for linha in resultados:
        print(
            f"{linha['n']}, {linha['original_mediana_s'] * 1000:.6f}, "
            f"{linha['otimizada_mediana_s'] * 1000:.6f}, "
            f"{linha['ganho_mediana_x']:.2f}"
        )
    print(f"\nArquivos gerados em: {pasta_resultados}")
    return resultados


if __name__ == "__main__":
    executar()
