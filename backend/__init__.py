from . import llm
from . import stt
from . import tts
from . import audio_utils

from .llm import query_hokkien_llm
from .stt import transcribe_hokkien
from .tts import synthesize_hokkien

__version__ = "0.1.0"

__all__ = [
    "llm",
    "stt",
    "tts",
    "audio_utils",
    "query_hokkien_llm",
    "transcribe_hokkien",
    "synthesize_hokkien"
]