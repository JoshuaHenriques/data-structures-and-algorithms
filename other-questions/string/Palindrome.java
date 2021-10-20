// Given a string S, check if it is palindrome or not.

import java.io.*;

class GFG {
	public static void main(String args[]) throws IOException {
		BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(read.readLine());
		while (t-- > 0) {
			String S = read.readLine();

			Solution ob = new Solution();
			System.out.println(ob.isPalindrome(S));
		}
	}
}

// User function Template for Java

class Solution {
	int isPalindrome(String S) {
		if (S.length() == 0)
			return 0;
		if (S.length() == 1)
			return 1;

		int j = S.length() - 1;
		int isPalindrome = 0;

		for (int i = 0; i < S.length(); i++) {
			if (S.charAt(i) == S.charAt(j--))
				isPalindrome = 1;
			else
				return 0;
		}

		return isPalindrome;
	}
};