class DiffractionSpot:
    """
    Représente un spot de diffraction particulier sur l'écran d'observation.
    """

    def __init__(self, position, angle, intensity):
        """
        Initialise une instance de la classe DiffractionSpot.

        :param position: Position du spot sur l'écran (en mètres).
        :param angle: Angle de diffraction associé au spot (en radians).
        :param intensity: Intensité lumineuse du spot (échelle relative de 0 à 1).
        """
        self.position = position
        self.angle = angle
        self.intensity = intensity

    def calculate_intensity(self, base_intensity, order):
        """
        Calcule l'intensité lumineuse du spot basé sur son ordre et une intensité de base.

        :param base_intensity: Intensité lumineuse de la source (échelle de 0 à 1).
        :param order: Ordre de diffraction (entier positif ou négatif).
        :return: Intensité calculée.
        """
        # Exemple : modèle simple basé sur une modulation cos²
        self.intensity = base_intensity * (np.cos(np.pi * order) ** 2)
        return self.intensity

    def display(self):
        """
        Retourne une représentation textuelle du spot de diffraction.

        :return: Chaîne décrivant le spot.
        """
        return (
            f"Position: {self.position:.6f} m, "
            f"Angle: {self.angle:.6f} radians, "
            f"Intensité: {self.intensity:.2f}"
        )

# Exemple d'utilisation
# if __name__ == "__main__":
#     import numpy as np

#     # Création d'un spot de diffraction
#     spot = DiffractionSpot(position=0.01, angle=np.pi / 6, intensity=0.5)

#     # Calcul de l'intensité pour un ordre donné
#     base_intensity = 1.0
#     order = 1
#     spot.calculate_intensity(base_intensity, order)

#     # Affichage des détails du spot
#     print(spot.display())
