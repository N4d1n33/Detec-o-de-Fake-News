import pandas as pd
import re
import os

pasta_fake = r"C:\Users\Nadine\Downloads\Fake.br-Corpus-master\Fake.br-Corpus-master\full_texts\fake"
pasta_true = r"C:\Users\Nadine\Downloads\Fake.br-Corpus-master\Fake.br-Corpus-master\full_texts\true"

saida = r"C:\Users\Nadine\Downloads\FakeBr.csv"


def limpar_texto(texto):
    texto = str(texto)

    texto = re.sub(r"http\S+", "", texto)

    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U00002700-\U000027BF"
        u"\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )

    texto = emoji_pattern.sub("", texto)
    texto = re.sub(r"[@#]\w+", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip()

    return texto


dados = []

# fake = 0
for arquivo in os.listdir(pasta_fake):

    if arquivo.endswith(".txt"):

        caminho_arquivo = os.path.join(pasta_fake, arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            texto = f.read()

        dados.append({
            "texto": limpar_texto(texto),
            "origem": "FakeBr",
            "label": 0
        })


# true = 1
for arquivo in os.listdir(pasta_true):

    if arquivo.endswith(".txt"):

        caminho_arquivo = os.path.join(pasta_true, arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            texto = f.read()

        dados.append({
            "texto": limpar_texto(texto),
            "origem": "FakeBr",
            "label": 1
        })


# cria dataframe
df_final = pd.DataFrame(dados)

# remove vazios
df_final = df_final.dropna()

# embaralha
df_final = df_final.sample(frac=1, random_state=42).reset_index(drop=True)

# salva
df_final.to_csv(saida, index=False, encoding="utf-8-sig", sep=";")

print("criado e limpo")
print(df_final.head())

print("\nQuantidade de notícias:", df_final.shape[0])
print("Quantidade de colunas:", df_final.shape[1])

print("\nDistribuição das classes:")
print(df_final["label"].value_counts())