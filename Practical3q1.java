package Practical3;

import java.util.Scanner; // import java util scanner package.

public class Practical3q1 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		System.out.println("Please enter a string: ");
		String str = input.nextLine();
		// Read a string from the console.
		
		int vowels_count = 0;
		// Count the vowels.
		
		int consonant_count = 0;
		// Count the consonants.
		
		str = str.toLowerCase();
		// Converts to lowercase to ignore the case of the string.
		
		for (int i = 0; i < str.length(); i++) {
		// Loop over each character of the string.
			
			char ch = str.charAt(i);
			// Change letter to character type.
			
			if (ch =='a' || ch =='e' || ch =='i' || ch =='o' || ch =='u') {
				vowels_count ++;
				// if the character is a vowel then consonant_count plus 1.
				
			}else if(ch >= 'a' && ch <= 'z'){
				consonant_count ++;
				// if the character is a consonant then vowels_count plus 1.
			}
//			
		}
		System.out.println("The number of vowels are " + vowels_count);
		System.out.println("The number of consonants are " + consonant_count);
		// Display the result.

	}

}
