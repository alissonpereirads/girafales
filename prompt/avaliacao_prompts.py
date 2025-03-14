from langchain.prompts import ChatPromptTemplate


def get_avaliacao_prompt():
    prompt = ChatPromptTemplate.from_template(
        """
        Você é um especialista em análise de comportamento de alunos. Sua tarefa é analisar o texto fornecido e determinar o sentimento geral (positivo, negativo ou neutro) em relação ao comportamento do aluno, bem como fornecer um resumo analítico em uma frase.

        Instruções:
        1. Leia o texto cuidadosamente.
        2. Determine o sentimento geral em relação ao comportamento do aluno. O sentimento deve ser classificado como 'positivo', 'negativo' ou 'neutro'.
        3. Forneça um resumo analítico em uma frase que capture os principais aspectos do comportamento do aluno.

        Exemplo de Entrada:
        Joao tem se mostrado bastante atento e participativo nas aulas. Ele contribui com ideias interessantes e sempre está disposto a ajudar os colegas. Além disso, é muito cooperativo e respeitoso com todos, trabalhando bem em equipe e resolvendo conflitos de maneira pacífica.

        Exemplo de Saída:
        Sentimento: Positivo
        Analise: Joao demonstra um comportamento exemplar, sendo participativo, cooperativo e respeitoso com os colegas.

        Texto: {texto}
        Sentimento: 
        Analise:
        """
    )
    return prompt
