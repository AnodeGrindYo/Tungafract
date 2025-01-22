class LightSource:
    """
    Représente une source lumineuse avec des propriétés configurables.
    """

    def __init__(self, position=(0, 0), wavelength=550e-9, intensity=1.0, coherence=1.0):
        """
        Initialise une instance de la classe LightSource.

        :param position: Tuple représentant la position (x, y) de la source lumineuse (en mètres).
        :param wavelength: Longueur d'onde de la lumière (en mètres).
        :param intensity: Intensité de la lumière (échelle relative de 0 à 1).
        :param coherence: Degré de cohérence de la lumière (de 0 à 1).
        """
        self.position = position
        self.wavelength = wavelength
        self.intensity = intensity
        self.coherence = coherence

    def set_position(self, x, y):
        """
        Définit une nouvelle position pour la source lumineuse.

        :param x: Coordonnée x (en mètres).
        :param y: Coordonnée y (en mètres).
        """
        self.position = (x, y)

    def set_wavelength(self, wavelength):
        """
        Définit une nouvelle longueur d'onde pour la lumière.

        :param wavelength: Longueur d'onde (en mètres).
        """
        if wavelength <= 0:
            raise ValueError("La longueur d'onde doit être positive.")
        self.wavelength = wavelength

    def set_intensity(self, intensity):
        """
        Définit une nouvelle intensité lumineuse.

        :param intensity: Intensité (de 0 à 1).
        """
        if not (0 <= intensity <= 1):
            raise ValueError("L'intensité doit être comprise entre 0 et 1.")
        self.intensity = intensity

    def propagate(self):
        """
        Simule la propagation de la lumière à partir de la position actuelle.

        :return: Dictionnaire avec les paramètres actuels de la lumière.
        """
        return {
            "position": self.position,
            "wavelength": self.wavelength,
            "intensity": self.intensity,
            "coherence": self.coherence,
        }

# Exemple d'utilisation
# if __name__ == "__main__":
#     light_source = LightSource(position=(0, 0), wavelength=500e-9, intensity=0.8, coherence=0.9)
#     print("Source lumineuse initiale:", light_source.propagate())

#     # Mise à jour des paramètres
#     light_source.set_position(0.1, 0.2)
#     light_source.set_wavelength(650e-9)
#     light_source.set_intensity(0.6)

#     print("Source lumineuse mise à jour:", light_source.propagate())
