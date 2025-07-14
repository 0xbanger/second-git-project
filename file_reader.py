list_from_text = []

with open('pokedex.txt', 'r') as file:
    for line in file:
        clean_line = line.strip()
        list_from_text.append(clean_line)
    
print(list_from_text)

