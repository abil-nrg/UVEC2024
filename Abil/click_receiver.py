click_gotten_from_Abil = ((250, 500), "P1") # x, y of mouse click, who is clicking
click_location, player = click_gotten_from_Abil

intersections = [] # list of intersections
for intersection in intersections:
    if click_location in intersection.get_area() and player == intersection.user:
        "Valid request"

