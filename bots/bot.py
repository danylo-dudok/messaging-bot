from dataclasses import dataclass

from chatterbot import ChatBot, response_selection
from chatterbot.response_selection import get_most_frequent_response

from dialogs.dialog import Dialog
from dialogs.enums import StorageAdapters, LogicAdapters


@dataclass
class BotConfig:
    name: str
    storage_adapter: str
    database: str
    logic_adapters: list[Dialog]
    learn: bool
    selection: response_selection = get_most_frequent_response


class Bot(ChatBot):
    def __init__(self, config: BotConfig):
        super().__init__(
            config.name,
            storage_adapter=config.storage_adapter,
            database_uri=config.database,
            logic_adapters=[adapter.to_dict() for adapter in config.logic_adapters],
            read_only=config.learn,
            response_selection_method=config.selection
        )


class BotSettingsProvider:
    def provide(self) -> BotConfig:
        return BotConfig(
            name='The Bot',
            storage_adapter=StorageAdapters.SQL.value,
            database='sqlite:///db.sqlite3',
            logic_adapters=[
                Dialog(LogicAdapters.BEST_MATCH.value)
            ],
            learn=False
        )
