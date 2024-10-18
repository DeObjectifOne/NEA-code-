# Function to add notes to "note.txt"
def add_note(note, filename="note.txt"):  # Fixed filename
    with open(filename, 'a') as file:
        file.write(note + '\n')

# Adding notes to the file
add_note("Meet with the client")
add_note("Talk about the initial plan")
add_note("Give them project proposal")
add_note("Clean up the board room when done")
add_note("Call the supplier before leaving")

# Function to search notes in "note.txt"
def search_notes(keyword, filename="note.txt"):
    with open(filename, 'r') as file:
        notes = file.readlines()  # All file lines go into a list
        # Case-insensitive search for keyword
        results = [note.strip() for note in notes if keyword.lower() in note.lower()]
        return results

# Search for the keyword "client" in the notes
search_results = search_notes("give")
print("Search Results:", search_results)
