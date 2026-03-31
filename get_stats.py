from collections import defaultdict

vocab = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}

## Conta a frequência de cada par de símbolos adjacentes no corpus
def get_stats(vocab):
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i + 1])] += freq
    return pairs


if __name__ == '__main__':
    stats = get_stats(vocab)

    print("Frequência dos pares:")
    for pair, freq in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  {pair}: {freq}")

    ## Validação: ('e', 's') deve ter contagem máxima de 9
    assert stats[('e', 's')] == 9, "Erro: par ('e', 's') deveria ter frequência 9"
    print(f"\n✓ Validação OK — ('e', 's') = {stats[('e', 's')]}")
