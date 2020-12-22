# use predefined string constants
import string


# TODO: predefined string constants can be used in common scenarios
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)

# TODO: Use the constants to filter information out
test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of December"
test_string2 = "Supercalifragilistic"
test_string3 = "90210"

# TODO: String testing methods
print("".join([x for x in test_string1 if x in string.ascii_letters]))
print(test_string1.isalnum())