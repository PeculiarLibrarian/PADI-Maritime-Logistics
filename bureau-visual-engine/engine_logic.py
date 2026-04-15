import json
import os

class VisualArchitect:
    def __init__(self, config_path):
        if not os.path.exists(config_path):
            print(f"ERROR: Configuration not found at {config_path}")
            return
        with open(config_path, 'r') as f:
            self.config = json.load(f)

    def compose_prompt(self, project_name, depth):
        prompt = (
            f"Style: {self.config['aesthetic']}. "
            f"Subject: A high-fidelity technical visualization of {project_name}. "
            f"Technical Depth: {depth}. "
            f"Include: {', '.join(self.config['required_elements'])}. "
            f"Constraint: {self.config['forbidden_elements'][0]}."
        )
        return prompt

config_file = 'manifest_schema.json'
architect = VisualArchitect(config_file)
print("--- BUREAU VISUAL ENGINE INITIALIZED ---")
print(architect.compose_prompt("Nairobi-01 Maritime Node", "Institutional"))
