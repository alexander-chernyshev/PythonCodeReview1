from Graph import Graph, dfs_generation, kruskal_generation
import time

for i in range(2, 21):
    start_time = time.time()
    graph = Graph(i, i)
    dfs_generation(graph)
    print("dfs {0} x {1} ".format(i, i) + str(time.time()-start_time))

for i in range(2, 21):
    start_time = time.time()
    graph = Graph(i, i)
    kruskal_generation(graph)
    print("kruskal {0} x {1} ".format(i, i) + str(time.time()-start_time))