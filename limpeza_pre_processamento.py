from main import np, pd, plt, sns
from geracao_dados import df_vendas

# Copiando o  DataFrame para manter o original intacto
df_limpo = df_vendas.copy()

# --- 1. Corrigindo Tipos de Dados ---
print("Corrigindo tipos de dados...")
# Convertendo 'Preco_Unitario' para numérico, tratando erros
# errors = 'coerce' transformará valores inválidos (como 'valor_invalido') em Nan
df_limpo['Preco_Unitario'] = pd.to_numeric(df_limpo['Preco_Unitario'], errors = 'coerce')

# Convertendo 'Cliente_ID' para numérico, tratando erros
df_limpo['Cliente_ID'] = pd.to_numeric(df_limpo['Cliente_ID'], errors = 'coerce').astype('Int64') # Usamos Int64 para permitir NaN
# Convertendo 'Quantidade' para numérico, especificamente para 'Int64'
df_limpo['Quantidade'] = df_limpo['Quantidade'].astype('Int64')
print("\n",df_limpo.dtypes)

# --- 2. Tratando Valores Ausentes (NaN) ---
print("Tratando valores ausentes...")

# Para 'Quantidade', vamos preencher com a mediana, que é mais robusta a outliers
mediana_qnt = df_limpo['Quantidade'].median()
df_limpo.fillna({'Quantidade': mediana_qnt}, inplace = True) # Fill = Preencher e inplace -> salva no proprio DataFrame

# Para 'Status_Entrega', podemos preencher com o valor mais frequente(moda)
moda_status = df_limpo['Status_Entrega'].mode()[0]
df_limpo['Status_Entrega'] = df_limpo['Status_Entrega'].fillna(moda_status)

# Para 'Preco_Unitario' e 'Cliente_ID', onde o NaN foi gerado por erro ou falta de informação,
# a melhor abordagem é remover as linhas, pois não podemos inferir esses dados.
df_limpo.dropna(subset = ['Preco_Unitario', 'Cliente_ID'], inplace = True)

# --- 3. Removendo Duplicatas ---
print("Removendo registros duplicados...")
df_limpo.drop_duplicates(inplace = True)

# --- 4. Tratando Outliers ---
# Vamos visualizar o outlier na coluna 'Quantidade'
print("Tratando outliers...")
sns.boxplot(x = df_limpo['Quantidade'])
plt.title('Boxplot de Quantidade (Antes de tratar outlier)')
plt.show()

# Vamos remover valores de 'Quantidade' que estão muito distantes da média
# Uma abordagem comum é remover valores que estão além de 3 desvios padrão da média.
limite_superior = df_limpo['Quantidade'].mean() + 3 * df_limpo['Quantidade'].std()
df_limpo = df_limpo[df_limpo['Quantidade'] < limite_superior]

# Verificando o resultado
sns.boxplot(x = df_limpo['Quantidade'])
plt.title('Boxplot de Quantidade (Depois de tratar outlier)')
plt.show()

# --- Verificação Final ---
print("\n---  Verificação Final Pós-Limpeza ---\n")
df_limpo.info()
print("\nValores ausentes restantes:\n",df_limpo.isna().sum())
print(f"\nLinhas duplicadas restantes: {df_limpo.duplicated().sum()}")


