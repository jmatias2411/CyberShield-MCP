# prompts/threat_response.py

def suggest_block_action(threat_description: str) -> str:
    """
    Prompt que sugiere qué acción tomar ante una amenaza.
    Ideal para modelos LLM que interactúan con el servidor MCP.
    """
    return (
        f"Se detectó la siguiente amenaza:\n\n{threat_description}\n\n"
        "¿Qué acción de ciberseguridad deberíamos ejecutar?\n"
        "- Bloquear IP\n"
        "- Bloquear puerto\n"
        "- Ejecutar diagnóstico de red\n"
        "- Ignorar\n"
        "Explica brevemente tu elección."
    )
