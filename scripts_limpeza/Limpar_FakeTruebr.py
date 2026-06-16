import pandas as pd
import re

caminho = r"C:\Users\Nadine\Downloads\FakeTrueBr_corpus.csv"
saida = r"C:\Users\Nadine\Downloads\FakeTrueBr.csv"

df = pd.read_csv(caminho)
# padroniza nomes das colunas
df.columns = df.columns.str.strip().str.lower()
df = df.replace('"', '', regex=True)

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

# fake = label 0
df_fake = pd.DataFrame({
    "texto": df["fake"].apply(limpar_texto),
    "origem": "FakeTrueBr",
    "label": 0
})

# true = label 1
df_true = pd.DataFrame({
    "texto": df["true"].apply(limpar_texto),
    "origem": "FakeTrueBr",
    "label": 1
})

df_final = pd.concat([df_fake, df_true], ignore_index=True)
df_final = df_final.dropna()
df_final = df_final.sample(frac=1, random_state=42).reset_index(drop=True)
df_final.to_csv(saida, index=False, encoding="utf-8-sig", sep=";")


print("\nQuantidade de notícias:", df_final.shape[0])
print("Quantidade de colunas:", df_final.shape[1])

print("\nDistribuição das classes:")
print(df_final["label"].value_counts())