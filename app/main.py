from rich.console import Console
from app.controllers.CommandController import CommandController

console = Console()
command_controller = CommandController()

console.print("[bold green]-----------------------------")
console.print("[bold green]AI Assistant using Ollama")
console.print("[bold green]Type '/exit' to quit\n")
console.print("[bold green]Default model used is set in the .env file. Use /setmodel to change it.\n")
console.print("[bold green]-----------------------------")

command_controller.list_commands()
command_controller.ask_what_to_do()
