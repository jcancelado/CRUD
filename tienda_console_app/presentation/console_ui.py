class ConsoleUI:
    def input(self, prompt: str) -> str:
        return input(prompt)

    def print(self, *args, **kwargs):
        __builtins__['print'](*args, **kwargs)

    def show_menu(self, title: str, options: list):
        print('\n' + title)
        for k, v in options:
            print(f"{k}. {v}")

    def pause(self):
        input('\nPresiona Enter para continuar...')
