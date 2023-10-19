package graph;

import java.util.*;

class DepthFirstSearch {

	public static <T> boolean dfsIterative(Graph<T> graph, T vertex0, T vertex1) {
		Stack<T> stack = new Stack<T>();
		Set<T> visited = new HashSet<T>();
		stack.add(vertex0);

		while (!stack.isEmpty()) {
			T v = stack.pop();
			if (!visited.contains(v)) {
				if (v.equals(vertex1)) {
					return true;
				}
				visited.add(v);
			}

			List<T> adj = graph.getAdjMap().get(v);
			for (int i = 0; i < adj.size(); i++) {
				T vert = adj.get(i);
				if (!visited.contains(vert)) {
					stack.add(vert);
				}
			}
		}
		return false;
	}

	public static <T> void dfsRecursionCaller(Graph<T> graph, T vertex0, T vertex1) {
		Set<T> visited = new HashSet<>();
		System.out.println(dfsRecursion(visited, graph, vertex0, vertex1));
	}

	public static <T> boolean dfsRecursion(Set<T> visited, Graph<T> graph, T vertex0, T vertex1) {
		List<T> adj = graph.getAdjMap().get(vertex0);
		visited.add(vertex0);
		if (vertex0.equals(vertex1)) {
			return true;
		}
		for (int i = 0; i < adj.size(); i++) {
			T vert = adj.get(i);
			if (!visited.contains(vert)) {
				if (dfsRecursion(visited, graph, vert, vertex1))
					return true;
			}
		}
		return false;
	}

	public static void main(String[] args) {
		Map<Integer, List<Integer>> edges = new HashMap<>();
		edges.put(0, new ArrayList<>(Arrays.asList(3, 4)));
		edges.put(1, new ArrayList<>(Arrays.asList(0)));
		edges.put(2, new ArrayList<>(Arrays.asList(2, 4)));
		edges.put(3, new ArrayList<>(Arrays.asList(0, 3)));
		edges.put(4, new ArrayList<>(Arrays.asList(2)));
		Graph<Integer> graph = new Graph<>(edges);

		System.out.println(dfsIterative(graph, 1, 2));
		System.out.println(dfsIterative(graph, 0, 1));
		dfsRecursionCaller(graph, 1, 2);
		dfsRecursionCaller(graph, 0, 1);
	}
}