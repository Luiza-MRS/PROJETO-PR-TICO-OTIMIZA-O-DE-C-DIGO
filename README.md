# Projeto Otimização - Trabalho Igor

**Disciplina:** Análise e Otimização de Sistemas - Ciência da Computação (UNIJORGE)  
**Professor:** Igor Gonzalez  
**Entrega:** AV2 - diagnóstico e primeira otimização  
**Tema:** Detecção de duplicatas em listas

## Objetivo

Comparar o código-base de comparação de todos os pares, com complexidade quadrática no pior caso, a uma primeira versão otimizada que utiliza `set` (hashing) para detectar valores repetidos em tempo esperado linear.

## Estrutura

```text
.
├── src/otimizacao_duplicatas.py   # implementações original e otimizada
├── tests/test_duplicatas.py       # testes de equivalência e casos de borda
├── benchmarks/benchmark.py       # benchmark reproduzível
├── results/benchmark.csv         # medições em CSV
├── results/benchmark.json        # medições e metadados
├── assets/benchmark_duplicatas.png
├── docs/relatorio_av2_abnt.pdf        # relatório em PDF

```

## Requisitos

- Python 3.10 ou superior (o código usa anotações de tipo modernas).
- O programa, testes e benchmark usam apenas a biblioteca padrão do Python.


## Como executar

Na raiz do projeto:

```bash
python -m unittest discover -s tests -v
python benchmarks/benchmark.py
```

O benchmark gera/atualiza `results/benchmark.csv` e `results/benchmark.json`. Ele utiliza listas sem duplicatas para forçar a versão original a percorrer todos os pares e medir seu pior caso.

## Implementações

- `tem_duplicata_original`: mantém a lógica do enunciado, comparando cada posição com as seguintes.
- `tem_duplicata_otimizada`: percorre a lista uma vez e armazena os elementos já vistos em um `set`. Para valores hashable, a complexidade esperada é O(n). Se encontrar um valor não hashable (por exemplo, uma lista), recorre à implementação original para preservar a compatibilidade com entradas desse tipo.

## Complexidade

| Implementação | Tempo | Espaço auxiliar |
|---|---:|---:|
| Original | O(n²) no pior caso | O(1) |
| Otimizada | O(n) esperado para elementos hashable | O(n) |

A garantia linear da versão otimizada é esperada, pois operações de hashing têm custo médio constante; colisões adversas podem aumentar o custo. O fallback para valores não hashable preserva a correção, mas volta ao custo quadrático.

## Resultado medido

No ambiente desta execução (Python 3.13.5, Linux x86_64, AMD EPYC 9V74), a versão otimizada foi de aproximadamente **163x a 2.346x mais rápida** pela mediana dos tempos medidos para os cinco tamanhos testados. Os números dependem do hardware, da versão do Python e da carga do sistema; o benchmark pode ser repetido localmente.

Os testes automatizados cobrem listas vazias, listas unitárias, casos sem repetição, duplicatas no início e no final, elementos não hashable e 300 listas aleatórias reprodutíveis. Resultado validado: **8 testes aprovados**.

## Entrega acadêmica

O relatório e a apresentação acompanham o código. Os campos de integrantes foram deixados em aberto para preenchimento do grupo, pois esses nomes não constam no material recebido. O trabalho foi elaborado com auxílio de IA generativa; os integrantes devem revisar, executar e compreender o código e as medições, conforme as orientações de integridade do enunciado.
