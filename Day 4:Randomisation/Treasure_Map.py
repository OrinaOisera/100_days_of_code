#creates emojis with unicode
row1 = ["\U0001F600", "\U0001F600", "\U0001F600"]
row2 = ["\U0001F600", "\U0001F600", "\U0001F600"]
row3 = ["\U0001F600", "\U0001F600", "\U0001F600"]


map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put The treasure:")


horizontal = int(position[0])
vertical = int(position[1])


selected_row = map[vertical - 1]
selected_row[horizontal -1 ] = "X"


print(f"{row1}\n{row2}\n{row3}")
