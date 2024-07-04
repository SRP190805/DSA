Here is the markdown file code for the given content about Graphs:

## Graphs

A Graph is a non-linear data structure that consists of vertices (nodes) and edges.

### Vertices and Edges

* A vertex, also called a node, is a point or an object in the Graph.
* An edge is used to connect two vertices with each other.

Graphs are non-linear because the data structure allows us to have different paths to get from one vertex to another, unlike with linear data structures like Arrays or Linked Lists.

### Applications of Graphs

Graphs are used to represent and solve problems where the data consists of objects and relationships between them, such as:

* **Social Networks:** Each person is a vertex, and relationships (like friendships) are the edges. Algorithms can suggest potential friends.
* **Maps and Navigation:** Locations, like a town or bus stops, are stored as vertices, and roads are stored as edges. Algorithms can find the shortest route between two locations when stored as a Graph.
* **Internet:** Can be represented as a Graph, with web pages as vertices and hyperlinks as edges.
* **Biology:** Graphs can model systems like neural networks or the spread of diseases.

### Graph Properties

**Use the animation below to get an understanding of the different Graph properties, and how these properties can be combined.**

[Imagen of Graph properties animation (You can replace this line with a link to an image depicting Graph properties animation]

* **Weighted:** A weighted Graph is a Graph where the edges have values. The weight value of an edge can represent things like distance, capacity, time, or probability.
* **Connected:** A connected Graph is when all the vertices are connected through edges somehow. A Graph that is not connected, is a Graph with isolated (disjoint) subgraphs, or single isolated vertices.
* **Directed:** A directed Graph, also known as a digraph, is when the edges between the vertex pairs have a direction. The direction of an edge can represent things like hierarchy or flow.
* **Cyclic:** A cyclic Graph is defined differently depending on whether it is directed or not:
    * A directed cyclic Graph is when you can follow a path along the directed edges that goes in circles. Removing the directed edge from F to G in the animation above makes the directed Graph not cyclic anymore.
    * An undirected cyclic Graph is when you can come back to the same vertex you started at without using the same edge more than once. The undirected Graph above is cyclic because we can start and end up in vertes C without using the same edge twice.
* **Loop:** A loop, also called a self-loop, is an edge that begins and ends on the same vertex. A loop is a cycle that only consists of one edge. By adding the loop on vertex A in the animation above, the Graph becomes cyclic.

### Graph Representations

A Graph representation tells us how a Graph is stored in memory.

Different Graph representations can:

* Take up more or less space.
* Be faster or slower to search or manipulate.
* Be better suited depending on what type of Graph we have (weighted, directed, etc.), and what we want to do with the Graph.
* Be easier to understand and implement than others.

Below are short introductions of the different Graph representations, but Adjacency Matrix is the representation we will use for Graphs moving forward in this tutorial, as it is easy to understand and implement, and works in all cases relevant for this tutorial.

Graph representations store information about which vertices are adjacent, and how the edges between the vertices are. Graph representations are slightly different if the edges are directed or weighted.

Two vertices are adjacent, or neighbors, if there is an edge between them.

### Adjacency Matrix Graph Representation

The Adjacency Matrix is the Graph representation (structure) we will use for this tutorial.

How to implement an Adjacency Matrix is shown on the next page.

The Adjacency Matrix is a 2D array (matrix) where each cell on index `(i,j)` stores information about the edge from vertex `i` to vertex `j`.

Below is a Graph with the Adjacency Matrix representation next to it.

| A | B | C | D |
|---|---|---|---|
| 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 |

An undirected Graph and the adjacency matrix

The adjacency matrix above represents an undirected Graph, so the values '1' only tell us where the edges are. Also, the values in the adjacency matrix is symmetrical because the edges go both ways (undirected Graph).

To create a directed Graph with an adjacency matrix, we must decide which vertices the edges go from and to, by
