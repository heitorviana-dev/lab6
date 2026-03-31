# Laboratório 6 — Tokenizador BPE e WordPiece

Implementação do algoritmo Byte Pair Encoding (BPE) do zero e exploração do WordPiece via Hugging Face, desenvolvida como atividade prática da disciplina de PLN.

## Estrutura

```
lab6_bpe/
├── tarefa1_get_stats.py   # Motor de frequências
├── tarefa2_merge_loop.py  # Loop de fusão (K=5)
└── tarefa3_wordpiece.py   # Integração com BERT multilíngue
```

## Como executar

```bash
pip install transformers

python tarefa1_get_stats.py
python tarefa2_merge_loop.py
python tarefa3_wordpiece.py
```

## Relatório — O que significa `##` no WordPiece?

Ao tokenizar a frase de teste com o BERT multilíngue, palavras longas ou desconhecidas são particionadas em sub-palavras. O prefixo `##` sinaliza que aquele fragmento é uma **continuação** do token anterior — ele não inicia uma nova palavra. Por exemplo, `inconstitucionalmente` pode virar algo como `['in', '##const', '##itucional', '##mente']`.

Essa convenção resolve diretamente o problema do vocabulário aberto (*open vocabulary problem*): em vez de o modelo travar ao encontrar uma palavra que nunca viu durante o treinamento, ele a decompõe em partes menores que já conhece. O pior caso possível é a palavra ser reduzida a caracteres individuais — mas o modelo nunca retorna um token `[UNK]` para texto comum. Isso torna os Transformers robustos a neologismos, termos técnicos, palavras morfologicamente complexas e erros de digitação.

## Uso de IA

A expressão regular utilizada na função `merge_vocab` (Tarefa 2) foi construída com auxílio do Claude (Anthropic). O trecho em questão é o padrão `r'(?<!\S)' + bigram + r'(?!\S)'`, que garante que apenas ocorrências do par como símbolos isolados — e não como substrings de tokens já fundidos — sejam substituídas. O código foi revisado e validado manualmente contra os casos de teste do enunciado.

## Versionamento

A versão final avaliável está marcada com a tag `v1.0`.

```bash
git tag v1.0
git push origin v1.0
```
