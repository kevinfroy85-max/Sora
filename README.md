# 🌸 Sora — Personal AI Assistant with a Sweet Voice

**Sora** is a local-first personal AI assistant with the personality of a warm, affectionate, and friendly young woman.  
She listens to you, speaks with a soft female voice, remembers important things about you across sessions, and runs entirely on your machine.

Inspired by projects like OpenJarvis, but focused on simplicity, warmth, and ease of use.

> **100% local** · Voice in & out · Long-term memory · Bilingual (Spanish + English)

---

## Features

| Feature | Description |
|---------|-------------|
| 💬 **Chat** | Text or voice conversation |
| 🎤 **Speech-to-Text** | Listens to you with faster-whisper |
| 🗣️ **Text-to-Speech** | Soft female voice via edge-tts (Dalia, Elvira, Aria…) |
| 💕 **Personality** | Sweet, caring, playful and supportive |
| 🌍 **Bilingual** | Replies in Spanish or English depending on what you speak |
| 🧠 **Strong memory** | Remembers your name, likes, important facts, notes and conversation summaries between sessions |
| 🛠️ **Tools** | Time, calculator, personal notes, memory management |
| 🔒 **Private** | Everything stays on your computer (Ollama + local models) |

---

## Quick Start

### 1. Install Ollama
Download from [ollama.com](https://ollama.com) or:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Pull a model
```bash
ollama pull qwen2.5:7b
# Alternatives: llama3.1:8b, qwen2.5:14b, gemma2:9b
```

### 3. Install Python dependencies
```bash
git clone https://github.com/kevinfroy85-max/Sora.git
cd Sora
pip install -r requirements.txt
```

### 4. Run Sora
```bash
python sora.py
```

Open your browser at **http://127.0.0.1:7860**

---

## Memory System

Sora keeps two local files (never uploaded):

| File | Content |
|------|---------|
| `sora_memory.json` | Profile, important facts, likes/dislikes, notes, conversation summaries |
| `sora_history.json` | Chat history (restored when you restart) |

### Useful phrases

| You say | Sora does |
|---------|-----------|
| «Me llamo Ana» / «Call me Carlos» | Saves your name |
| «Me gusta el café» | Remembers likes |
| «No me gusta madrugar» | Remembers dislikes |
| «Recuerda que trabajo en diseño» | Saves an important fact |
| «Guarda esta nota: comprar leche» | Saves a personal note |
| «¿Qué sabes de mí?» | Tells you everything she remembers |
| «Olvida que me gusta el café» | Forgets specific information |
| «Mis notas» | Shows your notes |

She also **automatically** extracts important facts from conversations and creates short summaries.

---

## Customization

Edit the top of `sora.py`:

```python
MODEL_NAME = "qwen2.5:7b"
TTS_VOICE = "es-MX-DaliaNeural"   # Soft Mexican Spanish
```

### Recommended voices (edge-tts)

| Voice ID | Style |
|----------|-------|
| `es-MX-DaliaNeural` | Mexican, very sweet (default) |
| `es-ES-ElviraNeural` | Spanish (Spain), soft |
| `es-AR-ElenaNeural` | Argentine |
| `en-US-AriaNeural` | English, warm |
| `en-US-JennyNeural` | English, friendly |

List all voices:
```bash
edge-tts --list-voices | grep -E "es-|en-US"
```

---

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) running
- Microphone (optional, only for voice input)
- 4–8 GB RAM recommended (depends on the model)

---

## Project Structure

```
Sora/
├── sora.py            # Main application
├── requirements.txt   # Python dependencies
├── LICENSE            # MIT
├── README.md
└── .gitignore
```

---

## Roadmap ideas

- [ ] Wake-word support
- [ ] More tools (weather, calendar, web search)
- [ ] Optional vector memory
- [ ] Docker image
- [ ] Desktop packaging (Tauri / Electron)

---

## License

MIT License — free to use, modify and share.

---

Made with care 💕  
Inspired by the spirit of local-first personal AI.
