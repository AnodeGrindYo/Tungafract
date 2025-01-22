import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from canvas import Canvas
from control_panel import ControlPanel
from simulation import Simulation


class MainWindow(QMainWindow):
    """
    Fenêtre principale de l'application de simulation de diffraction.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simulation de Diffraction")
        self.resize(1200, 800)

        self.simulation = Simulation()
        self.init_ui()

    def init_ui(self):
        """
        Initialise l'interface utilisateur principale.
        """
        main_widget = QWidget()
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # Ajout des composants
        self.canvas = Canvas()
        self.control_panel = ControlPanel()

        layout.addWidget(self.canvas)
        layout.addWidget(self.control_panel)

        # Connecter les signaux
        self.control_panel.connect_signals(self.apply_settings, self.reset_simulation)

        # Charger les paramètres par défaut
        self.load_default_settings()

    def load_default_settings(self, config_file="default_config.json"):
        """
        Charge les paramètres par défaut depuis un fichier JSON et configure la simulation.

        :param config_file: Chemin du fichier de configuration par défaut.
        """
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)

            # Charger les paramètres de la lentille
            lens_params = config["lens"]
            from lens import Lens
            lens = Lens(**lens_params)

            # Charger les paramètres de la source lumineuse
            light_params = config["light_source"]
            from light_source import LightSource
            light_source = LightSource(**light_params)

            # Configurer la simulation avec les paramètres par défaut
            screen_distance = config["simulation"]["screen_distance"]
            self.simulation.configure_components(lens, light_source, screen_distance)

            # Appliquer les paramètres au canvas
            self.simulation.start_simulation()
            self.canvas.set_simulation_data(
                self.simulation.lens,
                self.simulation.light_source,
                self.simulation.diffraction_pattern,
                self.simulation.wavefronts,
            )

            # Mettre à jour le panneau de contrôle
            self.control_panel.set_parameters(lens_params, light_params)

            print("Paramètres par défaut chargés.")
        except Exception as e:
            print(f"Erreur lors du chargement des paramètres par défaut : {e}")


    def apply_settings(self):
        """
        Applique les paramètres entrés dans le panneau de contrôle à la simulation.
        """
        try:
            lens_params = self.control_panel.get_lens_parameters()
            light_params = self.control_panel.get_light_source_parameters()

            # Configurer les composants de la simulation
            from lens import Lens
            from light_source import LightSource

            lens = Lens(**lens_params)
            light_source = LightSource(**light_params)

            self.simulation.configure_components(lens, light_source, screen_distance=1.0)
            self.simulation.start_simulation()

            # Mise à jour du canvas
            self.canvas.set_simulation_data(
                self.simulation.lens,
                self.simulation.light_source,
                self.simulation.diffraction_pattern,
                self.simulation.wavefronts,
            )
        except Exception as e:
            print(f"Erreur lors de l'application des paramètres : {e}")

    def reset_simulation(self):
        """
        Réinitialise la simulation et le panneau de contrôle.
        """
        self.simulation.reset_simulation()
        self.canvas.set_simulation_data(None, None, None, [])
        print("Simulation réinitialisée.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
