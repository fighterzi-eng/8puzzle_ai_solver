from node import Node
from bfs import BFS
from dfs import DFS
from idfs import IDDFS
from ucs import UCS
from astar import Astar
from interface import read_input 

goal_state = Node(None, [0, 1, 2, 3, 4, 5, 6, 7, 8])

algo, heu, state = read_input()
#initial_node = Node(heuristic=heu, state=state)
initial_node = Node(heuristic=heu, state=[8, 6, 7, 2, 5, 4, 3, 0, 1])

if algo == "astar":
    agent = Astar(init_state=initial_node, goal_state=goal_state)
elif algo == "bfs":
    agent = BFS(init_state=initial_node, goal_state=goal_state)
elif algo == "dfs":
    agent = DFS(init_state=initial_node, goal_state=goal_state)
elif algo == "iddfs":
    agent = IDDFS(init_state=initial_node, goal_state=goal_state)
else:
    agent = UCS(init_state=initial_node, goal_state=goal_state)

result = agent.search()

if result is None:
    print("No solution found.")
else:
    path, nodes_expanded, max_depth, running_time = result
    print("\n--- SEARCH RESULTS ---")
    print(f"Algorithm Used: {algo}")
    print(f"Path to Goal Cost: {len(path) - 1} ")
    print(f"Nodes Expanded: {nodes_expanded}")
    print(f"Max Search Depth Reached: {max_depth}")
    print(f"Running Time: {running_time:.3f} ms")

    confirm = input("\nEnter anything to reconstruct path step-by-step: ")
    print("Reconstructing path.....")
    for node in path:
        node.display(1.0)