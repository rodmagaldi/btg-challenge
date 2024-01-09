"""
Main Flask app to play rock-paper-scissors and selected variations
"""

from flask import Blueprint, request, jsonify
from app.exceptions import InvalidChoiceException
from app.game import Game
from app.strategies import RockPaperScissorsStrategy, RockPaperScissorsLizardSpockStrategy

main = Blueprint('main', __name__)

@main.route('/', methods=['POST'])
def play():
    """
    Inputs:
    - player_one_choice (string)
    - player_two_choice (string)

    Returns:
    - which player is the winner
    """
    player_one_choice = request.json.get("player_one_choice")
    player_two_choice = request.json.get("player_two_choice")

    strategy = request.json.get("strategy", "rock-paper-scissors-lizard-spock")

    # presumes strategy includes lizard and spock
    if strategy == "rock-paper-scissors":
        game = Game(RockPaperScissorsStrategy())
    else:
        game = Game(RockPaperScissorsLizardSpockStrategy())

    try:
        winner, message = game.play_game(player_one_choice, player_two_choice)

        return_obj = {
            "player_one_choice": player_one_choice,
            "player_two_choice": player_two_choice,
            "winner": winner,
            "message": message
        }

        return jsonify(return_obj)

    except InvalidChoiceException as exc:
        return jsonify({"error": str(exc)}), 400

    except exc:
        return jsonify({"error": f"Unexpected error: {str(exc)}"}), 500
