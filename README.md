## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Serveur arrêté, taper la commande `python manage.py createsuperuser` puis saisissez les informations requises
- Relancez le serveur puis aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur le compte créé ci-dessus

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Afin que le travail de développement de l'application n'impact pas la production,
seul les commit sur la branche "master" ne doivent déclencher un deploiement. 

Par conséquent il est important que **chaque modification** apportée à l'application (résolution 
d'issue, mise en place de nouvelle feature, etc...) donne lieu à la **création d'une branche dédiée**
et toujours créée à **partir de la branche master**

### Pipeline CI/CD

####Prérequis

Afin que les action s'execute, le repository doit contenir les secrets suivants :

- "SECRET_KEY" : clé du server django
- "DOCKER_USERNAME" : username du compte DockerHub
- "DOCKER_PASSWORD" : password du compte DockerHub
- "AWS_ACCESS_KEY_ID" : id user du compte AWS
- "AWS_SECRET_ACCESS_KEY" : clé d'accès AWS
- "DOT_ENV" : les variables d'environnement de production du server django

#### Workflow

Deux script distincts ont donc été écrit dans le workflow:

- Cette action permet un retour immédiat sur la **qualité du code** implémenté
et atteste qu'**aucune dégradation n'est à noté sur l'existant**.

  - ci_others(Pour tout autres branche que master):
    - charge l'environnement python 
    - installe les dépendances via `requirements.txt`
    - lance le **linting**
    - lance les test **pytest**



- Une fois assuré que **le code de la branche fonctionne parfaitement**, il ne restera plus qu'a **merger** votre branch **dans la branche master** pour declencher la **dockerisation** ainsi que le **deploiement**
  - ci_cd_master(uniquement au commit sur master):
    - charge l'environnement python 
    - installe les dépendances via `requirements.txt`
    - lance le **linting**
    - lance les test **pytest**
    - lance le build de l'image docker et la push sur DockerHub
      - cette action créer une image docker nommée master-<_numéro_du_commit_git_> et la dépose sur le repository dockerhub : https://hub.docker.com/r/sylvaingauthier2pro/p13_python-oc-lettings-fr
    - lance le déploiement de l'image docker sur AWS

