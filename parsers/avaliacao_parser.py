from langchain.schema import BaseOutputParser


class AvaliacaoOutputParser(BaseOutputParser):

    def parse(self, text: str) -> str:
        # Remove espaços em branco no início e no final
        text = text.strip()

        # Verifica se o texto contém "Sentimento" e "Análise"
        if "Sentimento:" in text and "Análise:" in text:
            # Divide o texto em partes
            partes = text.split("Análise:")
            sentimento = partes[0].replace("Sentimento:", "").strip()
            analise = partes[1].strip()

            # Formata a saída com Markdown para negrito
            return f"**Sentimento:** {sentimento}\n\n**Análise:** {analise}"
        else:
            # Se o formato não for o esperado, retorna o texto original
            return text
