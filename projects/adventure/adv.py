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

# graph to store our rooms and their exits
graph = {}

opposite = {
    'n': 's',
    's': 'n',
    'w': 'e',
    'e': 'w'
    
}

# add room 0 to the graph, and for every exit it has, mark it with ?
graph[player.current_room.id] = {}
for direction in player.current_room.get_exits():
    graph[player.current_room.id][direction] = '?'
    

while True:
    # get current room
    room = player.current_room.id

    # if len(graph) == len(room_graph), we've visited all rooms and can break
    if len(graph) == len(room_graph):
        break
    
    # grab list of possible exits
    possible_directions = player.current_room.get_exits()
    
    # randomly choose a direction to move in
    move_to = random.choice(possible_directions)
    
    # travel in that direction
    player.travel(move_to)
    
    # add that direction to the traversal path
    traversal_path.append(move_to)
    
    # add new room to graph with its exits as ?
    graph[player.current_room.id] = {}
    for direction in player.current_room.get_exits():
        graph[player.current_room.id][direction] = '?'
    
    
    # update old room and new room in graph based on the direction moved
    graph[room][move_to] = player.current_room.id
    graph[player.current_room.id][opposite[move_to]] = room



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
