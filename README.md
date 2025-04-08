# 🚨 Projeto Semantix: Análise de Segurança Pública nas Grandes Cidades do Brasil

## 🤩 1. Problema e Justificativa

A segurança pública é um dos pilares fundamentais para o bem-estar da população. Em grandes centros urbanos, a criminalidade, a violência e a sensação de insegurança têm aumentado significativamente nas últimas décadas. Furtos, assaltos, violência policial, homicídios e crimes patrimoniais se tornaram parte da rotina de muitos cidadãos.

Esse cenário alarmante é impulsionado por fatores como urbanização acelerada, desigualdade social, baixa efetividade das políticas públicas e carência de infraestrutura nas periferias urbanas. Adicionalmente, limitações orçamentárias e dificuldades na gestão e alocação de recursos agravam o problema.

Esse projeto tem como objetivo entender a distribuição e evolução dos principais crimes no Brasil, utilizando dados públicos para apoiar decisões de políticas públicas e ações preventivas. A análise de dados pode contribuir para mapear áreas críticas, identificar correlações com fatores socioeconômicos, avaliar políticas existentes e antecipar estratégias de prevenção. Essa abordagem baseada em dados possibilita uma gestão mais eficiente, transparente e direcionada, colaborando para a construção de cidades mais seguras e justas.

## 🔍 2. Coleta e Fontes de Dados Selecionadas

Foram utilizados dois conjuntos de dados com abrangência nacional, disponibilizados em formato CSV:

#### 1. [Data.gov.br ](https://dados.gov.br/home)– Portal Brasileiro de Dados Abertos

- **Descrição**: Reúne milhares de conjuntos de dados produzidos por órgãos da administração pública brasileira.
- **Tipo de dados estruturados**: CSV, XLS, JSON – ocorrências criminais, segurança, violênciaurbana, policiamento.
- **Método de acesso**: Download direto ou via APIs REST.
- **Aplicabilidade**: Permite análise profunda e integração com indicadores socioeconômicos.

#### 2. [Kaggle ](https://www.kaggle.com)– Base de Dados Internacionais

- **Descrição**: Plataforma de dados com contribuições de governos, ONGs e pesquisadores.
- **Tipo de dados estruturados**: CSV – taxas de criminalidade, violência armada, índices de paz.
- **Método de acesso**: Download direto após login.
- **Aplicabilidade**: Comparativo entre cidades brasileiras e internacionais, identificação de boas práticas.

Ambos os datasets foram carregados localmente para análise e estão disponíveis na pasta `dados/`.

- **indicadores_ocorrecia_uf.csv**: Dados de ocorrências por tipo de crime, ano, mês e estado.
- **indicadores_vitimas_uf.csv**: Dados de vítimas por sexo, tipo de crime, ano, mês e estado.

## 💠 3. Análise Exploratória

Scripts e notebooks em Python foram utilizados para:

- Leitura dos dados e verificação de colunas nulas ou inconsistentes;
- Padronização dos nomes de colunas, estados e tipos de crime;
- Geração de estatísticas descritivas;
- Identificação de crimes mais comuns, distribuição por estado e perfil das vítimas.

### Bibliotecas utilizadas:
- `pandas`

- `SparkSession`

- `col, upper, trim`

- `IntegerType`

## 📊 4. Indicadores e Visualizações

As principais visualizações desenvolvidas incluem:

- 📌 **Crimes mais comuns no Brasil**  
- 📌 **Estados com mais ocorrências totais**
- 📌 **Estados com mais vítimas**
- 📌 **Distribuição por sexo das vítimas**
- 📈 **Tendência anual de ocorrências e vítimas**
- 🗺️ **Gráfico interativo com distribuição por UF**
- 🔍 **Filtros por tipo de crime, ano e estado**

As visualizações estão disponíveis no dashboard interativo criado no [Looker Studio](https://lookerstudio.google.com/reporting/88f12e8a-d82b-4521-a21f-819f085874fa).

## 💡 5. Insights e Conclusões

- Os crimes mais recorrentes são os contra o patrimônio: **furto** e **roubo de veículos**.
- **São Paulo** e **Rio de Janeiro** lideram em número absoluto de ocorrências.
- Os estados do **Nordeste** têm os maiores números de vítimas, sugerindo vulnerabilidades sociais e estruturais.
- O número de vítimas do sexo **masculino** é muito maior, mas há um volume significativo de registros com "sexo não informado".
- Houve queda significativa nas ocorrências em 2020, possivelmente relacionada à pandemia.

### Propostas de ação:
- Reforçar o policiamento preventivo em áreas urbanas críticas.
- Criar campanhas de conscientização para melhorar a notificação de gênero das vítimas.
- Investir em políticas públicas voltadas à proteção das populações mais vulneráveis nas regiões Norte e Nordeste.

## 📂 6. Estrutura do Repositório

```
📁 projeto-seguranca-publica/
├── 📁 dados/
│   ├── indicadores_ocorrecia_uf.csv
│   └── indicadores_vitimas_uf.csv
├── 📁 notebooks/
│   └── analise_exploratoria.py
│   └── analise_exploratoria_pyspark.py
├── 📄 coleta_modelagem_conclusoes.md
├── 🔗 dashboard_looker_studio.pdf (ou link direto na descrição)
├── 📄 README.md
└── 📄 relatorio_insights.md
```

## 🔗 7. Acesso ao Dashboard

[Acessar Dashboard no Looker Studio](https://lookerstudio.google.com/reporting/88f12e8a-d82b-4521-a21f-819f085874fa)