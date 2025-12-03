def read_file(path):
    """
    Lit un fichier texte et retourne son contenu.
    Retourne None si le fichier n'existe pas.
    """
    try:
        # 'with' assure que le fichier est fermé proprement après lecture
        # 'r' = mode lecture (read)
        # 'utf-8' = encodage standard pour gérer les accents
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erreur critique : Le fichier '{path}' n'a pas été trouvé.")
        return None
    
def count_elements(text):
    """
    Retourne un dictionnaire avec le nombre de mots et de caractères.
    """
    if text is None:
        return {"words": 0, "chars": 0}
        
    words = text.split() # Découpe le texte par espace
    return {
        "words": len(words),
        "chars": len(text)
    }