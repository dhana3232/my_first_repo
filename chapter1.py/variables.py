# x = 5
# y = 10
# z = x + y
# print(z)

# The template of the letter
letter_template = '''
Dear <|NAME|>,

You are selected!

Date: <|DATE|>
'''

# Ask the user for inputs
name = input("Enter the name: ")
date = input("Enter the date: ")

# Replace <|NAME|> and <|DATE|> in the template
filled_letter = letter_template.replace("<|NAME|>", name)
filled_letter = filled_letter.replace("<|DATE|>", date)

# Show the final letter
print("\nHere is your letter:")
print(filled_letter)
