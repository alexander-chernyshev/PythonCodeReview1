from Graph import Graph, dfs_generation, kruskal_generation
from Maze import Maze, bfs
from InOut import open_maze
import time


def test_big_input_dfs_case():
    start_time = time.time()
    graph = Graph(50, 50)
    dfs_generation(graph)
    test_time = time.time() - start_time
    print("time for input 50x50 dfs is", test_time)
    assert test_time < 2


def test_big_input_kruskal_case():
    start_time = time.time()
    graph = Graph(50, 50)
    kruskal_generation(graph)
    test_time = time.time() - start_time
    print("time for input 50x50 kruskal is", test_time)
    assert test_time < 3


def test_big_input_bfs_1():
    m = open_maze("tests/big_input_1.txt")
    start_time = time.time()
    bfs(m)
    test_time = time.time() - start_time
    print("bfs big_input_1 time", test_time)
    assert test_time < 2


def test_big_input_bfs_2():
    m = open_maze("tests/big_input_2.txt")
    start_time = time.time()
    bfs(m)
    test_time = time.time() - start_time
    print("bfs big_input_2 time", test_time)
    assert test_time < 2