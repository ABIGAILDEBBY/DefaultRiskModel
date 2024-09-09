import nbformat
import re


def extract_imports(notebook_path):
    with open(notebook_path, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    imports = set()
    for cell in nb.cells:
        if cell.cell_type == 'code':
            lines = cell.source.split('\n')
            for line in lines:
                if line.startswith('import ') or line.startswith('from '):
                    match = re.match(r'(?:import (\S+)|from (\S+))', line)
                    if match:
                        libraries = match.groups()
                        libraries = [lib.split('.')[0] for lib in libraries if lib]
                        imports.update(libraries)

    return imports


def write_requirements(libraries, output_path):
    with open(output_path, 'w') as f:
        for lib in sorted(libraries):
            f.write(f"{lib}\n")


# Adjust the path to your notebook
notebook_path = './loan-dafaulter.ipynb'
requirements_path = 'requirements.txt'

libraries = extract_imports(notebook_path)
write_requirements(libraries, requirements_path)
