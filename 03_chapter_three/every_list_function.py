#This is Netflix's current Top Ten movies in the UK
netflix = ['carry-on', 'the grinch animated', '65', 'that christmas', 'the grinch original', 'batman', 'nativity', 'alice, darling', 'terminator dark fate', 'operation mincemeat']
print(netflix)

#Proving that it is ten movies
print(len(netflix))

#Correcting 65 so it's char like the rest
netflix[2] = 'sixty-five'
print(netflix)

#Reversing the list
netflix.reverse()
print(netflix)

#Temporarily putting it in alphabetical order
print(sorted(netflix))

#Proving it's only temporary
print(netflix)

#Putting it in alphabetical permanently
netflix.sort()
print(netflix)

#Putting that last in permanent alphabetical reverse
netflix.sort(reverse=True)
print(netflix)

#Using individual elements
print(f"I have seen {netflix[0].title()} but I haven't seen {netflix[1].title()}")
print("We don't need both. Goodbye, animated version!")
del netflix[1]
print(netflix)
print("I'll add in my favourite Christmas film to replace it")
netflix.append('the muppet christmas carol')
print(netflix[9].title())

print("Some people call this a Christmas film")
netflix.insert(6,'die hard')
print(netflix[6].title())

print("Need a recommendation?")
popped_movie = netflix.pop(7)
print(f"Netflix says {popped_movie.title()}")
