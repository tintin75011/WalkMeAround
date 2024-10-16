from openai import OpenAI
import re
import os




from maps_path_generator import Maps_path_generator

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

my_maps_path_generator = Maps_path_generator() 


def ask_chatgpt(user_lat, user_lon, max_distance_km, available_time_hours):
    prompt = (f"Je suis à la position latitude {user_lat} et longitude {user_lon}. "
              f"Je souhaite marcher maximum {max_distance_km} km "
              f"et j'ai seulement {available_time_hours} heures disponibles. "
              f"génère moi un parcours composé d'une liste de lieu à visiter autour de moi. Je veux que ca fasse une boucle. Le parcours total doit faire moins de {max_distance_km}"
              f"et me ramener à mon point de départ. Le temps total ne doit pas dépasser {available_time_hours}, penses à prendre en compte le temps des activités si tu m'en propose(par exemple les musées prennent beaucoup de temps)"
              f"génère moi la liste sous la forme 'nom du lieu','latitude du lieu','longitude du lieu'.Le temps total ne doit pas dépasser {available_time_hours}! c'est important")



    try:
        response = client.chat.completions.create(model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7)

        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erreur : {e}"



# Exemple d'utilisation
user_latitude = 46.1591
user_longitude = -1.1511
max_distance = 10
available_time = 2
matches = []
while not matches:
    response = ask_chatgpt(user_latitude, user_longitude, max_distance, available_time)
    print("Réponse de ChatGPT :\n", response)
    # Expression régulière pour extraire les données
    pattern = r'\'(.*?)\', \'(.*?)\', \'(.*?)\''

    # Extraire les informations (nom, latitude, longitude)
    matches = re.findall(pattern, response)
print(matches)
# Stocker les informations dans un dictionnaire
lieux = []
for match in matches:
    lieux.append({
        "nom": match[0],
        "latitude": float(match[1]),
        "longitude": float(match[2])
    })

# Afficher le dictionnaire
for lieu in lieux:
    print(lieu)


maps_url = my_maps_path_generator.create_google_maps_url(lieux)
# Afficher l'URL
print("Itinéraire Google Maps :", maps_url)

# Ouvrir l'URL dans le navigateur par défaut
my_maps_path_generator.open_url(maps_url)