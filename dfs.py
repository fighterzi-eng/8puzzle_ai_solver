from base_search import base ,time


class DFS(base):
    def __init__(self, init_state, goal_state):
        super().__init__(init_state, goal_state)
        self.visited = {init_state}
        self.stack = [(init_state, 0)]  # (state, depth)

    def search(self):
        start_time = time.perf_counter()
        while self.stack:
            current_state, depth = self.stack.pop()
            self.n += 1
            self.max_depth = max(self.max_depth, depth)

            if current_state == self.goal_state:
                running_time = (time.perf_counter() - start_time) * 1000
                return self._build_path(current_state), self.n, self.max_depth, running_time

            for neighbor in current_state.get_neighbors():
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    self.parent[neighbor] = current_state
                    self.stack.append((neighbor, depth + 1))
        return None