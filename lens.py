class Lens:
    """
    Représente une lentille avec des propriétés physiques ajustables.
    """

    def __init__(self, focal_length, curvature_radius, refractive_index, shape="circular"):
        """
        Initialise une instance de la classe Lens.

        :param focal_length: Longueur focale de la lentille (en mètres).
        :param curvature_radius: Rayon de courbure de la lentille (en mètres).
        :param refractive_index: Indice de réfraction du matériau de la lentille.
        :param shape: Forme de la lentille ("circular", "elliptical", ou "custom").
        """
        self.focal_length = focal_length
        self.curvature_radius = curvature_radius
        self.refractive_index = refractive_index
        self.shape = shape

    def refract(self, light_source):
        """
        Calcule le comportement de la lumière après passage à travers la lentille.

        :param light_source: Instance de LightSource représentant la source lumineuse incidente.
        :return: Coordonnées du point focal ou données de propagation selon la configuration.
        """
        # Placeholder pour le calcul réel basé sur les équations optiques.
        focal_point = self.calculate_focal_point()
        return focal_point

    def calculate_focal_point(self):
        """
        Calcule la position du point focal en fonction des propriétés de la lentille.

        :return: Position du point focal (en mètres).
        """
        # Simplification : formule classique de la lentille mince
        if self.curvature_radius == 0 or self.refractive_index <= 1:
            raise ValueError("Propriétés invalides pour calculer le point focal.")
        return 1 / ((self.refractive_index - 1) * (1 / self.curvature_radius))

    def get_lens_profile(self):
        """
        Génère un profil descriptif de la lentille.

        :return: Dictionnaire contenant les propriétés de la lentille.
        """
        return {
            "focal_length": self.focal_length,
            "curvature_radius": self.curvature_radius,
            "refractive_index": self.refractive_index,
            "shape": self.shape,
        }

# Exemple d'utilisation
# if __name__ == "__main__":
#     lens = Lens(focal_length=0.05, curvature_radius=0.1, refractive_index=1.5, shape="circular")
#     print("Profil de la lentille:", lens.get_lens_profile())
#     try:
#         focal_point = lens.calculate_focal_point()
#         print("Point focal calculé:", focal_point)
#     except ValueError as e:
#         print("Erreur lors du calcul du point focal:", e)
