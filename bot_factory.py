from dataclasses import dataclass

from chatterbot import ChatBot


class BotFactory:
    @dataclass
    class BotConfig:
        name: str
        storage_adapter: str
        database: str
        logic_adapters: list[str]
        learn: bool

    _config: BotConfig

    def __init__(self, config: BotConfig = None):
        if not config:
            config = self.BotConfig(
                name='The Bot',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                database='sqlite:///db.sqlite3',
                logic_adapters=[
                    'chatterbot.logic.BestMatch'
                ],
                learn=False
            )
        self._config = config

    def create(self) -> ChatBot:
        return ChatBot(
            self._config.name,
            storage_adapter=self._config.storage_adapter,
            database_uri=self._config.database,
            logic_adapters=self._config.logic_adapters,
            read_only=self._config.learn
        )
