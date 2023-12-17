# Guide d'installation et d'utilisation du projet

Ce document explique les étapes nécessaires pour installer les bibliothèques **PlantUML** et **Six**. De plus, il fournit des instructions pour exécuter le projet qui nécessite la version **Python 3.11** ainsi que des fichiers `.txt` dans le dossier `memory`.

## Installation des bibliothèques

Avant de pouvoir utiliser ce projet, vous devez installer les bibliothèques suivantes:

- **PlantUML**: executez la commande suivante:

```
pip3 install plantuml
```

- **Six**: executez la commande suivante:

```
pip3 install six
```

## Utilisation du projet

1. Assurez-vous d'avoir installé Python 3.11 sur votre machine.

2. Placez les fichiers `.txt` requis dans le dossier `memory`.

3. Exécutez le script principal en utilisant la commande suivante:

```
python3 plantumlprinter.py
```

Le script générera des images à partir des fichiers `.txt` du dossier `memory` en utilisant le serveur PlantUML.
Les fichiers de sortie seront sauvegardés dans le répertoire actuel.

4. Après l'exécution du script, vous verrez les résultats affichés à l'écran.
   Les fichiers générés avec succès seront affichés en vert,
   tandis que ceux qui ont échoué seront affichés en rouge.

Il est important de noter que ce projet utilise les bibliothèques **PlantUML** et **Six** pour le traitement des fichiers. 
Assurez-vous de les avoir installées correctement avant d'exécuter le projet.

Veuillez également vous assurer d'avoir les fichiers `.txt` requis dans le dossier `memory` pour que le projet fonctionne correctement.

Bon usage du projet !
