import java.util.*;

public class BreadthFirstSearch {

	public static <T> boolean bfsIterative(Graph<T> graph, T vertex0, T vertex1) {
		Queue<T> queue = new PriorityQueue<>();
		Set<T> visited = new HashSet<T>();
		queue.add(vertex0);

		while (!queue.isEmpty()) {
			T v = queue.poll();
			if (v.equals(vertex1)) {
				return true;
			}
			visited.add(v);

			List<T> adj = graph.getAdjMap().get(v);
			for (int i = 0; i < adj.size(); i++) {
				T vert = adj.get(i);
				if (!visited.contains(vert)) {
					queue.add(vert);
				}
			}
		}
		return false;
	}

	public static <T> void bfsRecursionCaller(Graph<T> graph, T vertex0, T vertex1) {
		Set<T> visited = new HashSet<>();
		Queue<T> queue = new PriorityQueue<>();
		queue.add(vertex0);
		System.out.println(bfsRecursion(visited, graph, vertex0, vertex1, queue));
	}

	public static <T> boolean bfsRecursion(Set<T> visited, Graph<T> graph, T vertex0, T vertex1, Queue<T> queue) {
		if (queue.isEmpty()) {
			return false;
		}
		
		T v = queue.poll();

		if (v.equals(vertex1)) {
			return true;
		}

		List<T> adj = graph.getAdjMap().get(v);
		for (T vert: adj) {
			if (!visited.contains(vert)) {
				visited.add(vert);
				queue.add(vert);
			}
		}
		if (bfsRecursion(visited, graph, v, vertex1, queue)) return true;
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

		System.out.println(bfsIterative(graph, 1, 2));
		System.out.println(bfsIterative(graph, 0, 1));
		bfsRecursionCaller(graph, 1, 2);
		bfsRecursionCaller(graph, 0, 1);
	}
}
