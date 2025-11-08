from groq import Groq

from src.llm.prompt import USER_PROMPT


class GroqLLM:

    def __init__(self, key, model):
        self.model = model
        self.client = Groq(
            api_key=key
        )

    def chat(self, question):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": USER_PROMPT.format(question=question),
                }
            ],
            model=self.model
        )

        return chat_completion.choices[0].message.content
