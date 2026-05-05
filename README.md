# 🌱🏙️ Memória Local – Raízes Urbanas da nossa história

A história não vive apenas nos livros. Ela está guardada em papéis antigos, em arquivos esquecidos, em registros que o tempo insiste em apagar aos poucos.

Cada documento carrega mais do que palavras, carrega decisões, contextos, trajetórias e fragmentos de vidas que ajudaram a construir o que somos hoje. O passado não está distante. Ele se reflete nas ruas que percorremos, nas cidades que habitamos e nas escolhas que moldam o presente.

Preservar essa memória não é apenas um ato de registro, mas de continuidade. Porque compreender de onde viemos nos dá clareza sobre para onde estamos indo.

Em um mundo cada vez mais digital, muitos desses registros ainda permanecem inacessíveis, presos em formatos físicos, limitados pelo tempo e pela dificuldade de consulta. E, aos poucos, aquilo que não é acessível corre o risco de ser perdido e esquecido.

É nesse contexto que surge o Memória Local, como uma forma de aproximar o passado do presente, utilizando a tecnologia para transformar registros históricos em informação viva, pesquisável e acessível.

Porque no fim aquilo que não pode ser acessado se perde com o tempo. Conectar o passado ao presente é dar continuidade à nossa história presente nas ruas, nos documentos e na vida das cidades.

---

## 🏛️ Sobre o projeto

Memória Local é um aplicativo web que utiliza **OCR (reconhecimento óptico de caracteres)** para transformar imagens de documentos históricos em texto pesquisável, revelando e valorizando a memória urbana. 

A proposta é facilitar o acesso a informações que muitas vezes estão restritas a arquivos físicos, permitindo que registros do passado se tornem mais acessíveis, organizados e úteis no presente. 

Com isso, o projeto busca contribuir para a preservação da história local, conectando tecnologia e patrimônio cultural de forma simples e funcional.

---

## ⚙️ Tecnologias utilizadas

- **Python 3.11** – linguagem de programação usada para desenvolver o aplicativo e integrar todas as funcionalidades.  
- **Flask** – framework web que permite criar o servidor e as páginas do aplicativo.  
- **Pillow** – biblioteca para abrir, processar e manipular imagens dentro do Python.  
- **pytesseract** – biblioteca Python que faz a ponte entre o Python e o Tesseract, permitindo extrair texto de imagens.  
- **Tesseract-OCR** – motor de reconhecimento óptico de caracteres que lê imagens e transforma os textos nelas em texto digital pesquisável.

---

## 🧩 Funcionalidades

- Upload de imagens de documentos históricos.  
- Extração de texto em **português** usando OCR.  
- Visualização do texto extraído no navegador.  
- Busca de palavras dentro do texto reconhecido, com destaque.

---
 
## 📌 Instalação

1. Clone o repositório.
2. Crie um ambiente virtual: python -m venv venv
3. Ative o ambiente virtual, no Git Bash: source venv/Scripts/activate
4. Instale as dependências: pip install -r requirements.txt
5. Abra o navegador e acesse localmente: http://127.0.0.1:5000/
