##########################################################
# Name: Sean Chen
# Assignment:  Cellular Automaton Simulations - Problem 1
# Date: 05/02/2018
##########################################################

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

#-create a x*y grid 
def grid(x,y,cold, neighbor, hot):
    my_grid = np.zeros((x*y), dtype='f').reshape(y,x)
    my_grid[:] = neighbor
    
    my_grid[1:3,4] = cold
    my_grid[-3,2:8] = hot
    
    return my_grid
    
def diffusion(diff_rate, site, N, NE, E, SE, S, SW, W, NW):
    return (1-8*diff_rate)*site + diff_rate*(N + NE + E +  SE + S + SW + W + NW)

def diffusion_nonSto (x,y,times, diff_rate, cold, hot, neighbor):
    #create a diffusion grid
    diff_grid = grid(x,y,cold,hot, neighbor)
    
    cell = np.array(diff_grid)
    
    for n in range(times):
       for i in np.arange(1, x - 1):
            for j in np.arange(1, y - 1):
                   cell[i][j] = diffusion(diff_rate, diff_grid[i][j], diff_grid[i][j-1],
                   diff_grid[i+1][j-1], diff_grid[i+1][j], diff_grid[i+1][j+1],
                   diff_grid[i][j+1], diff_grid[i-1][j+1], diff_grid[i-1][j],diff_grid[i-1][j-1])
           
       diff_grid = np.array(cell)
    return diff_grid
          
def diffusion_Stochastic (x,y,times,diff_rate,cold, hot, neighbor):
    
    rnd = random.normal(0,.5, size=(8,))
    rnd +=((.0 - np.sum(rnd))/8.0)
    
    #create a diffusion grid 
    diff_grid = grid(x,y,cold,hot, neighbor)
    cell = np.array(diff_grid)
    
    for n in range(times):
        for i in np.arange(1, x - 1):
            for j in np.arange(1, y -1):
                cell[i][j] = ((diff_rate * (1.0+rnd[0]) * diff_grid[i][j-1]) +
                (diff_rate * (1.0 + rnd[1]) * diff_grid[i+1][j-1]) +
                (diff_rate * (1.0 + rnd[2]) * diff_grid[i+1][j]) +
                (diff_rate * (1.0 + rnd[3]) * diff_grid[i+1][j+1]) +
                (diff_rate * (1.0 + rnd[4]) * diff_grid[i][j+1]) + 
                (diff_rate * (1.0 + rnd[5]) * diff_grid[i-1][j+1])+
                (diff_rate * (1.0 + rnd[6]) * diff_grid[i-1][j]) + 
                (diff_rate * (1.0 + rnd[7]) * diff_grid[i-1][j-1]) + 
                ((1.0-(diff_rate * (8.0 + np.sum(rnd)))) * diff_grid[i,j]))
        diff_grid = np.array(cell)
    return diff_grid

def plot (grid_plot):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_axes((0,0,1,1))
    image = ax.imshow(grid_plot, interpolation='none', cmap=plt.cm.RdBu_r,
                    extent=[0,20,0,20], aspect = 'auto', zorder=0)
                    
    return plt.show()
    
if __name__ == "__main__": 

    a = diffusion_Stochastic (20,20,100,.1,0, 60, 20)
    b = diffusion_nonSto (20,20,100,.1,0, 60, 20)
    
    plot(a)
    plot(b)