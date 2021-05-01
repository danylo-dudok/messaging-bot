from bots.bot import Bot, BotSettingsProvider
from inputs.terminal_bot import TerminalBot
from training.coach import Coach
from training.smart_coach import SmartCoach


def main() -> None:
    coach = SmartCoach(
        Coach()
    )
    provider = BotSettingsProvider()
    settings = provider.provide()
    bot = Bot(settings)
    coach.train(bot)

    TerminalBot(bot).execute()


if __name__ == '__main__':
    main()
