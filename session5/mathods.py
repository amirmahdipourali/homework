#finds the match of your word things before the match and things after the match
text = "I Could Eat Bananas All Day"
r = text.partition("Bananas")
print(r)
# make the lower case letters upper case and the upper case letters lower case
new_text=text.swapcase()
print(new_text)
# Returns true if the string ends with the specified value
x = text.endswith("y")
print(x)