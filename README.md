# WalkMeAround

WalkMeAround est une application mobile qui génère des itinéraires optimisés en fonction de la position actuelle de l'utilisateur, de son temps disponible et de ses préférences (par exemple, visiter des musées, manger dans des restaurants, etc.). L'application utilise les API Google Maps et OpenAI GPT-4 pour recommander des lieux à visiter et créer des parcours adaptés.

## Fonctionnalités

- **Génération d'itinéraire personnalisé :** Créez un parcours en fonction de votre position actuelle, votre temps disponible, et vos envies.
- **Préférences de l'utilisateur :** Sélectionnez vos préférences (ex : visiter un musée, prendre un verre) pour un parcours sur mesure.
- **Optimisation des trajets :** Utilisation des API Google Maps pour optimiser les itinéraires, en prenant en compte les contraintes de temps.
- **Boucle :** Option permettant de créer un parcours en boucle où le point de départ et d'arrivée sont les mêmes.

## Technologies utilisées

- **Google Maps API :** Pour récupérer les lieux d'intérêt et optimiser les itinéraires.
- **OpenAI GPT-4 :** Pour générer des suggestions de lieux à visiter en fonction des préférences de l'utilisateur.
- **Python :** Utilisé pour certaines parties du traitement backend.
  
## Installation

1. Clonez le dépôt GitHub :
    ```bash
    git clone https://github.com/tintin75011/WalkMeAround.git
    ```
2. Accédez au répertoire du projet :
    ```bash
    cd WalkMeAround
    ```
3. Installez les dépendances Python à l'aide de `requirements.txt` :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

1. **Lancez l'application Android :** Utilisez Android Studio pour compiler et lancer l'application sur un appareil ou un émulateur.
2. **Configurer les API :** Assurez-vous d'avoir configuré les clés API pour Google Maps et OpenAI dans votre fichier `config` avant de démarrer.
3. **Créer un parcours :** Après avoir défini vos préférences, appuyez sur "Générer un itinéraire" pour obtenir une suggestion optimisée en fonction de vos choix.

## Fichiers importants

- **`main.py`** : Le fichier principal pour l'initialisation du backend.
- **`Maps.py`** : Contient les fonctions de gestion des API Google Maps.
- **`OpenAI.py`** : Gère les interactions avec l'API OpenAI GPT-4.
- **`requirements.txt`** : Liste des dépendances Python nécessaires pour le projet.

## Clés API

Assurez-vous d'avoir les clés API pour :

- **Google Maps API**
- **OpenAI GPT-4 API**

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre une Pull Request ou ouvrir une issue pour discuter de vos changements avant de soumettre une PR.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
