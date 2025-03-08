from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="error-message-translator",
    version="0.1.0",
    author="chrisdvz.io",
    author_email="csoukoulis.tech@gmail.com",
    description="A web application that translates cryptic error messages into beginner-friendly explanations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrissouk-001/error-message-translator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Debuggers",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Flask>=2.0.0",
        "Werkzeug>=2.0.0",
        "Jinja2>=3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "error-translator=app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
) 