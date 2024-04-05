from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Define your API endpoint
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    # Check if the data is cached in Redis
    cached_data = redis_client.get('leaderboard_data')
    if cached_data:
        # If cached data exists, return it
        return jsonify(cached_data.decode('utf-8'))

    # If no cached data, retrieve the data from your database or source
    leaderboard_data = fetch_leaderboard_data_from_database()

    # Cache the data in Redis for future requests
    redis_client.set('leaderboard_data', leaderboard_data)

    # Return the fetched data
    return jsonify(leaderboard_data)

if __name__ == '__main__':
    app.run(debug=True)
