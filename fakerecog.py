import pandas as pd
import re

caminho = r"C:\Users\Nadine\Downloads\FakeRecogna_no_removal_words.xlsx"


df = pd.read_excel(caminho)


def limpar_texto(texto):
    texto = str(texto)
    texto = re.sub(r"http\S+", "", texto)                 
    texto = re.sub(r"[\U00010000-\U0010ffff]", "", texto) 
    texto = re.sub(r"[@#]\w+", "", texto)                 
    texto = re.sub(r"\s+", " ", texto).strip()            
    return texto


df_limpo = pd.DataFrame({
    "texto": (df["Titulo"].fillna("") + ". " + df["Subtitulo"].fillna("") + ". " + df["Noticia"].fillna("")).apply(limpar_texto),
    "categoria": df["Categoria"].fillna(""),
    "origem": "FakeRecogna",
    "label": df["Classe"].astype(int)
})


df_limpo = df_limpo.dropna(subset=["texto", "label"]).drop_duplicates().reset_index(drop=True)


saida = r"C:\Users\Nadine\Downloads\fakerecogna_limpo.csv"
df_limpo.to_csv(saida, sep=";", index=False, encoding="utf-8-sig")

print("criado e limpo")
print(df_limpo.head())
