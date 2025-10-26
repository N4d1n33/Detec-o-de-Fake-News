import pandas as pd
import re

caminho = r"C:\Users\Nadine\Downloads\boatos_br_corpus_simples.json"


df = pd.read_json(caminho, encoding="utf-8")

#remove emogis, caracter especial, espaços vazios, etc
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
    texto = emoji_pattern.sub(r"", texto)
    texto = re.sub(r"[@#]\w+", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


#remove as colunas p deixar somente texto, categoria origem e label
df_simplificado = pd.DataFrame({
    "texto": df["texto"].apply(limpar_texto),
    "categoria": df["categorias"].apply(lambda x: ", ".join(x)),
    "origem": df["origem"],
    "label": df["rotulo"].map({"falso": 0, "verdade": 1})   #converte label p binario
})


df_simplificado["categoria"] = df_simplificado["categoria"].str.strip() #converte p csv


saida = r"C:\Users\Nadine\Downloads\boatosbr_limpo.csv"
df_simplificado.to_csv(saida, index=False, encoding="utf-8-sig", sep=";")

print("criado e limpo ")
print(df_simplificado.head())
