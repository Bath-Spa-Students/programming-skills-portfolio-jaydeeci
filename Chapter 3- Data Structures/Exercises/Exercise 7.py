# Create a list of places to visit, not in alphabetical order
places_to_visit = ["Tokyo", "Korea", "Greece", "Australia", "Philippines"]

# Print the list in its original order
print("Original Order:", places_to_visit)

# Use sorted() to print the list in alphabetical order without modifying the actual list
print("Alphabetical Order:", sorted(places_to_visit))

# Show that the original list is still in its original order
print("Original Order:", places_to_visit)

# Use sorted() to print the list in reverse alphabetical order without changing the original list
print("Reverse Alphabetical Order:", sorted(places_to_visit, reverse=True))

# Show that the original list is still in its original order
print("Original Order:", places_to_visit)

# Use reverse() to change the order of the list
places_to_visit.reverse()
print("Reversed Order:", places_to_visit)

# Use reverse() again to change the order back to the original
places_to_visit.reverse()
print("Original Order:", places_to_visit)

# Use sort() to change the list to alphabetical order
places_to_visit.sort()
print("Alphabetical Order:", places_to_visit)

# Use sort() to change the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("Reverse Alphabetical Order:", places_to_visit)