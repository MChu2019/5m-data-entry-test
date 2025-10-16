def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s[::-1]   # slicing to reverse the string


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
print(string_reverse("Hello World"))   # Expected: "dlroW olleH"
print(string_reverse("Python"))        # Expected: "nohtyP"
