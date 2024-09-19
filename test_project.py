import pytest
from project import DrawHangman, counter, PrintGuessedLetters


def test_DrawHangman():
    assert DrawHangman(4) == ["+======+", "|      O", "|     /|へ ", "|      ", "|      ", "|", "==========="]
    assert DrawHangman(2) == ["+======+", "|      O", "|     / ", "|      ", "|      ", "|", "==========="]
    assert DrawHangman(7) == ["+======+", "|      O", "|     /|へ ", "|      |", "|     / へ ", "|", "==========="]

def test_PrintGuessedLetters():
    assert PrintGuessedLetters(["a","b","c"]) == "a b c"
    assert PrintGuessedLetters(["ABc","5","!"]) == "ABc 5 !"

def test_counter():
    assert counter(["A","B","C"],"SINGAPORE") == 1
    assert counter(["A","B","OE"],"SINGAPORE") == 1
    assert counter(["A","SINGAPORE","OE"],"SINGAPORE") == 1
