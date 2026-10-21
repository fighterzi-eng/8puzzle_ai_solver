from ucs import heapq ,UCS
class Astar(UCS):
  
  #override
  def search(self):
          while self.heap:
              cost, current_state = heapq.heappop(self.heap)
              self.n += 1
              #current_state.display(0)
  
              if current_state == self.goal_state:
                  return self._build_path(current_state)
  
              for neighbor in current_state.get_neighbors():
                  new_cost = cost + 1 +neighbor.get_cost()
                  if neighbor not in self.best_cost or new_cost < self.best_cost[neighbor]:
                      self.best_cost[neighbor] = new_cost
                      self.parent[neighbor] = current_state
                      heapq.heappush(self.heap, (new_cost, neighbor))
          return None
        