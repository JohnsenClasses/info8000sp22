a_string = "a double quoted string can contain ''"
another_string = 'a single quoted string can contain ""'
an_escaped_string= "a double quoted string can contain \"\", but \\ must be escaped"
a_triple_quoted_string = '''something
something else
something else'''

"""
Anything I type here is ignored
f
a
sdf
as
df
asdf

"""

# print(3)
# print(4)

a_formatted_string = f"a formatted string can contain variables like {a_string}"

print(a_formatted_string)

a_long_number = 3.146

print(f'{a_long_number:.400f}')

a_string = "abc"
b_string = "b"
ab_string = f"{a_string}{b_string}"
print(ab_string)


a_raw_string = r"a raw string can contain \ characters"
print(a_raw_string)

a_raw_formatted_string = rf"a raw formatted string can still contain other things {a_string}"
print(a_raw_formatted_string)

a_concatentation = "The approximation of pi is: " + str(a_long_number)
print(a_concatentation)

a_capitalized_string = "ABC"
a_lowercase_string = a_capitalized_string.lower()
print(a_lowercase_string)

a_string_with_padding = "     3     4    \n"
a_string = a_string_with_padding.strip()

a_string_as_a_list = list(a_string)
print(a_string_as_a_list)
a_list_as_a_string = "".join(a_string_as_a_list)
print(a_list_as_a_string)
a_string = "hello world"
a_substring = a_string[:3]
print(a_substring)

print(len(a_substring))

for i in range(0,len(a_substring)):
    print(a_substring[i])

for c in a_substring:
    print(c)
correct_number = 7
correct = False
while not correct:
    user_input = int(input("Guess a number: "))
    correct = user_input == correct_number
    print(correct)
    
print("good job")
