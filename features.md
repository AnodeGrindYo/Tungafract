# Simulation de diffraction de la lumière à travers une lentille hautement paramétrable

## Fonctionnalités en Gherkin

```gherkin
Feature: Lens Diffraction Simulation

  Scenario: Initialize the lens with customizable parameters
    Given the lens has a configurable focal length
    And the lens has a configurable curvature radius
    And the lens material can be selected with its refractive index
    And the lens shape can be circular, elliptical, or custom
    When the lens is placed in the simulation environment
    Then the lens properties should be applied and displayed on the canvas

  Scenario: Set light source parameters
    Given a point light source can be placed at any position on the canvas
    And the wavelength of the light source can be adjusted
    And the light source intensity can be configured
    When the light source is positioned on the canvas
    Then the light's wavelength, intensity, and position should be reflected in the simulation

  Scenario: Simulate diffraction through the lens
    Given the light source is placed and the lens is configured
    When the light passes through the lens
    Then diffraction patterns should appear on the canvas
    And the diffraction fringes should be calculated and displayed
    And the interference patterns should be visible, showing wave behavior

  Scenario: Control diffraction simulation parameters
    Given the user can change the distance between the light source and the lens
    And the user can change the distance between the lens and the observation screen
    And the user can change the aperture size of the lens
    When the user modifies any of these parameters
    Then the diffraction pattern should update according to the changes

  Scenario: Visualize wavefront propagation
    Given wavefronts should be visible as they propagate through the system
    When light passes through the lens
    Then wavefronts should be drawn from the light source to the lens and from the lens to the observation screen
    And the wavefronts should demonstrate the effect of lens curvature on the propagation

  Scenario: Measure diffraction angles and spot positions
    Given the diffraction pattern is visible
    When the user clicks on a diffraction spot
    Then the angle of diffraction and the distance from the center should be displayed

  Scenario: Apply advanced simulation features
    Given the simulation can include multi-slit diffraction
    And the simulation can include varying the coherence of the light source
    And the simulation can incorporate phase shifts in the light wave
    When the user enables these advanced features
    Then the simulation should update to reflect the multi-slit diffraction patterns, coherence effects, and phase shifts

  Scenario: Export diffraction patterns and simulation data
    Given the diffraction pattern is displayed on the canvas
    When the user chooses to export the simulation data
    Then the diffraction data should be available for download in CSV or JSON format
    And the image of the diffraction pattern should be available for download as PNG or SVG
```

## Liste des classes

### 1. **Canvas**
   - **Responsabilité** : Gérer l'affichage et la mise à jour du contenu de la simulation sur l'interface utilisateur.
   - **Méthodes** :
     - `drawLens(Lens lens)`
     - `drawLightSource(LightSource source)`
     - `drawDiffractionPattern(DiffractionPattern pattern)`
     - `clear()`
     - `update()`

### 2. **Lens**
   - **Responsabilité** : Représenter une lentille avec des propriétés physiques ajustables, telles que le rayon de courbure, la longueur focale, et le matériau.
   - **Propriétés** :
     - `focalLength` : longueur focale
     - `curvatureRadius` : rayon de courbure
     - `refractiveIndex` : indice de réfraction
     - `shape` : forme de la lentille (circular, elliptical, custom)
   - **Méthodes** :
     - `refract(LightSource source)`
     - `calculateFocalPoint()`
     - `getLensProfile()`

### 3. **LightSource**
   - **Responsabilité** : Représenter une source lumineuse avec des propriétés telles que l'intensité, la position, et la longueur d'onde.
   - **Propriétés** :
     - `position` : coordonnées de la source
     - `wavelength` : longueur d'onde de la lumière
     - `intensity` : intensité de la source
     - `coherence` : cohérence de la source (si applicable)
   - **Méthodes** :
     - `propagate()`
     - `setPosition(x, y)`
     - `setWavelength(wavelength)`
     - `setIntensity(intensity)`

### 4. **DiffractionPattern**
   - **Responsabilité** : Représenter le modèle de diffraction observé sur l'écran ou à une certaine distance après la lentille.
   - **Propriétés** :
     - `spots` : liste des spots de diffraction
     - `patternType` : type de modèle de diffraction (monochromatique, multi-slit, etc.)
     - `screenDistance` : distance entre la lentille et l'écran d'observation
   - **Méthodes** :
     - `calculatePattern(LightSource source, Lens lens)`
     - `updatePattern()`
     - `displayPattern()`

### 5. **Wavefront**
   - **Responsabilité** : Représenter les fronts d'onde de la lumière au fur et à mesure de sa propagation à travers le système optique.
   - **Propriétés** :
     - `origin` : position du point d'origine de la vague
     - `angle` : angle de propagation des fronts d'onde
     - `phase` : phase de la vague (si applicable)
   - **Méthodes** :
     - `propagate()`
     - `draw()`

### 6. **DiffractionSpot**
   - **Responsabilité** : Représenter un spot de diffraction particulier sur l'écran d'observation.
   - **Propriétés** :
     - `position` : position du spot sur l'écran
     - `angle` : angle de diffraction
     - `intensity` : intensité du spot
   - **Méthodes** :
     - `display()`
     - `calculateIntensity()`

### 7. **Simulation**
   - **Responsabilité** : Gérer l'ensemble du processus de simulation, de la configuration des paramètres à l'exécution des calculs physiques.
   - **Propriétés** :
     - `lens` : instance de la classe Lens
     - `lightSource` : instance de la classe LightSource
     - `diffractionPattern` : instance de la classe DiffractionPattern
     - `wavefronts` : liste des instances de la classe Wavefront
   - **Méthodes** :
     - `startSimulation()`
     - `resetSimulation()`
     - `updateParameters()`
     - `run()`
     - `exportData()`

### 8. **Exporter**
   - **Responsabilité** : Gérer l'exportation des résultats de la simulation (patterns, données de diffraction) dans différents formats.
   - **Méthodes** :
     - `exportPatternAsImage(format)`
     - `exportDataAsCSV()`
     - `exportDataAsJSON()`

### 9. **ControlPanel**
   - **Responsabilité** : Fournir une interface pour que l'utilisateur puisse ajuster les paramètres de la simulation (lens, light source, etc.).
   - **Méthodes** :
     - `updateLensParameters(Lens lens)`
     - `updateLightSourceParameters(LightSource source)`
     - `toggleAdvancedOptions()`
     - `resetSimulation()`

### 10. **AdvancedOptions**
   - **Responsabilité** : Gérer les options avancées pour des simulations complexes (diffraction multiple, cohérence de la source, etc.).
   - **Méthodes** :
     - `enableMultiSlit()`
     - `setPhaseShift(phase)`
     - `enableCoherence()`

