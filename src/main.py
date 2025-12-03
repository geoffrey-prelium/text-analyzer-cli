# TODO: Ajouter plus de couleurs dans le terminal

import sys
from analyzer import read_file, count_elements # <--- Ajout de l'import

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <chemin_du_fichier>")
        return

    file_path = sys.argv[1]
    content = read_file(file_path)
    
    if content:
        # Analyse
        stats = count_elements(content) # <--- Appel de la fonction
        
        # Affichage
        print(f"--- Analyse de {file_path} ---")
        print(f"Nombre de caractères : {stats['chars']}")
        print(f"Nombre de mots       : {stats['words']}")

if __name__ == "__main__":
    main()