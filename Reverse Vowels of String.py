class Zoho:
    def reverse_vowels(self, s):
        """
        Reverses the vowels in a given string.

        Args:
            s: The input string.

        Returns:
            The string with vowels reversed.
        """
        arr = []
        if "A" in s or "E" in s or "I" in s or "O" in s or "U" in s or "a" in s or "e" in s or "i" in s or "o" in s or "u" in s:
            arr.append(s)
            return arr
        

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
