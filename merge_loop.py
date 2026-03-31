import re
from collections import defaultdict
from tarefa1_get_stats import get_stats, vocab

## Substitui todas as ocorrências do par mais frequente pela versão fundida
def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    pattern = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        new_word = pattern.sub(''.join(pair), word)
        v_out[new_word] = v_in[word]
    return v_out


## Loop principal: executa K=5 fusões sucessivas
K = 5
current_vocab = dict(vocab)

for i in range(K):
    stats = get_stats(current_vocab)
    best_pair = max(stats, key=stats.get)
    current_vocab = merge_vocab(best_pair, current_vocab)

    print(f"Iteração {i + 1}")
    print(f"  Par fundido: {best_pair}")
    print(f"  Vocab: {current_vocab}\n")
