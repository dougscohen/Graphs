from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()

file_path = 'C:\\Users\\dougcohen\\Repos\\CS\\Graphs\\projects\\adventure\\maps\\'

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = file_path + "test_line.txt"
# map_file = file_path + "test_cross.txt"
# map_file = file_path + "test_loop.txt"
# map_file = file_path + "test_loop_fork.txt"
map_file = file_path + "main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

visited = {}

opposite = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}

# stack to hold the path that we've traveled so far (reverse route)
s = Stack()

# mark current room as vistied
visited[player.current_room.id] = player.current_room.get_exits()

while len(visited) < len(room_graph):

    # if current room has not been visited....
    if player.current_room.id not in visited:
        # add the room as a key to visited, with its exits as the values
        visited[player.current_room.id] = player.current_room.get_exits()

        # grab the last direction put on the stack (opposite direction we came
        #. in to get to current room)
        backward = s.stack[-1]

        # and remove that direction from the current room's exits so we don't
        # go back to the previous room until we need to
        visited[player.current_room.id].remove(backward)

    # if the current room has no remaining exits to be tried...
    if len(visited[player.current_room.id]) == 0:
        # pop the top of the stack and assign it as the direction to travel
        backward = s.pop()
        # traverse backwards
        player.travel(backward)
        # add it to the traversal directions
        traversal_path.append(backward)

    else:
        # choose a direction to go
        direction = visited[player.current_room.id].pop()
        # travel in that direction
        player.travel(direction)
        # add it to the traversal directions
        traversal_path.append(direction)
        # push the opposite direction to the stack
        s.push(opposite[direction])


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
