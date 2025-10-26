import pandas as pd


boatos_path = r"C:\Users\Nadine\Downloads\boatosbr_balanceado_embaralhado.csv"
fake_path   = r"C:\Users\Nadine\Downloads\fakerecogna_limpo.csv"


boatos = pd.read_csv(boatos_path, sep=";", encoding="utf-8-sig")
fake = pd.read_csv(fake_path, sep=";", encoding="utf-8-sig")


colunas = ["texto", "categoria", "origem", "label"]
boatos = boatos[colunas]
fake = fake[colunas]


df_final = pd.concat([boatos, fake], ignore_index=True)


df_final = df_final.dropna(subset=["texto", "label"]).drop_duplicates().reset_index(drop=True)


df_final = df_final.sample(frac=1, random_state=42).reset_index(drop=True)


saida = r"C:\Users\Nadine\Downloads\dataset_final_fakenews.csv"
df_final.to_csv(saida, sep=";", index=False, encoding="utf-8-sig")


contagem = df_final["label"].value_counts().sort_index()
print("dados finais certos")
print(f"Fake (0): {contagem.get(0, 0)}")
print(f"Real (1): {contagem.get(1, 0)}")
print(f"total: {len(df_final)}")

