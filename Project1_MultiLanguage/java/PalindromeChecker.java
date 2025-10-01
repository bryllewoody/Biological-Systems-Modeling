// PalindromeChecker.java
// Program checks if a word or phrase is a palindrome.

import java.util.Scanner;  // Import Scanner class for user input
public class PalindromeChecker {

    // Check if a string is a palindrome
    public static boolean isPalindrome(String text) {
        // Clean up the input, remove spaces, and convert to lowercase
        text = text.replaceAll("[^a-zA-Z]", "").toLowerCase();

        // Use two pointers, one from the left and one from the right
        int left = 0;
        int right = text.length() - 1;

        // Compare characters moving towards the center
        while (left < right) {
            if (text.charAt(left) != text.charAt(right)) {
                // If mismatch found, it's not a palindrome
                return false;
            }
            left++;
            right--;
        }
        // If loop finishes with no mismatches, it is a palindrome
        return true;
    }
    public static void main(String[] args) {
        // Create an object that scans to read input from user
        Scanner scanner = new Scanner(System.in);

        // Prompt the user
        System.out.print("Enter a word or phrase: ");
        String input = scanner.nextLine();  // Read the entire line as input

        // Call the isPalindrome method and show result
        if (isPalindrome(input)) {
            System.out.println("\"" + input + "\" is a palindrome.");
        } else {
            System.out.println("\"" + input + "\" is NOT a palindrome.");
        }

        // Step 4: Close the scanner to free resources
        scanner.close();
    }
}