from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    
    g = Graph()
    added = set()

    # create vertex for every ancestor
    for tup in ancestors:
        if tup[0] not in added:
            g.add_vertex(tup[0])
            added.add(tup[0])

        if tup[1] not in added:
            g.add_vertex(tup[1])
            added.add(tup[1])

    # add edge from child to parent
    for tup in ancestors:
        g.add_edge(tup[1], tup[0])

    # breadth first traversal
    x = g.bft(starting_node)
    
    # if the last item in BFT is starting_node, then we know it doesn't have a
    #. a parent
    if x[-1] == starting_node:
        return -1
    
    # return earliest ancestor
    return x[-1]


if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 9))
