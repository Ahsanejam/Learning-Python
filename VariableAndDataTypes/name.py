# Strings
 
# name = "ada lovelace"
# print(name.title())

# Output -> Ada Lovelace

# name = "Ada Lovelace"
# print(name.upper())
# print(name.lower())

# Output----
# ADA LOVELACE
# ada lovelace


# Using Variable in Strings
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name)


# Output -> ada lovelace

# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name.title())

# Output -> Ada Lovelace


# Adding Whitespace to Strings with Tabs or Newlines

# print("Python")
# print("\tPython")

# Output 

# Python
#         Python

# print("Languages:\nPython\nC\nJavaScript")
# Output
# Languages:
# Python
# C
# JavaScript


# print("Languages:\n\tPython\n\tC\n\tJavaScript")
#Output
# Languages:
#         Python
#         C
#         JavaScript


# Stripping Whitespaces
# favorite_language = 'python '
# print(favorite_language)
# print(favorite_language.rstrip())



# favorite_language = 'python '
# favorite_language = favorite_language.rstrip()
# print(favorite_language)

# favorite_language = ' python '
# print(favorite_language.rstrip())
# print(favorite_language.lstrip())
# print(favorite_language.strip())


# Avoiding Syntax Errors with Strings
# message = "One of Pyton's strenghts is its diverse community."
# print(message)


# Exersice 1.3
person_name = "Ahsan"
print(f"Hello {person_name}, would you like to learn some Python todqy?")

# Exersice 1.4
person_name = "Asad"
print(person_name.lower())
print(person_name.upper())
print(person_name.title())

# Exersice 1.5
famous_person = "Albert Einstein"
Quote = "A person who never made a mistake never tried anyting new."
print(f"{famous_person} once said, {Quote}")

# Exersice 1.6
person_name = '\t\n Ahsans \n\t'
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())