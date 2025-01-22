import numpy as np

class Wavefront:
    """
    Représente les fronts d'onde de la lumière au cours de leur propagation.
    """

    def __init__(self, origin=(0, 0), angle=0.0, phase=0.0):
        """
        Initialise une instance de la classe Wavefront.

        :param origin: Point d'origine du front d'onde (x, y en mètres).
        :param angle: Angle de propagation du front d'onde (en radians).
        :param phase: Phase initiale du front d'onde (en radians).
        """
        self.origin = origin
        self.angle = angle
        self.phase = phase
        self.propagation_path = []  # Liste des points suivis par le front d'onde

    def propagate(self, distance, step_size=0.01):
        """
        Simule la propagation du front d'onde sur une distance donnée.

        :param distance: Distance totale de propagation (en mètres).
        :param step_size: Taille des pas de simulation (en mètres).
        """
        num_steps = int(distance / step_size)
        x, y = self.origin

        for _ in range(num_steps):
            x += step_size * np.cos(self.angle)
            y += step_size * np.sin(self.angle)
            self.propagation_path.append((x, y))

    def draw(self):
        """
        Génère une représentation textuelle du chemin du front d'onde.

        :return: Liste des points visités par le front d'onde.
        """
        return self.propagation_path

    def update_phase(self, increment):
        """
        Met à jour la phase du front d'onde.

        :param increment: Incrément à ajouter à la phase actuelle (en radians).
        """
        self.phase = (self.phase + increment) % (2 * np.pi)

# Exemple d'utilisation
# if __name__ == "__main__":
#     # Création d'un front d'onde
#     wavefront = Wavefront(origin=(0, 0), angle=np.pi / 4, phase=0.0)

#     # Propagation sur 1 mètre avec des pas de 0.1 mètre
#     wavefront.propagate(distance=1.0, step_size=0.1)

#     # Mise à jour de la phase
#     wavefront.update_phase(np.pi / 2)

#     # Affichage du chemin de propagation
#     for point in wavefront.draw():
#         print(f"Point: {point}")

#     print(f"Phase actuelle: {wavefront.phase:.2f} radians")
