from presentation.console_ui import ConsoleUI
from data.json_repository import JSONRepository
from presentation.controllers import Controller

def main():
    repo = JSONRepository('db.json')
    ui = ConsoleUI()
    controller = Controller(repo, ui)
    controller.run()

if __name__ == '__main__':
    main()
