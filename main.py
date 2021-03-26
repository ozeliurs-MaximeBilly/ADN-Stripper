with open("test.mp4", 'rb') as file:  # Lit le fichier
    contents = file.read()

contents = contents.split(b'Rdata')  # Identifie Rdata et coupe le fichier en deux à cet endroit

contents[1] = b'\x00' * len(contents[1])  # Remplace la deuxième partie du fichier (apres Rdata) par des bytes "vides"

contents = b'Rdata'.join(contents)  # Reconstruit le fichier

with open("out.mp4", 'wb') as file:  # Ecrit le fichier
    file.write(contents)
