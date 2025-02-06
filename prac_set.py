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
print()
#union
joined_colors = colors.union(other_colors)
print(f"Joined colors set = {joined_colors}")
print()
#intersection
duplicates = colors.intersection(other_colors)
print(f"Duplicates = {duplicates}")
#intersection update
colors.intersection_update(other_colors)
print(f"Duplicates = {colors}")
print()
#difference 
#return items in the 1st set that are not in 2nd set
colors = {"yellow", "beige", "red", "blue", "khakhi", "orange"}
color_dif = colors.difference(joined_colors)
print(f"Here is the set difference: {color_dif}") #get back to fixing this
print()
#difference update
colors.difference_update(joined_colors)
print(f"updated color = {colors}")
print()
#symmetric difference
set2 = colors.symmetric_difference(joined_colors)
print(set2)
#symmetric difference update
colors.symmetric_difference_update(joined_colors)
print(colors)