/*
#1
Given a directed graph, design an algorithm to find out whether there is a route
between two nodes.

Example:
Directed
Input: [[3, 4], [0], [2, 4], [0, 3], [2]], start=1, target=2
Output: True
*/
import java.util.*;

class RouteBetweenNodes {

	public static boolean routeBetween(Graph<Integer> graph, int start, int target) {
		Queue<Integer> queue = new PriorityQueue<>();
		Set<Integer> visited = new HashSet<>();
		queue.add(start);
		

		while (!queue.isEmpty()) {
			int vertex = queue.poll();

			if (vertex == target) {
				return true;
			}
			visited.add(vertex);

			for (int vert: graph.getAdjMap().get(vertex)) {
				if (!visited.contains(vert)) {
					queue.add(vert);
				}
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

		System.out.println(routeBetween(graph, 1, 2));
		System.out.println(routeBetween(graph, 0, 1));
	}
}