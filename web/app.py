from flask import Flask, render_template, jsonify, request
import utility

app = Flask(__name__)

initial_board_state = {
    "cats": [
        {"colour": "(0, 0, 255)", "direction": "r", "x": 1, "y": 1, "size": 20},
        {"colour": "(0, 255, 0)", "direction": "d", "x": 5, "y": 1, "size": 20}
    ],
    "homes": [
        {"colour": "(0, 0, 255)", "x": 10, "y": 1, "size": 40},
        {"colour": "(0, 255, 255)", "x": 4, "y": 1, "size": 40}
    ],
    "intersections": [
        {"x": 8, "y": 1, "possible_direction": ["r", "d"], "current_direction": "d", "user": "None", "size": 40}
    ],
    "tunnel": {"x": 1, "y": 1, "size": 50}, 
    "ticks_since_last_cat": 60,
    "time": 50
}

games = {

}

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/make_random_game_id")
def make_random_game_id():
    game_id = utility.make_random_game_id()
    return jsonify({"game_id": game_id}), 200

@app.route("/waiting_for_game/<game_id>")
def waiting_for_players(game_id):
    player_id = request.args.get('player_id')  # Get the player ID from the request
    
    if game_id not in games:
        games[game_id] = {"players": [], "board": initial_board_state}
    
    # Add the player to the game
    if(player_id not in games[game_id]["players"]):
        games[game_id]["players"].append(player_id)
    print(games)
    # Check if we have 2 players
    if len(games[game_id]["players"]) == 2:
        return jsonify({"state": "done","status": "Game is starting!", "game_id": game_id}), 200

    print(games)
    return jsonify({"state": "waiting", "status": "Waiting for another player...", "game_id": game_id}), 200


@app.route("/game/<id>")
def start_game_by_id(id):
    return render_template("game.html", game_id=id)


@app.route("/game/fetch_board_data_by_game_id/<game_id>")
def fetch_board_data_by_game_id(game_id):
    try: 
        board = games[game_id]["board"]
        return jsonify(board), 200
    except Exception as e:
        return {}

if __name__ == '__main__':
    app.run(port=8080, debug=True)