from setuptools import setup, find_packages

setup(
    name= "openalex_matching",  
    version = "0.1",  
    author="Bryan Yuk", 
    author_email= "dzg5cg@virginia.edu",  
    description="A Python package for matching people with their OpenAlex ID using OpenAlex data",  
    long_description= open('README.md').read(),  # Long description (usually from README)
    long_description_content_type='text/markdown',  # Format of the long description (Markdown)
    url="https://github.com/byuk729/openalex_matching",  # URL of your project (GitHub, etc.)
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