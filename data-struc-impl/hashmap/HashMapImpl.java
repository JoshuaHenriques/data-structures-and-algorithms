import java.util.AbstractMap.SimpleEntry;
import java.util.*;


class Bucket<K, V> {
	private List<SimpleEntry<K, V>> entries;

	public Bucket() {
		this.entries = new LinkedList<>();
	}

	public List<SimpleEntry<K, V>> getEntries() {
		return this.entries;
	}

	public void addEntry(SimpleEntry<K, V> entry) {
		this.entries.add(entry);
	}

	public void removeEntry(SimpleEntry<K, V> entry) {
		this.entries.remove(entry);
	}
}

public class HashMapImpl<K, V> {
	private int capacity;
	private int size;
	private Bucket<K, V>[] bucket;

	public HashMapImpl() {
		this.capacity = 8;
		this.bucket = new Bucket[this.capacity];
	}

	public HashMapImpl(int capacity) {
		this.capacity = capacity;
		this.bucket = new Bucket[this.capacity];
	}

	private int getHash(K key) {
		return key.hashCode() % this.capacity;
	}

	private SimpleEntry<K, V> getEntry(K key) {
		int hash = getHash(key);
		for (int i = 0; i < this.bucket[hash].getEntries().size(); i++) {
			SimpleEntry<K, V> entry = this.bucket[hash].getEntries().get(i); 
			if (entry.getKey().equals(key)) {
				return entry; 
			}
		}
		return null;
	}

	public void put(K key, V value) {
		if(containsKey(key)) {
			SimpleEntry<K, V> entry = getEntry(key);
			entry.setValue(value);
		}
		else {
			int hash = getHash(key);
			if(this.bucket[hash] == null) {
				this.bucket[hash] = new Bucket<>();
			}
			this.bucket[hash].addEntry(new SimpleEntry<>(key, value));
			this.size++;
		}
	}

	public V getValue(K key) {
		return containsKey(key) ? (V) getEntry(key).getValue() : null;
	}

	public boolean containsKey(K key) {
		int hash = getHash(key);
		return !(Objects.isNull(bucket[hash]) || Objects.isNull(getEntry(key)));
	
	}

	public void delete(K key) {
		if(containsKey(key)) {
			int hash = getHash(key);
			this.bucket[hash].removeEntry(getEntry(key));
			this.size--;
		}
	}

	public int size() {
		return this.size;
	}

	// Driver code
	public static void main(String[] args) {
		HashMapImpl<String, String> map0 = new HashMapImpl<>(8);
		HashMapImpl<String, String> map1 = new HashMapImpl<>();
		System.out.println(map0.size());
		System.out.println(map0.containsKey("A"));
		System.out.println("B".hashCode() % map0.capacity);
		map0.put("A", "Albert");
		System.out.println(map0.containsKey("A"));
		map0.put("B", "Blunder");
		System.out.println(map0.size());
	 	map0.delete("B");
		System.out.println(map0.size());
		System.out.println(map0.containsKey("B"));
	}
}