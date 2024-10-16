### Prérequis

- Python 3.8+
- [Hugging Face API](https://huggingface.co/) (pour les LLM)
- Google Maps API (pour la génération des itinéraires)

### Étapes d'installation

1. **Cloner le dépôt Git** :

    ```bash
    git clone https://github.com/tintin75011/walkmearound.git
    cd walkmearound
    ```

2. **Créer un environnement virtuel** :

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez venv\Scripts\activate
    ```

3. **Installer les dépendances** :

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurer les API Keys** :

   Pour fonctionner, le script nécessite une clé API. Vérifiez que vous avez bien une clé API définie dans vos variables d'environnement.
    
5. **Lancer l'application** :

    ```bash
    python maps_path_generator.py
    ```
### Erreurs rencontrées : 
1. **import openai**
     [OpenAI Python Discussion](https://github.com/openai/openai-python/discussions/742)




### Prerequisites

- Python 3.8+
- [Hugging Face API](https://huggingface.co/) (for LLMs)
- Google Maps API (for route generation)

### Installation Steps

1. **Clone the Git repository**:

    ```bash
    git clone https://github.com/tintin75011/walkmearound.git
    cd walkmearound
    ```

2. **Create a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the API Keys**:

   To function properly, the script requires an API key. Make sure you have defined an API key in your environment variables.
    
5. **Run the application**:

    ```bash
    python maps_path_generator.py
    ```

### Errors Encountered:
1. **import openai**  
   [OpenAI Python Discussion](https://github.com/openai/openai-python/discussions/742)


