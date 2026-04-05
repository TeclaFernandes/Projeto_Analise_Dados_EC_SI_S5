from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Cabeçalho padrão em todas as páginas
        self.set_font('helvetica', 'B', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'Trabalho Prático 01 - Estatística Computacional', border=False, align='R')
        self.ln(10)

    def footer(self):
        # Rodapé com número da página
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

# Inicializar o PDF
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# --- TÍTULO ---
pdf.set_font('helvetica', 'B', 16)
pdf.set_text_color(0, 0, 0)
titulo = "Análise Estatística e Preditiva do Rastreamento do Câncer do Colo do Útero no Brasil: Um Estudo sobre Desigualdades e Eficiência na Atenção Primária"
pdf.multi_cell(0, 8, titulo, align='C')
pdf.ln(5)

# --- AUTORES ---
pdf.set_font('helvetica', 'I', 12)
pdf.cell(0, 10, "Autores: Lucas, Fernando, Tecla, Gustavo.", align='C')
pdf.ln(15)

# --- RESUMO ---
pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 10, "1. Resumo (Abstract)", ln=True)
pdf.set_font('helvetica', '', 11)
resumo = (
    "O financiamento da Atenção Primária à Saúde (APS) no Brasil é fortemente balizado pelo desempenho "
    "dos municípios. Este artigo propõe uma análise estatística computacional do volume de exames "
    "citopatológicos (Papanicolau) realizados em mulheres de 25 a 64 anos, utilizando dados governamentais "
    "abertos. Através de técnicas de limpeza de dados, estatística descritiva e modelagem preditiva "
    "(Regressão Linear), o estudo investiga a eficiência dos indicadores do programa Previne Brasil e "
    "expõe as profundas desigualdades regionais na oferta desse serviço. Resultados preliminares indicam "
    "uma alta assimetria na distribuição dos exames, evidenciada por uma discrepância significativa entre a "
    "média nacional e a moda municipal, ressaltando os desafios de infraestrutura nos pequenos municípios."
)
pdf.multi_cell(0, 6, resumo, align='J')
pdf.ln(5)

# --- INTRODUÇÃO ---
pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 10, "2. Introdução e Contextualização", ln=True)
pdf.set_font('helvetica', '', 11)
introducao = (
    "O monitoramento de indicadores de saúde é fundamental para a elaboração de políticas públicas eficientes. "
    "No contexto brasileiro, o programa Previne Brasil estabelece metas para o repasse de recursos do Sistema "
    "Único de Saúde (SUS). Um dos pilares desse programa é a Saúde da Mulher, com foco direto na prevenção do "
    "câncer de colo de útero.\n\n"
    "O objetivo deste estudo é analisar a eficiência e a distribuição temporal e geográfica da realização de "
    "exames preventivos (Papanicolau) no país. O direcionamento principal é investigar as desigualdades latentes "
    "nos dados: como o volume de atendimentos varia drasticamente dependendo da região, evidenciando disparidades "
    "de infraestrutura, capacidade de atendimento e eficiência na submissão de dados pelos municípios."
)
pdf.multi_cell(0, 6, introducao, align='J')
pdf.ln(5)

# --- COMPREENSÃO DOS DADOS ---
pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 10, "3. Compreensão e Estrutura dos Dados", ln=True)
pdf.set_font('helvetica', '', 11)
dados = (
    "A base de dados analisada (ccmec25a64.csv) é proveniente do Ministério da Saúde e foca especificamente no "
    "indicador de Câncer de Colo e Mama - Exames Citopatológicos (CCMEC) para a faixa etária de 25 a 64 anos.\n\n"
    "O dataset original é estruturado em uma matriz de 55.702 linhas e 25 colunas, possuindo uma granularidade "
    "baseada no município e no mês de competência. As variáveis foram classificadas computacionalmente em nominais "
    "(identificadores geográficos), ordinais (marcadores temporais) e quantitativas discretas (volume absoluto de "
    "exames realizados)."
)
pdf.multi_cell(0, 6, dados, align='J')
pdf.ln(5)

# --- METODOLOGIA ---
pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 10, "4. Metodologia Computacional", ln=True)
pdf.set_font('helvetica', '', 11)
metodologia = (
    "O trabalho foi estruturado em um pipeline de dados dividido em etapas modulares:\n"
    "- Engenharia e Limpeza: Tratamento de valores anômalos e mitigação de ruídos de municípios com reporte zerado.\n"
    "- Análise Exploratória e Descritiva: Cálculo de medidas de tendência central e dispersão para mapear o cenário.\n"
    "- Modelagem Preditiva: Aplicação de Regressão Linear para identificar tendências de crescimento no volume nacional."
)
pdf.multi_cell(0, 6, metodologia, align='J')
pdf.ln(5)

# --- RESULTADOS ---
pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 10, "5. Resultados e Discussões (Preliminar)", ln=True)
pdf.set_font('helvetica', '', 11)
resultados = (
    "A análise descritiva inicial revela um cenário de forte desigualdade na eficiência dos indicadores municipais. "
    "A disparidade entre a Média Municipal (aprox. 11.317 exames) e a Moda Municipal (1 exame) comprova estatisticamente "
    "uma distribuição de cauda longa altamente assimétrica.\n\n"
   )
pdf.multi_cell(0, 6, resultados, align='J')


nome_arquivo = "Artigo_Previne_Brasil.pdf"
pdf.output(nome_arquivo)
print(f"✅ Arquivo gerado com sucesso: {nome_arquivo}")