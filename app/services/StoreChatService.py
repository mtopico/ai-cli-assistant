import json
import os
from datetime import datetime

class StoreChatService:
    def __init__(self):
        self.storage_path = os.getenv("session_storage_path", "app/storage/sessions")

    def save_chat(self, label, model, messages, session_file=None):

        current_time = datetime.now()
        timestamp = current_time.strftime("%y%m%d_%H%M%S")
        file_name = session_file if session_file else f"session_{timestamp}.json"

        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

        with open(f"{self.storage_path}/{file_name}", "w") as f:
            json.dump({"label": label, "model": model, "timestamp": current_time.isoformat(), "messages": messages}, f, indent=4)

        return file_name

    def list_saved_chats(self):
        if not os.path.exists(self.storage_path):
            return []

        files = [f for f in os.listdir(self.storage_path) if f.endswith(".json")]
        chats = []
        for file in files:
            with open(f"{self.storage_path}/{file}", "r") as f:
                chat_data = json.load(f)
                chat_data["file_name"] = file
                chats.append(chat_data)
        return chats

    def delete_chat(self, file_name):
        file_path = f"{self.storage_path}/{file_name}"
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False