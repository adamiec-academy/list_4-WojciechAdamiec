def is_palindrome(text):
    transformed_text = text.lower()
    transformed_text = ''.join(transformed_text.split())
    return transformed_text == transformed_text[::-1]
