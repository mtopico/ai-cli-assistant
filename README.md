# ai-cli-assistant

## What the app is about

`ai-cli-assistant` is a simple Python command-line assistant that sends prompts to an Ollama model and prints the replies in the terminal.

The app lets you:
- set a persona when the session starts
- have a back-and-forth conversation in the terminal
- keep the current chat history for the duration of the session
- exit at any time by typing `exit`

The main entrypoint is `app/main.py`.

## Dependencies

### Runtime requirements

- Python 3.12 or compatible Python 3 environment
- Access to an Ollama server
- An available Ollama model, defaulting to `llama3`

### Python packages

Install the packages from `requirements.txt`, including:

- `ollama`
- `python-dotenv`
- `httpx`
- `pydantic`
- `rich`

## How to run

### Local Python run

From the `ai-cli-assistant` folder:

```powershell
pip install -r requirements.txt
python app/main.py
```

Optional environment variables in `.env`:

- `ollama_host` defaults to `http://ollama:11434`
- `ollama_model` defaults to `llama3`

If you are running Ollama on your local machine instead of Docker, set:

```env
ollama_host=http://localhost:11434
```

### Docker-based run from the workspace root

If you want to use the provided Docker setup:

```powershell
docker compose up --build -d
docker exec -it ai-engineer-py bash
cd /workspace/ai-cli-assistant
pip install -r requirements.txt
python app/main.py
```