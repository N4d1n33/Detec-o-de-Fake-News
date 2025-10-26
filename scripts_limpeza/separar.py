import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv(r"C:\Users\Nadine\Downloads\dataset_final_fakenews.csv", sep=";", encoding="utf-8-sig")

# divide 80% treino 20% teste
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df["label"])

train_df.to_csv(r"C:\Users\Nadine\Downloads\train_bertimbau.csv", sep=";", index=False, encoding="utf-8-sig")
test_df.to_csv(r"C:\Users\Nadine\Downloads\test_bertimbau.csv", sep=";", index=False, encoding="utf-8-sig")

print("dataset dividido")
print(f"treino: {len(train_df)} notícias")
print(f"teste:  {len(test_df)} notícias")
