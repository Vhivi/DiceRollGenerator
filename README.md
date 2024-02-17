--------------------------------
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
--------------------------------

# FR - Modèle de projet Python

## Description
Le but de ce projet est de créer un modèle à appliquer à chaque nouveau projet
Python. N'étant pas très régulier dans ma programmation, il s'agit d'un loisir,
je me retrouve souvent à chercher comment j'avais fait pour tel ou tel projet.
D'où l'idée de créer un modèle de projet Python qui me permettrait de gagner du
temps et de ne pas avoir à réinventer la roue à chaque fois.

On y trouvera la base, c'est-à-dire un fichier README.md pour la description,
un fichier .gitignore car je travaille avec un environnement virtuel pour
essayer de cloisonner mes projets proprements, un fichier requirements.txt pour
les librairies utilisées et l'installation de ces dernières, un fichier main.py
pré-rempli pour débuter rapidement (enfin j'espère :)).

## Comment l'utiliser
Le projet a été développé avec Python 3.10.11 sous Windows 10 et dispose des
libraires Black (https://github.com/psf/black), isort
(https://github.com/pycqa/isort/) et flake8 (https://github.com/PyCQA/flake8).
Vous pouvez les installer grâce au fichier requirements.txt.
Au moment de la création de ce projet, je teste ces librairies pour voir leur
utilité dans mon processus de développement. Ils font peut-être doublons dans
leur usage mais je verrais ça au fil du temps.

:warning: Quand le projet est cloné, pensez à lancer le setup.bat et à créer immédiatement
un environnement virtuel pour ne pas polluer votre installation de Python (Cette
partie est en cours de développement). :warning:

### Lancement du setup.bat

Pour cela, sous Visual Studio Code, vous pouvez ouvrir un terminal et taper la
commande suivante :
```
.\setup.bat
```

### Documentation de setup.bat

Le fichier setup.bat de préparer votre dossier en supprimant le dossier caché
.git et en lançant la création de l'environnement virtuel et l'installation des
librairies contenues dans le fichier requirements.txt.

### Installation manuelle

Si vous ne souhaitez pas utiliser le setup.bat, vous pouvez créer manuellement
votre environnement virtuel et installer les librairies. Pensez à renommer le
dossier. Puis supprimer le dossier caché .git. Enfin lancer la création de
l'environnement virtuel comme indiqué ci-dessous. Puis installer les librairies.

#### Création de l'environnement virtuel

Pour cela, sous Visual Studio Code, vous pouvez ouvrir un terminal et taper la
commande suivante :
```
python -m venv <nom de l'environnement virtuel>
```

Ensuite, vous pouvez activer l'environnement virtuel avec la commande : 
```
<nom de l'environnement virtuel>\Scripts\activate
```

#### Installation des librairies

Vous pouvez installer les librairies avec la commande : 
```
pip install -r requirements.txt
```

## Remerciements


# EN - Python Project Template

## Description

The aim of this project is to create a template to be applied to each new Python
project. As I don't do my programming very regularly - it's a hobby - I often
find myself looking up how I did it for this or that project.
Hence the idea of creating a Python project template that would save me time
and mean I wouldn't have to reinvent the wheel every time.

It will contain the basics, i.e. a README.md file for the description, a
.gitignore file because I work with a virtual environment to try to partition
my projects properly, a requirements.txt file for the libraries used and their
installation, and a pre-filled main.py file to get started quickly (I hope :)).

## How to use it
The project was developed with Python 3.10.11 on Windows 10 and includes the
Black (https://github.com/psf/black), isort (https://github.com/pycqa/isort/)
and flake8 (https://github.com/PyCQA/flake8) libraries.
You can install them using the requirements.txt file. At the time of creating
this project, I'm testing these libraries to see how useful they are in my
development process. They may duplicate each other in their use but I'll see as
time goes by.

:warning: When the project is cloned, remember to run setup.bat and immediately create a
virtual environment so as not to pollute your Python installation (this part is
under development). :warning:

### Launching setup.bat

To do this in Visual Studio Code, you can open a terminal and type the following
command:
```
.\setup.bat
```

### Documentation for setup.bat

The setup.bat file prepares your folder by deleting the hidden .git folder and
launching the creation of the virtual environment and the installation of the
libraries contained in the requirements.txt file.

### Manual installation

If you don't want to use setup.bat, you can manually create your virtual
environment and install the libraries. Remember to rename the folder.
Then delete the hidden .git folder. Finally, create the virtual environment as
shown below. Then install the libraries.

#### Creating the virtual environment

To do this in Visual Studio Code, you can open a terminal and type the following
command:
```
python -m venv <virtual environment name>
```

Next, you can activate the virtual environment with the command: 
```
<virtual environment name>\Scripts\activate
```

#### Installing libraries

You can install the libraries with the command : 
```
pip install -r requirements.txt
```

## Acknowledgements
