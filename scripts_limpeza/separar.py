import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv(
    r"C:\Users\Nadine\Downloads\Final.csv",
    sep=";",
    encoding="utf-8-sig"
)


minimo = df["label"].value_counts().min()
while minimo % 10 != 0:
    minimo -= 1

df_balanceado = (
    df.groupby("label", group_keys=False)
    .sample(n=minimo, random_state=42)
)

df_balanceado = (
    df_balanceado
    .sample(frac=1, random_state=42)
    .reset_index(drop=True)
)


train_val_df, test_df = train_test_split(
    df_balanceado,
    test_size=0.20,
    random_state=42,
    stratify=df_balanceado["label"]
)


train_df, val_df = train_test_split(
    train_val_df,
    test_size=0.25,
    random_state=42,
    stratify=train_val_df["label"]
)

train_df.to_csv(
    r"C:\Users\Nadine\Downloads\train_dataset.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

val_df.to_csv(
    r"C:\Users\Nadine\Downloads\val_dataset.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

test_df.to_csv(
    r"C:\Users\Nadine\Downloads\test_dataset.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig"
)


print("\ntreino")
print(train_df["label"].value_counts())
print("Total treino:", len(train_df))

print("\nvalidação")
print(val_df["label"].value_counts())
print("Total validação:", len(val_df))

print("\nteste")
print(test_df["label"].value_counts())
print("Total teste:", len(test_df))