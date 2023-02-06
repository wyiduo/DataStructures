import random

class Node:
    def __init__(self):
        self.edge_arr = []

    def get_edge_arr(self):
        return self.edge_arr

    def get_edge_arr_index(self, i):
        return self.edge_arr[i]

    def get_edge_arr_index_2d(self, i, j):
        return self.edge_arr[i][j]

class Graph:
    def __init__(self):
        self.node_arr = []

        self.bfs_visited = [] # will give order of visited from BFS
        self.bfs_queue = [] # queue is needed to find next node for a breadth-based search
        self.bfs_total_weight = 0

        self.prims_visited = []
        self.prims_mst = []
        self.prims_total_weight = 0

        self.rand_starting_node = None

    def add_node(self):
        new_node = Node()
        self.node_arr.append(new_node)
        # identifer for each node will be their index in the array

    def add_edge(self, n1_i, n2_i, weight): # node1_index, node2_index

        edge_already_exists = False

        # checks to see if there is an existing edge from n1_i to n2_i
        for i in range(0, len(self.node_arr[n1_i].get_edge_arr())):
            if self.node_arr[n1_i].get_edge_arr_index_2d(i, 0) == n2_i:
                edge_already_exists = True
                break

        if not edge_already_exists:        
            self.node_arr[n1_i].get_edge_arr().append([n2_i, weight])
        # adds an ordered two-variable list to store the vertex index and weight

    def generate_random_graph(self, n):
        # using Erdos-Renyi Model for generating random graphs
        # step 1: generate n nodes
        # step 2: for each node with pair {i,j}, there is a probability p
        # that there is will be an edge that connects both directions of
        # pair {i,j}, where the weight of that edge is from probability w
        # For constants, p is 30%, w is a random int from [10 to 100]
        for i in range(0, n):
            self.add_node()
        
        for i in range(0, n):
            for j in range(0, n):
                bool_add_edges = random.randint(1, 10)

                if bool_add_edges <= 3:
                    # 30% chance for an edge to exist between any two nodes
                    
                    w = random.randint(10, 100)
                    
                    self.add_edge(i,j, w)
                    self.add_edge(j,i, w)


    def reset_bfs_cache(self):
        self.bfs_visited = []
        self.bfs_queue = []
        self.bfs_total_weight = 0

    def bfs(self):
        if self.rand_starting_node == None:
            rand_node = random.randint(0, len(self.node_arr) -1)
        else: # for common starting node with prims
            rand_node = self.rand_starting_node
        
        self.bfs_visited.append(rand_node)
        self.bfs_queue.append(rand_node)

        while len(self.bfs_queue) != 0:
            current_node = self.bfs_queue.pop(0)
            # for each [node, weight] adjacent to current_node
            for neighbour in self.node_arr[current_node].get_edge_arr():
                if neighbour[0] not in self.bfs_visited:
                    self.bfs_visited.append(neighbour[0])
                    self.bfs_queue.append(neighbour[0])
                    self.bfs_total_weight += neighbour[1]

        return self.bfs_total_weight

    def reset_prims_cache(self):
        self.prims_visited = []
        self.prims_mst = []
        self.prims_total_weight = 0
    
    def prims(self):
        if self.rand_starting_node == None:
            rand_node = random.randint(0, len(self.node_arr) -1)
        else:
            rand_node = self.rand_starting_node

        self.prims_visited.append(rand_node)

        while len(self.prims_visited) < len(self.node_arr):
            # next node is the node with lowest weight connected to preexisting nodes
            starting_node_min_weight = 0
            ending_node_min_weight = 0
            min_weight = 10000 # set arbitrarily high

            # for each visited_node in the current mst
            for visited in self.prims_visited:
                # for each [node, weight] adjacent to visited_node
                for neighbour in self.node_arr[visited].get_edge_arr():
                    if neighbour[0] not in self.prims_visited: # ensure no cycles
                        if neighbour[1] < min_weight:
                            starting_node_min_weight = visited
                            ending_node_min_weight = neighbour[0]
                            min_weight = neighbour[1]

            self.prims_visited.append(ending_node_min_weight)
            self.prims_mst.append([starting_node_min_weight, ending_node_min_weight, min_weight])

        for path in self.prims_mst:
            self.prims_total_weight += path[2]
        
        return self.prims_total_weight

    def set_common_rand_starting_node(self):
        # when comparing BFS and Prim's, it is important to give the same
        # random starting node
        # consider the case where the starting node is isolated from the rest of
        # the graph for one algorithm, but the starting node for the other
        # algorithm is not isolated
        # setting a common random starting node prevents the case above
        self.rand_starting_node = random.randint(0, len(self.node_arr) -1)

    def compare_bfs_and_prims(self, k):
        # for n = 20
        Diff_n20 = []
        for i in range(0, k):
            graph = Graph()
            graph.generate_random_graph(20)
            graph.set_common_rand_starting_node()
            B = graph.bfs()
            graph.reset_bfs_cache()
            P = graph.prims()
            graph.reset_prims_cache()
            Diff_n20.append((B-P)/P)
            
        average_Diff_n20 = sum(Diff_n20)/len(Diff_n20)

        # for n = 40
        Diff_n40 = []
        for i in range(0, k):
            graph = Graph()
            graph.generate_random_graph(40)
            graph.set_common_rand_starting_node()
            B = graph.bfs()
            graph.reset_bfs_cache()
            P = graph.prims()
            graph.reset_prims_cache()
            Diff_n40.append((B-P)/P)
            
        average_Diff_n40 = sum(Diff_n40)/len(Diff_n40)

        # for n = 60
        Diff_n60 = []
        for i in range(0, k):
            graph = Graph()
            graph.generate_random_graph(60)
            graph.set_common_rand_starting_node()
            B = graph.bfs()
            graph.reset_bfs_cache()
            P = graph.prims()
            graph.reset_prims_cache()
            Diff_n60.append((B-P)/P)
            
        average_Diff_n60 = sum(Diff_n60)/len(Diff_n60)

        return [average_Diff_n20, average_Diff_n40, average_Diff_n60]

    
if __name__ == "__main__":
    # initialize a graph1 with 30 vertices and random edges between the vertices
    graph1 = Graph()
    graph1.generate_random_graph(30)

    graph2 = Graph()
    graph2.add_node() # node_0
    graph2.add_node() # node_1
    graph2.add_node() # node_2
    graph2.add_node() # node_3
    graph2.add_node() # node_4
    graph2.add_node() # node_5

    graph2.add_edge(0, 1, 15)
    graph2.add_edge(0, 3, 7)
    graph2.add_edge(0, 4, 10)
    graph2.add_edge(1, 0, 15)
    graph2.add_edge(1, 2, 9)
    graph2.add_edge(1, 3, 11)
    graph2.add_edge(1, 5, 9)
    graph2.add_edge(2, 1, 9)
    graph2.add_edge(2, 4, 12)
    graph2.add_edge(2, 5, 7)
    graph2.add_edge(3, 0, 7)
    graph2.add_edge(3, 1, 11)
    graph2.add_edge(3, 4, 8)
    graph2.add_edge(3, 5, 14)
    graph2.add_edge(4, 0, 10)
    graph2.add_edge(4, 2, 12)
    graph2.add_edge(4, 3, 8)
    graph2.add_edge(4, 5, 8)
    graph2.add_edge(5, 1, 9)
    graph2.add_edge(5, 2, 7)
    graph2.add_edge(5, 3, 14)
    graph2.add_edge(5, 4, 8)

    print("graph2.bfs() = ")
    print(graph2.bfs())
    print("graph2.prims() = ")
    print(graph2.prims())

    print("Comparing bfs to prims for k = 50,")
    graph3 = Graph()
    out_buffer = graph3.compare_bfs_and_prims(50)
    print("For n = 20, average difference is")
    print(out_buffer[0])
    print("For n = 40, average difference is")
    print(out_buffer[1])
    print("For n = 60, average difference is")
    print(out_buffer[2])
    
