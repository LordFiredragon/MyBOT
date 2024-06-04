from speech_processor import SpeechProcessing
from command_processor import CommandProcessing
from openai_agent import OpenAIAgent
from todo_manager import ToDoManager


class MainApp:
    def __init__(self):
        self.speech_process = SpeechProcessing()
        self.command_process = CommandProcessing()
        self.openai_agent = OpenAIAgent()
        self.todo_manager = ToDoManager()

    def run(self):
        while True:
            command = self.speech_process.listen()
            if command != "":

                label = self.command_process.handle_comment(command)
                print(f"Label recognised as : [label]")

                if label == "To-do list":
                    print("Something to do with ToDos list manager!")
                else:
                    get_answer = self.openai_agent.get_response(command)
                    print(f"Hamura Answered:{get_answer}")


if __name__ == "_main_":
    app = MainApp()
    app.run()
