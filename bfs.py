from collections import deque

class BFS:
    def __init__(self, init_state, goal_state):
        self.init_state = init_state
        self.goal_state = goal_state
        self.visited = set()
        self.queue = deque([init_state])
        self.visited.add(init_state)
        self.parent = {init_state: None}  
        self.n=0

    def search(self):
        while self.queue:
            current_state = self.queue.popleft()
            n+=1
            current_state.display()
            

            if current_state == self.goal_state:
                return self._build_path(current_state)
          
            for neighbor in current_state.get_neighbors(current_state):
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    self.parent[neighbor] = current_state
                    self.queue.append(neighbor)
        return None
    
    def _build_path(self, state):
            path = []
            while state is not None:
                path.append(state)
                state = self.parent[state]
            path.reverse()
            return path,self.n

 
