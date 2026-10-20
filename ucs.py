import heapq

class UCS:
    def __init__(self, init_state, goal_state):
        self.init_state = init_state
        self.goal_state = goal_state
        self.heap = [(0, init_state)]
        self.best_cost = {init_state: 0}
        self.parent = {init_state: None}
        self.n = 0

    def search(self):
        while self.heap:
            cost, current_state = heapq.heappop(self.heap)
            self.n += 1
            current_state.display()

            if current_state == self.goal_state:
                return self._build_path(current_state)

            for neighbor in current_state.get_neighbors():
                new_cost = cost + 1 
                if neighbor not in self.best_cost or new_cost < self.best_cost[neighbor]:
                    self.best_cost[neighbor] = new_cost
                    self.parent[neighbor] = current_state
                    heapq.heappush(self.heap, (new_cost, neighbor))
        return None

    def _build_path(self, state):
        path = []
        while state is not None:
            path.append(state)
            state = self.parent[state]
        path.reverse()
        return path