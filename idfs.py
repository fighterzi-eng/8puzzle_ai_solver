from base_search import base ,time



class IDDFS(base):
    def __init__(self, init_state, goal_state, max_limit=50):
        super().__init__(init_state, goal_state)
        self.max_limit = max_limit

    def search(self):
        start_time = time.perf_counter()
        for limit in range(self.max_limit):
            self.parent = {self.init_state: None}
            visited = {self.init_state}
            found = self._dls(self.init_state, 0, limit, visited)
            if found is not None:
                running_time = (time.perf_counter() - start_time) * 1000
                return self._build_path(found), self.n, self.max_depth, running_time
        return None

    def _dls(self, current, depth, limit, visited):
        self.n += 1
        self.max_depth = max(self.max_depth, depth)
        if current == self.goal_state:
            return current
        if depth >= limit:
            return None

        for neighbor in current.get_neighbors():
            if neighbor not in visited:
                visited.add(neighbor)
                self.parent[neighbor] = current
                result = self._dls(neighbor, depth + 1, limit, visited)
                if result is not None:
                    return result
                visited.remove(neighbor)
        return None