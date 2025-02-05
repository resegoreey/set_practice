#Set Creation
colors = {"yellow", "beige", "red", "blue", "khakhi", "orange"}
print(f"Colors = {colors}")
print()

#Adding and removing items in a set
user_add = input("Add another color to the set: ")
colors.add(user_add)
print(f"updated colors = {colors}")
print()
user_remove = input("Remove a color: ")
colors.discard(user_remove)
print(f"updated colors = {colors}")
print()


#set operations

print(f"colors = {colors}")
other_colors = {"black", "white", "red", "white", "pink", "beige"}
print(f"Other colors ={other_colors}")
#union
joined_colors = colors.union(other_colors)
print(f"Joined colors set = {joined_colors}")
print()
#intersection
duplicates = colors.intersection(other_colors)
print(f"Duplicates = {duplicates}")