
import heapq
from base_search import base,time

class UCS(base):
    def __init__(self, init_state, goal_state):
        super().__init__(init_state, goal_state)
        # Heap elements: (cost, depth, state)
        self.heap = [(0, 0, init_state)]
        self.best_cost = {init_state: 0}

    def search(self):
        start_time = time.perf_counter()
        while self.heap:
            cost, depth, current_state = heapq.heappop(self.heap)
            self.n += 1
            self.max_depth = max(self.max_depth, depth)

            if current_state == self.goal_state:
                running_time = (time.perf_counter() - start_time) * 1000
                return self._build_path(current_state), self.n, self.max_depth, running_time

            for neighbor in current_state.get_neighbors():
                new_cost = cost + 1
                if neighbor not in self.best_cost or new_cost < self.best_cost[neighbor]:
                    self.best_cost[neighbor] = new_cost
                    self.parent[neighbor] = current_state
                    heapq.heappush(self.heap, (new_cost, depth + 1, neighbor))
        return None