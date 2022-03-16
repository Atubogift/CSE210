from card import Card

SCORE_INCREASE = 100
SCORE_DECREASE = -75

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        first_card(instance of Card): First card to be drawn.
        second_card(instance of Card): Second card to be drawn.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
        guess(string): Variable to hold player's guess.
        play_again(string): Variable to hold player's intent to keep playing.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        # Initialize first_card and second_card.
        self.first_card = Card()
        self.second_card = Card()
        
        # Ensure second_card is different from first_card. 
        self.second_card.draw(self.first_card.value)

        # Initialize conditions of the game.
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        
        # Initialize user input variables.
        self.guess = ""
        self.play_again = ""


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.compute_probability()
            self.get_guess()
            self.update_score()
            self.display_result()
            self.determine_is_playing()
            self.reset_game()

    def get_guess(self):
        """Get the player's guess.
        Args:
            self (Director): An instance of Director.
        """
        print("The card is: ", self.first_card.value)

        # Initialize loop condition.
        self.guess = ""
        while (self.guess != 'h') and (self.guess != 'l'):
            print(f"High probability: {self.high:.0f}%")
            print(f"Low probability: {self.low:.0f}%")
            self.guess = input("Higher or lower? [h/l] ")

            # Guess input validation.
            if (self.guess != 'h') and (self.guess != 'l'):
                print("Please, enter 'h' for higher or 'l' for lower.")
    
    def compute_probability(self):
        """Determine probability of next card being high or low.
        Args:
            self (Director): An instance of Director.
        """


        # Values from 1 to 13.
        FIRST_VALUE = 1
        LAST_VALUE = 13

        # Probability of each card. 
        # Exclusive: the first card cannot be equal to the second card.
        PROBABILITY = 100 / 12

        # Reset counter.
        self.low = 0
        self.high = 0

        for card in range(FIRST_VALUE, self.first_card.value):
            self.low += PROBABILITY
        
        for card in range(self.first_card.value, LAST_VALUE):
            self.high += PROBABILITY

    def update_score(self):
        """Updates the player's score.
        Args:
            self (Director): An instance of Director.
        """
        
        # Update self.score based on self.guess.
        if (self.guess == 'h'):
            if self.second_card.value > self.first_card.value:
                self.score = SCORE_INCREASE
            else:
                self.score = SCORE_DECREASE

        # (guess == 'l')
        else:
            if self.second_card.value < self.first_card.value:
                self.score = SCORE_INCREASE
            else:
                self.score = SCORE_DECREASE

        self.total_score += self.score

        # If self.total_score is a negative number,
        # make self.total_score 0 instead.
        if self.total_score < 0:
            self.total_score = 0

    def display_result(self):
        """Display the player's score.
        Args:
            self (Director): An instance of Director.
        """

        print("Next card was: ", self.second_card.value)
        print("Your score is: ", self.total_score)

    def determine_is_playing(self):
        """Determine if game is over.
        Args:
            self (Director): An instance of Director.
        """

        if self.total_score > 0:

            # Initialize loop condition.
            self.play_again = ""
            while (self.play_again != 'y') and (self.play_again != 'n'):
                self.play_again = input("Play again? [y/n] ")

                # play_again input validation.
                if (self.play_again != 'y') and (self.play_again != 'n'):
                    print("Please, enter 'y' for yes or 'n' for no.")
            
            print()

            if self.play_again == 'y':
                self.is_playing = True
            else:
                self.is_playing = False
        
        else:
            self.is_playing = False
        
    def reset_game(self):
        """Reset conditions for the game.
        Args:
            self (Director): An instance of Director.
        """

        self.first_card.draw()
        self.second_card.draw(self.first_card.value)