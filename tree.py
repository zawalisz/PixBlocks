height = int(input("Write the number of parts of the tree: "))
if height <= 0:
    print("Try again and write the number greater than 0.")
else:
    for i in range(height):
        space = height
        stars = 1
        for j in range(i + 2):
            print(' ' * space + '*' * stars)
            stars += 2
            space -= 1