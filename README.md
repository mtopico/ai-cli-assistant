# AI CLI Assistant

A command-line AI assistant powered by Ollama that allows users to chat with local LLMs, switch between installed models, customize AI personas, and save or restore conversation sessions.

## Overview

AI CLI Assistant is a lightweight terminal-based chat application that connects to an Ollama server and provides an interactive conversational interface.

The application automatically discovers available Ollama models and allows users to:

- Chat with local AI models
- Change AI personalities
- Switch between installed models
- Save conversations
- Restore previous conversations
- Reset chat sessions

The application uses streaming responses for a real-time chat experience and stores conversation history locally in JSON format.

---

## Features

### AI Chat

Start interactive conversations with locally hosted Ollama models.

```text
/chat
```

Responses are streamed live as they are generated.

---

### Persona Customization

Change how the AI behaves by defining a persona.

```text
/persona
```

Example:

```text
Set the AI persona: senior software engineer
```

The assistant will then behave according to the selected role.

---

### Model Selection

View and switch between installed Ollama models.

```text
/setmodel
```

The application automatically retrieves all available models from Ollama.

Examples:

```text
llama3
deepseek-r1
mistral
codellama
```

---

### Conversation Persistence

Save conversations to disk for future use.

```text
/save
```

Each conversation stores:

- Label
- Model used
- Timestamp
- Complete message history

Sessions are saved as JSON files.

---

### Restore Previous Conversations

Load previously saved conversations.

```text
/restore
```

When restored:

- Previous messages are loaded
- Original model is restored
- Conversation can continue from where it stopped

---

### Reset Conversation

Clear the current session and start fresh.

```text
/reset
```

This restores:

- Default system prompt
- Default model
- Empty conversation history

---

### Command Help

Display available commands.

```text
/help
```

---

### Exit Application

Close the assistant.

```text
/exit
```

---

## Requirements

### Python

Python 3.10+ recommended.

### Ollama

Install Ollama and ensure at least one model is available.

Example:

```bash
ollama pull llama3
```

Verify installation:

```bash
ollama list
```

---

## Python Dependencies

All dependencies are listed in `requirements.txt`.

### Install Dependencies

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```cmd
.venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Installed packages include:

- ollama
- rich
- python-dotenv
- httpx
- pydantic
- tqdm

and their supporting dependencies.

---

## Configuration

Create a `.env` file in the project root.

Example:

```env
ollama_host=http://localhost:11434
ollama_model=llama3
session_storage_path=app/storage/sessions
```

### Configuration Options

| Variable | Description | Default |
|-----------|-------------|----------|
| `ollama_host` | Ollama server URL | `http://ollama:11434` |
| `ollama_model` | Default model to use | `llama3` |
| `session_storage_path` | Directory for saved conversations | `app/storage/sessions` |

---

## Running the Application

From the project root:

```bash
python -m app.main
```

or

```bash
cd app
python main.py
```

After startup you will see:

```text
AI Assistant using Ollama
Type '/exit' to quit

Default model used is set in the .env file.
Use /setmodel to change it.
```

---

## Available Commands

| Command | Description |
|----------|-------------|
| `/help` | Show available commands |
| `/persona` | Set AI personality |
| `/chat` | Start a conversation |
| `/setmodel` | Select an Ollama model |
| `/save` | Save current conversation |
| `/restore` | Restore saved conversation |
| `/reset` | Reset current conversation |
| `/exit` | Exit the application |

---

## Conversation Storage

Saved conversations are stored as JSON files.

Example structure:

```json
{
    "label": "Python Help Session",
    "model": "llama3",
    "timestamp": "2026-06-18T15:30:22",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant"
        },
        {
            "role": "user",
            "content": "Explain Python generators"
        }
    ]
}
```

---

## Project Structure

```text
ai-cli-assistant/
│
├── app/
│   ├── controllers/
│   │   └── CommandController.py
│   │
│   ├── services/
│   │   └── StoreChatService.py
│   │
│   └── main.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## How It Works

1. Application starts.
2. Connects to Ollama.
3. Retrieves available models.
4. Loads the default model from `.env`.
5. Waits for user commands.
6. Streams AI responses in real time.
7. Allows saving and restoring conversation sessions.

---

## License

This project is provided as-is for educational and personal use.