from setuptools import setup, find_packages

# Function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name='mvdiffusion',
    version='0.1.0',
    description='',
    url='https://github.com/Mirage-AI/mvdiffusion',  # Update with your project's URL
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    python_requires='>=3.6',
)