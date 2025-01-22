from diffraction_pattern import DiffractionPattern
from wave_front import Wavefront

class Simulation:
    """
    Gère l'ensemble du processus de simulation de diffraction, y compris les composants optiques et les calculs physiques.
    """

    def __init__(self):
        """
        Initialise une instance de la simulation avec des composants par défaut.
        """
        self.lens = None
        self.light_source = None
        self.diffraction_pattern = None
        self.wavefronts = []

    def configure_components(self, lens, light_source, screen_distance):
        """
        Configure les composants de la simulation.

        :param lens: Instance de la classe Lens.
        :param light_source: Instance de la classe LightSource.
        :param screen_distance: Distance entre la lentille et l'écran d'observation (en mètres).
        """
        self.lens = lens
        self.light_source = light_source
        self.diffraction_pattern = DiffractionPattern(screen_distance)

    def start_simulation(self):
        """
        Lance la simulation en calculant les motifs de diffraction et les fronts d'onde.
        """
        if not self.lens or not self.light_source:
            raise ValueError("La lentille et la source lumineuse doivent être configurées avant de lancer la simulation.")

        # Calcul du motif de diffraction
        self.diffraction_pattern.calculate_pattern(self.light_source, self.lens)

        # Génération des fronts d'onde
        self.wavefronts.clear()
        wavefront = Wavefront(origin=self.light_source.position, angle=0, phase=0)
        wavefront.propagate(self.diffraction_pattern.screen_distance)
        self.wavefronts.append(wavefront)

    def reset_simulation(self):
        """
        Réinitialise la simulation à son état initial.
        """
        self.lens = None
        self.light_source = None
        self.diffraction_pattern = None
        self.wavefronts.clear()

    def update_parameters(self, lens=None, light_source=None, screen_distance=None):
        """
        Met à jour les paramètres de la simulation et recalcule les résultats.

        :param lens: Nouvelle instance de Lens (optionnel).
        :param light_source: Nouvelle instance de LightSource (optionnel).
        :param screen_distance: Nouvelle distance entre la lentille et l'écran (optionnel).
        """
        if lens:
            self.lens = lens
        if light_source:
            self.light_source = light_source
        if screen_distance and self.diffraction_pattern:
            self.diffraction_pattern.screen_distance = screen_distance

        # Recalculer la simulation
        self.start_simulation()

    def export_data(self):
        """
        Exporte les données de la simulation (motif de diffraction et fronts d'onde).

        :return: Dictionnaire contenant les données exportées.
        """
        return {
            "lens_profile": self.lens.get_lens_profile() if self.lens else None,
            "light_source": self.light_source.propagate() if self.light_source else None,
            "diffraction_pattern": self.diffraction_pattern.display_pattern() if self.diffraction_pattern else None,
            "wavefronts": [wavefront.draw() for wavefront in self.wavefronts],
        }

# Exemple d'utilisation
# if __name__ == "__main__":
#     from lens import Lens
#     from light_source import LightSource
#     from diffraction_pattern import DiffractionPattern
#     from wavefront import Wavefront

#     # Configuration de la simulation
#     lens = Lens(focal_length=0.1, curvature_radius=0.02, refractive_index=1.5)
#     light_source = LightSource(position=(0, 0), wavelength=550e-9, intensity=1.0)

#     simulation = Simulation()
#     simulation.configure_components(lens, light_source, screen_distance=0.5)
#     simulation.start_simulation()

#     # Exportation des résultats
#     results = simulation.export_data()
#     print("Résultats de la simulation:", results)
