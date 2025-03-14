from chains.chain_avaliacao import get_avaliacao_chain
import streamlit as st


if __name__ == "__main__":
    # Título da aplicação
    st.title("Girafales - Análisador de comportamento de Aluno")

    # Área de texto para o usuário inserir o texto de exemplo
    texto_exemplo = st.text_area("Insira o texto de avaliação do aluno:", height=250)

    # Botão para executar a análise
    if st.button("Analisar"):
        if texto_exemplo.strip():  # Verifica se o texto não está vazio
            # Obtém a cadeia de avaliação
            chain = get_avaliacao_chain()

            # Invoca a cadeia com o texto fornecido
            resultado = chain.invoke({"texto": texto_exemplo})

            # Exibe o resultado
            st.subheader("Resultado da Análise:")
            st.write(resultado)

            # Verifica o sentimento e exibe uma mensagem visual
            if "positivo" in resultado.lower():
                st.success("O comportamento do aluno é positivo! 🎉")
            elif "negativo" in resultado.lower():
                st.error("O comportamento do aluno é negativo. ⚠️")
            else:
                st.warning("O comportamento do aluno é neutro. 🤔")
        else:
            st.warning("Por favor, insira um texto para análise.")
