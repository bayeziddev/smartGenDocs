import os
import yaml
import subprocess
import shutil

def build_all():
    config_path = 'smartgen.yml'
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    themes = ['default', 'book', 'education', 'techblog', 'agency', 'medicine', 'apiplay']
    
    # Ensure site directory is clean
    if os.path.exists('site'):
        shutil.rmtree('site')
    os.makedirs('site')

    # Build all themes into temporary directories first
    temp_build_dir = 'temp_build'
    if os.path.exists(temp_build_dir):
        shutil.rmtree(temp_build_dir)
    os.makedirs(temp_build_dir)

    for theme in themes:
        print(f"--- Building theme variant: {theme} ---")
        temp_config = config.copy()
        temp_config['theme'] = temp_config.get('theme', {}).copy()
        temp_config['theme']['name'] = theme
        
        temp_config_path = f'smartgen_{theme}.yml'
        with open(temp_config_path, 'w') as f:
            yaml.dump(temp_config, f)
        
        out_dir = os.path.join(temp_build_dir, theme)
        subprocess.run(['smartgen-docs', 'build', '--config', temp_config_path, '--site-dir', out_dir], check=True)
        os.remove(temp_config_path)

    # Now build the main site (root)
    print("--- Building main site to root ---")
    subprocess.run(['smartgen-docs', 'build', '--config', config_path, '--site-dir', 'site'], check=True)

    # Move all theme variants into site/styles/
    styles_dir = os.path.join('site', 'styles')
    os.makedirs(styles_dir, exist_ok=True)
    
    for theme in themes:
        src = os.path.join(temp_build_dir, theme)
        dst = os.path.join(styles_dir, theme)
        shutil.move(src, dst)
    
    # Cleanup
    shutil.rmtree(temp_build_dir)
    
    # Ensure .nojekyll is in the root
    with open('site/.nojekyll', 'w') as f:
        pass

if __name__ == '__main__':
    build_all()
