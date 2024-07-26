from setuptools import setup, find_packages

# Function to read the requirements.txt file
def parse_requirements(filename):
    requirements = []
    dependency_links = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('--'):
                dependency_links.append(line)
            else:
                requirements.append(line)
    return requirements, dependency_links

requirements, dependency_links = parse_requirements('requirements.txt')

setup(
    name='mvdiffusion',
    version='0.1.0',
    description='',
    url='https://github.com/Mirage-AI/mvdiffusion',
    packages=find_packages(),
    install_requires=requirements,
    dependency_links=dependency_links,
    python_requires='>=3.6',
)