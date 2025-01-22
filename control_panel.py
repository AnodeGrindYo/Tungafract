from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QSlider
from PyQt5.QtCore import Qt

class ControlPanel(QWidget):
    """
    Fournit une interface utilisateur pour ajuster les paramètres de la simulation.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.init_ui()

    def init_ui(self):
        """
        Initialise les composants de l'interface utilisateur.
        """
        # Section de la lentille
        self.lens_controls = QFormLayout()
        self.lens_focal_length = QLineEdit()
        self.lens_curvature_radius = QLineEdit()
        self.lens_refractive_index = QLineEdit()
        self.lens_controls.addRow("Focal Length (m):", self.lens_focal_length)
        self.lens_controls.addRow("Curvature Radius (m):", self.lens_curvature_radius)
        self.lens_controls.addRow("Refractive Index:", self.lens_refractive_index)

        # Section de la source lumineuse
        self.light_controls = QFormLayout()
        self.light_position_x = QLineEdit()
        self.light_position_y = QLineEdit()
        self.light_wavelength = QLineEdit()
        self.light_intensity = QSlider(Qt.Horizontal)
        self.light_intensity.setRange(0, 100)
        self.light_intensity.setValue(50)
        self.light_controls.addRow("Position X (m):", self.light_position_x)
        self.light_controls.addRow("Position Y (m):", self.light_position_y)
        self.light_controls.addRow("Wavelength (nm):", self.light_wavelength)
        self.light_controls.addRow("Intensity:", self.light_intensity)

        # Boutons
        self.apply_button = QPushButton("Apply")
        self.reset_button = QPushButton("Reset")

        # Organisation
        self.layout.addWidget(QLabel("Lens Parameters"))
        self.layout.addLayout(self.lens_controls)
        self.layout.addWidget(QLabel("Light Source Parameters"))
        self.layout.addLayout(self.light_controls)
        self.layout.addWidget(self.apply_button)
        self.layout.addWidget(self.reset_button)

    def get_lens_parameters(self):
        """
        Récupère les paramètres de la lentille depuis les champs de saisie.

        :return: Dictionnaire contenant les paramètres de la lentille.
        """
        return {
            "focal_length": float(self.lens_focal_length.text()),
            "curvature_radius": float(self.lens_curvature_radius.text()),
            "refractive_index": float(self.lens_refractive_index.text()),
        }

    def get_light_source_parameters(self):
        """
        Récupère les paramètres de la source lumineuse depuis les champs de saisie.

        :return: Dictionnaire contenant les paramètres de la source lumineuse.
        """
        return {
            "position": (float(self.light_position_x.text()), float(self.light_position_y.text())),
            "wavelength": float(self.light_wavelength.text()) * 1e-9,  # Convertir en mètres
            "intensity": self.light_intensity.value() / 100.0,  # Normalisé entre 0 et 1
        }

    def connect_signals(self, apply_callback, reset_callback):
        """
        Connecte les boutons aux fonctions de rappel.

        :param apply_callback: Fonction appelée lors du clic sur "Apply".
        :param reset_callback: Fonction appelée lors du clic sur "Reset".
        """
        self.apply_button.clicked.connect(apply_callback)
        self.reset_button.clicked.connect(reset_callback)

    def set_parameters(self, lens_params, light_params):
        """
        Met à jour les champs du panneau de contrôle avec les paramètres donnés.

        :param lens_params: Dictionnaire des paramètres de la lentille.
        :param light_params: Dictionnaire des paramètres de la source lumineuse.
        """
        self.lens_focal_length.setText(str(lens_params["focal_length"]))
        self.lens_curvature_radius.setText(str(lens_params["curvature_radius"]))
        self.lens_refractive_index.setText(str(lens_params["refractive_index"]))

        self.light_position_x.setText(str(light_params["position"][0]))
        self.light_position_y.setText(str(light_params["position"][1]))
        self.light_wavelength.setText(str(light_params["wavelength"] * 1e9))  # Convertir en nanomètres
        self.light_intensity.setValue(int(light_params["intensity"] * 100))  # Convertir en %



# Exemple d'utilisation
# if __name__ == "__main__":
#     from PyQt5.QtWidgets import QApplication
#     import sys

#     def apply_settings():
#         print("Applying settings...")
#         print("Lens:", panel.get_lens_parameters())
#         print("Light Source:", panel.get_light_source_parameters())

#     def reset_settings():
#         print("Resetting settings...")

#     app = QApplication(sys.argv)
#     panel = ControlPanel()
#     panel.connect_signals(apply_settings, reset_settings)
#     panel.show()
#     sys.exit(app.exec_())
