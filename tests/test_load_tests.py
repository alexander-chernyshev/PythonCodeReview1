from Graph import Graph, dfs_generation, kruskal_generation
from Maze import Maze, bfs
from InOut import open_maze
import time


def test_2x2_dfs_case():
    start_time = time.time()
    graph = Graph(2, 2)
    dfs_generation(graph)
    test_time = time.time() - start_time
    print("dfs 2x2", test_time)


def test_3x3_dfs_case():
    start_time = time.time()
    graph = Graph(3, 3)
    dfs_generation(graph)
    test_time = time.time() - start_time
    print("dfs 3x3", test_time)


def test_4x4_dfs_case():
    start_time = time.time()
    graph = Graph(4, 4)
    dfs_generation(graph)
    test_time = time.time() - start_time
    print("dfs 4x4", test_time)


def test_2x5_dfs_case():
    start_time = time.time()
    graph = Graph(2, 5)
    dfs_generation(graph)
    test_time = time.time() - start_time
    print("dfs 2x5", test_time)


def test_5x2_dfs_case():
    start_time = time.time()
    graph = Graph(5, 2)
    dfs_generation(graph)
    test_time = time.time() - start_time
    print("dfs 5x2", test_time)


def test_10x2_dfs_case():
    start_time = time.time()
    graph = Graph(10, 2)
    dfs_generation(graph)
    test_time = time.time() - start_time
    print("dfs 10x2", test_time)


def test_2x10_dfs_case():
    start_time = time.time()
    graph = Graph(2, 10)
    dfs_generation(graph)
    test_time = time.time() - start_time
    print("dfs 2x10", test_time)


def test_10x5_dfs_case():
    start_time = time.time()
    graph = Graph(10, 5)
    dfs_generation(graph)
    test_time = time.time() - start_time
    print("dfs 10x5", test_time)


def test_5x10_dfs_case():
    start_time = time.time()
    graph = Graph(5, 10)
    dfs_generation(graph)
    test_time = time.time() - start_time
    print("dfs 5x10", test_time)


def test_10x10_dfs_case():
    start_time = time.time()
    graph = Graph(10, 10)
    dfs_generation(graph)
    test_time = time.time() - start_time
    print("dfs 10x10", test_time)


def test_2x2_kruskal_case():
    start_time = time.time()
    graph = Graph(2, 2)
    kruskal_generation(graph)
    test_time = time.time() - start_time
    print("kruskal 2x2", test_time)


def test_3x3_kruskal_case():
    start_time = time.time()
    graph = Graph(3, 3)
    kruskal_generation(graph)
    test_time = time.time() - start_time
    print("kruskal 3x3", test_time)


def test_4x4_kruskal_case():
    start_time = time.time()
    graph = Graph(4, 4)
    kruskal_generation(graph)
    test_time = time.time() - start_time
    print("kruskal 4x4", test_time)


def test_2x5_kruskal_case():
    start_time = time.time()
    graph = Graph(2, 5)
    kruskal_generation(graph)
    test_time = time.time() - start_time
    print("kruskal 2x5", test_time)


def test_5x2_kruskal_case():
    start_time = time.time()
    graph = Graph(5, 2)
    kruskal_generation(graph)
    test_time = time.time() - start_time
    print("kruskal 5x2", test_time)


def test_10x2_kruskal_case():
    start_time = time.time()
    graph = Graph(10, 2)
    kruskal_generation(graph)
    test_time = time.time() - start_time
    print("kruskal 10x2", test_time)


def test_2x10_kruskal_case():
    start_time = time.time()
    graph = Graph(2, 10)
    kruskal_generation(graph)
    test_time = time.time() - start_time
    print("kruskal 2x10", test_time)


def test_10x5_kruskal_case():
    start_time = time.time()
    graph = Graph(10, 5)
    kruskal_generation(graph)
    test_time = time.time() - start_time
    print("kruskal 10x5", test_time)


def test_5x10_kruskal_case():
    start_time = time.time()
    graph = Graph(5, 10)
    kruskal_generation(graph)
    test_time = time.time() - start_time
    print("kruskal 5x10", test_time)


def test_10x10_kruskal_case():
    start_time = time.time()
    graph = Graph(10, 10)
    kruskal_generation(graph)
    test_time = time.time() - start_time
    print("kruskal 10x10", test_time)


def test_input1_bfs():
    m = open_maze("tests/input1.txt")
    start_time = time.time()
    bfs(m)
    test_time = time.time() - start_time
    print("bfs input1", test_time)


def test_input2_bfs():
    m = open_maze("tests/input2.txt")
    start_time = time.time()
    bfs(m)
    test_time = time.time() - start_time
    print("bfs input2", test_time)


def test_input3_bfs():
    m = open_maze("tests/input3.txt")
    start_time = time.time()
    bfs(m)
    test_time = time.time() - start_time
    print("bfs input3", test_time)


def test_input4_bfs():
    m = open_maze("tests/input4.txt")
    start_time = time.time()
    bfs(m)
    test_time = time.time() - start_time
    print("bfs input4", test_time)


def test_input5_bfs():
    m = open_maze("tests/input5.txt")
    start_time = time.time()
    bfs(m)
    test_time = time.time() - start_time
    print("bfs input5", test_time)
