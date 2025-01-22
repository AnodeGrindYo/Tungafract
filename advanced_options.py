class AdvancedOptions:
    """
    Gère les options avancées de la simulation, y compris la diffraction multiple, la cohérence et les déphasages.
    """

    def __init__(self):
        """
        Initialise les options avancées par défaut.
        """
        self.multi_slit_enabled = False
        self.slit_spacing = 0.001  # Distance entre les fentes (en mètres)
        self.num_slits = 2
        self.coherence_enabled = False
        self.phase_shift = 0.0  # Déphasage initial (en radians)

    def enable_multi_slit(self, enabled, slit_spacing=None, num_slits=None):
        """
        Active ou désactive la diffraction multiple et configure ses paramètres.

        :param enabled: Booléen pour activer/désactiver la diffraction multiple.
        :param slit_spacing: Distance entre les fentes (en mètres).
        :param num_slits: Nombre de fentes.
        """
        self.multi_slit_enabled = enabled
        if slit_spacing is not None:
            self.slit_spacing = slit_spacing
        if num_slits is not None:
            self.num_slits = num_slits

    def enable_coherence(self, enabled):
        """
        Active ou désactive la cohérence de la source lumineuse.

        :param enabled: Booléen pour activer/désactiver la cohérence.
        """
        self.coherence_enabled = enabled

    def set_phase_shift(self, phase):
        """
        Configure le déphasage.

        :param phase: Déphasage en radians.
        """
        self.phase_shift = phase

    def get_advanced_settings(self):
        """
        Retourne les paramètres avancés actuels sous forme de dictionnaire.

        :return: Dictionnaire des options avancées.
        """
        return {
            "multi_slit_enabled": self.multi_slit_enabled,
            "slit_spacing": self.slit_spacing,
            "num_slits": self.num_slits,
            "coherence_enabled": self.coherence_enabled,
            "phase_shift": self.phase_shift,
        }

# Exemple d'utilisation
# if __name__ == "__main__":
#     options = AdvancedOptions()

#     # Configurer la diffraction multiple
#     options.enable_multi_slit(True, slit_spacing=0.0005, num_slits=3)

#     # Activer la cohérence
#     options.enable_coherence(True)

#     # Définir un déphasage
#     options.set_phase_shift(3.14 / 4)

#     # Afficher les paramètres avancés
#     print("Options avancées:", options.get_advanced_settings())
