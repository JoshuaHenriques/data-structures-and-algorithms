import java.util.List;
import java.util.ArrayList;

public class SinglyLinkedList<T> {
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

		public Node(T data, Node<T> next) {
			this.data = data;
			this.next = next;
		}
	}

	private Node<T> head;
	private int size;

	public SinglyLinkedList() {
		this.head = null;
	}

	public void insert(T data) {
		Node<T> insert = new Node<>(data);
		if (this.head == null) {
			this.head = insert;
			size++;
			return;
		}
		Node<T> curr = this.head;
		while (curr.next != null) {
			curr = curr.next;
		}
		curr.next = insert;
		size++;
	}

	public void delete(T data) {
		if (this.head == null)
			return;
		Node<T> curr = this.head;
		Node<T> prev = this.head;
		while (curr.next != null) {
			if (curr.data == data) {
				prev.next = curr.next;
				size--;
				return;
			}
			prev = curr;
			curr = curr.next;
		}
	}

	public int search(T data) {
		Node<T> curr = this.head;
		int cnt = 0;
		while (curr.next != null && curr.data != data) {
			cnt++;
			curr = curr.next;
		}
		if (curr.data == data)
			return cnt;
		return -1;
	}

	public T get(int index) {
		Node<T> curr = this.head;
		int cnt = 0;
		while (curr.next != null && cnt != index) {
			cnt++;
			curr = curr.next;
		}
		if (cnt == index)
			return curr.data;
		return null;
	}

	public int size() {
		return this.size;
	}

	public String toString() {
		List<T> list = new ArrayList<>();
		Node<T> curr = this.head;
		while (curr != null) {
			list.add(curr.data);
			curr = curr.next;
		}
		return list.toString();
	}

	public static void main(String[] args) {
		SinglyLinkedList<Integer> ll = new SinglyLinkedList<>();
		System.out.println(ll.toString());
		ll.insert(4);
		System.out.println(ll.toString());
		ll.insert(2);
		ll.insert(18);
		ll.insert(43);
		ll.insert(993);
		ll.insert(34);
		System.out.println(ll.toString());
		System.out.println(ll.search(18));
		System.out.println(ll.get(2));
		System.out.println(ll.size());
		System.out.println(ll.get(4));
		System.out.println(ll.search(993));
	}
}