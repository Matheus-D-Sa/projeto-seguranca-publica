import pandas as pd

# Caminho até o arquivo
caminho_arquivo1 = '../dados/indicadores_ocorrecia_uf.csv'
caminho_arquivo2 = '../dados/indicadores_vitimas_uf.csv'

# Configurações visuais
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Carregar os arquivos CSV
df_ocorrencias = pd.read_csv(caminho_arquivo1, encoding='utf-8', sep=',')
df_vitimas = pd.read_csv(caminho_arquivo2, encoding='utf-8', sep=',')

# Padronizar nomes de colunas
def padronizar_colunas(df):
    df.columns = (
        df.columns.str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("ê", "e")
        .str.replace("í", "i")
    )
    return df

df_ocorrencias = padronizar_colunas(df_ocorrencias)
df_vitimas = padronizar_colunas(df_vitimas)

# Verificar nomes das colunas
print("Colunas Ocorrências:", df_ocorrencias.columns)
print("Colunas Vítimas:", df_vitimas.columns)

# Corrigir tipos de dados
df_ocorrencias['ano'] = pd.to_numeric(df_ocorrencias['ano'], errors='coerce')
df_ocorrencias['ocorrencias'] = pd.to_numeric(df_ocorrencias['ocorrencias'], errors='coerce')
df_ocorrencias['uf'] = df_ocorrencias['uf'].str.strip().str.upper()
df_ocorrencias['tipo_crime'] = df_ocorrencias['tipo_crime'].str.strip().str.upper()

df_vitimas['ano'] = pd.to_numeric(df_vitimas['ano'], errors='coerce')
df_vitimas['vitimas'] = pd.to_numeric(df_vitimas['vitimas'], errors='coerce')
df_vitimas['uf'] = df_vitimas['uf'].str.strip().str.upper()
df_vitimas['tipo_crime'] = df_vitimas['tipo_crime'].str.strip().str.upper()
df_vitimas['sexo_da_vitima'] = df_vitimas['sexo_da_vitima'].str.strip().str.upper()

# Verificando valores nulos
print("\nNulos - Ocorrências:")
print(df_ocorrencias.isnull().sum())

print("\nNulos - Vítimas:")
print(df_vitimas.isnull().sum())

# Visualizar dados únicos
print("\nUFs únicas:", df_ocorrencias['uf'].unique())
print("\nTipos de crime únicos:", df_ocorrencias['tipo_crime'].unique())
print("\nAnos disponíveis:", sorted(df_ocorrencias['ano'].dropna().unique()))

# Resumo estatístico dos dados
print("\n", df_ocorrencias.describe())
print("\n", df_vitimas.describe())

# Ocorrências totais por ano
print("\n", df_ocorrencias.groupby('ano')['ocorrencias'].sum())

# Vítimas totais por ano
print("\n", df_vitimas.groupby('ano')['vitimas'].sum())


## Principais Insights:
print("\n1. Crimes mais comuns no Brasil:")
print(df_ocorrencias.groupby('tipo_crime')['ocorrencias'].sum().sort_values(ascending=False))

print("\n2. Estados com mais ocorrências totais:")
print(df_ocorrencias.groupby('uf')['ocorrencias'].sum().sort_values(ascending=False))

print("\n3. Estados com mais vítimas:")
print(df_vitimas.groupby('uf')['vitimas'].sum().sort_values(ascending=False))

print("\n4. Distribuição por sexo das vítimas:")
print(df_vitimas.groupby('sexo_da_vitima')['vitimas'].sum())