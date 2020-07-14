"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # this will hold edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  # there's an edge from v1 to v2
            
        else:
            raise IndexError("nonexistent vert")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty Queue
        q = Queue()
        # create a set to store the visited nodes
        visited = set()
        
        # Init: enqueue the starting node
        q.enqueue(starting_vertex)
        
        # while queue isn't empty
        while q.size() > 0:
            # dequeue first item
            v = q.dequeue()
            # if its not been visited
            if v not in visited:
                # mark as visited (i.e. add to the visited set)
                visited.add(v)
                print(v)
                # add all the neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty Stack
        s = Stack()
        # create a set to store the visited nodes
        visited = set()
        
        # Init: push the starting node
        s.push(starting_vertex)
        
        # while stack isn't empty
        while s.size() > 0:
            # pop first item
            v = s.pop()
            # if its not been visited
            if v not in visited:
                # mark as visited (i.e. add to the visited set)
                visited.add(v)
                print(v)
                # add all the neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if starting_vertex hasn't been visted:
        if starting_vertex not in visited:
            # add it to visited set
            visited.add(starting_vertex)
            # print the vertex
            print(starting_vertex)
            
            # for each of its neighbors
            for neighbor in self.get_neighbors(starting_vertex):
                # recurse on the neighbor
                self.dft_recursive(neighbor, visited)
            

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex
        q = Queue()
        q.enqueue([starting_vertex])
        
        # Create a Set to store visited vertices
        visited = set()
        
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                  # IF SO, RETURN PATH
                  return path
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                  # COPY THE PATH
                  new_path = list(path)
                  # APPEND THE NEIGHBOR TO THE BACK
                  new_path.append(neighbor)
                  q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty Stack and push A PATH TO the starting vertex
        s = Stack()
        s.push([starting_vertex])
        
        # create a set to store visisted vertices
        visited = set()
        
        # while the stack is not empty...
        while s.size() > 0:
            # pop the first PATH
            path = s.pop()
            # grab the last vertex from the PATH
            v = path[-1]
            # if that vertex has not been visited
            if v not in visited:
                # check if its the destination vertex:
                if v == destination_vertex:
                    # if so, return PATH
                    return path
                # mark it as visited...
                visited.add(v)
                # then add A PATH TO its neighbors to the stack
                for neighbor in self.get_neighbors(v):
                    # COPY THE PATH
                    new_path = list(path)
                    # APPEND THE NEIGHBOR TO THE BACK
                    new_path.append(neighbor)
                    s.push(new_path)
        
        
    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('Breadth First Traversal:')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('Depth First Traversal:')
    graph.dft(1)
    print('Now DFT with Recursion... ')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS path:')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('DFS path:')
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
