import random
import uuid

def make_random_game_id():
    return str(uuid.uuid4())[:10]