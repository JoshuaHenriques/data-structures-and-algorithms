import java.util.List;
import java.util.ArrayList;

public class StackImpl<T> {
	public static class Node<T> {
		private T data;
		private Node<T> next;

		public Node() {
			this.data = null;
			this.next = null;
		}

		public Node(T data) {
			this.data = data;
		}
	}

	private Node<T> top;
	private int size;

	public StackImpl() {
		this.top = null;
		this.size = 0;
	}

	public T pop() {
		if(this.top == null) return null;
		T pop = this.top.data;
		this.top = top.next;
		size--;
		return pop;
	}

	public int size() {
		return this.size;
	}

	public boolean empty() {
		return this.top == null;
	}

	public T peek() {
		return this.top.data;
	}

	public T push(T data) {
		Node<T> push = new Node(data);
		push.next = this.top;
		this.top = push;
		size++;
		return data;
	}

	public int search(T data) {
		Node<T> curr = this.top;
		int pos = 0;
		while(curr != null) {
			if(curr.data == data) return pos+1;
			pos++;
			curr = curr.next;
		}
		return -1;
	}

	public String toString() {
		Node<T> curr = this.top;
		List<T> list = new ArrayList<>();
		while(curr != null) {
			list.add(curr.data);
			curr = curr.next;
		}
		return list.toString();
	}

	public static void main(String[] args) {
		StackImpl<Integer> stack = new StackImpl<>();
		System.out.println(stack.toString());
		System.out.println(stack.pop());
		stack.push(4);
		stack.push(2);
		stack.push(18);
		stack.push(43);
		stack.push(993);
		stack.push(34);
		System.out.println(stack.toString());
		System.out.println(stack.pop());
		System.out.println(stack.toString());
		System.out.println(stack.search(18));
		System.out.println(stack.toString());
		System.out.println(stack.peek());
		System.out.println(stack.empty());
		System.out.println(stack.size());
	}
}
