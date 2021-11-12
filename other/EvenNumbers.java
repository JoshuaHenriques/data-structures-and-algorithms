package other;
/*
Question:
Given an array arr[] of N elements. The task is to find the maximum number of
the contiguous even numbers in the given array.

Input: arr[] = {1, 2, 3, 4, 6, 7}
Output: 2
Max seq: {4, 6}

Input: arr[] = {1, 0, 2, 4, 3, 8, 9}
Ouput: 3
Max seq: {0, 2, 4}
*/

import java.util.HashSet;
import java.util.List;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Set;
import java.util.ArrayList;

class SinglyLinkedList<T> {
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

		public T getData() {
			return this.data;
		}

		public Node<T> getNext() {
			return this.next;
		}
	}

	private Node<T> head;
	private int size;

	public SinglyLinkedList() {
		this.head = null;
	}

	public Node<T> getHead(){
		return this.head;
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
}

// Time Complexity: O(N)
// Space Complexity: O(N)
public class EvenNumbers {

	private static int contigEvenNumbers0(int[] array) {
		int sP = 1;
		int cnt = 1;
		Set<Integer> contig = new HashSet<>();

		for(int i = 0; i < array.length - 1; i++){
			if(array[i] % 2 == 0 && array[sP] % 2 == 0) {
				cnt++;
				contig.add(array[i]);
				contig.add(array[sP]);
				sP++;
				continue;
			}
			sP++;
		}

		System.out.println(contig);
		return cnt;
	}

	private static int contigEvenNumbers1(List<Integer> list) {
		int sP = 1;
		int cnt = 1;
		Set<Integer> contig = new HashSet<>();
		 
		for(int i = 0; i < list.size() - 1; i++) {
			if(list.get(i) % 2 == 0 && list.get(sP) % 2 == 0) {
				cnt++;
				contig.add(list.get(i));
				contig.add(list.get(sP));
				sP++;
				continue;
			}
			sP++;
		}
		System.out.println(contig);
		return cnt;
	}

	private static int contigEvenNumbers2(SinglyLinkedList<Integer> list) {
		SinglyLinkedList.Node<Integer> curr = list.getHead().getNext();
		SinglyLinkedList.Node<Integer> prev = list.getHead();
		int cnt = 1;
		Set<Integer> contig = new HashSet<>();
		while(curr != null) {
			if(curr.getData() % 2 == 0 && prev.getData() % 2 == 0) {
				cnt++;
				contig.add(prev.getData());
				contig.add(curr.getData());
				prev = curr;
				curr = curr.getNext();
				continue;
			}
			prev = curr;
			curr = curr.getNext();
		}
		System.out.println(contig);
		return cnt;
	};
	
	public static void main(String[] args) {
		int[] intArray = {1, 2, 3, 0, 2, 4, 6, 7};
		System.out.println(contigEvenNumbers0(intArray));

		List<Integer> link = new ArrayList<>(Arrays.asList(1, 2, 3, 0, 2, 4, 6, 7));
		System.out.println(contigEvenNumbers1(link));

		SinglyLinkedList<Integer> list = new SinglyLinkedList<>();
		list.insert(1);
		list.insert(2);
		list.insert(3);
		list.insert(0);
		list.insert(2);
		list.insert(4);
		list.insert(6);
		list.insert(7);

		System.out.println(contigEvenNumbers2(list));
	}
}
