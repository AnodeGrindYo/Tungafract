import json
import csv
import os

class Exporter:
    """
    Gère l'exportation des résultats de la simulation sous différents formats.
    """

    @staticmethod
    def export_pattern_as_image(canvas, file_path):
        """
        Exporte le canvas de la simulation en tant qu'image.

        :param canvas: Instance du Canvas PyQt à exporter.
        :param file_path: Chemin du fichier de sortie (PNG ou SVG).
        """
        if not file_path.lower().endswith(('.png', '.svg')):
            raise ValueError("Le fichier doit être au format PNG ou SVG.")

        pixmap = canvas.grab()
        pixmap.save(file_path)

    @staticmethod
    def export_data_as_csv(data, file_path):
        """
        Exporte les données de la simulation en fichier CSV.

        :param data: Dictionnaire contenant les données de simulation.
        :param file_path: Chemin du fichier CSV de sortie.
        """
        if not file_path.lower().endswith('.csv'):
            raise ValueError("Le fichier doit avoir une extension .csv.")

        with open(file_path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Key", "Value"])
            for key, value in data.items():
                if isinstance(value, list):
                    writer.writerow([key, json.dumps(value)])
                else:
                    writer.writerow([key, value])

    @staticmethod
    def export_data_as_json(data, file_path):
        """
        Exporte les données de la simulation en fichier JSON.

        :param data: Dictionnaire contenant les données de simulation.
        :param file_path: Chemin du fichier JSON de sortie.
        """
        if not file_path.lower().endswith('.json'):
            raise ValueError("Le fichier doit avoir une extension .json.")

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

# Exemple d'utilisation
# if __name__ == "__main__":
#     example_data = {
#         "lens_profile": {
#             "focal_length": 0.1,
#             "curvature_radius": 0.02,
#             "refractive_index": 1.5
#         },
#         "light_source": {
#             "position": [0, 0],
#             "wavelength": 550e-9,
#             "intensity": 1.0
#         },
#         "diffraction_pattern": [
#             {"order": 1, "position": 0.01, "intensity": 0.8},
#             {"order": 2, "position": 0.02, "intensity": 0.6}
#         ],
#         "wavefronts": [[(0, 0), (0.01, 0.01), (0.02, 0.02)]]
#     }

#     # Export JSON
#     Exporter.export_data_as_json(example_data, "simulation_results.json")

#     # Export CSV
#     Exporter.export_data_as_csv(example_data, "simulation_results.csv")

#     # Export Image (nécessite un objet Canvas)
#     # Exporter.export_pattern_as_image(canvas, "simulation_canvas.png")
