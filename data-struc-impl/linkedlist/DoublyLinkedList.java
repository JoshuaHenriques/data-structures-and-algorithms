import java.util.List;
import java.util.ArrayList;

public class DoublyLinkedList<T> {
	public static class Node<T> {
		private T data;
		private Node<T> next;
		private Node<T> prev;

		public Node() {
			this.data = null;
			this.next = null;
			this.prev = null;
		}

		public Node(T data) {
			this.data = data;
		}
	}

	private Node<T> head;
	private int size;

	public DoublyLinkedList() {
		this.head = null;
	}

	public void insert(T data) {
		Node<T> insert = new Node<>(data);
		if(this.head == null) {
			this.head = insert;
			size++;
			return;
		}
		Node<T> curr = this.head;
		while(curr.next != null) {
			curr = curr.next;
		}
		insert.prev = curr;
		curr.next = insert;
		size++;
	}

	public void delete(T data) {
		if(this.head == null) return;
		Node<T> curr = this.head;
		Node<T> prev = this.head;
		while(curr.next != null) {
			if(curr.data == data) {
				curr.next.prev = prev;
				prev.next = curr.next;
				size--;
				break;
			}
			prev = curr;
			curr = curr.next;
		}
	}

	public int search(T data) {
		Node<T> curr = this.head;
		int cnt = 0;
		while(curr.next != null) {
			if(curr.data == data) {
				System.out.println("curr.prev.data: " + curr.prev.data);
				System.out.println("curr.data: " + curr.data);
				System.out.println("curr.next.data: " + curr.next.data);
				return cnt;
			}
			cnt++;
			curr = curr.next;
		}
		return -1;
	}

	public T get(int index) {
		Node<T> curr = this.head;
		int cnt = 0;
		while(curr.next != null && cnt != index && cnt < size) {
			cnt++;
			curr = curr.next;
		}
		if(cnt == index) return curr.data;
		else return null;
	}

	public int size() {
		return this.size;
	}

	public String toString() {
		List<T> list = new ArrayList<>();
		Node<T> curr = this.head;
		while(curr != null) {
			list.add(curr.data);
			curr = curr.next;
		}
		return list.toString();
	}

	public static void main(String[] args) {
		DoublyLinkedList<Integer> ll = new DoublyLinkedList<>();
		System.out.println(ll.toString());
		ll.insert(4);
		System.out.println(ll.toString());
		ll.insert(2);
		ll.insert(18);
		ll.insert(43);
		ll.insert(993);
		ll.insert(34);
		System.out.println(ll.toString());
		ll.search(18);
		System.out.println(ll.get(2));
		System.out.println(ll.size());
	}
}