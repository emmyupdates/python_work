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
print("Good news! Melanie Lynskey will now be joining us")