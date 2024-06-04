import openai
from dotenv import load_dotenv
import os

load_dotenv('.env')
openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAIAgent:
    def __init__(self,model='gpt-3.5-turbo'):
        self.model = model

    def get_response(self, command):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are always positive. "},
                {"role": "system", "content": "You have to keep your answers simple, efficient and smart"},
                {"role": "system", "content":  "You have to answer within 10secs"},
                {"role": "user", "content": command}
            ]
        )
        assistant_reply = response["choices"][0]["messages"]["content"]
        return assistant_reply

    def get_command_label(self, command):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a vocal assistant. "},
                {"role": "system", "content": "Your role is to classify user command and return corresponding label. "},
                {"role": "system", "content": "The labels are : To-do list, Normal question. "},
                {"role": "system", "content": "If command is recognized as To-do list request (for example). "},
                {"role": "system", "content": "then return 'To-do list'"},
                {"role": "user", "content": command}
            ]
        )
        label = response["choices"][0]["messages"]["content"]
        return label
