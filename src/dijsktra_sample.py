from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path


if __name__ == '__main__':
  g = Graph()
  g.add_node('a')
  g.add_node('b')
  g.add_node('c')

  g.add_edge('a', 'b', 10)
  g.add_edge('b', 'a', 10)
  g.add_edge('b', 'c', 10)
  g.add_edge('c', 'b', 10)
  g.add_edge('a', 'c', 15)
  g.add_edge('c', 'a', 15)

  v, p = dijsktra(g, 'a')

  print("how well does it work? {} {}".format(v,p))

  # returns ({'a': 0}, {})
  #s = [(0,0),(1,1),(2,2),(2,1)]

  #print('hi')