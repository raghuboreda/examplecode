# find number of connected components in an undirected graph
# n = 4, edges = [[0,1],[1,2],[2,3]]
from collections import deque


def num_connected_components(n, edges):
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        src = edge[0]
        dst = edge[1]
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    visited = [-1]*n
    cnt = 0
    for i in range(n):
        if visited[i] == -1:
            dfs(i, visited, adj_list)
            cnt += 1
    return cnt


def dfs(node, visited, adj):
    visited[node] = 1
    for neighbor in adj[node]:
        if visited[neighbor] == -1:
            dfs(neighbor, visited, adj)
    return


def bfs(node, visited, adj):
    q = deque()
    q.append(node)
    while q:
        curr = q.popleft()
        visited[curr] = 1
        for neighbor in adj[curr]:
            if visited[neighbor] == -1:
                q.append(neighbor)
                visited[neighbor] = 1
    return


print(num_connected_components(5, [[0, 1], [1, 2], [3, 4]]))
# Is undirected graph have cycles
# differentiate between tree edge's and cross edge's in BFS
# differentiate between tree edge's and back edge
# n = 4, edges = [[0,1],[1,2],[2,3]]


def is_graph_has_cycles(n, edges):
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        src = edge[0]
        dst = edge[1]
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    visited = [-1]*n
    cnt = 0
    for i in range(n):
        if visited[i] == -1:
            # This is not a tree.
            if cnt == 1:
                return False
            v = bfs_graph(i, visited, adj_list)
            if not v:
                return False
            cnt += 1
    return True


def bfs_graph(node, visited, adj):
    q = deque()
    q.append(node)
    visited[node] = 1
    parent = {}
    while q:
        curr = q.popleft()
        for neighbor in adj[curr]:
            if visited[neighbor] == -1:
                visited[neighbor] = 1
                parent[neighbor] = curr
                q.append(neighbor)
            else:
                if parent[curr] == neighbor:  # tree edge in reverse
                    continue
                else:  # This is cross edge
                    return False
    return True

# Problem 3: Is undirected graph a bipartite graph
# outer loop? Yes. graphs can be disconnected
# base dfs
# extension , just checking the colors


def is_graph_bipartite(n, edges):
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        src = edge[0]
        dst = edge[1]
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    visited = [-1]*n
    # colors can be 0 or 1
    colors = [-1]*n
    for i in range(n):
        if visited[i] == -1:
            colors[i] = 0
            v = dfs_bipartite(i, visited, adj_list, colors)
            if not v:
                return False
    return True


def dfs_bipartite(node, visited, adj, colors):
    visited[node] = 1
    for neighbor in adj[node]:
        if visited[neighbor] == -1:
            colors[neighbor] = 1 - colors[node]
            return dfs_bipartite(neighbor, visited, adj, colors)
        else:
            if colors[neighbor] == colors[node]:
                return False
    return True

# Problem 4: Number of islands
# input is a matrix of 1's and 0's. 1 is land and 0 is water
# If any one of four neighbors is 1


def num_islands(matrix):
    visited = {}
    cnt = 0
    row_len = len(matrix)
    col_len = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) not in visited and matrix[i][j] == 1:
                visited[(i, j)] = True
                dfs_islands(i, j, visited, matrix, row_len, col_len)
                cnt += 1
    return cnt


def dfs_islands(i, j, visited, matrix, row_len, col_len):
    # base case
    if i < 0 or j < 0 or i > row_len or j > col_len:
        return
    visited[(i, j)] = True
    if matrix[i][j] == 1:
        dfs_islands(i+1, j, visited, matrix, row_len, col_len)
        dfs_islands(i-1, j, visited, matrix, row_len, col_len)
        dfs_islands(i, j+1, visited, matrix, row_len, col_len)
        dfs_islands(i, j-1, visited, matrix, row_len, col_len)
    return

# snake and ladder game
# use bfs to find shortest path to destination


def minimum_steps_to_goal(n, s_l):
    distance = [-1] * (n + 1)
    q = deque()
    q.append(0)
    while q:
        curr = q.popleft()
        for neighbor in range(curr+1, curr+7):
            landed = s_l[neighbor]
            if distance[landed] != -1 and landed != n:
                distance[landed] = distance[curr] + 1
                q.append(landed)
            elif landed == n:
                return distance
    return -1


# cycle detection on a DAG
def class_course_schedule(n, courses):
    # Do we need to build a graph, yes, we need to make adj_list
    # How do we traverse? Use DFS to detect cycles on DAG
    # Do you need a outer loop? Yes.
    adj_list = [[] for _ in range(n)]
    for edge in courses:
        src = edge[0]
        dst = edge[1]
        adj_list[src].append(dst)

    arrival = [-1] * n
    departure = [-1] * n
    visited = [-1] * n
    time = [0]
    def dfs_bk( node ):
        visited[node] = 1
        arrival[node] = time[0]
        time[0] += 1
        for neighbor in adj_list[node]:
            if visited[neighbor] == -1:
                if dfs_bk(neighbor) == False:
                    return False
            else:
                if departure[node] == -1:
                    return False
        departure[node] = time[0]
        time[0] += 1
        return True

    for i in range(n):
        if not dfs_bk(i):
            return True
    return False

def kahns():
    pass

def num_basins( matrix ):
    '''
    :param matrix:
    sink is defined as the minimum of all adjacent neighbors
    direct flow is when
    :return:
    list with number of connected components of each basin
    '''





