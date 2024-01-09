import pytest
from app import create_app

class TestGame:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_invalid_inputs(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "invalido 1", "player_two_choice": "invalido 2"}
        )
        assert response.status_code == 400
        data = response.get_json()
        assert len(data.get("errors")) == 2

    def test_ties(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "rock", "player_two_choice": "rock"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Empate!"
        assert data.get("player_one_choice") == "rock"
        assert data.get("player_two_choice") == "rock"
        assert data.get("winner") == None
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "paper", "player_two_choice": "paper"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Empate!"
        assert data.get("player_one_choice") == "paper"
        assert data.get("player_two_choice") == "paper"
        assert data.get("winner") == None
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "scissors", "player_two_choice": "scissors"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Empate!"
        assert data.get("player_one_choice") == "scissors"
        assert data.get("player_two_choice") == "scissors"
        assert data.get("winner") == None
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "lizard", "player_two_choice": "lizard"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Empate!"
        assert data.get("player_one_choice") == "lizard"
        assert data.get("player_two_choice") == "lizard"
        assert data.get("winner") == None
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "spock", "player_two_choice": "spock"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Empate!"
        assert data.get("player_one_choice") == "spock"
        assert data.get("player_two_choice") == "spock"
        assert data.get("winner") == None

    def test_rock_beats_scissors(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "rock", "player_two_choice": "scissors"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Pedra esmaga tesoura."
        assert data.get("player_one_choice") == "rock"
        assert data.get("player_two_choice") == "scissors"
        assert data.get("winner") == "rock"
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "scissors", "player_two_choice": "rock"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Pedra esmaga tesoura."
        assert data.get("player_one_choice") == "scissors"
        assert data.get("player_two_choice") == "rock"
        assert data.get("winner") == "rock"

    def test_rock_beats_lizard(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "rock", "player_two_choice": "lizard"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Pedra esmaga lagarto."
        assert data.get("player_one_choice") == "rock"
        assert data.get("player_two_choice") == "lizard"
        assert data.get("winner") == "rock"
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "lizard", "player_two_choice": "rock"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Pedra esmaga lagarto."
        assert data.get("player_one_choice") == "lizard"
        assert data.get("player_two_choice") == "rock"
        assert data.get("winner") == "rock"

    def test_paper_beats_rock(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "paper", "player_two_choice": "rock"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Papel cobre pedra."
        assert data.get("player_one_choice") == "paper"
        assert data.get("player_two_choice") == "rock"
        assert data.get("winner") == "paper"
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "rock", "player_two_choice": "paper"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Papel cobre pedra."
        assert data.get("player_one_choice") == "rock"
        assert data.get("player_two_choice") == "paper"
        assert data.get("winner") == "paper"

    def test_paper_beats_spock(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "paper", "player_two_choice": "spock"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Papel refuta Spock."
        assert data.get("player_one_choice") == "paper"
        assert data.get("player_two_choice") == "spock"
        assert data.get("winner") == "paper"
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "spock", "player_two_choice": "paper"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Papel refuta Spock."
        assert data.get("player_one_choice") == "spock"
        assert data.get("player_two_choice") == "paper"
        assert data.get("winner") == "paper"

    def test_scissors_beats_paper(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "scissors", "player_two_choice": "paper"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Tesoura corta papel."
        assert data.get("player_one_choice") == "scissors"
        assert data.get("player_two_choice") == "paper"
        assert data.get("winner") == "scissors"
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "paper", "player_two_choice": "scissors"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Tesoura corta papel."
        assert data.get("player_one_choice") == "paper"
        assert data.get("player_two_choice") == "scissors"
        assert data.get("winner") == "scissors"

    def test_scissors_beats_lizard(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "scissors", "player_two_choice": "lizard"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Tesoura decapita lagarto."
        assert data.get("player_one_choice") == "scissors"
        assert data.get("player_two_choice") == "lizard"
        assert data.get("winner") == "scissors"
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "lizard", "player_two_choice": "scissors"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Tesoura decapita lagarto."
        assert data.get("player_one_choice") == "lizard"
        assert data.get("player_two_choice") == "scissors"
        assert data.get("winner") == "scissors"

    def test_lizard_beats_spock(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "lizard", "player_two_choice": "spock"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Lagarto envenena Spock."
        assert data.get("player_one_choice") == "lizard"
        assert data.get("player_two_choice") == "spock"
        assert data.get("winner") == "lizard"
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "spock", "player_two_choice": "lizard"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Lagarto envenena Spock."
        assert data.get("player_one_choice") == "spock"
        assert data.get("player_two_choice") == "lizard"
        assert data.get("winner") == "lizard"

    def test_lizard_beats_paper(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "lizard", "player_two_choice": "paper"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Lagarto come papel."
        assert data.get("player_one_choice") == "lizard"
        assert data.get("player_two_choice") == "paper"
        assert data.get("winner") == "lizard"
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "paper", "player_two_choice": "lizard"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Lagarto come papel."
        assert data.get("player_one_choice") == "paper"
        assert data.get("player_two_choice") == "lizard"
        assert data.get("winner") == "lizard"

    def test_spock_beats_scissors(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "spock", "player_two_choice": "scissors"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Spock quebra tesoura."
        assert data.get("player_one_choice") == "spock"
        assert data.get("player_two_choice") == "scissors"
        assert data.get("winner") == "spock"
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "scissors", "player_two_choice": "spock"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Spock quebra tesoura."
        assert data.get("player_one_choice") == "scissors"
        assert data.get("player_two_choice") == "spock"
        assert data.get("winner") == "spock"

    def test_spock_beats_rock(self):
        response = self.client.post(
            '/',
            json={"player_one_choice": "spock", "player_two_choice": "rock"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Spock vaporiza pedra."
        assert data.get("player_one_choice") == "spock"
        assert data.get("player_two_choice") == "rock"
        assert data.get("winner") == "spock"
        
        response = self.client.post(
            '/',
            json={"player_one_choice": "rock", "player_two_choice": "spock"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Spock vaporiza pedra."
        assert data.get("player_one_choice") == "rock"
        assert data.get("player_two_choice") == "spock"
        assert data.get("winner") == "spock"
