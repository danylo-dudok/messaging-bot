from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class Coach:
    def train(self, bot: ChatBot) -> None:
        conversation = [
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome."
        ]

        trainer = ListTrainer(bot)

        trainer.train(conversation)
