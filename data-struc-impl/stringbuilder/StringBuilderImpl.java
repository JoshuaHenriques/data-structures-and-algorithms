import java.lang.StringBuilder;

class StringBuilderImpl {
	
	private int size;
	private int index;
	private char[] string;

	public StringBuilderImpl() {
		this.index = 0;
		this.size = 16;
		this.string = new char[this.size];
	}

	public StringBuilderImpl(int size) {
		this.index = 0;
		this.size = size;
		this.string = new char[this.size];
	}

	public void insert(char character) {
		if(this.index == this.size - 1) {
			incrSize();
		}
		this.string[index] = character;
		index++;
	}

	private void incrSize() {
		this.size *= 2;
		char[] biggerString = new char[this.size];
		for(int i = 0; i < this.size; i++) {
			biggerString[i] = this.string[i];
		} 
		this.string = biggerString;
	}

	public void delete(char character) {
		for(int i = 0; i < this.size; i++) {
			if(this.string[i] == character) {
				this.string[i] = this.string[i+1];
				break;
			}
		}
		this.index--;
	}

	public char get(char character) {
		for(int i = 0; i < this.size; i++) {
			if(this.string[i] == character) return this.string[i];
		}
		return 0;
	}

	public boolean isEmpty() {
		return this.index == 0;
	}

	public int size() {
		return this.index;
	}

	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("[");
		for(int i = 0; i < this.size; i++) {
			sb.append(this.string[i] + ", ");
		}
		sb.append("]");
		return sb.toString();
	}

	public static void main(String[] args) {
		StringBuilderImpl string = new StringBuilderImpl();

		string.insert('H');
		string.insert('e');
		string.insert('l');
		string.insert('l');
		string.insert('o');
		string.insert('!');
		System.out.println(string.toString());
		System.out.println(string.size());	
		string.delete('o');
		System.out.println(string.toString());
		System.out.println(string.size());	
		System.out.println(string.get('o'));
		System.out.println(string.isEmpty());
	}
}
