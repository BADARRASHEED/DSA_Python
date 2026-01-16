"""
balanced_brackets.py

Utility module to check whether a string has balanced brackets.
Supported brackets: (), {}, []
Uses a stack-based approach.

Example:
    is_balanced("{[()]}") -> True
    is_balanced("{{}]")   -> False
"""


def is_balanced(s: str) -> bool:
    """
    Check if the input string has balanced brackets.

    Args:
        s (str): Input string containing brackets

    Returns:
        bool: True if brackets are balanced, False otherwise
    """
    # Mapping: closing bracket -> opening bracket
    pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    opening = set(pairs.values())  # {'(', '{', '['}
    stack = []

    for ch in s:
        # Step 1: push opening brackets
        if ch in opening:
            stack.append(ch)

        # Step 2: handle closing brackets
        elif ch in pairs:
            if not stack:
                return False

            if stack[-1] != pairs[ch]:
                return False

            stack.pop()

        # Step 3: ignore all other characters
        else:
            continue

    # Step 4: stack must be empty at the end
    return len(stack) == 0


# Example usage:
if __name__ == "__main__":
    # Simple test cases
    tests = [
        "()",
        "({[]})",
        "((())",
        "([)]",
        "{{[]}}",
        "{[()]}abc",  # non-bracket chars ignored
    ]

    for t in tests:
        print(f"{t:12} -> {is_balanced(t)}")
