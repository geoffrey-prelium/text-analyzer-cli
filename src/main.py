import sys
from analyzer import read_file

def main():
    # sys.argv est la liste des arguments. 
    # [0] est le nom du script, [1] est le premier argument donné.
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <chemin_du_fichier>")
        return

    # On récupère le chemin donné par l'utilisateur
    file_path = sys.argv[1]
    
    # On appelle la fonction du moteur
    content = read_file(file_path)
    
    if content:
        print(f"--- Lecture de {file_path} ---")
        print(content)

if __name__ == "__main__":
    main()