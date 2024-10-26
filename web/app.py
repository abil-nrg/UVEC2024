from flask import Flask, render_template, jsonify, request
import utility

app = Flask(__name__)

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
        games[game_id] = []
    
    # Add the player to the game
    if(player_id not in games[game_id]):

        games[game_id].append(player_id)

    print(games)
    # Check if we have 2 players
    if len(games[game_id]) == 2:
        return jsonify({"state": "done","status": "Game is starting!", "game_id": game_id}), 200

    print(games)
    return jsonify({"state": "waiting", "status": "Waiting for another player...", "game_id": game_id}), 200


@app.route("/game/<id>")
def start_game_by_id(id):
    return render_template("game.html", game_id=id)



if __name__ == '__main__':
    app.run(port=8080, debug=True)