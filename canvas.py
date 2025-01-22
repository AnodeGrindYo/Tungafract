from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class Canvas(QWidget):
    """
    Classe gérant l'affichage graphique de la simulation.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.lens = None
        self.light_source = None
        self.diffraction_pattern = None
        self.wavefronts = []

    def set_simulation_data(self, lens, light_source, diffraction_pattern, wavefronts):
        """
        Configure les données à afficher sur le canvas.

        :param lens: Instance de la classe Lens.
        :param light_source: Instance de la classe LightSource.
        :param diffraction_pattern: Instance de la classe DiffractionPattern.
        :param wavefronts: Liste des instances de Wavefront.
        """
        self.lens = lens
        self.light_source = light_source
        self.diffraction_pattern = diffraction_pattern
        self.wavefronts = wavefronts
        self.update()

    def paintEvent(self, event):
        """
        Gère le rendu des éléments graphiques sur le canvas.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.lens:
            self.draw_lens(painter)

        if self.light_source:
            self.draw_light_source(painter)

        if self.diffraction_pattern:
            self.draw_diffraction_pattern(painter)

        if self.wavefronts:
            self.draw_wavefronts(painter)

    def draw_lens(self, painter):
        """
        Dessine la lentille sur le canvas.
        """
        pen = QPen(Qt.blue, 2)
        painter.setPen(pen)
        # Logique simplifiée pour dessiner une lentille au centre du canvas
        width = self.width()
        height = self.height()
        painter.drawEllipse(width // 2 - 50, height // 2 - 100, 100, 200)

    def draw_light_source(self, painter):
        """
        Dessine la source lumineuse sur le canvas.
        """
        pen = QPen(Qt.red, 2)
        painter.setPen(pen)
        x, y = self.light_source.position
        painter.drawEllipse(int(x * self.width()), int(y * self.height()), 10, 10)

    def draw_diffraction_pattern(self, painter):
        """
        Dessine le motif de diffraction sur le canvas.
        """
        if not self.diffraction_pattern or not self.diffraction_pattern.spots:
            return

        pen = QPen(Qt.green, 1)
        painter.setPen(pen)
        width = self.width()
        height = self.height()
        center_x = width // 2
        center_y = height - 50  # Position de base des spots

        for spot in self.diffraction_pattern.spots:
            # Convertir la position en pixels
            x = center_x + int(spot["position"] * (width / self.diffraction_pattern.screen_distance))
            y = center_y
            intensity = min(255, int(spot["intensity"] * 255))  # Limiter à 255

            # Dessiner un cercle proportionnel à l'intensité
            size = max(3, intensity // 50)  # Taille dépend de l'intensité
            painter.setBrush(Qt.green)
            painter.drawEllipse(x - size // 2, y - size // 2, size, size)


    def draw_wavefronts(self, painter):
        """
        Dessine les fronts d'onde sur le canvas.
        """
        pen = QPen(Qt.yellow, 1, Qt.DashLine)
        painter.setPen(pen)
        for wavefront in self.wavefronts:
            points = wavefront.draw()
            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i + 1]
                painter.drawLine(
                    int(x1 * self.width()), int(y1 * self.height()),
                    int(x2 * self.width()), int(y2 * self.height())
                )

# Exemple d'utilisation avec PyQt (nécessite un main.py pour un fonctionnement complet)
# if __name__ == "__main__":
#     from PyQt5.QtWidgets import QApplication
#     import sys

#     app = QApplication(sys.argv)
#     canvas = Canvas()
#     canvas.resize(800, 600)
#     canvas.show()
#     sys.exit(app.exec_())
