# AI CLI Assistant

A lightweight command-line AI assistant powered by Ollama that enables interactive conversations with local Large Language Models (LLMs). The application provides model switching, persona customization, chat session persistence, session restoration, and session deletion directly from the terminal.

---

# Features

## Interactive AI Chat

Chat with locally hosted Ollama models directly from the command line.

Features include:

- Streaming AI responses
- Multi-turn conversations
- Conversation memory within the current session
- Support for any installed Ollama model

Command:

```bash
/chat
```

---

## Persona Configuration

Customize how the AI behaves by setting a persona.

Examples:

- Senior Software Engineer
- DevOps Engineer
- Technical Writer
- Database Administrator
- Python Instructor

Command:

```bash
/persona
```

The selected persona is applied as the system prompt for future conversations.

---

## Model Selection

Switch between installed Ollama models at runtime.

The application automatically retrieves available models from Ollama and displays them for selection.

Command:

```bash
/setmodel
```

Examples:

- llama3
- mistral
- deepseek-r1
- codellama

---

## Save Conversations

Save the current conversation to disk for future use.

Saved sessions include:

- Session label
- Model used
- Timestamp
- Complete message history

Command:

```bash
/save
```

### Smart Save Behavior

- New conversations create a new session file.
- Restored conversations update the existing session file instead of creating duplicates.

---

## Restore Conversations

Restore a previously saved conversation.

Command:

```bash
/restore
```

When a conversation is restored:

- Message history is loaded
- Original model is restored
- Session metadata is loaded
- Conversation can continue seamlessly

---

## Delete Conversations

Delete the currently restored conversation.

Command:

```bash
/delete
```

Notes:

- A conversation must first be restored using `/restore`
- The currently loaded session file will be deleted
- The application automatically resets after deletion

---

## Reset Conversation

Reset the application to a fresh session.

Command:

```bash
/reset
```

This action:

- Clears conversation history
- Resets the system prompt
- Restores the default model
- Clears active session information

---

## Help Menu

Display all available commands.

Command:

```bash
/help
```

---

## Exit Application

Exit the application safely.

Command:

```bash
/exit
```

---

# Requirements

## Software Requirements

- Python 3.10+
- Ollama installed and running
- At least one Ollama model installed

Install a model:

```bash
ollama pull llama3
```

Verify installation:

```bash
ollama list
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/mtopico/ai-cli-assistant.git
cd ai-cli-assistant
```

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```cmd
.venv\Scripts\activate
```

## Install Dependencies

Install all required packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

# Configuration

Create a `.env` file in the project root.

Example:

```env
ollama_host=http://localhost:11434
ollama_model=llama3
session_storage_path=app/storage/sessions
```

## Environment Variables

| Variable | Description |
|-----------|-------------|
| `ollama_host` | Ollama server URL |
| `ollama_model` | Default model loaded at startup |
| `session_storage_path` | Directory where conversation sessions are stored |

---

# Running the Application

From the project root:

```bash
python -m app.main
```

Alternatively:

```bash
cd app
python main.py
```

Upon startup:

```text
AI Assistant using Ollama
Type '/exit' to quit
```

The default model configured in `.env` will be loaded automatically.

---

# Available Commands

| Command | Description |
|----------|-------------|
| `/help` | Show available commands |
| `/chat` | Start chatting with the AI |
| `/persona` | Configure AI persona |
| `/setmodel` | Change Ollama model |
| `/save` | Save current conversation |
| `/restore` | Restore a saved conversation |
| `/delete` | Delete the currently restored conversation |
| `/reset` | Reset the current session |
| `/exit` | Exit the application |

---

# Conversation Storage

Conversations are stored as JSON files inside the configured storage directory.

Example structure:

```json
{
  "label": "Python Learning Session",
  "model": "llama3",
  "timestamp": "2026-06-20T14:30:00",
  "messages": [
    {
      "role": "system",
      "content": "You are a Python Instructor."
    },
    {
      "role": "user",
      "content": "Explain list comprehensions."
    }
  ]
}
```

---

# Project Structure

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
│   ├── storage/
│   │   └── sessions/
│   │
│   └── main.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# Architecture

## CommandController

Responsible for:

- Command processing
- User interaction
- Chat lifecycle management
- Ollama communication
- Model switching
- Persona configuration
- Session management

## StoreChatService

Responsible for:

- Saving conversations
- Restoring conversations
- Listing saved sessions
- Deleting session files

---

# Application Flow

1. Load environment configuration.
2. Connect to Ollama.
3. Retrieve installed models.
4. Load the default model.
5. Wait for user commands.
6. Stream AI responses.
7. Save, restore, update, or delete sessions as needed.

---

# License

This project is provided for educational, learning, and personal use.