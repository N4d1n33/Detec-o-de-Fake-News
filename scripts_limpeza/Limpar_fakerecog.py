import pandas as pd
import re

caminho = r"C:\Users\Nadine\Downloads\FakeRecogna_no_removal_words.xlsx"

df = pd.read_excel(caminho)

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

df_limpo = pd.DataFrame({
    "texto": (
        df["Titulo"].fillna("") + ". " +
        df["Subtitulo"].fillna("") + ". " +
        df["Noticia"].fillna("")
    ).apply(limpar_texto),

    "categoria": df["Categoria"].fillna(""),
    "origem": "FakeRecogna",
    "label": df["Classe"]
})

linhas_vazias = df_limpo[
    df_limpo["texto"].isna() |
    (df_limpo["texto"].str.strip() == "") |
    df_limpo["label"].isna()
]

print("\nVazias")
print(linhas_vazias[["texto", "label"]])
print("\nQuantidade de linhas vazias:", len(linhas_vazias))

df_limpo = df_limpo[
    df_limpo["texto"].notna() &
    (df_limpo["texto"].str.strip() != "") &
    df_limpo["label"].notna()
]


df_limpo["label"] = df_limpo["label"].astype(int)
df_limpo = df_limpo.reset_index(drop=True)
df_limpo = df_limpo.sample(frac=1, random_state=42).reset_index(drop=True)
saida = r"C:\Users\Nadine\Downloads\fakerecogna.csv"
df_limpo.to_csv(saida, sep=";", index=False, encoding="utf-8-sig")


print("\nQuantidade")
print(df_limpo["label"].value_counts())
print("\nTotal", len(df_limpo))