# Ouvrir le fichier et lire toutes les lignes
with open('Polish.txt', 'r') as file:
    lines = file.readlines()

# Parcourir chaque ligne (expression RPN)
for line in lines:
    expression = line.strip()  # Supprimer les espaces inutiles autour de la ligne
    stack = []  # Pile pour les opérandes
    operators = {'+', '-', '*', '/'}  # Ensemble des opérateurs

    # Parcourir chaque élément de l'expression
    for token in expression.split():
        if token in operators:
            # Extraire deux opérandes de la pile
            b = stack.pop()
            a = stack.pop()

            # Effectuer l'opération
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b  # Division

            # Pousser le résultat sur la pile
            stack.append(result)
        else:
            # Si c'est un nombre, on le pousse sur la pile
            stack.append(float(token))

    # Afficher le résultat de l'expression
    print(f"Résultat pour '{expression}': {stack[0]}")

