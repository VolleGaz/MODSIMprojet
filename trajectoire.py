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
r_plaque = 0.75  # Rayon du trou de la plaque

# Fonction d'évolution pour solve_ivp
def equations(t, z):
    x, y, vx, vy = z
    ax = 0  # Accélération horizontale nulle

    # Accélération verticale en fonction de la position de la balle
    if y > r:  # Chute libre
        ay = -g
    else:  # Phase de rebond
        ay = -g - k * (y - r) / m - c * vy / m

    return [vx, vy, ax, ay]

# Fonction pour vérifier si la balle passe dans le trou de la plaque
def traverse_plaque(x_values, y_values):
    for x, y in zip(x_values, y_values):
        if x >= x_plaque - r and x <= x_plaque + r:
            distance_to_center = abs(y - y_plaque)
            if distance_to_center <= r_plaque:
                return True  # La balle passe dans le trou
    return False

# Simulation de la trajectoire
initial_conditions = [x0, y0, -3, 0]  # Exemple de vitesse initiale
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

# Génération de trajectoires avec différentes vitesses initiales pour vx
for vx0 in np.linspace(-5, 5, 10):  # Différentes vitesses initiales horizontales
    vy0 = 0  # Vitesse initiale verticale fixe
    initial_conditions = [x0, y0, vx0, vy0]
    solution = spi.solve_ivp(equations, [0, t_max], initial_conditions, t_eval=np.linspace(0, t_max, 1000))

    x_values = solution.y[0]
    y_values = solution.y[1]

    # Vérification si la trajectoire passe dans le trou de la plaque
    if traverse_plaque(x_values, y_values):
        color = 'green'  # La trajectoire passe dans le trou
    else:
        color = 'red'  # La trajectoire échoue

    # Tracé de la trajectoire
    plt.plot(x_values, y_values, color=color, alpha=0.6)

# Ajout du trou de la plaque
trou_plaque = plt.Circle((x_plaque, y_plaque), r_plaque, color="black", alpha=0.1, label="Trou de la plaque")
plt.gca().add_patch(trou_plaque)

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


