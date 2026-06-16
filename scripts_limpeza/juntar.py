import pandas as pd

faketru_path = r"C:\Users\Nadine\Downloads\FakeTrueBr.csv"
fakebr_path = r"C:\Users\Nadine\Downloads\FakeBr.csv"
fakerecogna_path = r"C:\Users\Nadine\Downloads\fakerecogna.csv"

# lê datasets
faketru = pd.read_csv(faketru_path, sep=";", encoding="utf-8-sig")
fakebr = pd.read_csv(fakebr_path, sep=";", encoding="utf-8-sig")
fakerecogna = pd.read_csv(fakerecogna_path, sep=";", encoding="utf-8-sig")

# colunas desejadas
colunas = ["texto", "origem", "label"]

# mantém só as colunas necessárias
faketru = faketru[colunas]
fakebr = fakebr[colunas]
fakerecogna = fakerecogna[colunas]

# junta tudo
df_final = pd.concat(
    [faketru, fakebr, fakerecogna],
    ignore_index=True
)

# verifica linhas vazias
linhas_vazias = df_final[
    df_final["texto"].isna() |
    (df_final["texto"].astype(str).str.strip() == "") |
    df_final["label"].isna()
]

print("\ Linhas")
print(linhas_vazias[["texto", "label"]])

print("\nQuantidade de linhas vazias:", len(linhas_vazias))

# salva
saida = r"C:\Users\Nadine\Downloads\Final.csv"

df_final.to_csv(
    saida,
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

# contagem final
contagem = df_final["label"].value_counts().sort_index()

print("\ndados finais certos")
print(f"Fake (0): {contagem.get(0, 0)}")
print(f"Real (1): {contagem.get(1, 0)}")
print(f"Total: {len(df_final)}")