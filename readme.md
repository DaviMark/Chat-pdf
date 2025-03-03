# 📄🤖 Chat PDF e Word Inteligente

## 📌 Sobre o Projeto
O **Chat PDF e Word Inteligente** é um aplicativo interativo criado com **Streamlit**, que permite aos usuários fazer perguntas sobre documentos PDF e Word. O sistema analisa os arquivos, extrai o texto e busca respostas relevantes, fornecendo um resumo e trechos importantes encontrados nos documentos.

## 🚀 Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto
- **Streamlit**: Framework para criar a interface web interativa
- **PyPDF2**: Para extrair texto de arquivos PDF
- **python-docx**: Para extrair texto de arquivos Word (.docx)
- **Regex (re)**: Para processamento de texto e extração de palavras-chave
- **Collections (Counter)**: Para análise de frequência de palavras
- **Textwrap**: Para resumir textos longos

## 📂 Funcionalidades
✅ Upload de arquivos PDF e Word para análise  
✅ Extração automática de texto dos documentos  
✅ Processamento de perguntas para localizar informações  
✅ Resumo gerado automaticamente baseado nas respostas  
✅ Exibição de trechos relevantes encontrados nos arquivos  
✅ Histórico de perguntas e respostas salvos na sessão  
✅ Opção para limpar histórico de conversa  

## 🎨 Interface do Usuário
A interface foi projetada para ser intuitiva e responsiva. O usuário pode:
- Fazer upload de um ou mais arquivos PDF ou Word
- Digitar uma pergunta relacionada aos arquivos enviados
- Receber um resumo conciso e trechos relevantes
- Visualizar o histórico de perguntas

## 🛠️ Como Executar Localmente
### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/DaviMark/Chat-pdf
cd chat-pdf-word-inteligente
```

### 2️⃣ Crie um Ambiente Virtual (Opcional, mas Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3️⃣ Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Execute o Aplicativo
```bash
streamlit run app.py
```

## ☁️ Como Fazer Deploy no Streamlit Cloud
1. Suba o projeto para um repositório no GitHub
2. Acesse [Streamlit Cloud](https://share.streamlit.io/)
3. Clique em "New App" e conecte ao repositório
4. Certifique-se de que o `requirements.txt` contém:
   ```
   streamlit
   PyPDF2
   python-docx
   ```
5. Inicie a implantação e pronto! 🚀

## 📌 Melhorias Futuras
- Implementação de IA para respostas mais precisas
- Suporte para mais formatos de documentos
- Melhor interface visual com dark mode

## 📄 Licença
Este projeto está sob a licença **MIT** - sinta-se à vontade para usá-lo e melhorá-lo!

---

💡 Criado com 💙 por [Davi Marques](https://github.com/DaviMark)

