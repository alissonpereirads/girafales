from langchain_core.runnables import RunnablePassthrough
from prompt.avaliacao_prompts import get_avaliacao_prompt
from parsers.avaliacao_parser import AvaliacaoOutputParser
from config.config import get_groq
from langchain_core.output_parsers import StrOutputParser


def get_avaliacao_chain():
    llm = get_groq()
    prompt = get_avaliacao_prompt()
    output_parser = AvaliacaoOutputParser()

    chain = (
        RunnablePassthrough()
        | prompt
        | llm
        | output_parser
        | StrOutputParser()  # Converte a saída final em string
    )

    return chain
