guest_list = ['bart nickerson', 'ashley lyle', 'jonathan lisco']
print(guest_list)

bart = guest_list.pop(0)
jonathan = guest_list.pop(1)
ashley = guest_list.pop()

print(f"This is a guest panel announcement for Manchester Comic Con 2025!")
print(f"{bart.title()} will tell us what to expect in Yellowjackets Season 4,")
print(f"You can ask {ashley.title()} about the Season 3 finale")
print(f"And {jonathan.title()} will explain why Shauna did that one thing!")
print(f"Due to schedule clashes, {jonathan.title()} will no longer be on the panel.")

guest_list = ['bart nickerson', 'ashley lyle', 'jonathan lisco']
guest_list[2] = 'melanie lynskey'
print(guest_list)
print("The wonderful Melanie Lynskey has now joined the panel")
print("Good news! Due to popularity, we have invited even more panelists to speak")

guest_list.insert(0, 'sophie nelisse')
guest_list.insert(2, 'christina ricci')
guest_list.insert(5, 'sammi hanratty')
print(guest_list)
print("We would like to announce that Christina Ricci, Sophie Nelisse and Sammi Hanratty will now be joining us!")

print(f"{guest_list.pop(0).title()} will no longer be speaking")
print(f"{guest_list.pop(4).title()} will no longer be speaking")
print(f"{guest_list.pop().title()} will no longer be speaking")
print(f"{guest_list.pop().title()} will no longer be speaking")

print(guest_list)
print(f"We are happy to say that {guest_list[0].title()} and {guest_list[1].title()} will still be speaking")
