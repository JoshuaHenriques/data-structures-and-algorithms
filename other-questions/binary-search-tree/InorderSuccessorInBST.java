import java.util.ArrayList;
import java.util.List;

public class InorderSuccessorInBST {
	static class Node {
		int data;
		Node left, right;

		Node(int d) {
			data = d;
			left = right = null;
		}
	}

	// returns the inorder successor of the Node x in BST (rooted at 'root')
	public static void inorderSuccessor(Node root, Node x) {

		List inorder = new ArrayList();

		if (root == null)
			return;

		while (root != null) {
			inorder.add(root.data);
			inorderSuccessor(root.left, x);
			inorderSuccessor(root.right, x);
		}
		System.out.println(inorder.toString());
	}

	public static void main(String[] args) {

		Node root = new Node(3);
		root.left = new Node(1);
		root.right = new Node(2);

		Node ref = new Node(2);

		inorderSuccessor(root, ref);
	}
}