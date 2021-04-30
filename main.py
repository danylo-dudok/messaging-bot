from bot_factory import BotFactory
from inputs.terminal_bot import TerminalBot
from training.coach import Coach
from training.smart_coach import SmartCoach


def main() -> None:
    bot = BotFactory().create()

    coach = SmartCoach(
        Coach()
    )
    coach.train(bot)

    TerminalBot(bot).execute()


if __name__ == '__main__':
    main()
