# 📝 Formatador de Texto

Aplicação web desenvolvida em **Python e Flask** que permite transformar e organizar textos de maneira simples e prática, por meio de uma interface intuitiva.

O projeto foi criado para praticar o desenvolvimento de aplicações web com Python, o processamento de formulários e a utilização de templates HTML com Flask.

## ✨ Funcionalidades

- **🔠 Converter para maiúsculas:** transforma todas as letras do texto em letras maiúsculas.
- **🔡 Converter para minúsculas:** transforma todas as letras do texto em letras minúsculas.
- **📝 Capitalizar frases:** converte a primeira letra de cada frase para maiúscula.
- **🧹 Remover espaços extras:** elimina espaços desnecessários e normaliza os espaços entre as palavras.

## 🛠️ Tecnologias utilizadas

- **Python** — lógica e processamento dos textos.
- **Flask** — framework utilizado para desenvolver a aplicação web.
- **HTML5** — estrutura da interface.
- **CSS3** — estilização dos elementos da página.
- **Jinja2** — renderização dinâmica dos templates HTML, integrada ao Flask.

## 📂 Estrutura do projeto

```text
Formatador-de-Texto/
├── app.py
├── templates/
│   └── index.html
└── README.md
```

- `app.py`: configura as rotas, recebe os dados do formulário, executa as operações de formatação e envia os resultados para a página.
- `templates/index.html`: contém a interface da aplicação, os botões de formatação e a exibição do resultado.
- `README.md`: documentação do projeto.

## ⚙️ Como executar o projeto

### 1. Pré-requisitos

- Python 3 instalado.
- Git instalado, caso queira clonar o repositório.

### 2. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd NOME_DA_PASTA
```

### 3. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

Ative o ambiente virtual:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Instale o Flask

```bash
pip install Flask
```

### 5. Execute a aplicação

```bash
python app.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

## 💡 Aprendizados

Durante o desenvolvimento, pratiquei conceitos importantes, como:

- Criação de aplicações web utilizando Python e Flask.
- Definição de rotas com suporte a requisições GET e POST.
- Recebimento e processamento de dados enviados por formulários HTML.
- Integração entre Python e templates HTML com Jinja2.
- Manipulação de strings e criação de operações de formatação de texto.
- Estilização de interfaces com CSS.

## 🚀 Possíveis melhorias futuras

- Adicionar um botão para copiar o resultado.
- Permitir baixar o texto formatado em um arquivo.
- Implementar a opção de desfazer a formatação.
- Melhorar a experiência em dispositivos móveis.
- Adicionar novas ferramentas de edição de texto.

---

Desenvolvido como projeto de prática e aprendizado em desenvolvimento web com Python.

