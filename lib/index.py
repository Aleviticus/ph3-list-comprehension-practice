# 1. Use list comprehension to return a list of capitalized strings

# for example ["Banana", "Apple", "Orange",...]

def capital_fruit():

    fruit = ["banana", "apple", "orange", "kiwi", "kumquat"]

    return [item.capitalize() for item in fruit] # <<--- write your list comprehension here



# 2. Use list comprehension to return a list of reversed strings

# for example ["ananab","elppa","egnaro",...]

def reversed_fruit():

    fruit = ["banana", "apple", "orange", "kiwi", "squash"]

    return[item[::-1] for item in fruit ]





# 3. Use list comprehension to return a list of strings without whitespace

# for example ["banana","apple","orange",...]

def unspaced_fruit():

    fruit = ["    banana", "apple     ", "ora  nge", " k i w i ", "star fruit"]

    return [item.replace(" ", "") for item in fruit]



# 4. Use list comprehension to return a list of strings that have been upcased and reversed

# for example ["ANANAB","ELPPA","EGNARO",...]

def upversed_fruit():

    fruit = ["banana", "apple", "orange", "kiwi", "peach"]

    return [item[::-1].upper() for item in fruit]



# 5. Use list comprehension to return the inauguration date of each president

# for example [1789, 1797, 1801, ...]

def inauguration_dates():

    us_presidents = [
        { "name": "George Washington", "inauguration": 1789 },
        { "name": "John Adams", "inauguration": 1797 },
        { "name": "Thomas Jefferson", "inauguration": 1801 },
        { "name": "James Madison", "inauguration": 1809 },
        { "name": "James Monroe", "inauguration": 1817 },
    ]

    return [item["inauguration"] for item in us_presidents]



# 6. Use list comprehension to return a new list of concatenated tuples

# for example ["Chett Tiller", "Ricardo Guerra", "Charlie Kozey",...]

def say_names():

    some_people = [
        ("Chett", "Tiller"),
        ("Ricardo", "Guerra"),
        ("Charlie", "Kozie"),
        ("Alina", "Pisarenko"),
        ("Aakash", "Sudhakar"),
        ("Sakib", "Rasul"),
        ("Daniel", "Gaston"),
        ("Ben", "Cavins"),
        ("Mohammad", "Hossain"),
        ("Chelsea", "Green")
    ]

    return [item[0] + " " + item[1] for item in some_people]



# 7. Use list comprehension to return a new list of only dogs

# for example ["dog", "dog", "dog",...]

def get_dogs():

    pets = ["dog", "cat", "dog", "dog", "cat", "dog", "cat", "dog"]

    return [ pet for pet in pets if pet == "dog"]



# 8. Use list comprehension to return a new list of only even numbers

# for example [8, 16, 20,...]

def get_evens():

    numbers = [1, 8, 9, 99, 16, 20, 21]

    return [number for number in numbers if number % 2 == 0 ]



# 9. Use list comprehension to return a new list of each number in a range squared

# for example [1,4,9,...]

def squared_numbers():

    numbers = range(1,10)

    return [number**2 for number in numbers]



# 10. Use list comprehension to return a new list of the average of each sub-list

# for example [15,35,0,...]

def summed_lists():

    number_lists = [
        [1,2,3,4,5],
        [9,8,7,6,5],
        [-100,100],
        [21,7,3,4,1,6]
    ]

    return [sum(num_range_list) for num_range_list in number_lists ]