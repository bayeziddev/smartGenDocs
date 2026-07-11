import click
import os
from .core import Builder
from .server import DevServer

@click.group()
def main():
    """SmartGen Docs - A unique documentation platform by Sayad Md Bayezid Hosan."""
    pass

@main.command()
@click.option('--config', default='smartgen.yml', help='Path to config file.')
@click.option('--site-dir', default='site', help='Directory to output the built site.')
def build(config, site_dir):
    """Build the documentation site."""
    if not os.path.exists(config):
        click.echo(f"Error: Config file '{config}' not found.")
        return
    
    click.echo(f"Building site using {config}...")
    builder = Builder(config, site_dir)
    builder.build()
    click.echo(f"Successfully built site to '{site_dir}'.")

@main.command()
@click.option('--config', default='smartgen.yml', help='Path to config file.')
@click.option('--port', default=8000, help='Port to serve on.')
def serve(config, port):
    """Start the development server with live reload."""
    if not os.path.exists(config):
        click.echo(f"Error: Config file '{config}' not found.")
        return
    
    click.echo(f"Starting dev server on http://localhost:{port}...")
    server = DevServer(config, port)
    server.run()

@main.command()
def init():
    """Initialize a new SmartGen Docs project."""
    if os.path.exists('smartgen.yml'):
        click.echo("Error: smartgen.yml already exists.")
        return
    
    with open('smartgen.yml', 'w') as f:
        f.write("site_name: My SmartGen Docs\n")
        f.write("site_url: https://www.smartgentools.com\n")
        f.write("site_author: Sayad Md Bayezid Hosan\n")
        f.write("nav:\n")
        f.write("  - Home: index.md\n")
    
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.md', 'w') as f:
        f.write("# Welcome to SmartGen Docs\n\n")
        f.write("This site was built with SmartGen Docs by Sayad Md Bayezid Hosan.\n")
    
    click.echo("Project initialized. Run 'smartgen-docs serve' to see it in action.")

if __name__ == "__main__":
    main()
