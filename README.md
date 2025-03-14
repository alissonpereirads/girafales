
# Avaliador de Comportamento de Alunos com LLM

Bem-vindo ao repositório do projeto **Girafales - Avaliador de Comportamento de Alunos**! Este é um projeto de estudo que desenvolvi para explorar o uso de **Large Language Models (LLMs)** e suas ferramentas, como **LangChain** e **Streamlit**. Como estudante de Ciência de Dados no 3º semestre, tenho me dedicado a projetos práticos para aprimorar minhas habilidades em Inteligência Artificial e Machine Learning, e este é um dos resultados desse esforço.

---

## 🚀 Sobre o Projeto

Este projeto é uma aplicação web que utiliza um modelo de linguagem (LLM) para analisar e avaliar o comportamento de alunos com base em textos descritivos. A aplicação classifica o comportamento como **positivo**, **negativo** ou **neutro** e fornece um resumo analítico. O objetivo é demonstrar como LLMs podem ser aplicados em contextos educacionais para auxiliar professores e gestores na avaliação de alunos.

### Ferramentas e Tecnologias Utilizadas

- **LangChain**: Framework para integração e manipulação de LLMs.
- **Streamlit**: Biblioteca para criação de interfaces web simples e interativas.
- **Groq API**: Utilizada para acessar o modelo **LLaMA 3** (70B), um dos mais avançados disponíveis.
- **Python**: Linguagem principal do projeto.
- **Git e GitHub**: Para versionamento e compartilhamento do código.

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como parte do meu processo de aprendizado em **Inteligência Artificial** e **Ciência de Dados**. Meu objetivo é:
- Aprender a integrar LLMs em aplicações práticas.
- Explorar frameworks como LangChain para criar pipelines de processamento de linguagem natural.
- Desenvolver interfaces amigáveis com Streamlit.
- Consolidar conhecimentos em Python e APIs.

Além disso, este projeto faz parte do meu portfólio pessoal, que estou construindo para buscar oportunidades de **estágio** na área de Ciência de Dados e IA. Acredito que a combinação de teoria e prática é essencial para o crescimento profissional, e projetos como este são uma forma de demonstrar minhas habilidades e paixão pela área.

---

## 📋 Como Funciona?

A aplicação funciona da seguinte forma:
1. O usuário insere um texto descrevendo o comportamento de um aluno.
2. O texto é processado por um pipeline que utiliza o LangChain para chamar o modelo LLaMA 3 via Groq API.
3. O modelo classifica o comportamento como **positivo**, **negativo** ou **neutro** e gera um resumo analítico.
4. A interface exibe o resultado de forma clara, com destaque visual (verde para positivo, vermelho para negativo e amarelo para neutro).

### Exemplo de Uso

**Entrada:**
```text
João tem se mostrado bastante atento e participativo nas aulas. Ele contribui com ideias interessantes e sempre está disposto a ajudar os colegas.
```

**Saída:**
```markdown
**Sentimento:** Positivo

**Análise:** João demonstra um comportamento exemplar, sendo respeitoso, participativo e colaborativo, contribuindo para um ambiente de aprendizado agradável e produtivo.
```

---

## 🛠️ Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior.
- Conta na [Groq](https://groq.com/) para acessar a API.
- Instalação das bibliotecas necessárias.

### Passo a Passo

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/avaliador-comportamento-alunos.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API Groq:
   ```env
   GROQ_API_KEY=sua_chave_aqui
   ```

4. Execute a aplicação:
   ```bash
   streamlit run main.py
   ```

5. Acesse a aplicação no navegador através do link fornecido pelo Streamlit.

---

## 🌟 Destaques do Projeto

- **Integração com LLM**: Uso avançado de um modelo de linguagem para análise de texto.
- **Interface Amigável**: Desenvolvida com Streamlit, é simples e intuitiva.
- **Código Modular**: Organizado em módulos (chains, parsers, prompts) para facilitar manutenção e expansão.
- **Visualização Dinâmica**: Feedback visual imediato com cores e formatação.

---

## 📚 Aprendizados

Este projeto me permitiu:
- Aprofundar meu conhecimento em LLMs e suas aplicações.
- Trabalhar com APIs e frameworks modernos como LangChain e Streamlit.
- Desenvolver habilidades em engenharia de prompt e processamento de linguagem natural.
- Melhorar minha capacidade de documentar e compartilhar projetos no GitHub.

---

## 📩 Contato

Se você gostou deste projeto ou tem alguma sugestão, ficarei feliz em conversar! Estou em busca de oportunidades de **estágio** na área de Ciência de Dados e IA, e adoraria contribuir com projetos desafiadores.

- **LinkedIn**: [Alisson Pereira](https://www.linkedin.com/in/alisson-pereira-ds/)
- **E-mail**: alissonpereira.contato@gmail.com
- **GitHub**: [alissonpereirads](https://github.com/alissonpereirads)

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito com 💙 por [Alisson Pereira]
*Estudante de Ciência de Dados | Apaixonado por IA e Aprendizado Contínuo*






