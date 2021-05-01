from src.dialogs.dialog import Dialog, DEFAULT_MAXIMUM_SIMILARITY_THRESHOLD
from src.dialogs.enums import LogicAdapters


class QADialog(Dialog):
    _input_text: str
    _output_text: str

    def __init__(
            self,
            input: str,
            output: str,
            maximum_similarity_threshold: float = DEFAULT_MAXIMUM_SIMILARITY_THRESHOLD
    ):
        super().__init__(LogicAdapters.SPECIFIC_RESPONSE.value, maximum_similarity_threshold)
        self._input_text = input
        self._output_text = output

    def to_dict(self) -> dict:
        return {
            **super().to_dict(),
            'input_text': self._input_text,
            'output_text': self._output_text,
        }
