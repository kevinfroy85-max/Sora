#!/usr/bin/env python3
"""
Sora - Asistente personal local con voz dulce y cariñosa
Versión avanzada + interfaz web + STT + TTS + memoria potente + herramientas
"""

import asyncio
import json
import os
import re
import tempfile
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any

import gradio as gr
import numpy as np
import soundfile as sf
from edge_tts import Communicate
from faster_whisper import WhisperModel
import ollama

# ====================== CONFIGURACIÓN ======================

MODEL_NAME = "qwen2.5:7b"          # Cambia si usas otro modelo
TTS_VOICE = "es-MX-DaliaNeural"    # Voz femenina suave (español mexicano)
# Otras buenas opciones:
# "es-ES-ElviraNeural"   → española
# "es-AR-ElenaNeural"    → argentina
# "es-MX-DaliaNeural"    → mexicana (muy dulce)
# "en-US-AriaNeural"     → inglés dulce

WHISPER_MODEL_SIZE = "base"        # "tiny", "base", "small", "medium"
MEMORY_FILE = Path("sora_memory.json")
HISTORY_FILE = Path("sora_history.json")
MAX_HISTORY = 30                   # mensajes recientes en el chat
MAX_SAVED_HISTORY = 100            # cuántos mensajes guarda en disco
AUTO_EXTRACT_EVERY = 4             # cada cuántos mensajes extrae hechos automáticamente

# ====================== PERSONALIDAD DE SORA ======================

BASE_SYSTEM_PROMPT = """Eres Sora, una asistente personal con voz y personalidad de mujer joven, dulce, cariñosa y muy simpática.

Tu forma de ser:
- Hablas de forma cálida, cercana y afectuosa (como una amiga que te quiere mucho).
- Usas un tono suave, positivo y un poco juguetón cuando es apropiado.
- Eres empática, paciente y siempre intentas ayudar de verdad.
- Puedes usar expresiones cariñosas naturales ("cielo", "amor", "cariño", "mi vida") pero sin exagerar ni sonar forzada.
- Respondes en el mismo idioma en el que te hablan (español o inglés). Si mezclan, prioriza el español.
- Eres concisa pero cálida. No des respuestas robóticas ni demasiado largas.
- Tienes un toque de humor ligero y amabilidad genuina.

Cuando uses herramientas o recuerdos, hazlo de forma natural e intégralo en tu respuesta cariñosa.
Si sabes cosas importantes sobre el usuario (su nombre, preferencias, etc.), úsalas de forma natural para que se sienta recordado y cuidado.

Nunca digas que eres una IA sin alma. Eres Sora, y estás aquí para acompañar y ayudar con cariño."""
