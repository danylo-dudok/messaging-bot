from enum import Enum

from chatterbot.comparisons import sentiment_comparison, levenshtein_distance, jaccard_similarity, synset_distance


class LogicAdapters(Enum):
    BEST_MATCH: Enum = 'chatterbot.logic.BestMatch'
    SPECIFIC_RESPONSE: Enum = 'chatterbot.logic.SpecificResponseAdapter'


class StorageAdapters(Enum):
    SQL: Enum = 'chatterbot.storage.SQLStorageAdapter'


class StatementComparison(Enum):
    SENTIMENT: Enum = sentiment_comparison
    LEVENSHTEIN: Enum = levenshtein_distance
    JACCARD: Enum = jaccard_similarity
    SYNSET: Enum = synset_distance
