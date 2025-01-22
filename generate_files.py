import os

# List of Python files to create
files = [
    "main.py",
    "canvas.py",
    # "lens.py",
    "light_source.py",
    "diffraction_pattern.py",
    "diffraction_spot.py",
    "wave_front.py",
    "simulation.py",
    "control_panel.py",
    "exporter.py",
    "advanced_options.py"
]

# Create each file if it doesn't already exist
for file_name in files:
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            # Optionally, add a docstring to each file
            file.write(f"""# {file_name.capitalize().replace('_', ' ').replace('.py', '')}

# This is the placeholder for the {file_name} module.
""")
        print(f"Created: {file_name}")
    else:
        print(f"Skipped (already exists): {file_name}")

print("All files processed.")
