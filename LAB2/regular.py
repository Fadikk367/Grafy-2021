import random
from collections import defaultdict


# takes list of edges and number of nodes, returns adjacency matrix
def adjacency_matrix_from_edges_set(edges_set, n):
    rows, cols = (n, n)
    arr = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(0)
        arr.append(col)
    for edge in edges_set:
        arr[edge[0]][edge[1]] = 1
        arr[edge[1]][edge[0]] = 1
    return arr


# returns k-regular graph with n vertices -> as adjacency matrix
# k * n must be even number
def generate_random_regular_graph(k, n, seed=random):

    # make sure that none of the vertices have loops or multiple edges
    def is_plain(edges, potential_edges):

        if not potential_edges:
            return True

        for point1 in potential_edges:
            for point2 in potential_edges:
                if point1 == point2:
                    break
                if point1 > point2:
                    point1, point2 = point2, point1
                if (point1, point2) not in edges:
                    return True

        return False

    def generate():

        edges_set = set()
        buckets = list(range(n)) * k

        while buckets:
            # takes zero when argument is not present potential_edges[argument] -> potential_edges[argument] = 0
            potential_edges = defaultdict(int)
            seed.shuffle(buckets)
            bucket_iterator = iter(buckets)

            # we match randomly 2 points from buckets in order to retrieve edges
            for point1, point2 in zip(bucket_iterator, bucket_iterator):
                # replace if needed, first number need be smaller
                if point1 > point2:
                    point1, point2 = point2, point1
                # if not already in edges set we put it and send further for testing
                if point1 != point2 and ((point1, point2) not in edges_set):
                    edges_set.add((point1, point2))
                # if such edge exists we increment possible edge from this node
                else:
                    potential_edges[point1] += 1
                    potential_edges[point2] += 1

            # check if set fulfills expectations
            if not is_plain(edges_set, potential_edges):
                return None

            # refreshing bucket with nodes repeated * their potential
            buckets = [node for node, potential in potential_edges.items() for _ in range(potential)]

        return edges_set

    if (n * k) % 2 != 0:
        raise ValueError("n * k must be even")

    if not 0 <= k < n:
        raise ValueError("the 0 <= d < n inequality must be satisfied")

    if k == 0:
        return adjacency_matrix_from_edges_set({}, n)

    # first shot
    result = generate()

    # retry graph generation when previous one fell short of expectations
    # if the graph is not simple -> restart
    while result is None:
        result = generate()

    return adjacency_matrix_from_edges_set(result, n)
