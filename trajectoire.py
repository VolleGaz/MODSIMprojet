import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Paramètres
m, r = 0.2, 0.05  # Masse et rayon de la balle
g, c, k = 9.81, 5, 5000  # Constantes de simulation
x0, y0 = 10, 10  # Position initiale
t_max = 10

# Paramètres des obstacles
x_plaque = 5  # Position de la plaque
y_plaque = 1  # Hauteur du centre du trou de la plaque
r_plaque = 1  # Rayon du trou de la plaque
x_trou = 4
r_trou = 1

# Fonction d'évolution pour solve_ivp
def equations(t, z):
    x, y, vx, vy = z
    ax = 0  # Accélération horizontale nulle
    ay = -g  # Accélération verticale par défaut

    # Vérifier si la balle est sous la plaque et rebondir si nécessaire
    if y <= y_plaque + r_plaque and (x_plaque - r <= x <= x_plaque + r):
        # La balle touche la plaque, on inverse la vitesse verticale
        vy = -vy * 0.8  # Coefficient de restitution pour l'élasticité du rebond
        y = y_plaque + r_plaque  # Assurer que la balle ne passe pas à travers la plaque
    elif y > r:  # Chute libre
        ay = -g  # Accélération gravitationnelle (avant la plaque)
    else:  # Phase de rebond (sur le sol ou après un rebond sur la plaque)
        ay = -g - k * (y - r) / m - c * vy / m

    return [vx, vy, ax, ay]


# Fonction pour vérifier si la balle passe dans le trou de la plaque
def traverse_plaque(x_values, y_values):
    for x, y in zip(x_values, y_values):
        if x_plaque - r <= x <= x_plaque + r:
            distance_to_center = abs(y - y_plaque)
            if distance_to_center <= r_plaque:
                return True  # La balle passe dans le trou
    return False

# Fonction pour vérifier si la balle atterrit dans le trou du sol
def atterrir_dans_trou_sol(x_values, y_values):
    for x, y in zip(x_values, y_values):
        # Vérifier si la balle est dans la plage horizontale du trou du sol
        if x_trou - r_trou <= x <= x_trou + r_trou:

            # Vérifier si la balle touche le sol dans la plage du trou
            if y <= r:  # Le sol est au niveau y = 0, donc y <= r signifie qu'elle touche le sol
                return True  # La balle atterrit dans le trou du sol
    return False


# Simulation avec une vitesse initiale modifiée
initial_conditions = [x0, y0, -3, 0]  # Exemple de vitesse initiale (ajustée si nécessaire)
solution = spi.solve_ivp(equations, [0, t_max], initial_conditions, t_eval=np.linspace(0, t_max, 1000))
x_values = solution.y[0]
y_values = solution.y[1]

# Création d'une figure avec une grille 2x2 pour les sous-graphes
plt.figure(figsize=(12, 10))

# Tracé de la position x(t)
plt.subplot(2, 2, 1)
plt.plot(solution.t, solution.y[0], label='x(t)', color='blue')
plt.xlabel('Temps (s)')
plt.ylabel('Position x (m)')
plt.title('Position x en fonction du temps')
plt.legend()
plt.grid()

# Tracé de la position y(t)
plt.subplot(2, 2, 2)
plt.plot(solution.t, solution.y[1], label='y(t)', color='orange')
plt.xlabel('Temps (s)')
plt.ylabel('Position y (m)')
plt.title('Position y en fonction du temps')
plt.legend()
plt.grid()

# Tracé de la trajectoire y(x)
plt.subplot(2, 2, 3)
plt.plot(solution.y[0], solution.y[1], label='y(x)', color='purple')
plt.xlabel('Position x (m)')
plt.ylabel('Position y (m)')
plt.title('Trajectoire y en fonction de x')
plt.legend()
plt.grid()

# Tracé des vitesses vx(t) et vy(t)
plt.subplot(2, 2, 4)
plt.plot(solution.t, solution.y[2], label="v_x(t)", linestyle='--', color='green')
plt.plot(solution.t, solution.y[3], label="v_y(t)", linestyle='--', color='red')
plt.xlabel('Temps (s)')
plt.ylabel('Vitesse (m/s)')
plt.title('Vitesses en fonction du temps')
plt.legend()
plt.grid()

# Partie 1.3 : Trajectoires multiples avec la plaque
plt.figure(figsize=(8, 6))

# Tracé de la plaque comme une ligne noire
plt.axvline(x=x_plaque, color="black", linestyle="-", linewidth=2, label="Plaque")

# Ajout du trou de la plaque
trou_plaque = plt.Circle((x_plaque, y_plaque), r_plaque, color="black", alpha=0.1, label="Trou de la plaque")
plt.gca().add_patch(trou_plaque)

# Ajout du trou dans le sol
trou_sol = plt.Circle((x_trou, 0), r_trou, color="blue", alpha=0.3, label="Trou dans le sol")
plt.gca().add_patch(trou_sol)

# Génération de trajectoires avec différentes vitesses initiales pour vx
for vx0 in np.linspace(-5, 5, 10):  # Différentes vitesses initiales horizontales
    vy0 = 0  # Vitesse initiale verticale fixe
    initial_conditions = [x0, y0, vx0, vy0]
    solution = spi.solve_ivp(equations, [0, t_max], initial_conditions, t_eval=np.linspace(0, t_max, 1000))

    x_values = solution.y[0]
    y_values = solution.y[1]

    # Vérification si la trajectoire passe dans le trou de la plaque
    if traverse_plaque(x_values, y_values) and atterrir_dans_trou_sol(x_values, y_values):
        color = 'green'  # La trajectoire passe dans le trou
    else:
        color = 'red'  # La trajectoire échoue

    # Tracé de la trajectoire
    plt.plot(x_values, y_values, color=color, alpha=0.6)

# Réglages du graphique pour la 1.3
plt.xlabel("Position x (m)")
plt.ylabel("Position y (m)")
plt.title("Multiples trajectoires avec obstacles")
plt.legend()
plt.grid()
plt.xlim(0, x0 + 2)
plt.ylim(-1, y0 + 2)
plt.gca().set_aspect('equal', adjustable='box')

# Affichage
plt.tight_layout()
plt.show()
