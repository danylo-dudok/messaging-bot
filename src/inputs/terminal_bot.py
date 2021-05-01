from chatterbot import ChatBot


class TerminalBot:
    def __init__(self, bot: ChatBot):
        self._bot = bot

    def execute(self) -> None:
        while True:
            sentence = input('Talk to the bot: ')
            if not sentence:
                continue
            response = self._bot.get_response(sentence)
            print(f'\n\n{response}\n\n')
