// Given a string in the form of a Linked List, check whether the string is palindrome or not.

import java.util.LinkedList;
import java.util.List;

class LinkedListPalindrome {

	private static int isListPalindrome(String S) {

		if (S.length() == 0) return 0;
		List<Character> str = listify(removePunc(S.toLowerCase()));
		int isPalindrome = 0;
		int j = str.size() - 1;

		for (int i = 0; i < str.size(); i++) {
			if (str.get(i) == str.get(j)) {
				j--;
				isPalindrome = 1;
			} else {
				isPalindrome = 0;
				break;
			}
		}

		return isPalindrome;
	}

	private static int isStrPalindrome(String S) {

		String str = removePunc(S.toLowerCase());
		int j = str.length() - 1;

		int isPalindrome = 0;

		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == str.charAt(j)) {
				j--;
				isPalindrome = 1;
			} else {
				isPalindrome = 0;
				break;
			}
		}

		return isPalindrome;
	}

	private static List<Character> listify(String S) {

		List<Character> l = new LinkedList<>();
		for (int i = 0; i < S.length(); i++) {
			l.add(S.charAt(i));
		}

		return l;
	}

	private static String removePunc(String S) {
		
		return S.replaceAll("\\p{Punct}", "").replaceAll("\\s", "");
	}

	public static void main(String args[]) {

		assert isListPalindrome("Anna") == 1 : "test 1";
		assert isListPalindrome("test") == 0 : "test 2";
		assert isListPalindrome("Madam, I'm Adam") == 1 : "test 3";
		assert isListPalindrome("a") == 1 : "test 4";
		assert isListPalindrome("ad") == 0 : "test 5";

		assert isStrPalindrome("Anna") == 1 : "test 6";
		assert isStrPalindrome("test") == 0 : "test 7";
		assert isStrPalindrome("Madam, I'm Adam") == 1 : "test 8";
		assert isStrPalindrome("a") == 1 : "test 9";
		assert isStrPalindrome("ad") == 0 : "test 10";
	}
}