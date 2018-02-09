from collections import defaultdict

class Graph:

  def init(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
  visited = {initial: 0}
  path = defaultdict(list)

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
              path[edge].append(min_node)
  return path

g = Graph()

g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')

g.add_edge('A','B',12)
g.add_edge('A','C',7)
g.add_edge('B','D',1)
g.add_edge('B','A',12)
g.add_edge('D','E',8)
g.add_edge('C','F',3)
g.add_edge('D','G',5)
g.add_edge('F','B',1)
g.add_edge('F','G',2)
g.add_edge('C','D',13)
g.add_edge('E','B',6)

print(dijkstra(g, 'A')['B'])