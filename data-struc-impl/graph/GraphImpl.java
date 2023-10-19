import java.util.*;

class GraphImpl<T> {

	// edges
	private Map<T, List<T>> adjVerticies = new HashMap<>();

	// insert vertex
	public void addVertex(T v) {
		this.adjVerticies.putIfAbsent(v, new LinkedList<T>());
	}

	public void removeVertex(T v) {
		this.adjVerticies.values().stream().forEach(e -> e.remove(v));
		this.adjVerticies.remove(v);	
	}
	// Undirected
	public void addEdge(T src, T dest) {
		if (!this.adjVerticies.containsKey(src)) addVertex(src);
		if (!this.adjVerticies.containsKey(dest)) addVertex(dest);
		this.adjVerticies.get(src).add(dest);
		this.adjVerticies.get(dest).add(src);
	}

	public void removeEdge(T src, T dest) {
		List<T> srcList = this.adjVerticies.get(src);
		List<T> destList = this.adjVerticies.get(dest);
		if (srcList != null && destList != null) {
			System.out.println("removeEdge");
			this.adjVerticies.get(src).remove(dest);
			this.adjVerticies.get(dest).remove(src);
		}
	}

	public int getVertexCount() {
		return this.adjVerticies.keySet().size();
	}

	public int getEdgesCount(boolean bi) {
		int count = 0;
		for (T v: adjVerticies.keySet()) {
			count += adjVerticies.get(v).size();
		}
		if (bi) {
			count /= 2;
		}
		return count;
	}

	public boolean hasVertex(T v) {
		return this.adjVerticies.containsKey(v);
	}

	public boolean hasEdge(T s, T d) {
		return this.adjVerticies.get(s).contains(d);
	}

	public static void main(String args[]) {
  
        // Object of graph is created.
        GraphImpl<Integer> g = new GraphImpl<Integer>();
  
        // edges are added.
        // Since the graph is bidirectional,
        // so boolean bidirectional is passed as true.
		g.addVertex(0);
 		g.addVertex(1);
 		g.addVertex(2);
 		g.addVertex(3);
 		g.addVertex(4);
	 	g.addVertex(5);
        g.addEdge(0, 1);
        g.addEdge(0, 4);
        g.addEdge(1, 2);
        g.addEdge(1, 3);
        g.addEdge(1, 4);
        g.addEdge(2, 3);
        g.addEdge(3, 4);
  
        System.out.println(g.getVertexCount());
  
        System.out.println(g.getEdgesCount(false));
        System.out.println(g.hasVertex(5));
		g.removeVertex(5);
        System.out.println(g.hasVertex(5));
        System.out.println(g.getVertexCount()); 
		System.out.println(g.hasEdge(0, 1));
		g.removeEdge(0, 1);
		System.out.println(g.hasEdge(0, 1));
	}
}