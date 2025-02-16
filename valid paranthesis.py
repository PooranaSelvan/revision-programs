class Zoho:
    def is_valid(self, s):
        """
        Checks if the given string is a valid parentheses string.

        Args:
            s: The input string.

        Returns:
            True if the string is valid, False otherwise.
        """
        lst = []
        for i in s:
             if i == "(":
                  lst.append(i)
             elif i == ")":
                  lst.pop()
          
        if len(lst) == 0:
             return True
        else:
             return False
        

# Test cases
test_cases = ["()", "()[]{}", "(]", "[()]", "{[]}"]
expected_results = [True, True, False, False, True]

# Create an instance of the Zoho class
zoho = Zoho()

# Run each test case
for i, (s, expected) in enumerate(zip(test_cases, expected_results)):
    result = zoho.is_valid(s)
    if result == expected:
        print(f"Test case {i+1} passed.")
    else:
        print(f"Test case {i+1} failed.")
