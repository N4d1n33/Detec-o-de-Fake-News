

import pandas as pd

# lê o dataset balanceado
df = pd.read_csv(r"C:\Users\Nadine\Downloads\boatosbr_balanceado.csv", sep=";", encoding="utf-8-sig")

# embaralha todas as linhas
df_embaralhado = df.sample(frac=1, random_state=42).reset_index(drop=True)

# salva o novo arquivo embaralhado
saida = r"C:\Users\Nadine\Downloads\boatosbr_balanceado_embaralhado.csv"
df_embaralhado.to_csv(saida, index=False, sep=";", encoding="utf-8-sig")

print("✅ Dataset embaralhado com sucesso!")
print("Total de linhas:", len(df_embaralhado))
print("Exemplo de linhas embaralhadas:")
print(df_embaralhado.head(10))

