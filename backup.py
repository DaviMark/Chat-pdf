import streamlit as st
import PyPDF2
import textwrap
import time
import re
from collections import Counter
import docx  # Biblioteca para manipular arquivos Word

# Configuração da página
st.set_page_config(page_title="Chat PDF e Word Inteligente 📄🤖", page_icon="📄", layout="wide")

# Função para extrair texto do PDF
def extrair_texto_pdf(pdf_file):
    """Extrai o texto de um arquivo PDF."""
    texto = ""
    leitor = PyPDF2.PdfReader(pdf_file)
    for pagina in range(len(leitor.pages)):
        texto += leitor.pages[pagina].extract_text() + "\n"
    return texto

# Função para extrair texto do Word
def extrair_texto_word(word_file):
    """Extrai o texto de um arquivo Word (.docx)."""
    texto = ""
    doc = docx.Document(word_file)
    for paragrafo in doc.paragraphs:
        texto += paragrafo.text + "\n"
    return texto

# Lista de palavras comuns que podem ser ignoradas
palavras_comuns = {"o", "é", "de", "do", "da", "um", "uma", "os", "as", "em", "para", "por", "com", "sobre"}

# Função para extrair palavras importantes da pergunta
def extrair_palavras_importantes(pergunta):
    """Remove palavras comuns e mantém apenas termos importantes."""
    palavras = re.findall(r'\b\w+\b', pergunta.lower())  # Separa palavras
    palavras_filtradas = [p for p in palavras if p not in palavras_comuns]  # Remove palavras comuns
    return palavras_filtradas

# Função para encontrar parágrafos onde a pergunta aparece
def encontrar_paragrafos(texto, pergunta):
    """Busca frases onde as palavras-chave aparecem."""
    palavras_chave = extrair_palavras_importantes(pergunta)  # Obtém palavras-chave
    if not palavras_chave:
        return []

    texto_lower = texto.lower()
    frases = texto.replace("\n", " ").split(". ")  # Divide o texto em frases

    # Verifica se pelo menos uma palavra-chave está na frase
    resultados = [frase.strip() + "." for frase in frases if any(palavra in frase.lower() for palavra in palavras_chave)]
    
    return resultados

# Função para gerar um resumo curto
def gerar_resumo(resultados):
    """Gera um resumo simplificado do conteúdo encontrado."""
    if not resultados:
        return "Nenhuma informação relevante encontrada."

    resumo = " ".join(resultados)
    resumo_curto = textwrap.shorten(resumo, width=350, placeholder="...")
    return resumo_curto

# Função para salvar histórico
def salvar_historico(historico):
    """Salva o histórico de perguntas e respostas na sessão."""
    st.session_state["historico"] = historico

# Função para carregar histórico
def carregar_historico():
    """Carrega o histórico de perguntas e respostas da sessão."""
    return st.session_state.get("historico", [])

# Função para limpar histórico
def limpar_historico():
    """Limpa todo o histórico de interação."""
    st.session_state["historico"] = []

# Interface Streamlit
st.title("📄🔍 Chat com PDF e Word Inteligente 🤖")

# Barra lateral
st.sidebar.header("📂 Enviar Arquivos")

# Upload de arquivos
arquivos = st.sidebar.file_uploader("Envie um ou mais PDFs ou Word", type=["pdf", "docx"], accept_multiple_files=True)

# Botão para limpar histórico
if st.sidebar.button("🗑️ Limpar Conversa"):
    limpar_historico()
    st.toast("🔄 Conversa limpa!", icon="✅")
    time.sleep(0.5)
    st.rerun()

# Inicializa histórico
historico = carregar_historico()

# Exibe histórico com animação
for item in historico:
    with st.chat_message("user"):
        st.write(f"💬 **Pergunta:** {item['pergunta']}")
    with st.chat_message("assistant"):
        st.write(f"🤖 **Resumo:** {item['resumo']}")
        for i, trecho in enumerate(item["resultados"], 1):
            st.write(f"📌 **Trecho {i}:**\n> {trecho}\n")

# Caixa de entrada para perguntas
pergunta = st.chat_input("Digite sua pergunta sobre os PDFs ou Word...")

# Função para manter a rolagem no lugar
def manter_rolagem():
    """Impede que o Streamlit role automaticamente para o final da página."""
    if "scroll_position" not in st.session_state:
        st.session_state.scroll_position = 0
    else:
        st.session_state.scroll_position = st.session_state.scroll_position

# Executando a função para controlar a rolagem
manter_rolagem()

if arquivos and pergunta:
    textos_pdfs_word = []
    for arquivo in arquivos:
        if arquivo.type == "application/pdf":
            texto_extraido = extrair_texto_pdf(arquivo)
        elif arquivo.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            texto_extraido = extrair_texto_word(arquivo)
        textos_pdfs_word.append(texto_extraido)

    texto_completo = " ".join(textos_pdfs_word)  # Junta todos os textos extraídos

    resultados = encontrar_paragrafos(texto_completo, pergunta)

    if resultados:
        resumo = gerar_resumo(resultados)
        with st.chat_message("user"):
            st.write(f"💬 **Pergunta:** {pergunta}")
        
        with st.chat_message("assistant"):
            st.success("✅ **Resumo das informações encontradas:**")
            st.write(resumo)
            st.success("🔎 **Trechos Relevantes:**")
            for i, trecho in enumerate(resultados, 1):
                st.write(f"📌 **Trecho {i}:**\n> {trecho}\n")

        historico.append({"pergunta": pergunta, "resumo": resumo, "resultados": resultados})
        salvar_historico(historico)
    else:
        with st.chat_message("user"):
            st.write(f"💬 **Pergunta:** {pergunta}")
        with st.chat_message("assistant"):
            st.warning("❌ Não encontrei essa informação nos PDFs ou Word enviados.")
