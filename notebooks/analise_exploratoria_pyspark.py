from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, trim
from pyspark.sql.types import IntegerType

# Inicializar a sessão Spark
spark = SparkSession.builder \
    .appName("Analise de Segurança Publica") \
    .getOrCreate()

# Caminhos dos arquivos
caminho_arquivo1 = '../dados/indicadores_ocorrecia_uf.csv'
caminho_arquivo2 = '../dados/indicadores_vitimas_uf.csv'

# Carregar os dados
df_ocorrencias = spark.read.option("header", True).option("sep", ",").csv(caminho_arquivo1)
df_vitimas = spark.read.option("header", True).option("sep", ",").csv(caminho_arquivo2)

# Padronizar colunas (nomes para minúsculo e snake_case)
def padronizar_colunas(df):
    for old_name in df.columns:
        new_name = (old_name.lower()
                            .strip()
                            .replace(" ", "_")
                            .replace("ê", "e")
                            .replace("í", "i"))
        df = df.withColumnRenamed(old_name, new_name)
    return df

df_ocorrencias = padronizar_colunas(df_ocorrencias)
df_vitimas = padronizar_colunas(df_vitimas)

# Corrigir tipos e padronizar textos
df_ocorrencias = df_ocorrencias \
    .withColumn("ano", col("ano").cast(IntegerType())) \
    .withColumn("ocorrencias", col("ocorrencias").cast(IntegerType())) \
    .withColumn("uf", upper(trim(col("uf")))) \
    .withColumn("tipo_crime", upper(trim(col("tipo_crime"))))

df_vitimas = df_vitimas \
    .withColumn("ano", col("ano").cast(IntegerType())) \
    .withColumn("vitimas", col("vitimas").cast(IntegerType())) \
    .withColumn("uf", upper(trim(col("uf")))) \
    .withColumn("tipo_crime", upper(trim(col("tipo_crime")))) \
    .withColumn("sexo_da_vitima", upper(trim(col("sexo_da_vitima"))))

# Verificar colunas
print("Colunas Ocorrências:", df_ocorrencias.columns)
print("Colunas Vítimas:", df_vitimas.columns)

# Verificar valores nulos
print("\nNulos - Ocorrências:")
df_ocorrencias.select([col(c).isNull().alias(c) for c in df_ocorrencias.columns]).show()

print("\nNulos - Vítimas:")
df_vitimas.select([col(c).isNull().alias(c) for c in df_vitimas.columns]).show()

# Valores únicos
print("\nUFs únicas:")
df_ocorrencias.select("uf").distinct().show()

print("\nTipos de crime únicos:")
df_ocorrencias.select("tipo_crime").distinct().show()

print("\nAnos disponíveis:")
df_ocorrencias.select("ano").distinct().orderBy("ano").show()

# Estatísticas descritivas
print("\nResumo estatístico - Ocorrências:")
df_ocorrencias.describe().show()

print("\nResumo estatístico - Vítimas:")
df_vitimas.describe().show()

# Ocorrências totais por ano
print("\nOcorrências totais por ano:")
df_ocorrencias.groupBy("ano").sum("ocorrencias").orderBy("ano").show()

# Vítimas totais por ano
print("\nVítimas totais por ano:")
df_vitimas.groupBy("ano").sum("vitimas").orderBy("ano").show()

# Insights
print("\n1. Crimes mais comuns no Brasil:")
df_ocorrencias.groupBy("tipo_crime").sum("ocorrencias").orderBy("sum(ocorrencias)", ascending=False).show()

print("\n2. Estados com mais ocorrências totais:")
df_ocorrencias.groupBy("uf").sum("ocorrencias").orderBy("sum(ocorrencias)", ascending=False).show()

print("\n3. Estados com mais vítimas:")
df_vitimas.groupBy("uf").sum("vitimas").orderBy("sum(vitimas)", ascending=False).show()

print("\n4. Distribuição por sexo das vítimas:")
df_vitimas.groupBy("sexo_da_vitima").sum("vitimas").show()

# Finalizar a sessão Spark
spark.stop()
