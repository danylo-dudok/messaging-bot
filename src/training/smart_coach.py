from chatterbot import ChatBot

from src.training.coach import Coach


class SmartCoach(Coach):
    _trained = False

    def __init__(self, coach: Coach):
        self._coach = coach

    def train(self, bot: ChatBot) -> None:
        if not self._trained:
            super().train(bot)
