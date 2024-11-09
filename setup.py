from setuptools import setup, find_packages

setup(
    name= "openalex_matching",  
    version = "0.1",  
    author="Your Name",  # Your name or organization
    author_email="your.email@example.com",  # Your email address
    description="A Python package for matching people using OpenAlex data",  # Short description of your package
    long_description= open('README.md').read(),  # Long description (usually from README)
    long_description_content_type='text/markdown',  # Format of the long description (Markdown)
    url="https://github.com/yourusername/openalex-matching",  # URL of your project (GitHub, etc.)
    packages=find_packages(),  # Automatically find all packages in your directory
    install_requires=[
        "requests",  # List of dependencies
        "pandas",
        "tqdm",
        "seaborn",
        "matplotlib",
        "fuzzywuzzy",
        "nicknames"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",  # Supported Python versions
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)