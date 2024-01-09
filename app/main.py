"""
Main Flask app to play rock-paper-scissors-lizard-spock
"""

from flask import Blueprint, request, jsonify
from app.utils import play_game, VALID_CHOICES

main = Blueprint('main', __name__)

@main.route('/', methods=['POST'])
def rock_paper_scissors_lizard_spock():
    """
    Inputs:
    - player_one_choice (string)
    - player_two_choice (string)

    Returns:
    - which player is the winner
    """
    player_one_choice = request.json.get("player_one_choice")
    player_two_choice = request.json.get("player_two_choice")

    input_errors = []

    if player_one_choice not in VALID_CHOICES:
        input_errors.append(
            f"Player one choice {player_one_choice} is invalid. Choice must be one of: {', '.join(VALID_CHOICES)}.")
    if player_two_choice not in VALID_CHOICES:
        input_errors.append(
            f"Player two choice {player_two_choice} is invalid. Choice must be one of: {', '.join(VALID_CHOICES)}.")

    if len(input_errors) > 0:
        return jsonify({"errors": input_errors}), 400

    winner, message = play_game(player_one_choice, player_two_choice)

    return_obj = {
        "player_one_choice": player_one_choice,
        "player_two_choice": player_two_choice,
        "winner": winner,
        "message": message
    }

    return jsonify(return_obj)
