# 📥 Coleta de Dados, Modelagem e Conclusões

## 📥 Coleta de Dados

Foram utilizados neste projeto dois conjuntos de dados com abrangência nacional obtidos a partir de dois arquivos em formato CSV:

- `indicadores_ocorrecia_uf.csv`: contendo informações sobre a quantidade de ocorrências de crimes por tipo, estado, ano e mês.
- `indicadores_vitimas_uf.csv`: contendo informações sobre o número de vítimas por tipo de crime, estado, ano, mês e sexo da vítima.

Esses dados foram carregados localmente para análise com bibliotecas como `pandas` e `numpy`.

## 🧰 Modelagem e Preparação

### Padronização

- Padronização de nomes de colunas (`snake_case`).
- Conversão de colunas categóricas para valores uniformes.
- Verificação e tratamento de valores nulos.
  - Apenas 1 valor nulo identificado na coluna `ocorrencias`, que foi tratado/removido.

### Estrutura dos Dados

- As tabelas contêm dados entre os anos de 2015 e 2022.
- As UFs e os tipos de crime foram categorizados para permitir agrupamentos e comparações.
- Sexo das vítimas dividido entre `MASCULINO`, `FEMININO` e `SEXO NI`.

## 💡 Conclusões

- O Brasil possui alta incidência de crimes patrimoniais (furto/roubo de veículos).
- A distribuição das ocorrências é desigual entre os estados, com maior concentração em São Paulo e Rio de Janeiro.
- O Nordeste tem maior concentração de vítimas, sugerindo fragilidade na prevenção à violência.
- Crimes letais (como homicídios e estupros) exigem atenção especial de políticas públicas.
- A análise temporal evidencia queda de crimes em 2020, possivelmente associada à pandemia de COVID-19.
- A predominância de vítimas do sexo masculino é clara, porém a subnotificação no campo de gênero pode mascarar dados reais sobre violência contra a mulher.

Essas informações podem orientar intervenções estratégicas e políticas públicas mais eficazes.
