# ai-cli-assistant

## What the app is about

`ai-cli-assistant` is a simple Python command-line assistant that sends prompts to an Ollama model and prints the replies in the terminal.

The app lets you:
- set a persona when the session starts
- have a back-and-forth conversation in the terminal
- keep the current chat history for the duration of the session
- exit at any time by typing `exit`

The main entrypoint is `app/main.py`.

# ai-cli-assistant
------------------------------------------------------

This Python script, `CommandController.py`, is part of the `ai-cli-assistant` project, a simple command-line AI assistant that communicates with an Ollama model to provide responses in the terminal.


## Dependencies

### Runtime requirements

- Python 3.12 or compatible Python 3 environment
- Access to an Ollama server
- An available Ollama model, defaulting to `llama3`
