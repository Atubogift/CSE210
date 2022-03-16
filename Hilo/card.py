import random

class Card:
    """Individual card represented as a number from 1 to 13.
    The responsibility of Card is to keep track of the value represented by the card.
    Attributes:
        value (int): The value represented by the card.
    """

    def __init__(self):
        """Constructs a new instance of Card with a value.
        Args:
            self (Card): An instance of Card.
        """

        self.value = random.randint(1, 13)

    def draw(self, excluding=0):
        """Draws a new value for the card.
        If excluding == 0, no values are excluded.
        If exluding != 0, a new value will be drawn."""

        # Assert excluding is of type int.
        assert type(excluding) == int

        self.value = random.randint(1, 13)

        while self.value == excluding:
            self.value = random.randint(1, 13)