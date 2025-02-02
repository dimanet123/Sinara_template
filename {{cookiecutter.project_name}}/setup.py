from setuptools import setup, find_packages
import os

# 📌 Получаем версию пакета из `__init__.py`
def get_version():
    version = {}
    with open(os.path.join("src", "{{cookiecutter.project_name}}", "__init__.py")) as f:
        exec(f.read(), version)
    return version["__version__"]

setup(
    name="{{cookiecutter.project_name}}",  # Имя пакета
    version=get_version(),  # Версия пакета
    author="{{cookiecutter.author_name}}",
    author_email="your_email@example.com",
    description="Описание вашего проекта",
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "numpy",  # Добавляй сюда нужные зависимости
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

