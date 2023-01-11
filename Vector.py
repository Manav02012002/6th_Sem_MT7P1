import numpy as np
from matplotlib import pyplot as plt

colors = ['red', 'steelblue', 'blue', 'green', 'yellow']

def plot_vectors(vectors, title=None):
    fig, ax = plt.subplots(figsize=(5, 5))
    
    

    i = -1
    for x_cor, y_cor in vectors:
        i = i + 1
        ax.quiver(0, 0, x_cor, y_cor, scale=1, angles='xy', scale_units='xy', color=colors[i % len(colors)])
        
    limit = np.max(np.abs(vectors)) * 1.25
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_aspect('equal')
    
    ax.grid(True, linewidth=0.5, alpha=0.85)
    
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    if title:
        plt.title(title)
        
    plt.show()
    
    
vectors = [(1,1), (1,2), (2,3), (1,3)]
plot_vectors(vectors)

a = np.array([1,3])
b = np.array([3,1])
vectors = ([a, b, a+b])
plot_vectors(vectors)

a = np.array([1,2])
vectors = [a, 2*a]
plot_vectors(vectors)

a = np.array([1, 2])
b = np.array([-2, 3])
vectors = [a, b, a+b, a-b, 2*a, -3*a]
plot_vectors(vectors)
