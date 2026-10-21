import tkinter as tk


TILE = 100
GAP = 6


import tkinter as tk
import time

def show_state(state, seconds=1, title="8-Puzzle"):
    """Open or update a persistent 3x3 board window to avoid flickering."""
    # 1. Initialize the window and canvas only on the very first call
    if not hasattr(show_state, "root") or show_state.root is None:
        try:
            show_state.root = tk.Tk()
        except RuntimeError:
            show_state.root = tk.Tk()
            
        show_state.root.title(title)
        show_state.root.resizable(False, False)

        size = 3 * TILE + 4 * GAP
        show_state.canvas = tk.Canvas(show_state.root, width=size, height=size, bg="#2b2b2b", highlightthickness=0)
        show_state.canvas.pack()
        
        # Handle manual window closure safely
        def on_close():
            show_state.root.destroy()
            show_state.root = None
        show_state.root.protocol("WM_DELETE_WINDOW", on_close)

    root = show_state.root
    if root is None:
        return  # Exit early if the user closed the window manually

    canvas = show_state.canvas
    root.title(title)
    
    # 2. Clear previous tiles instantly without destroying the window
    canvas.delete("all")

    # 3. Draw the new state tiles
    for i, tile in enumerate(state):
        row, col = divmod(i, 3)
        x = GAP + col * (TILE + GAP)
        y = GAP + row * (TILE + GAP)
        if tile == 0:
            canvas.create_rectangle(x, y, x + TILE, y + TILE, fill="#e8e8e8", outline="")
        else:
            canvas.create_rectangle(x, y, x + TILE, y + TILE, fill="#4a90d9", outline="")
            canvas.create_text(x + TILE / 2, y + TILE / 2, text=str(tile),
                               fill="white", font=("Arial", 36, "bold"))

    # 4. Refresh the UI and pause for the specified seconds without blocking execution
    root.update()
    if seconds > 0:
        start_time = time.time()
        while time.time() - start_time < seconds:
            # Check if window was closed mid-animation
            if show_state.root is None:
                break
            root.update_idletasks()
            root.update()
            time.sleep(0.01)  


def read_input():
    """Returns (algorithm, heuristic, state); state is None for a random one."""
    algorithm = input("Algorithm (bfs / dfs / ucs / astar): ").strip().lower()
    while algorithm not in ("bfs", "dfs", "ucs", "astar"):
        algorithm = input("Invalid. Choose bfs, dfs, ucs or astar: ").strip().lower()

    heuristic = None
    if algorithm == "astar":
        heuristic = input("Heuristic (manhattan / euclidean): ").strip().lower()
        while heuristic not in ("manhattan", "euclidean"):
            heuristic = input("Invalid. Choose manhattan or euclidean: ").strip().lower()

    while True:
        text = input("Initial state (9 numbers, or Enter for random): ").replace(",", " ").split()
        if not text:
            return algorithm, heuristic, None
        nums = [x for x in map(int, text) if x != 0]
        if sorted(text) == sorted(map(str, range(9))) and inversionCount(nums) % 2 == 0:
            return algorithm, heuristic, list(map(int, text))
        print("Invalid or unsolvable state. Use each of 0-8 once.")

#this is a standard merge sort inversion count i implemented it bec i read that 8 puzzle are solvable 
#only if the inversions are even
def countAndMerge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]
    res = 0
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            res += (n1 - i)
        k += 1
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

    return res
def countInv(arr, l, r):
    res = 0
    if l < r:
        m = (r + l) // 2
        res += countInv(arr, l, m)
        res += countInv(arr, m + 1, r)
        res += countAndMerge(arr, l, m, r)
    return res

def inversionCount(arr):
    result=countInv(arr, 0, len(arr) - 1)
   
    return result