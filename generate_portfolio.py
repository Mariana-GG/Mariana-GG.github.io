import json
import os
from datetime import datetime, timezone
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# === PATH CONFIGURATION ===
TEMPLATE_DIR = Path('./templates')  # HTML templates location
STATIC_DIR = Path('./static')       # CSS/JS/images location
DATA_FILE = Path('portfolio-mariana.json')  # Your custom data file
OUTPUT_DIR = Path('.')              # Where to save generated files
# ==========================

def main():
    # Load and prepare data
    with DATA_FILE.open(encoding="utf-8") as f:
        data = json.load(f)

    # Add dynamic content
    data["current_year"] = datetime.now(timezone.utc).year
    
    # Process social links SVGs
    if "social_links" in data:
        for link in data["social_links"]:
            if svg_path := link.get("svg_path"):
                full_svg_path = STATIC_DIR / svg_path
                with full_svg_path.open(encoding="utf-8") as svg_file:
                    link["svg_data"] = svg_file.read()

    # Configure template environment
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=True
    )

    # Render templates
    index_template = env.get_template("index_template.html")
    resume_template = env.get_template("resume_template.html")

    # Generate output files
    output_paths = {
        OUTPUT_DIR / "index.html": index_template.render(**data),
        OUTPUT_DIR / "resume.html": resume_template.render(**data)
    }

    for path, content in output_paths.items():
        with path.open("w", encoding="utf-8") as f:
            f.write(content)

    print(f"Success! Generated files in {OUTPUT_DIR.resolve()}")

if __name__ == "__main__":
    main()