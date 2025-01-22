import numpy as np

class DiffractionPattern:
    """
    Représente le motif de diffraction observé après le passage de la lumière à travers une lentille.
    """

    def __init__(self, screen_distance, pattern_type="monochromatic"):
        """
        Initialise une instance de la classe DiffractionPattern.

        :param screen_distance: Distance entre la lentille et l'écran d'observation (en mètres).
        :param pattern_type: Type de motif de diffraction ("monochromatic", "multi-slit", etc.).
        """
        self.screen_distance = screen_distance
        self.pattern_type = pattern_type
        self.spots = []  # Liste des spots de diffraction calculés

    def calculate_pattern(self, light_source, lens):
        """
        Calcule le motif de diffraction basé sur la source lumineuse et la lentille.

        :param light_source: Instance de LightSource.
        :param lens: Instance de Lens.
        """
        # Exemple simplifié : calcul des positions des maxima principaux (monochromatique, fente unique)
        wavelength = light_source.wavelength
        aperture_size = lens.curvature_radius  # Supposons que le rayon de courbure est lié à l'ouverture

        if aperture_size == 0 or self.screen_distance == 0:
            raise ValueError("Les dimensions de l'ouverture ou la distance de l'écran sont invalides.")

        # Calcul des angles des maxima principaux : sin(θ) = mλ / a
        m_values = np.arange(-10, 11)  # Ordres de diffraction (-10 à +10)
        angles = m_values * wavelength / aperture_size
        
        # Filtrer les angles valides (|sin(θ)| <= 1)
        valid_angles = angles[np.abs(angles) <= 1]

        # Convertir en positions sur l'écran : x = L * tan(θ)
        positions = self.screen_distance * np.tan(np.arcsin(valid_angles))

        # Stocker les spots de diffraction
        self.spots = [
            {
                "order": m,
                "position": pos,
                "intensity": light_source.intensity * (np.cos(np.pi * m) ** 2),  # Exemple d'intensité
            }
            for m, pos in zip(m_values[:len(positions)], positions)
        ]

    def update_pattern(self):
        """
        Met à jour le motif de diffraction. Recalcule si nécessaire.
        """
        # Placeholder pour des fonctionnalités futures
        pass

    def display_pattern(self):
        """
        Retourne une représentation textuelle ou graphique du motif de diffraction.

        :return: Liste des positions et intensités des spots de diffraction.
        """
        return self.spots

# Exemple d'utilisation
# if __name__ == "__main__":
#     from light_source import LightSource
#     from lens import Lens

#     # Initialisation
#     light = LightSource(position=(0, 0), wavelength=600e-9, intensity=1.0)
#     lens = Lens(focal_length=0.1, curvature_radius=0.01, refractive_index=1.5)
#     pattern = DiffractionPattern(screen_distance=0.5)

#     # Calcul du motif
#     pattern.calculate_pattern(light, lens)

#     # Affichage
#     for spot in pattern.display_pattern():
#         print(f"Ordre: {spot['order']}, Position: {spot['position']:.6f} m, Intensité: {spot['intensity']:.2f}")
