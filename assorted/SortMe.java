import java.util.Collections;
import java.util.ArrayList;
import java.util.Arrays;
 
class SortMe {
	public static void main(String[] args) {
		ArrayList<Integer> list = new ArrayList<>();
		list.add(34);
		list.add(328);
		list.add(22);
		list.add(95);
 
		System.out.println(list.toString());
		Collections.sort(list);
		System.out.println(list);
 
		int arrr[] = {348, 33, 23, 13};
 
		for(int num: arrr) {
			System.out.print(num + " ");
		}
		System.out.println();
		Arrays.sort(arrr);
		for(int num: arrr) {
			System.out.print(num + " ");
		}
	}
}