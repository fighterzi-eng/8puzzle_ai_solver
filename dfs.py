class DFS:
    def __init__(self, init_state, goal_state):
        self.init_state = init_state
        self.goal_state = goal_state
        self.visited = {init_state}
        self.stack = [init_state]
        self.parent = {init_state: None}  
        self.n=0

    def search(self):
     
        while self.stack:
            current_state = self.stack.pop()
            self.n+=1
          #  current_state.display(0)
            if current_state == self.goal_state:
                return self._build_path(current_state)
            for neighbor in current_state.get_neighbors():
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    self.parent[neighbor] = current_state
                    self.stack.append(neighbor)
        return None

    def _build_path(self, state):
        path = []
        while state is not None:
            path.append(state)
            state = self.parent[state]
        path.reverse()
        return path ,self.n