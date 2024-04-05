import pytest
import requests

@pytest.fixture
def leaderboard_url():
    return 'http://localhost:5000/leaderboard'

@pytest.fixture
def trade_producer_url():
    return 'http://localhost:5001/send_trade_data'

def test_trade_data_integration(leaderboard_url, trade_producer_url):
    # Send mock trade data
    trade_data = {'user_id': 1, 'volume': 100}
    response = requests.post(trade_producer_url, json=trade_data)
    assert response.status_code == 200

    # Retrieve leaderboard data and verify the updated rank
    leaderboard_response = requests.get(leaderboard_url)
    assert leaderboard_response.status_code == 200
    leaderboard_data = leaderboard_response.json()
    assert leaderboard_data[0]['user_id'] == 1
    assert leaderboard_data[0]['rank'] == 1
