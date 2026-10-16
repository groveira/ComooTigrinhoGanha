"""
Simulação de dois dados de 6 lados em várias quantidades de lançamentos.
Compara a frequência relativa observada com a probabilidade teórica.
Requer: Python 3 + matplotlib   (pip install matplotlib)

Adaptado da ideia do PyDice, de Robert Carlos (2018, CC BY 3.0 BR):
https://datalivre.medium.com/quebrando-a-banca-com-python-probabilidade-e-estatistica-3e6ba6d09065
"""
import random
from collections import Counter
import matplotlib.pyplot as plt

LADOS = 6
DADOS = 2
SOMAS = list(range(DADOS, DADOS * LADOS + 1))          # 2, 3, ..., 12

# Probabilidade teórica: contamos as combinações do espaço amostral (36)
combinacoes = Counter(a + b for a in range(1, LADOS + 1) for b in range(1, LADOS + 1))
TEORICA = [combinacoes[s] / LADOS**2 for s in SOMAS]   # 1/36, 2/36, ..., 6/36, ..., 1/36


def lancar(n):
    """Lança DADOS dados n vezes e devolve a lista das somas."""
    return [sum(random.randint(1, LADOS) for _ in range(DADOS)) for _ in range(n)]


def grafico(n, ax):
    contagem = Counter(lancar(n))
    freq_abs = [contagem[s] for s in SOMAS]
    freq_rel = [f / n for f in freq_abs]
    ax.bar(SOMAS, freq_rel, color="#6c6fd6", label="Observado (frequência relativa)")
    ax.plot(SOMAS, TEORICA, "o-", color="#d9534f", label="Probabilidade teórica")
    for s, f in zip(SOMAS, freq_abs):
        if f:
            ax.text(s, freq_rel[SOMAS.index(s)], str(f), ha="center", va="bottom", fontsize=8)
    ax.set_title(f"{n} lançamentos")
    ax.set_xticks(SOMAS)
    ax.set_ylim(0, 0.35)
    ax.set_xlabel("Soma dos dois dados")


if __name__ == "__main__":
    ITERACOES = [11, 36, 360, 3600, 36000]
    fig, axs = plt.subplots(1, len(ITERACOES), figsize=(22, 4.5), sharey=True)
    for n, ax in zip(ITERACOES, axs):
        grafico(n, ax)
    axs[0].set_ylabel("Frequência relativa")
    axs[0].legend(fontsize=7, loc="upper left")
    plt.tight_layout()
    plt.savefig("dados.png", dpi=110)
    print("ok", [round(t * 36) for t in TEORICA], sum(TEORICA))
