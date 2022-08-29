#DFS
def find_biggest_island(map_matrix):  
    if not map_matrix or len(map_matrix) == 0:
        return 0
    island_size = 0
    max_island_size = 0
    for i in range(len(map_matrix)):
        for j in range(len(map_matrix[0])):

            if map_matrix[i][j] == 1:
                island_size = mark_island(map_matrix, i, j, island_size)
                if island_size > max_island_size:
                    max_island_size = island_size
                island_size = 0
    
    return max_island_size

def mark_island(map_matrix, i, j, island_size):
    if i > len(map_matrix) - 1 or j > len(map_matrix[0]) - 1 or i < 0 or j < 0: 
        return island_size
    if map_matrix[i][j] == 1:
        map_matrix[i][j] = 0
        island_size += 1

        island_size = mark_island(map_matrix, i, j + 1, island_size) #right
        island_size = mark_island(map_matrix, i, j - 1, island_size) #left
        island_size = mark_island(map_matrix, i - 1, j, island_size) #up
        island_size = mark_island(map_matrix, i + 1, j, island_size) #down
        return island_size
    else:
        return island_size
