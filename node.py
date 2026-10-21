import random
from math import sqrt
from interface import show_state,inversionCount

class Node:
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    @staticmethod
    def coords_to_index(x, y):
        return 3 * y + x

    @staticmethod
    def index_to_coords(n):
        return n % 3, n // 3  # (x, y)

    def __init__(self, heuristic, state):
        self.heuristic = heuristic
        if state is None:
            state = random.sample(range(9), 9)
            copy=state.copy()
            while inversionCount(copy) % 2 != 0:
                state = random.sample(range(9), 9)
                copy=state.copy()
        self.state = state
        self.blank = self.state.index(0)

    def get_neighbors(self):
        x, y = Node.index_to_coords(self.blank)
        neighbors = []
        for dx, dy in Node.MOVES:
            nx, ny = x + dx, y + dy #new position
            if not (0 <= nx < 3 and 0 <= ny < 3):
                continue
            target = Node.coords_to_index(nx, ny)
            new_state = self.state.copy()  # copy, so the parent isn't mutated
            new_state[self.blank], new_state[target] = new_state[target], new_state[self.blank]
            neighbors.append(Node(self.heuristic, new_state))
        return neighbors

    def get_cost(self):
        cost = 0
        if self.heuristic == "manhattan":
            for i in range(0, 9):
                tile = self.state[i]
                if tile == 0:
                    continue  # Skip the blank tile
                tx, ty = Node.index_to_coords(tile) # Target coordinates
                cx, cy = Node.index_to_coords(i)     # Current coordinates
                cost += abs(tx - cx) + abs(ty - cy)
            
        elif self.heuristic == "euclidean":  # Fixed spelling matching input check
            for i in range(0, 9):
                tile = self.state[i]
                if tile == 0:
                    continue  # Skip the blank tile
                tx, ty = Node.index_to_coords(tile)
                cx, cy = Node.index_to_coords(i)
                cost += sqrt((tx - cx) ** 2 + (ty - cy) ** 2)
            
        return cost
    def __eq__(self, other):
        return other.state==self.state


    def __hash__(self):
        # Convert the mutable list into an immutable tuple just for hashing
        return hash(tuple(self.state))
    def __lt__(self, other):
        
        return self.state < other.state
    def __gt__(self, other):
            
            return self.state > other.state
    
    
        



    def display(self,time):
        show_state(self.state,time)
















