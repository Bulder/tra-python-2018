This is a repository for an university course Python-assignment

#main.py
The script finds the route in a weighted undirectional graph with the smallest maximum weight for an edge

Usage:
```python
python main.py graph_file.txt
```

The script expects files with the syntax of
```
 1|[int number of nodes] [int number of edges]
 n|[int node1] [int node2] [int weight]
   ...
-2|[int target node]
-1|
```
with the last line of the file being empty

On a successful operation it will output an array containing the sequence of nodes forming the or one of the best paths, followed by the highest weight along the route

#tester.py
A script for helping in testing the performance of the main script.
It runs the main.py script, passing along files as chosen by the first variable (you can use * wildcards). By adding a number onto the command, you can set how many times it'll iterate each file to create more data points. It expects that the files ends have a file extension and have some unique value as the last part separated from the main part with _ (eg "graph_big_100.txt")
Usage:
```python
python tester.py /folder/of/files* [optionally number for iterations]
```

The script will print the results as a CSV string
