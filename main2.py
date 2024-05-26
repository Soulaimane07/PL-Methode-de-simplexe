def fonction_Objectif():
    num_variables = int(input("Entrer le nombre des variables de la fct objectif: "))

    objective_function = []
    for i in range(num_variables):
        var = float(input(f"Entrer la variable numero {i+1}: "))
        objective_function.append(var)

    sin_objective_function = [-x for x in objective_function]

    print(f"\nLa fonction objectif: {objective_function}")
    print(f"La fonction objectif (-): {sin_objective_function}")

    return (num_variables, sin_objective_function)


def contraints():
    (num_variables, sin_objective_function) = fonction_Objectif()
    num_contraintes = int(input("\nEntrer le nombre des contraintes: "))

    contraintes = []
    contraintes_resultat = []

    for i in range(num_contraintes):
        row = [] 
        for j in range(num_variables):
            value = float(input(f"Enter pour contrainte {i+1}, variable {j+1}: "))
            row.append(value) 
        contraintes.append(row)

    print('')
    for i in range(num_contraintes):
        value = float(input(f"Enter pour contrainte {i+1}, le resultat: "))
        contraintes_resultat.append(value) 


    new_contraintes = []
    new_objectif_function = sin_objective_function

    for i in range(num_contraintes):
        new_objectif_function.append(0)
        row = contraintes[i] 
        for j in range(num_contraintes):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        new_contraintes.append(row)

    print("\nMatrice des contrantes: ")
    for row in new_contraintes:
        print(row)

    print("\nListe des resultats: ")
    print(contraintes_resultat)

    return (new_objectif_function, new_contraintes, contraintes_resultat)




def display_variables(tableau):
    num_variables = len(tableau[0]) - 1  # Nombre de variables dans la fonction objective

    # Trouver les indices des variables de base
    base_indices = [i for i in range(num_variables) if sum(row[i] for row in tableau[1:]) == 1]

    # Trouver les indices des variables hors base
    non_base_indices = [i for i in range(num_variables) if i not in base_indices]

    print("\nLes valeurs de base: ")
    for idx in base_indices:
        for row in tableau[1:]:
            if row[idx] == 1:
                print(f'x{idx + 1}: {row[-1]}')

    print("\nLes valeurs hors base: ")
    for idx in non_base_indices:
        print(f'x{idx + 1}: 0')

    # print(f"z: {}")
    print(f"Z: {tableau[0][-1]}")











# Fonction pour déterminer la colonne pivot
def pivot_column(tableau):
    result = min(range(len(tableau[-1]) - 1), key=lambda i: tableau[0][i])
    return result


def pivot_row(tableau, col):
    ratios = [(i, tableau[i][-1] / tableau[i][col]) for i in range(1, len(tableau)) if tableau[i][col] > 0]
    result = min(ratios, key=lambda x: x[1])[0]

    return result


def pivot(tableau, row, col):
    pivot_val = tableau[row][col]
    if pivot_val == 0:
        raise ValueError("La valeur pivot est nulle.")
    tableau[row] = [x / pivot_val for x in tableau[row]]
    for i in range(len(tableau)):
        if i != row:
            factor = tableau[i][col]
            tableau[i] = [x - factor * tableau[row][j] for j, x in enumerate(tableau[i])]




def simplex_solver(new_objectif_function, new_contraintes, contraintes_resultat):
    tableau = [ new_objectif_function +[0]]  # Première ligne du tableau avec les coefficients de l'objectif
    tableau.extend([c + [v] for c, v in zip(new_contraintes, contraintes_resultat)])  # Lignes suivantes représentant les contraintes


    # Fonction pour afficher le tableau
    def display_tableau(tableau, i):
        print(f"\n\n----> Tableau {i}:")
        for row in tableau:
            rounded_row = [round(val, 2) for val in row]
            print(rounded_row)
        display_variables(tableau)


    display_tableau(tableau, 1)  # Afficher le tableau initial
    # Itération jusqu'à ce que toutes les valeurs de la fonction objectif soient non négatives
    i=2
    while min(tableau[0][:-1]) < 0: 
        col = pivot_column(tableau)  # Sélection de la colonne pivot
        row = pivot_row(tableau, col)  # Sélection de la ligne pivot
        pivot(tableau, row, col)  # Opération de pivot pour mettre à jour
        
        display_tableau(tableau, i)  # Afficher le tableau après chaque itération
        i+=1



















def main():
    print("Welcome to Algorithm Simplexe (Programation Lineaire)")
    (objective_coeffs, constraint_coeffs, constraint_values) = contraints()
    simplex_solver(objective_coeffs, constraint_coeffs, constraint_values)

main()