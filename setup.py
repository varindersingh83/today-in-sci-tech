from setuptools import setup, find_packages

setup(
    name="today-in-sci-tech",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "feedparser>=6.0.11",
        "openai>=1.0.0",
        "python-dotenv>=1.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "black>=24.0.0",
            "isort>=5.0.0",
            "flake8>=7.0.0",
        ]
    },
    python_requires=">=3.8",
    author="Your Name",
    author_email="your.email@example.com",
    description="An automated tool that generates engaging Twitter threads about the latest AI research papers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/today-in-sci-tech",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
) 