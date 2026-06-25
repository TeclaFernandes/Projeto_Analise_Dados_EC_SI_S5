# � Análise de Dados em Saúde Pública - Mamografia e Citopatologia

Projeto desenvolvido para a disciplina de Estatística Computacional, com foco em análise exploratória, visualização e interpretação de dados relacionados a exames de mamografia e citopatologia no Ceará, especialmente nas regiões do Cariri e de Crajubar.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-ff4b4b)
![Status](https://img.shields.io/badge/Status-em%20andamento-yellowgreen)

---

## 🎯 Objetivo do projeto

Este repositório reúne uma coleção de análises, notebooks e recursos visuais para:

- explorar indicadores de saúde pública relacionados a exames de mamografia e citopatologia;
- comparar padrões por município, faixa etária e etnia;
- aplicar técnicas de limpeza, tratamento e visualização de dados;
- gerar relatórios, gráficos e interpretações para apoiar a apresentação dos resultados.

A proposta é organizar o trabalho em etapas de análise, com foco em compreender a distribuição dos exames, possíveis desigualdades regionais e a consistência dos indicadores disponíveis nas bases de dados.

---

## 📁 Estrutura do projeto

```text
AnaliseDadosCancerDeMama/
├── app/
│   ├── Artigo1.0.py
│   └── dashboard.py
├── Datasets/
│   ├── N1/
│   └── N2/
├── Documentação/
│   └── OBSERVAÇÕES.txt
├── Notebooks/
│   ├── N1/
│   └── N2/
├── requirements.txt
└── README.md
```

### Descrição dos diretórios

- app/: scripts auxiliares e protótipos de dashboard.
- Datasets/: arquivos CSV utilizados nas análises, organizados por etapa N1 e N2.
- Documentação/: materiais complementares e observações do projeto.
- Notebooks/: notebooks com a análise exploratória, limpeza, visualização e interpretação dos dados.

---

## 📊 O que está sendo analisado

O trabalho utiliza bases sobre:

- exames de mamografia;
- exames citopatológicos;
- recortes por município;
- distribuição por faixa etária;
- distribuição por grupo étnico;
- comparação entre o total geral e os recortes específicos.

As análises estão organizadas na pasta Notebooks, com foco em estatística descritiva, visualização de dados e interpretação dos resultados.

---

## 🧪 Ferramentas e tecnologias

As principais ferramentas utilizadas no projeto são:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit

O arquivo requirements.txt reúne as dependências básicas para reproduzir as análises.

---

## ▶️ Como executar

1. Crie um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .\.venv\Scripts\activate    # Windows
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Abra os notebooks em Jupyter ou VS Code para executar as análises.

4. Para visualizar o dashboard, execute:

   ```bash
   streamlit run app/dashboard.py
   ```

---

## 📌 Notebooks principais

A pasta Notebooks contém a sequência de análises do projeto, incluindo:

- contexto e introdução;
- análise inicial dos dados;
- limpeza e filtragem;
- estatística descritiva;
- comparação por etnia e faixa etária;
- visualizações e relatórios.

Esses notebooks formam a base da análise e também servem como material de apresentação e revisão do trabalho.

---

## 📈 Resultados esperados

Com este projeto, espera-se:

- organizar e padronizar os dados de saúde pública;
- identificar padrões e diferenças entre grupos e regiões;
- gerar visualizações que facilitem a leitura dos resultados;
- construir uma base consistente para relatórios e apresentações acadêmicas.

---

## ⚠️ Observações importantes

- Os dados utilizados são baseados em fontes públicas e já tratadas para fins de análise.
- Algumas etapas podem depender da estrutura local dos arquivos CSV.
- O projeto está em evolução e pode receber ajustes conforme a análise avança.

---

## 👩‍💻 Autor

Projeto desenvolvido como parte da disciplina de Estatística Computacional, com foco em análise exploratória aplicada à saúde pública.

---

## ✅ Resumo

Este repositório reúne uma análise de dados aplicada à saúde pública, com atenção especial à organização, visualização e interpretação dos resultados. A estrutura do projeto foi atualizada para melhor refletir o que está sendo desenvolvido e como navegar pelos materiais disponíveis.