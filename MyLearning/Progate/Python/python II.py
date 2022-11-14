# block comment CTRL + /

# Python II
# In this lesson, we'll learn how to manage a group of data and work with loops.
# We'll also improve the shopping app using this knowledge.
# It's not as difficult as it sounds. Enjoy!

# Structuring Data
# Let's learn how to manage a group of data with a single variable. 
# When there's a list of food names, for example, it isn't so efficient to manage them with separate variables, like food1, food2, food3. 
# It's better to have a foods variable to manage the whole list.

# ---------------------------------------------------------------
# ---------------------------------------------------------------

# Lists
# The list data type allows you to manage a group of data all at once. You can create a list as follows: [element1, element2, ...]. 
# Each value in the list is called an element. Using lists, you can manage multiple strings and integers as one group.

# Assigning Lists to Variables
# Just like integers and strings, you can assign a list to a variable. As a convention, the variable name is pluralized, like foods, as it will contain multiple elements.

# Getting an Element of a List
# Each element of a list has a number allocated like 0, 1, 2, .... These are called index numbers. 
# Keep in mind that index numbers start from 0. You can get individual elements by writing list[index].

# Assign a list of strings to the fruits variable
fruits = ['apple', 'banana', 'orange']

# Print the element at index 0 
print(fruits[0])

# Concatenate the string and the element at index 2, and print the result
print('I like ' + fruits[2] + 's')

# ---------------------------------------------------------------
# ---------------------------------------------------------------

# Updating an Element of a List
# Let's also try updating an element of a list! This can be done by writing list[index] = value.

# Adding Elements to a List
# You can also add new elements to a list. Writing list.append(value) allows you to add a new element to the end of a defined list.

fruits = ['apple', 'banana', 'orange']

# Add 'grape' to 'fruits'
fruits.append('grape')

# Print 'fruits'
print(fruits)

# Update the element at index 0
fruits[0] = 'cherry'

# Print the element at index 0
print(fruits)

# ---------------------------------------------------------------
# ---------------------------------------------------------------

# Printing All the Elements
# When you want to print all the elements of a list, it isn't efficient to repeat the same code like the example on the left. You can use a for loop to make it easier.

# for Loops
# The for loop allows you to process each element of a list with a temporary variable, and apply the same code to it. 
# In the example below, each element of the foods variable is stored in a temporary variable called food, and printed.

# The Flow of for Loops
# Elements of the list will be assigned to the temporary variable one by one, and the code within the for loop gets executed with each assignment. 
# This is called iteration. 
# It's common to use the the list name's singular form for the temporary variable, but it can be anything.

fruits = ['apple', 'banana', 'orange']

# Get the elements of fruits using a for loop, and print 'I like ____s'
for fruit in fruits :
  print('I like '+fruit+'s')

# ---------------------------------------------------------------
# ---------------------------------------------------------------

Dictionaries

Like lists, dictionaries are used to manage groups of data. The difference is that dictionaries use keys instead of index numbers (index). 
In dictionaries, a key is paired with a value, also known as a key-value pair, to form one element.

How to Create Dictionaries
You can create a dictionary as follows: {key1: value1, key2: value2, ..}. In most cases, we use strings as keys. 
Dictionaries are enclosed with { } while lists are enclosed with [ ]. Be sure to put : between the key value pair, and , between elements.

The Order of Elements in Dictionaries
When you print a dictionary like in the example below, the printed order of the elements can be different from the order you defined them. 
This is because unlike lists, dictionaries don't have a fixed order prior to Python 3.7.

Getting an Element of a Dictionary
You can get a value from a dictionary using the key, by writing dictionary_name[key].