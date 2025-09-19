"""8. Конфігурація через контекстні менеджери
Напишіть власний контекстний менеджер для роботи з файлом конфігурацій (формат .ini або .json). Менеджер має автоматично зчитувати конфігурацію при вході в контекст і записувати зміни в файл після завершення роботи."""

import json


class ConfigManager:
    """Context manager for reading and writing JSON configuration"""

    def __init__(self, filename):
        #Initialize
        self.filename = filename
        self.config = {}

    def __enter__(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print(f"Файл з іменем '{self.filename}' не знайдено")
        return self.config

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.config, file, indent=4)


if __name__ == "__main__":
    #Create config file
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump({"theme": "dark", "font_size": 12}, file)
        print(json.dumps({"theme": "dark", "font_size": 12}, indent=4))

    #Modify config file
    with ConfigManager("config.json") as config:
        config["theme"] = "light"
        config["font_size"] = 10

        print(json.dumps(config, indent=4))
