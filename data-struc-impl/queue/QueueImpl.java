import java.util.List;
import java.util.ArrayList;

public class QueueImpl<T> {
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

	private Node<T> first;
	private Node<T> last;
	private int size;

	public QueueImpl() {
		this.first = null;
		this.last = null;
		this.size = 0;
	}

	public void offer(T data) {
		Node<T> offer = new Node(data);
		if(this.first != null) {
			Node<T> curr = this.first;
			while(curr.next != null) {
				curr = curr.next;
			}
			curr.next = offer;
			this.last = offer;
			size++;
		}
		else if(this.first == null && this.last == null) {
			this.first = offer;
			this.last = offer;
			size++;
		}
	}

	public T poll() {
		if(this.first == this.last && this.first != null) {
			Node<T> poll = this.first;
			this.first = null;
			this.last = null;
			size--;
			return poll.data;
		}
		else if(this.first == null) return null;
		else {
			Node<T> poll = this.first;
			this.first = this.first.next;
			size--;
			return poll.data;
		}
	}

	public T peek() {
		return this.first.data;
	}

	public T peekLast() {
		return this.last.data;
	}

	public boolean empty() {
		return this.first == null;
	}

	public int size() {
		return this.size;
	}

	public String toString() {
		List<T> list = new ArrayList<>();
		Node<T> curr = this.first;
		while(curr != null) {
			list.add(curr.data);
			curr = curr.next;
		}
		return list.toString();
	}

	public static void main(String[] args) {
		QueueImpl<Integer> queue = new QueueImpl<>();
		System.out.println(queue.toString());
		System.out.println(queue.poll());
		queue.offer(4);
		queue.offer(2);
		queue.offer(18);
		queue.offer(43);
		queue.offer(993);
		queue.offer(34);
		System.out.println(queue.toString());
		System.out.println(queue.poll());
		System.out.println(queue.toString());
		System.out.println(queue.peek());
		System.out.println(queue.peekLast());
		System.out.println(queue.empty());
		System.out.println(queue.size());
	}
}
