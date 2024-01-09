"""
Strategies
"""

from app.exceptions import InvalidChoiceException


class GeneralStrategy:
    """
    Defines the algorithm to check which player won the game.
    All that changes in the child implementations are valid_choices and win_conditions.
    """

    def determine_winner(self, player_one_choice, player_two_choice, valid_choices=None, win_conditions=None):
        """
        Determines who the winner is between two inputs in the game.
        Will throw an exception if one or both of the choices is not valid

        Inputs:
        - player_one_choice (string)
        - player_two_choice (string)

        Outputs:
        - either the winner or None, if there was a tie
        - a message that indicates the outcome of the game
        """
        if player_one_choice not in valid_choices or player_two_choice not in valid_choices:
            raise InvalidChoiceException(f"Choices must be one of: {', '.join(valid_choices)}.")

        if player_one_choice == player_two_choice:
            return None, "Empate!"

        for win_scenario in win_conditions[player_one_choice]:
            if player_two_choice == win_scenario["beats"]:
                return player_one_choice, win_scenario['message']

        for win_scenario in win_conditions[player_two_choice]:
            if player_one_choice == win_scenario["beats"]:
                return player_two_choice, win_scenario['message']

        # unreachable code
        return None, "Ocorreu um erro inesperado."


class RockPaperScissorsStrategy(GeneralStrategy):
    """
    Implements the winning conditions for a classic game of rock-paper-scissors
    """
    def __init__(self):
        self.valid_choices = ["rock", "paper", "scissors"]
        self.win_conditions = {
            "rock":[
                {
                    "beats":"scissors",
                    "message":"Pedra esmaga tesoura."
                },
            ],
            "paper":[
                {
                    "beats":"rock",
                    "message":"Papel cobre pedra."
                },
            ],
            "scissors":[
                {
                    "beats":"paper",
                    "message":"Tesoura corta papel."
                },
            ]
        }

    def determine_winner(self, player_one_choice, player_two_choice):
        return super().determine_winner(
            player_one_choice,
            player_two_choice,
            valid_choices=self.valid_choices,
            win_conditions=self.win_conditions
        )


class RockPaperScissorsLizardSpockStrategy(GeneralStrategy):
    """
    Implements the winning conditions for an classic game of rock-paper-scissors-lizard-spock
    """
    def __init__(self):
        self.valid_choices = ["rock", "paper", "scissors", "lizard", "spock"]
        self.win_conditions = {
            "rock":[
                {
                    "beats":"scissors",
                    "message":"Pedra esmaga tesoura."
                },
                {
                    "beats":"lizard",
                    "message":"Pedra esmaga lagarto."
                }
            ],
            "paper":[
                {
                    "beats":"rock",
                    "message":"Papel cobre pedra."
                },
                {
                    "beats":"spock",
                    "message":"Papel refuta Spock."
                }
            ],
            "scissors":[
                {
                    "beats":"paper",
                    "message":"Tesoura corta papel."
                },
                {
                    "beats":"lizard",
                    "message":"Tesoura decapita lagarto."
                }
            ],
            "lizard":[
                {
                    "beats":"spock",
                    "message":"Lagarto envenena Spock."
                },
                {
                    "beats":"paper",
                    "message":"Lagarto come papel."
                }
            ],
            "spock":[
                {
                    "beats":"scissors",
                    "message":"Spock quebra tesoura."
                },
                {
                    "beats":"rock",
                    "message":"Spock vaporiza pedra."
                }
            ]
        }

    def determine_winner(self, player_one_choice, player_two_choice):
        return super().determine_winner(
            player_one_choice,
            player_two_choice,
            valid_choices=self.valid_choices,
            win_conditions=self.win_conditions
        )
