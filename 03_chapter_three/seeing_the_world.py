places = ['california', 'iceland', 'japan', 'new zealand', 'new jersey']
print("This is the original order:")
print(places)

print("This is alphabetical order:")
print(sorted(places))

print("That wasn't permanant:")
print(places)

print("But this is:")
places.reverse()
print(places)

print("Just kidding!")
places.reverse()
print(places)

print("You can put it in alphabetical order permanantly")
places.sort()
print(places)

print("I didn't say which way!")
places.sort(reverse=True)
print(places)

print("And that's how you change the order of lists!")