import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def integrateur_simple(conditions_initiales, viteses, acceleration, masse_balle, rayon_balle, k, c, temps_simulation):   
    # Initial conditions: [position_x, position_y, velocity_x, velocity_y]
    etats_initiaux = conditions_initiales + viteses  # Concaténation des positions et des vitesses initiales

    # Fonction définissant le système d'équations différentielles
    def equations(t, etats):
        x, y, vx, vy = etats  # Décomposer les états

        # Accélérations selon x et y
        ax = 0  # Aucune accélération en x (pas de force)
        ay = -9.81  # Gravité en y
        if y > rayon_balle:
            ay += 0  # Pas de correction au-dessus du sol
        else:
            ay += -(k * (y - rayon_balle) + c * vy) / masse_balle  # Ajout de la force de rappel au contact

        return [vx, vy, ax, ay]

    # Résolution du système avec solve_ivp
    sol = spi.solve_ivp(equations, [0, temps_simulation], etats_initiaux, t_eval=np.linspace(0, temps_simulation, 500))

    # Création d'une figure avec une grille de 2x2 pour les sous-graphes
    plt.figure(figsize=(12, 10))

    # Tracé de la position x(t)
    plt.subplot(2, 2, 1)
    plt.plot(sol.t, sol.y[0], label='x(t)', color='blue')
    plt.xlabel('Temps (s)')
    plt.ylabel('Position x (m)')
    plt.title('Position x en fonction du temps')
    plt.legend()
    plt.grid()

    # Tracé de la position y(t)
    plt.subplot(2, 2, 2)
    plt.plot(sol.t, sol.y[1], label='y(t)', color='orange')
    plt.xlabel('Temps (s)')
    plt.ylabel('Position y (m)')
    plt.title('Position y en fonction du temps')
    plt.legend()
    plt.grid()

    # Tracé de la trajectoire y(x)
    plt.subplot(2, 2, 3)
    plt.plot(sol.y[0], sol.y[1], label='y(x)', color='purple')
    plt.xlabel('Position x (m)')
    plt.ylabel('Position y (m)')
    plt.title('Trajectoire y en fonction de x')
    plt.legend()
    plt.grid()

    # Tracé des vitesses vx(t) et vy(t)
    plt.subplot(2, 2, 4)
    plt.plot(sol.t, sol.y[2], label="v_x(t)", linestyle='--', color='green')
    plt.plot(sol.t, sol.y[3], label="v_y(t)", linestyle='--', color='red')
    plt.xlabel('Temps (s)')
    plt.ylabel('Vitesse (m/s)')
    plt.title('Vitesses en fonction du temps')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

# Appel de la fonction avec des paramètres
integrateur_simple([10, 10], [-3, 0], 9.81, 0.2, 0.05, 5000, 5, 10)
