from node import Node,inversionCount
from bfs import BFS
from dfs import DFS
from astar import Astar
from ucs import UCS
from interface import read_input 

goal_state= Node(None,[0,1,2,3,4,5,6,7,8])


algo,heu,state=read_input()


initial_node=Node(heuristic=heu,state=state)
if algo=="astar":
    agent=Astar(init_state=initial_node,goal_state=goal_state)
elif algo=="bfs":
    agent=BFS(init_state=initial_node,goal_state=goal_state)
elif algo=="dfs":
    agent=DFS(init_state=initial_node,goal_state=goal_state)
else:
    agent=UCS(init_state=initial_node,goal_state=goal_state)

path,nodes=agent.search()
print("the "+algo+" expanded "+str(nodes)+" nodes")
print("the total path cost  "+str(len(path)))
confirm=input("enter anything to recounstruct path..")
print("recounstructing path.....")
for node in path:
    node.display(2.5)

