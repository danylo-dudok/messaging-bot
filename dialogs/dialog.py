from typing import final

from dialogs.enums import LogicAdapters, StatementComparison

DEFAULT_RESPONSE: final = 'I am sorry, but I do not understand.'
DEFAULT_MAXIMUM_SIMILARITY_THRESHOLD: final = 0.90


class Dialog:
    def __init__(
            self,
            logic_adapter: LogicAdapters,
            maximum_similarity_threshold: float = DEFAULT_MAXIMUM_SIMILARITY_THRESHOLD
    ):
        self._logic_adapter = logic_adapter
        self._maximum_similarity_threshold = maximum_similarity_threshold

    def to_dict(self) -> dict:
        return {
            'import_path': self._logic_adapter,
            'default_response': DEFAULT_RESPONSE,
            'maximum_similarity_threshold': self._maximum_similarity_threshold,
            'statement_comparison_function': StatementComparison.SENTIMENT,
        }
