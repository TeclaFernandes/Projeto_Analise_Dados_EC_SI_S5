# 📊 Análise de Dados em Saúde Pública  
### Exames Citopatológicos e Infraestrutura Oncológica no Brasil

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow)
![Status](https://img.shields.io/badge/Status-Concluído-green)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

---

## 🎯 Sobre o Projeto

Este projeto realiza uma análise exploratória de dados (EDA) aplicada à saúde pública brasileira, com foco em:

- 🧪 Exames citopatológicos (Papanicolau) em mulheres (25–64 anos)  
- 🏥 Hospitais habilitados para tratamento de câncer  

O objetivo é identificar **padrões, desigualdades regionais e possíveis gargalos no sistema de saúde**.

---

## 📁 Estrutura do Projeto

```
ANALISEDADOSCANCERDEMAMA/
│
├── app/
│   ├── Artigo1.0.py
│   └── dashboard.py
│
├── Datasets/
│   ├── ccmec25a64_main.csv
│   ├── ccmhhcac.csv
│   ├── dados_tratados.csv
│   └── df_limpo_sem_outliers.csv
│
├── Documentação/
│   ├── Artigo_Previne_Brasil.pdf
│   ├── OBSERVAÇÕES.txt
│   └── RoteiroTrabalho.pdf
│
├── Notebooks/
│   ├── N1/
│   │   ├── Notebook1.ipynb
│   │   ├── Notebook2.ipynb
│   │   ├── Notebook3.ipynb
│   │   ├── Notebook4.ipynb
│   │   └── analise_cruzada_exames_hospitais.png
│   └── N2/
│
├── README.md
└── requirements.txt
```


---

## 📊 Principais Análises

### 📌 1. Estatísticas Descritivas
- Média, mediana e moda  
- Percentis (P10 → P95)  
- Variância e desvio padrão  
- Coeficiente de variação  

💡 **Insight:**  
Municípios apresentam **altíssima variabilidade**, enquanto o Brasil mostra estabilidade.

---

### 📌 2. Distribuição dos Dados

- 📉 Histogramas  
- 📦 Boxplots  
- 📈 Curvas CDF  

💡 **Insight:**  
- Municípios → forte assimetria (cauda longa)  
- UF → comportamento intermediário  
- Brasil → distribuição equilibrada  

---

### 📌 3. Detecção de Outliers

- Método: **IQR (Intervalo Interquartil)**  

| Etapa | Registros |
|------|---------:|
| Antes | 5986 |
| Depois | 4257 |
| Removidos | 1729 |

💡 **Resultado:**  
Redução significativa de distorções estatísticas.

---

### 📌 4. Dispersão dos Dados

| Nível | CV (%) | Interpretação |
|------|------:|-------------|
| Municípios | 953% | Extremamente heterogêneo |
| UF | 101% | Moderado |
| Brasil | 15% | Estável |

---

### 📌 5. Análise Cruzada

Comparação entre:

- Número de exames realizados  
- Quantidade de hospitais disponíveis  

💡 **Objetivo:**  
Identificar possíveis desigualdades entre **demanda e infraestrutura de saúde**.

---

## 📉 Visualizações

O projeto inclui:

- Histogramas
- Boxplots
- Gráficos de dispersão
- Gráficos por UF
- Análise comparativa entre regiões

📍 Exemplo:

![Análise Cruzada](Notebooks/N1/analise_cruzada_exames_hospitais.png)

---

## ⚠️ Limitações

- Dados secundários (SUS)
- Possível subnotificação
- Falta de dados clínicos e socioeconômicos
- Cobertura desigual entre regiões

---

## 🧠 Conclusões

✔ O dataset é **hierárquico e heterogêneo**  
✔ Municípios apresentam alta variabilidade  
✔ Dados agregados (UF/Brasil) são mais estáveis  
✔ Remoção de outliers foi essencial para qualidade da análise  

---

## 🚀 Próximos Passos

- 📊 Dashboard interativo (Streamlit)
- 🗺️ Mapas geográficos
- 🤖 Modelos preditivos
- 📈 Análise temporal avançada

---

## 🛠️ Tecnologias

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

---

## ▶️ Como Executar

```bash
pip install -r requirements.txt
```

## 👨‍💻 Autor

Projeto desenvolvido para disciplina de Estatística S4
com foco em análise de dados aplicada à saúde pública.

## ⭐ Destaque

Este projeto demonstra:

✔ Análise estatística completa <br>
✔ Limpeza e tratamento de dados <br>
✔ Detecção de outliers <br>
✔ Visualização de dados <br>
✔ Interpretação orientada a negócio