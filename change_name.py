import os

# Ścieżka do folderu z plikami
folder_path = 'tmp\labels'

# Iteracja po plikach w folderze
for file_name in os.listdir(folder_path):
    # Sprawdź, czy plik ma rozszerzenie .txt
    if file_name.endswith('.txt'):
        # Usuń '_mask' z nazwy pliku
        new_name = file_name.replace('_mask', '')
        # Stwórz pełne ścieżki
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        # Zmień nazwę pliku
        os.rename(old_path, new_path)
        print(f"Zmieniono nazwę: {file_name} -> {new_name}")

print("Zakończono zmianę nazw plików.")
