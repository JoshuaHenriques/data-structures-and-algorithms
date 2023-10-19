package graph;

import java.util.*;

// Directed graph
class Graph<T> {

	// Edges stored in both Map and 2D List (to show you can use both)
	private Map<T, List<T>> adjVerticies0;
	// Each index is a vertex
	private List<List<T>> adjVerticies1;

	public Graph() {
		this.adjVerticies0 = new HashMap<>();
		this.adjVerticies1 = new ArrayList<List<T>>();
	}

	public Graph(Map<T, List<T>> adjVerticies0) {
		this.adjVerticies0 = adjVerticies0;
	}

	public Graph(List<List<T>> adjVerticies1) {
		this.adjVerticies1 = adjVerticies1;
	}

	public Map<T, List<T>> getAdjMap() {
		return this.adjVerticies0;
	}

	public List<List<T>> getAdjList() {
		return this.adjVerticies1;
	}

	public static void main(String[] args) {
		Graph<Integer> graph0 = new Graph<>();
		graph0.getAdjList().add(new ArrayList<>(Arrays.asList(1, 3, 4)));
		graph0.getAdjList().add(new ArrayList<>(Arrays.asList(1)));
		graph0.getAdjList().add(new ArrayList<>(Arrays.asList(2, 4)));
		graph0.getAdjList().add(new ArrayList<>(Arrays.asList(0, 3)));
		graph0.getAdjList().add(new ArrayList<>(Arrays.asList(1, 3)));
		System.out.println(graph0.getAdjList());

		graph0.getAdjMap().put(0, new ArrayList<>(Arrays.asList(1, 3, 4)));
		graph0.getAdjMap().put(1, new ArrayList<>(Arrays.asList(1)));
		graph0.getAdjMap().put(2, new ArrayList<>(Arrays.asList(2, 4)));
		graph0.getAdjMap().put(3, new ArrayList<>(Arrays.asList(0, 3)));
		graph0.getAdjMap().put(4, new ArrayList<>(Arrays.asList(1, 3)));
		System.out.println(graph0.getAdjMap());
	}
}