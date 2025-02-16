class Zoho:
    def largest_good_integer(self, num):
        """
        Finds the largest "good" integer within the given string, 
        where a "good" integer is a substring of three consecutive 
        identical digits.

        Args:
            num: The input string.

        Returns:
            The largest "good" integer found, or an empty string 
            if no "good" integer exists.
        """
        s = ""
        for j in range(len(num)):
            for i in num:
                s = i
                j + 1
                if i[j] == s:
                    s += i
                if s[j] == i:
                    s += i
                    continue
                return ""
            return s
        

# Test cases
test_nums = ["6777133339", "2300019", "42352338", "000111222", "999"]
expected_outputs = ["777", "000", "", "222", "999"]

# Create an instance of the Zoho class
zoho = Zoho()

# Run each test case
for i, (num, expected) in enumerate(zip(test_nums, expected_outputs)):
    result = zoho.largest_good_integer(num)
    if result == expected:
        print(f"Test Case {i+1}: Passed")
    else:
        print(f"Test Case {i+1}: Failed")
        print(f"Expected Output: \"{expected}\"")
        print(f"Actual Output:    \"{result}\"")
    print()
