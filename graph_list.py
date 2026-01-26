from collections import deque


class GraphList:
    """
    Graph implementation using an Adjacency List.

    Key ideas:
    - The graph is stored as a dictionary:
        adj[u] = list of neighbors of u
      For weighted graphs:
        adj[u] = list of (neighbor, weight) pairs

    Supports:
    - Directed or undirected graphs
    - Weighted or unweighted edges
    - Add/remove edges
    - Check edge existence
    - Get neighbors
    - Display adjacency structure
    """

    def __init__(self, directed=False, weighted=False):
        """
        Initialize the graph.

        Parameters
        ----------
        directed : bool, optional
            If True, edges have direction (u -> v).
            If False, edges are bidirectional (u <-> v).

        weighted : bool, optional
            If True, edges store weights (u -> v has a weight).
            If False, edges are unweighted.
        """
        self.directed = directed
        self.weighted = weighted

        # Adjacency list storage:
        # Unweighted: adj[u] = [v1, v2, ...]
        # Weighted:   adj[u] = [(v1, w1), (v2, w2), ...]
        self.adj = {}

    def add_vertex(self, v):
        """
        Add a vertex to the graph if it does not already exist.

        Parameters
        ----------
        v : hashable
            Vertex label (int, str, tuple, etc.).
        """
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v, weight=1):
        """
        Add an edge between u and v.

        For unweighted graphs, 'weight' is ignored (default 1).
        For weighted graphs, the edge stores (v, weight).

        Parameters
        ----------
        u : hashable
            Source vertex.

        v : hashable
            Destination vertex.

        weight : int or float, optional
            Edge weight (used only if weighted=True).
        """
        # Ensure both vertices exist
        self.add_vertex(u)
        self.add_vertex(v)

        if self.weighted:
            # Add weighted edge u -> v
            self._add_weighted_neighbor(u, v, weight)

            # If undirected, add v -> u as well
            if not self.directed:
                self._add_weighted_neighbor(v, u, weight)
        else:
            # Add unweighted edge u -> v
            self._add_unweighted_neighbor(u, v)

            # If undirected, add v -> u as well
            if not self.directed:
                self._add_unweighted_neighbor(v, u)

    def remove_edge(self, u, v):
        """
        Remove the edge between u and v (if it exists).

        Parameters
        ----------
        u : hashable
            Source vertex.

        v : hashable
            Destination vertex.
        """
        if u not in self.adj or v not in self.adj:
            return  # nothing to remove

        if self.weighted:
            # Remove (v, w) from adj[u]
            self.adj[u] = [(nbr, w) for (nbr, w) in self.adj[u] if nbr != v]
            if not self.directed:
                self.adj[v] = [(nbr, w) for (nbr, w) in self.adj[v] if nbr != u]
        else:
            # Remove v from adj[u]
            self.adj[u] = [nbr for nbr in self.adj[u] if nbr != v]
            if not self.directed:
                self.adj[v] = [nbr for nbr in self.adj[v] if nbr != u]

    def has_edge(self, u, v):
        """
        Check whether there is an edge from u to v.

        Returns
        -------
        bool
            True if edge exists, otherwise False.
        """
        if u not in self.adj:
            return False

        if self.weighted:
            return any(nbr == v for (nbr, _) in self.adj[u])
        else:
            return v in self.adj[u]

    def neighbors(self, u):
        """
        Return neighbors of vertex u.

        For unweighted graphs:
            returns [v1, v2, ...]
        For weighted graphs:
            returns [(v1, w1), (v2, w2), ...]

        Raises
        ------
        KeyError
            If vertex u does not exist.
        """
        if u not in self.adj:
            raise KeyError(f"Vertex {u} does not exist in the graph.")
        return self.adj[u]

    def display(self):
        """
        Print the adjacency list in a readable format.
        """
        print("Adjacency List:")
        for u in self.adj:
            print(f"{u} -> {self.adj[u]}")

    # -------------------------
    # Depth First Search
    # -------------------------

    def dfs(self, start):
        """
        Perform Depth-First Search (DFS) using an explicit stack.

        Parameters
        ----------
        start : hashable
            Starting vertex for DFS.

        Returns
        -------
        list
            Order of vertices visited in DFS.
        """
        if start not in self.adj:
            raise KeyError(f"Vertex {start} does not exist in the graph.")

        visited = set()
        stack = [start]
        traversal = []

        while stack:
            u = stack.pop()

            if u not in visited:
                visited.add(u)
                traversal.append(u)

                # Push neighbors in reverse order
                # so DFS order looks natural (left to right)
                if self.weighted:
                    neighbors = [v for (v, _) in self.adj[u]]
                else:
                    neighbors = self.adj[u]

                for v in reversed(neighbors):
                    if v not in visited:
                        stack.append(v)

        return traversal

    # -------------------------
    # Breadth First Search
    # -------------------------

    def bfs(self, start):
        """
        Perform Breadth-First Search (BFS) using a queue.

        Parameters
        ----------
        start : hashable
            Starting vertex for BFS.

        Returns
        -------
        list
            Order of vertices visited in BFS.
        """
        if start not in self.adj:
            raise KeyError(f"Vertex {start} does not exist in the graph.")

        visited = set([start])
        q = deque([start])
        traversal = []

        while q:
            u = q.popleft()
            traversal.append(u)

            # Get neighbors depending on weighted/unweighted
            if self.weighted:
                neighbors = [v for (v, _) in self.adj[u]]
            else:
                neighbors = self.adj[u]

            for v in neighbors:
                if v not in visited:
                    visited.add(v)
                    q.append(v)

        return traversal

    # -------------------------
    # Internal helper methods
    # -------------------------

    def _add_unweighted_neighbor(self, u, v):
        """
        Add neighbor v to adj[u] for an unweighted graph,
        avoiding duplicate edges.
        """
        if v not in self.adj[u]:
            self.adj[u].append(v)

    def _add_weighted_neighbor(self, u, v, weight):
        """
        Add (v, weight) to adj[u] for a weighted graph.
        If v already exists as a neighbor, update its weight.
        """
        for i, (nbr, w) in enumerate(self.adj[u]):
            if nbr == v:
                # Update existing edge weight
                self.adj[u][i] = (v, weight)
                return
        # If not found, append new neighbor entry
        self.adj[u].append((v, weight))


# Example usage:

g = GraphList(directed=False, weighted=False)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

g.display()

# Depth First Search
print(f"\nDFS from 0: {g.dfs(0)}")

# Breadth First Search
print(f"\nBFS from 0: {g.bfs(0)}")
