import requests

def get_random_puzzle_fen():
    response = requests.get('https://api.chess.com/pub/puzzle/random')
    data = response.json()
    return data['fen']