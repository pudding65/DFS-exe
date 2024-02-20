import time
import networkx as nx
import matplotlib.pyplot as plt
import os

# DFS
def dfs(graph, start_node, end_node, visited=None):
    if visited is None:
        visited = set()

    order = []

    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)

        # Check if reach the goal
        if start_node == end_node:
            return order

        for node in graph[start_node]:
            if node not in visited:
                order.extend(dfs(graph, node, end_node, visited))
                # check step
                if order[-1] == end_node:
                    break

    return order

def perform_dfs(file_path):
    start_node, end_node, dfs_data = read_file(file_path)
    G = nx.Graph()
    G.add_edges_from(dfs_data)
    order = dfs(G, start_node, end_node)
    return order, 'DFS', G, nx.spring_layout(G)

# Draw Graph
def visualize(order, title, G, pos, print_output=False):
    expanded_node = set()
    adjacency_list = {}
    list_L = []

    plt.figure()
    plt.title(title)

    for i, node in enumerate(order, start=1):

        expanded_node.add(node)
        adjacency_list[node] = list(G.neighbors(node))
        list_L.append(node)

        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels=True, node_color=['red' if n == node else 'grey' for n in G.nodes()])
        plt.draw()
        plt.pause(0.4)

    # Print result
    if print_output:
        print("\nExpanded Nodes: ", expanded_node)
        print("Adjacency List:", adjacency_list)
        print("List L:", list_L)

        # Shortest path
        shortest_path = nx.shortest_path(G, source=list_L[0], target=list_L[-1])
        print("Path:", shortest_path, end = "\n\n")

        # Output to file
        output_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "output.txt")
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Expanded Nodes: {expanded_node}\n")
            output_file.write(f"Adjacency List: {adjacency_list}\n")
            output_file.write(f"List L: {list_L}\n")
            output_file.write(f"Path: {shortest_path}\n")
    time.sleep(0.5)
    plt.show()

# Read input file
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    start_node = data[0].strip()
    end_node = data[1].strip()
    dfs_data = eval(data[2].strip())

    return start_node, end_node, dfs_data

def main(file_path):
    order, title, G, pos = perform_dfs(file_path)
    visualize(order, title, G, pos)

if __name__ == "__main__":
    main("input.txt")
