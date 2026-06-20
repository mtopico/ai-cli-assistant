from ollama import chat, Client
from dotenv import load_dotenv
from rich.console import Console
from app.services.StoreChatService import StoreChatService
from datetime import datetime
import os

class CommandController:
    
    def __init__(self):
        load_dotenv()
        self.client = Client(os.environ.get("OLLAMA_HOST", "http://ollama:11434"))
        self.model_list = []
        self.console = Console()
        self.force_loop_break = False
        self.init_models()
        self.store_chat_service = StoreChatService()
        self.set_default()

    def set_default(self):
        self.model = os.environ.get("OLLAMA_MODEL", "llama3")
        self.messages = [{
            "role": "system",
            "content": "You are a helpful and friendly assistant. Always provide clear and concise answers to the user's questions."
        }]
        self.session_file = None
        self.session_label = None

    def ask_what_to_do(self):
        user_input = self.console.input("[bold blue]What would you like to do? (/help to see commands): ")
        self.handle_user_input(user_input)

    def converse(self):
        self.list_commands()
        self.__set_persona()

    def __set_persona(self):
        personality_input = self.console.input("[bold blue]Set the AI persona: ")
        if personality_input.strip():
            self.messages[0]["content"] = f"You are a {personality_input} assistant"
        self.console.print(f"[bold green]The AI assistant will behave as a [bold red]{personality_input}\n")

    def __send_message(self):

        inline_commands = """
            You can use the following inline commands during the conversation:
            /save - Save the current conversation to a file
            /restore - Restore a conversation from a file
            /reset - Reset the conversation and start fresh
            /delete - Delete the current conversation file (only available if a conversation is loaded)
            /help - List all general commands
            /exit - Exit the program
        """

        self.console.print(f"[bold cyan]{inline_commands}")

        while True:
            assistance_response = ""
            user_input = self.console.input("[bold blue]Tell me something: ")

            self.handle_user_input(user_input, lambda self, user_input: self.messages.append({'role': 'user','content': user_input}))

            if self.force_loop_break:
                self.force_loop_break = False
                break

            response = self.client.chat(
                model=self.model,
                messages= self.messages,
                stream=True
            )

            self.console.print("[bold yellow]AI Response: ", end='')

            for chunk in response:
                self.console.print(chunk["message"]["content"], end='')
                assistance_response += chunk["message"]["content"]

            self.messages.append({
                'role': 'assistant',
                'content': assistance_response
            })

            self.console.print("\n[bold green]-----------------------------")

    def end_program(self):
        self.console.print("[bold red]-----------------------------")
        self.console.print("[bold red]Exiting the AI Assistant. Goodbye!")
        self.console.print("[bold red]-----------------------------")
        exit()

    def list_commands(self):
        commands = """
        Here are some commands you can use:
        /help - List all available commands
        /persona - Set the AI persona
        /chat - Start a conversation with the AI assistant
        /setmodel - Select available model from provider
        /exit - Exit the program
        """
        self.console.print(f"[bold cyan]{commands}")

    def handle_user_input(self, user_input, callback=None):

        if user_input == "/help":
            self.force_loop_break = True
            self.list_commands()
            self.ask_what_to_do()
        elif user_input == "/persona":
            self.force_loop_break = True
            self.__set_persona()
            self.ask_what_to_do()
        elif user_input == "/exit":
            self.force_loop_break = True
            self.end_program()
        elif user_input == "/chat":
            self.force_loop_break = False
            self.__send_message()
        elif user_input == "/setmodel":
            self.force_loop_break = True
            self.set_model_list()
        elif user_input == "/save":
            self.force_loop_break = True
            self.save_conversation()
        elif user_input == "/restore":
            self.force_loop_break = True
            self.restore_conversation()
        elif user_input == "/reset":
            self.force_loop_break = True
            self.reset_conversation()
        elif user_input == "/delete":
            self.force_loop_break = True
            self.delete_conversation()
        else:
            if callback:
                callback(self, user_input)
            else:
                self.console.print("[bold red]Unknown command. Please try again.\n")
                self.ask_what_to_do()

    def init_models(self):
        models = self.client.list()
        if( models and models.models):
            for model in models.models:
                self.model_list.append(model.model)
            self.model_list.sort()
        else:
            self.console.print("[bold red]No models found from provider. This app needs a valid model to function properly.\n")
            self.end_program()


    def set_model_list(self):
        if(self.model_list):
            for index, model in enumerate(self.model_list, start=1):
                self.console.print(f"[bold blue][{index}] [white]{model}")
            while True:

                user_input = self.console.input("[bold blue]Select a model by number (/exit to cancel): ")

                try:

                    if user_input == "/exit":
                        self.ask_what_to_do()
                        break

                    selected_index = int(user_input) - 1

                    if( selected_index < 0 or selected_index >= len(self.model_list)):
                        self.console.print("[bold red]Invalid input. Please enter a valid number.\n")
                    else:
                        self.model = self.model_list[selected_index]
                        self.console.print(f"[bold green]Model set to [bold red]{self.model}\n")
                        self.ask_what_to_do()
                        break

                except ValueError:
                    self.console.print("[bold red]Invalid input. Please enter a valid number.\n")
                    
        else:
            self.console.print("[bold red]No models found from provider. This app needs a valid model to function properly.\n")
            self.end_program()
        
    def save_conversation(self):
        if self.session_file:
            self.store_chat_service.save_chat(self.session_label, self.model, self.messages, session_file=self.session_file)
        else:
            user_input = self.console.input("[bold blue]Enter a label for this conversation: ")
            if user_input.strip():
                self.store_chat_service.save_chat(user_input.strip(), self.model, self.messages, session_file=self.session_file)

        self.console.print(f"[bold green]Conversation saved\n")
        self.ask_what_to_do()

    def restore_conversation(self):
        chats = self.store_chat_service.list_saved_chats()
        if chats:
            for index, chat in enumerate(chats, start=1):
                timestamp = datetime.fromisoformat(chat["timestamp"])
                formatted_date = timestamp.strftime("%Y-%m-%d %I:%M:%S %p") if 'timestamp' in chat else "Unknown"
                self.console.print(f"[bold blue][{index}] [white]{chat['label']} - {formatted_date}")
            while True:
                user_input = self.console.input("[bold blue]Select a conversation to restore by number (/exit to cancel): ")
                try:
                    if user_input == "/exit":
                        self.ask_what_to_do()
                        break

                    selected_index = int(user_input) - 1

                    if( selected_index < 0 or selected_index >= len(chats)):
                        self.console.print("[bold red]Invalid input. Please enter a valid number.\n")
                    else:
                        selected_chat = chats[selected_index]
                        self.model = selected_chat["model"]
                        self.messages = selected_chat["messages"]
                        self.console.print(f"[bold green]Conversation restored\n")
                        self.session_file = selected_chat["file_name"]
                        self.session_label = selected_chat["label"]
                        self.__send_message()
                        break

                except ValueError:
                    self.console.print("[bold red]Invalid input. Please enter a valid number.\n")

    def reset_conversation(self):
        self.set_default()
        self.console.print(f"[bold green]Conversation reset\n")
        self.ask_what_to_do()

    def delete_conversation(self):
        if self.session_file:
            is_deleted = self.store_chat_service.delete_chat(self.session_file)
            if is_deleted:
                self.set_default()
                self.console.print(f"[bold green]Conversation deleted\n")
            else:
                self.console.print(f"[bold red]No conversation file to delete\n")
            self.ask_what_to_do()
        else:
            self.console.print(f"[bold red]No conversation loaded. Restore a conversation first.\n")
            self.ask_what_to_do()
