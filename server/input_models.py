from typing import TypedDict


class KeyEvent(TypedDict):
    key: str
    type: str
    timestampMillis: float


class TestData(TypedDict):
    username: str
    sentenceId: int
    results: list[KeyEvent]