from pydantic import BaseModel, Field


class AnaliseDeComportamento(BaseModel):
    """Estrutura para análise de sentimento e idioma do texto."""

    comportamento: str = Field(description="('positivo', 'negativo' ou 'neutro')")
    resumo: str = Field(description="Resumo do comportamento do texto em uma frase")
