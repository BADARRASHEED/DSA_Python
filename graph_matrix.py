class GraphMatrix:
    """
    Graph implementation using an Adjacency Matrix.

    This class supports:
    - Directed or undirected graphs
    - Weighted or unweighted edges
    - Edge addition, removal, and lookup
    - Graph visualization via matrix printing
    """

    def __init__(self, vertices, directed=False):
        """
        Initialize the graph.

        Parameters
        ----------
        vertices : int
            Total number of vertices in the graph.
            Vertices are labeled from 0 to vertices-1.

        directed : bool, optional
            If True, graph is directed.
            If False, graph is undirected.
        """
        self.vertices = vertices
        self.directed = directed

        # Create a V x V matrix initialized with 0
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        """
        Add an edge between vertex u and vertex v.

        Parameters
        ----------
        u : int
            Source vertex.

        v : int
            Destination vertex.

        weight : int or float, optional
            Weight of the edge (default is 1).
        """
        self._validate_vertex(u)
        self._validate_vertex(v)

        self.matrix[u][v] = weight

        # If graph is undirected, add symmetric edge
        if not self.directed:
            self.matrix[v][u] = weight

    def remove_edge(self, u, v):
        """
        Remove the edge between vertex u and vertex v.
        """
        self._validate_vertex(u)
        self._validate_vertex(v)

        self.matrix[u][v] = 0

        if not self.directed:
            self.matrix[v][u] = 0

    def has_edge(self, u, v):
        """
        Check whether an edge exists from u to v.

        Returns
        -------
        bool
            True if edge exists, False otherwise.
        """
        self._validate_vertex(u)
        self._validate_vertex(v)

        return self.matrix[u][v] != 0

    def get_weight(self, u, v):
        """
        Return the weight of the edge from u to v.

        Returns
        -------
        int or float
            Edge weight, or 0 if no edge exists.
        """
        self._validate_vertex(u)
        self._validate_vertex(v)

        return self.matrix[u][v]

    def display(self):
        """
        Print the adjacency matrix in a readable format.
        """
        print("Adjacency Matrix:")
        for row in self.matrix:
            print(row)

    def _validate_vertex(self, v):
        """
        Validate vertex index.

        Raises
        ------
        ValueError
            If vertex index is invalid.
        """
        if v < 0 or v >= self.vertices:
            raise ValueError(f"Vertex {v} is out of bounds")


# Example usage:

# Create an undirected graph with 4 vertices
graph = GraphMatrix(vertices=4, directed=False)

# display empty matrix
graph.display()

# Add edges
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3, weight=5)

# Display matrix
graph.display()

# Check edges
print(graph.has_edge(0, 1))  # True
print(graph.get_weight(1, 3))  # 5

# Remove edge
graph.remove_edge(0, 2)
graph.display()
