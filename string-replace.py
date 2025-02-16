def reverse_string_segments(s, k):
     
     lst = s[k:]
     fst = s[:k]
     fst = fst[::-1]
     print(fst, lst)
     return fst + lst

    

# Test cases
test_strings = ["abcdefg", "abcd", "a", "abcdefghij", "abcdefghijkl"]
test_k = [2, 4, 1, 3, 5]
expected_outputs = ["bacdfeg", "dcba", "a", "cbadefihgj", "edcbafghijlk"]

# Run each test case
for i, (s, k, expected) in enumerate(zip(test_strings, test_k, expected_outputs)):
    result = reverse_string_segments(s, k)
    if result == expected:
        print(f"Test Case {i+1}: Passed")
    else:
        print(f"Test Case {i+1}: Failed")
        print(f"Expected Output: \"{expected}\"")
        print(f"Actual Output:    \"{result}\"")
    print()