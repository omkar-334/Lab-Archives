import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    def tsp_branch_and_bound(self):
        visited = [False] * self.vertices
        visited[0] = True
        path = [0]
        min_cost = sys.maxsize
        min_path = []

        def bound(path, visited):
            total_cost = 0
            last_vertex = path[-1]
            for i in range(self.vertices):
                if not visited[i]:
                    min_edge = sys.maxsize
                    for j in range(self.vertices):
                        if self.graph[last_vertex][j] != 0 and not visited[j]:
                            min_edge = min(min_edge, self.graph[last_vertex][j])
                    total_cost += min_edge
            return total_cost

        def tsp_recursive(curr_pos, curr_cost, depth):
            nonlocal min_cost, min_path
            if depth == self.vertices - 1:
                if self.graph[curr_pos][0] != 0:
                    curr_cost += self.graph[curr_pos][0]
                    if curr_cost < min_cost:
                        min_cost = curr_cost
                        min_path = path[:]
                return
            for i in range(self.vertices):
                if self.graph[curr_pos][i] != 0 and not visited[i]:
                    path.append(i)
                    visited[i] = True
                    tsp_recursive(i, curr_cost + self.graph[curr_pos][i], depth + 1)
                    visited[i] = False
                    path.pop()

        tsp_recursive(0, 0, 0)
        return min_cost, min_path

def main():
    n = int(input("Enter the number of cities: "))
    g = Graph(n)
    print("Enter the adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            g.add_edge(i, j, row[j])

    min_cost, min_path = g.tsp_branch_and_bound()

    print("Minimum Cost:", min_cost)
    print("Optimal Path:")
    for city in min_path:
        print(city, end=" -> ")
    print(min_path[0])

if __name__ == "__main__":
    main()
