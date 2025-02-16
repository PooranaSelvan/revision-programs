class Zoho:
    def reverse_vowels(self, s):
        """
        Reverses the vowels in a given string.

        Args:
            s: The input string.

        Returns:
            The string with vowels reversed.
        """
        vowels = "aeiouAEIOU"
        
        s = list(s)
        
        vowel_list = []
        
        for j in s:
            if j in vowels:
                vowel_list.append(j)
        
        vowel_list.reverse()

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowel_list.pop(0)
        
        return ''.join(s)
        
        

# Test cases
test_strings = ["IceCreAm", "leetcode", "ReverseVowels", "xyz", "aA"]
expected_outputs = ["AceCreIm", "leotcede", "RevorseVewels", "xyz", "Aa"]

# Create an instance of the Zoho class
zoho = Zoho()

# Run each test case
for i, (s, expected) in enumerate(zip(test_strings, expected_outputs)):
    result = zoho.reverse_vowels(s)
    if result == expected:
        print(f"Test Case {i+1}: Passed")
    else:
        print(f"Test Case {i+1}: Failed")
        print(f"Expected Output: \"{expected}\"")
        print(f"Actual Output:    \"{result}\"")
    print()
