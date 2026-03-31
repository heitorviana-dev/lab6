from transformers import AutoTokenizer

## Carrega o tokenizador multilíngue do BERT (WordPiece)
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

frase = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."

tokens = tokenizer.tokenize(frase)

print("Tokens gerados pelo WordPiece:")
print(tokens)
