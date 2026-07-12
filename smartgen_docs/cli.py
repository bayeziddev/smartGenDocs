import click
import os
from .core import Builder
from .server import DevServer
from .autodoc import AutodocGenerator

@click.group()
def main():
    """SmartGen Docs - A premium documentation platform by Sayad Md Bayezid Hosan."""
    pass

@main.command()
@click.option('--config', default='smartgen.yml', help='Path to config file.')
@click.option('--site-dir', default='site', help='Directory to output the built site.')
def build(config, site_dir):
    """Build the documentation site."""
    if not os.path.exists(config):
        click.secho(f"Error: Config file '{config}' not found. Run 'smartgen-docs init' first.", fg="red")
        return
    
    click.secho(f"Building site using {config}...", fg="cyan")
    builder = Builder(config, site_dir)
    builder.build()
    click.secho(f"Successfully built site to '{site_dir}'.", fg="green", bold=True)

@main.command()
@click.option('--config', default='smartgen.yml', help='Path to config file.')
@click.option('--port', default=8000, help='Port to serve on.')
def serve(config, port):
    """Start the development server with live reload."""
    if not os.path.exists(config):
        click.secho(f"Error: Config file '{config}' not found. Run 'smartgen-docs init' first.", fg="red")
        return
    
    click.secho(f"Starting dev server on http://localhost:{port}...", fg="cyan")
    server = DevServer(config, port)
    server.run()

@main.command()
@click.option('--port', default=8001, help='Port to serve the upload manager on.')
def upload_manager(port):
    """Start the web-based upload and management interface."""
    click.secho(f"Starting upload manager on http://localhost:{port}", fg="cyan")
    click.echo("Open your browser to manage and upload documentation files.")
    try:
        from .upload_server import app
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=port)
    except ImportError:
        click.secho("Error: FastAPI is not installed. Install it with: pip install fastapi uvicorn", fg="red")

@main.command()
@click.argument('module_name')
@click.option('--output', default='docs/api', help='Directory to save API docs.')
def autodoc(module_name, output):
    """Generate API reference from Python module."""
    click.secho(f"Generating API reference for {module_name}...", fg="cyan")
    generator = AutodocGenerator(output)
    generator.generate_for_module(module_name)
    click.secho("API documentation generated successfully.", fg="green")

@main.command()
def init():
    """Initialize a new SmartGen Docs project."""
    if os.path.exists('smartgen.yml'):
        click.secho("Error: smartgen.yml already exists in this directory.", fg="red")
        return
    
    # Create the premium boilerplate config
    config_content = """# SmartGen Docs Configuration
site_name: My SmartGen Docs
site_url: https://www.smartgentools.com
site_author: Sayad Md Bayezid Hosan

theme:
  name: premium
  palette:
    primary: "#0052cc"
    accent: "#ff9900"

nav:
  - Home: index.md
  - Getting Started:
      - Welcome: getting-started/index.md
"""
    with open('smartgen.yml', 'w') as f:
        f.write(config_content)
    
    # Scaffold directories
    os.makedirs('docs/getting-started', exist_ok=True)
    
    # Create default markdown files
    with open('docs/index.md', 'w') as f:
        f.write("# Welcome to SmartGen Docs\n\nThis site was built with **SmartGen Docs** by Sayad Md Bayezid Hosan.\n\nEdit this file in `docs/index.md` to get started.\n")
        
    with open('docs/getting-started/index.md', 'w') as f:
        f.write("# Getting Started\n\nWelcome to your new documentation project. Run `smartgen-docs serve` to see your changes live!\n")
    
    click.secho("Project initialized successfully!", fg="green", bold=True)
    click.echo("Run ", nl=False)
    click.secho("smartgen-docs serve", fg="cyan", bold=True, nl=False)
    click.echo(" to see it in action.")

if __name__ == "__main__":
    main()