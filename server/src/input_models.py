from typing import TypedDict
from enum import Enum


class KeyEventType(str, Enum):
    KEYUP = "keyup"
    KEYDOWN = "keydown"


class KeyEvent(TypedDict):
    key: str
    type: KeyEventType
    timestampMillis: float


class Submission(TypedDict):
    username: str
    sentenceId: int
    results: list[KeyEvent]
