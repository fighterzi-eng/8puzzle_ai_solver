from abc import ABC, abstractmethod  
import time
class base(ABC):

    def __init__(self, init_state, goal_state):
        self.init_state = init_state
        self.goal_state = goal_state
        self.parent = {init_state: None}
        self.n = 0           # Total nodes expanded
        self.max_depth = 0
        self.running_time=0

    def _build_path(self, state):
        path = []
        while state is not None:
            path.append(state)
            state = self.parent[state]
        path.reverse()
        return path

    @abstractmethod
    def search(self): 
        pass
