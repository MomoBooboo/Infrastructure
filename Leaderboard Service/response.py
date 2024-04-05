# routes.py

from flask import jsonify
from .services import rank_traders

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    ranked_traders = rank_traders()
    leaderboard_list = []
    for rank, (user_id, volume) in enumerate(ranked_traders, start=1):
        leaderboard_list.append({
            'rank': rank,
            'user_id': user_id,
            'volume': volume
        })
    return jsonify(leaderboard_list)
