import tkinter as tk
from tkinter import filedialog
import subprocess
from DFS import *

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Choose input file", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
        order, title, G, pos = perform_dfs(file_path)
        visualize(order, title, G, pos,print_output=True)
def graph_dfs(file_path):
    order, title, G, pos = perform_dfs(file_path)
    visualize(order, title, G, pos,print_output=False)

root = tk.Tk()
root.title("Import")
root.geometry("300x200")

button = tk.Button(root, text="Import file", command=open_file_dialog)
button.pack(pady=20)
button_dfs = tk.Button(root, text="Graph DFS", command=lambda: graph_dfs("input.txt"))
button_dfs.pack(pady=20)

root.mainloop()
