import json
from pathlib import Path
from datetime import datetime, timezone
from jinja2 import Environment, FileSystemLoader

# Configuration matching your tree
BASE_DIR = Path(__file__).parent
TEMPLATE_DIR = BASE_DIR  # Templates are in root
STATIC_DIR = BASE_DIR    # CSS/JS in root
DATA_FILE = BASE_DIR / "portfolio-mariana.json"
OUTPUT_DIR = BASE_DIR

def load_profile_data():
    """Load and enhance portfolio data"""
    with DATA_FILE.open(encoding="utf-8") as f:
        data = json.load(f)
    
    # Add dynamic year
    data["current_year"] = datetime.now(timezone.utc).year
    
    # Process profile image path
    if "image_path" in data:
        data["profile_image"] = str(Path(data["image_path"]).relative_to(BASE_DIR)
    
    return data

def setup_jinja():
    """Configure template environment"""
    return Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True
    )

def render_templates(env, data):
    """Generate output files"""
    index_template = env.get_template("index_template.html")
    resume_template = env.get_template("resume_template.html")
    
    return {
        OUTPUT_DIR / "index.html": index_template.render(**data),
        OUTPUT_DIR / "resume.html": resume_template.render(**data)
    }

def main():
    print("🚀 Generating portfolio...")
    
    data = load_profile_data()
    env = setup_jinja()
    outputs = render_templates(env, data)
    
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
        print(f"✅ Generated: {path.relative_to(BASE_DIR)}")
    
    print("🎉 Success! Open index.html in your browser")

if __name__ == "__main__":
    main()