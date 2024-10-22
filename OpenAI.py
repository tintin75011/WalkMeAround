import os
import re
from openai import OpenAI

class OpenAI_request:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        

    def ask_chatgpt(self, places, types):
        # Extraire uniquement les noms des lieux
        place_names_with_coords = [
            f"{place.get('name', 'N/A')} (lat: {place['geometry']['location']['lat']}, lng: {place['geometry']['location']['lng']})" 
            for place in places
        ]

        only_one_types = ['restaurant','hotel'] #types que l'on ne veut pas voir plusieurs fois dans le parcours
        multiples_types = ['jardin'] #types que l'on peut visiter plusieurs fois
        prompt =(f"Je veux prévoir un parcours pour découvrir la ville où je me trouve. Voici une liste de lieux que je peux visiter : {', '.join(place_names_with_coords)}."
                f" Fais moi une sélection, pour que je visite au mieux la ville. Assure-toi que dans la liste que tu me fournis il n'y ait qu'un seul lieu de ces types : {only_one_types}."
                f"Cependant tu peux mettre plusieurs lieux de ce type : {multiples_types}."
                f"Egalement, j'aimerai qu'il y ai au moins un élément de chacun de ces types : {types}."
                f"Dernier point: Je veux que tu me génère une liste sous le format suivant :'nom du lieux','longitude','latidude'. je veux impérativement des simple côtes comme ceci : ''")

        try:
            response = self.client.chat.completions.create(model="gpt-4",
                                                        messages=[{"role": "user", "content": prompt}],
                                                        max_tokens=500,
                                                        temperature=0.7)

            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Erreur : {e}"
       
    def extract_data_from_response(self, response):
        matches = []
        pattern = r'\'(.*?)\', \'(.*?)\', \'(.*?)\''

        # Extraire les informations (nom, latitude, longitude)
        matches = re.findall(pattern, response)
        return matches


