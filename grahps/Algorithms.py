from .Graph import Graph, AdjacencyList


class Algorithms:

    @staticmethod
    def tutaj():
        pass

    @staticmethod
    def max_connected_comp(graph: Graph):
        def deep_first_search(adj_list, temp, vertex, visited):
            # Zaznaczamy aktualny jako odwiedzony i dodajemy go do listy
            visited[vertex] = True
            temp.append(vertex)
            for el in adj_list.list[vertex]:
                if not visited[el.id]:
                    temp = deep_first_search(adj_list, temp, el.id, visited)
            return temp

        adj_list = AdjacencyList(graph)

        visited = [False for el in adj_list.list.keys()]
        connected_comp = []
        for i in range(len(adj_list.list.keys())):
            if not visited[i]:
                start_vertex = i
                tmp = []
                connected_comp.append(deep_first_search(adj_list, tmp, start_vertex, visited))
        return connected_comp
