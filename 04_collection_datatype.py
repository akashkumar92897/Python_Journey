#📦 Collection Data-Types in Python (List | Tuple | Set | Dictionary
#----------------------------------------------------------------
# List  |           |  Mutable   |  Ordered   |  Collection| ⭐ 90%+
# Tuple |           |  Immutable |  Ordered   |  Collection|
# Set   |  Unique   |  Mutable   |  Unordered |  Collection|
# Dict  |  Mapped   |  Mutable   |  Ordered*  |  Collection|
# ----------------------------------------------------------------


# LIST (MUTABLE, ORDERED, COLLECTION) - Used in 90% CASES ⭐!
# ----------------------------------------------------------------
#📃 SYNTAX
empty_list = []
my_list = ['Wall', 'Floor', 'Roof', 'Ceiling', 'Wall', 'Floor', 'Roof', 'Ceiling']

#👉 GET SINGLE LIST ITEM
print (my_list)
print (my_list[0])      # First Item (Count starts from 0)
print (my_list[2])      # Third Item (Count starts from 0
print (my_list[-1])     # Last Item
print (my_list[-2])     # Second Last Item
# print (my_list[100])    # IndexError: List Index out of Range

#✂️ GET MULTIPLE ITEMS (SLICE)
print (my_list[:2])     # Get Until 2nd Item (Excluding 2)
print (my_list[2:])     # Get From 2nd Item (Including 2)
print (my_list[1:3])    # Get From 1st Item (Including) Until 3rd Item (Excluding)
print (my_list[::2])    # Get Every Second Item
print (my_list[0:6:2])  # Get Every 2nd Item from 0th Item (Including) Until 6th Item (Excluding)
print (my_list[::-1])   # Trick to Reverse List

#✨ REPLACE ITEMS IN A LIST
Groceries = ['Rice', 'Milk', 'Egg', 'Chicken']
Groceries[2] = 'NewItem'            # Replace Item from Index 2
Groceries[-1] = 'LastItem'          # Replace Item from Last Index
Groceries[1:3] = ['a', 'b']         # Replace Items from Indices
print (Groceries)

#🪚 SLICING USE-CASE EXAMPLE
my_list2 = ['Categories', 'Wall', 'Floor', 'Roof', 'Ceiling']
header = my_list2[0]
data = my_list2[1:]
print (header)
print (data)

#🔎 MEMBERSHIP OPERATORS (NECESSARY FOR LOGIC)
print ('Wall' in my_list2)
print ('wall' in my_list2)
print ('Door' not in my_list2)

#⚙️ POPULAR FUNCTIONS WITH LIST
numbers = [50, 60, 80, 10, 30, 40]
print (len(numbers))        # Get Length
print (sorted(numbers))     # Create new sorted List
print (sum(numbers))        # Sum Numbers
print (min(numbers))        # Get Min Value
print (max(numbers))        # Get Max Value


my_list3 = ['Wall', 'Floor', 'Roof', 'Ceiling']
my_list4 = ['Door', 'Window']

my_list3.append('Door')     # Add Single Item
my_list3.extend(my_list4)   # Join 2 Lists
my_list3 += my_list4        # Join 2 Lists
my_list3.sort()             # Short List Alphanumerically

print (my_list3)

print (my_list3.count('Door'))    # Count Value inside List
print (my_list3.index('Floor'))   # Find Index inside List
my_list3.insert(2, 'Table')       # Insert Item at certain Index
my_list3.remove('Window')         # Remove Item from the list (if possible)
my_list3.remove('Window')         # Remove Item from the list (if possible)
# item = my_list3.pop()           # Remove and Return the Item from last
item = my_list3.pop(3)            # Remove and Return the Item 3rd idx
my_list3.reverse()                # Reverse List Order
my_list3.clear()                  # Clear All List Items
my_list3 = []                     # Easier Way to Clear All List Items

print (my_list3)
print (item)

x = my_list3                      # Reference to the Same List
y = my_list3.copy()               # Create Independent Copy Of List

my_list3.append('NewItem')
print(x)
print(y)

#📂 NESTED LISTS
points = [
    [0, 0, 0],
    [2, 2, 0],
    [4, 4, 0],
    [6, 6, 0],
]

pt2 = points [1]
print (points)                  # Print The Whole Nested List
print(pt2[0], pt2[1], pt2[2])   # Prints Items at Each Index of 1st Index List
print (points[1][1])            # Prints 1st Idx Item from 1st Idx List

#➿ LOOPS (MORE IN ANOTHER LESSON!)
Groceries = ['Rice', 'Milk', 'Egg', 'Chicken']

for i in Groceries:
    print(i)
    print(i)
    print(i)









# TUPLES (IMMUTABLE, ORDERED, COLLECTION)
# ----------------------------------------------------------------