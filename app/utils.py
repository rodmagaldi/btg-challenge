"""
Utilities to resolve who the winner is.
"""

from typing import Tuple

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

WINNING_GAMES = {
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

def play_game(input_a: str, input_b: str) -> Tuple[str or None, str]:
    """
    Determines who the winner is between two inputs in the game.

    Inputs:
    - input_a (string)
    - input_b (string)

    Outputs:
    - either the winner or None, if there was a tie
    """
    if input_a == input_b:
        return None, "Empate!"

    for win_scenario in WINNING_GAMES[input_a]:
        if input_b == win_scenario["beats"]:
            return input_a, win_scenario['message']

    for win_scenario in WINNING_GAMES[input_b]:
        if input_a == win_scenario["beats"]:
            return input_b, win_scenario['message']

    return None, "Ocorreu um erro inesperado."
