from main import pd, np, plt, sns
from geracao_dados import df_vendas

# Verificando as informações gerais do DataFrame
print("\n--- Informações Gerais do DataFrame (df_vendas.info()) ---\n")
df_vendas.info()

print("\n--- Verificando valores ausentes ---\n")
print(df_vendas.isna().sum()) # Quantidade = 6 Nan e Status_Entrega = 3 Nan

print("\n--- Verificando a presença de registros duplicados ---\n")
print(f"Número de linhas duplicadas: {df_vendas.duplicated().sum()}")

print("\n--- Estatísticas descritivas para colunas númericas ---\n")
# Usamos o describe() para ter uma noção inicial. Note que Preco_Unitario não aparecerá por ser 'object'.
print(df_vendas.describe())

print("\n--- Estatísticas descritivas para colunas categóricas ---\n")
print(df_vendas.describe(include = [object]))

# Verificando as informações gerais do DataFrame
print("\n--- Tipos de dados ---\n")
print(df_vendas.dtypes)
