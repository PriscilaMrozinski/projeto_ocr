# Memória Local – Raízes Urbanas da nossa história

**Descrição:**  
Memória Local é um aplicativo web que usa **OCR (reconhecimento óptico de caracteres)** para transformar imagens de documentos históricos em texto pesquisável, revelando nossa memória urbana.

---

## Tecnologias utilizadas

- **Python 3.11** – linguagem de programação usada para desenvolver o aplicativo e integrar todas as funcionalidades.  
- **Flask** – framework web leve que permite criar o servidor e as páginas do aplicativo.  
- **Pillow** – biblioteca para abrir, processar e manipular imagens dentro do Python.  
- **pytesseract** – biblioteca Python que faz a ponte entre o Python e o Tesseract, permitindo extrair texto de imagens.  
- **Tesseract-OCR** – motor de reconhecimento óptico de caracteres que lê imagens e transforma os textos nelas em texto digital pesquisável.

---

## Funcionalidades

- Upload de imagens de documentos históricos.  
- Extração de texto em **português** usando OCR.  
- Visualização do texto extraído no navegador.  
- Busca de palavras dentro do texto reconhecido, com destaque.

---

## Instalação

1. Clone o repositório:

2. Crie um ambiente virtual: python -m venv venv

3. Ative o ambiente virtual, no Git Bash: source venv/Scripts/activate

4. Instale as dependências: pip install -r requirements.txt

5. Abra o navegador e acesse localmente: http://127.0.0.1:5000/