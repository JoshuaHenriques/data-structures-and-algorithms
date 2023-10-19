import java.lang.reflect.Array;

class ArrayListImpl<T> {

	private int size;
	Class<T> clazz;
	private int index;
	private T[] array;

	public ArrayListImpl(Class<T> c) {
		this.size = 16;
		this.clazz = c;
		@SuppressWarnings("unchecked")
		T[] arr = (T[]) Array.newInstance(this.clazz, this.size);
		this.array = arr;
		this.index = 0;
	}

	public ArrayListImpl(Class<T> c, int size) {
		this.size = size;
		this.clazz = c;
		@SuppressWarnings("unchecked")
		T[] arr = (T[]) Array.newInstance(this.clazz, this.size);
		this.array = arr;
		this.index = 0;
	}

	private void incrSize() {
		this.size *= 2;
		@SuppressWarnings("unchecked")
		T[] arr = (T[]) Array.newInstance(this.clazz, this.size);
		T[] biggerArray = arr;

		for(int i = 0; i < this.size; i++) {
			biggerArray[i] = this.array[i];
		}

		this.array = biggerArray;
	}

	public void insert(T data) {
		if(index == size - 1) 
			incrSize();

		this.array[index] = data;
		index++;		
	}

	public void delete(T data) {
		for(int i = 0; i < this.size; i++) {
			if(this.array[i] == data) {
				this.array[i] = this.array[i+1];
				break;
			}
		}
		this.index--;
	}

	public T get(T data) {
		for(int i = 0; i < this.size; i++) {
			if(this.array[i] == data) return this.array[i];
		}
		return null;
	}

	public int search(T data) {
		for(int i = 0; i < this.size; i++) {
			if(this.array[i] == data) return i;
		}
		return -1;
	}

	public int size() {
		return this.index;
	}
	
	public boolean isEmpty() {
		return this.index == 0;
	}

	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("[");
		for(int i = 0; i < this.size; i++) {
			sb.append(this.array[i] + ", ");
		}
		sb.append("]");
		return sb.toString();
	}

	public static void main(String[] args) {
		ArrayListImpl<Integer> array = new ArrayListImpl<>(Integer.class);

		array.insert(25);
		array.insert(35);
		array.insert(45);
		array.insert(55);
		System.out.println(array.toString());
		System.out.println(array.size());
		array.delete(55);
		System.out.println(array.toString());
		System.out.println(array.size());	
		System.out.println(array.get(45));
		System.out.println(array.search(45));
		System.out.println(array.isEmpty());
	}
}


