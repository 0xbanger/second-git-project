list_from_text = []

with open('pokedex.txt', 'r') as file:
    for line in file:
        clean_line = line.strip()
        list_from_text.append(clean_line)
    
print(list_from_text)

with open('log.txt', 'w') as log_file:
    log_file.write(f"-- LOG START --\nMy current program opens the pokedex.txt file.\nThat file\
contains the text of 6 pokémon.\nIt then adds each pokémon name to an empty list.\nAnd prints that list.\n-- LOG END --\n")
    


