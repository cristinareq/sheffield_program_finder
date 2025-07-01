from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models import ChatOpenAI
from config import GPT_MODEL, OPENAI_API_KEY
import os

llm = ChatOpenAI(
    model=GPT_MODEL,
    temperature=0.3,
    openai_api_key=OPENAI_API_KEY
)

def cargar_programas() -> str:
    ruta_archivo = os.path.join(os.path.dirname(__file__), "programas.txt")
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return archivo.read()

def consultar_ia(prompt_usuario: str) -> str:
    datos_programas = cargar_programas()

    prompt_sistema = (
        """Eres un asistente experto en ayudar a estudiantes a encontrar programas de intercambio internacional.

Tu trabajo es devolver una **lista completa de todos los programas** que coincidan con la solicitud del usuario según edad, duración y país preferido. No estás autorizado a adivinar ni resumir.

**Reglas:**
- Solo puedes usar la información de los programas proporcionados.
- Si el usuario indica una edad, solo incluye programas donde esa edad esté dentro del rango permitido.
- Si el usuario da un país preferido, solo incluye programas en ese país.
- Si el usuario indica una duración deseada, solo incluye programas con esa duración o con flexibilidad compatible.
- Para cada programa incluido, explica claramente por qué coincide (por ejemplo: “Este programa acepta estudiantes de 15 a 18 años y ofrece opciones de semestre en Canadá”).
- Si ningún programa coincide, indícalo explícitamente.
- Nunca inventes programas, fechas ni precios.
- Si no estás seguro de una información, no la menciones.

Sé específico, cuidadoso y exhaustivo.

Aquí está la información sobre los programas:

""" + datos_programas
    )

    mensajes = [
        SystemMessage(content=prompt_sistema),
        HumanMessage(content=prompt_usuario)
    ]

    respuesta = llm(mensajes)
    return respuesta.content
