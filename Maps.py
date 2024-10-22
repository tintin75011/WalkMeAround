import requests
import os
import webbrowser

class Maps:
    def __init__(self) -> None:
        self.API_KEY = os.getenv('GOOGLE_API_KEY')

    def get_places_list(self,position,types, radius):
        latitude = position[0]
        longitude = position[1]
        results = []
        for place_type in types:
            url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&type={place_type}&key={self.API_KEY}"
            response = requests.get(url)
            data = response.json()
            
            # Vérifier si des résultats sont renvoyés
            if 'results' in data:
                results.extend(data['results'])
        return results

    def print_places_data(self,res):
        # Afficher des informations détaillées pour chaque lieu
        for place in res:
            name = place.get('name', 'N/A')
            

            # Récupérer les types (c'est une liste, on peut les joindre par une virgule)
            place_types = ", ".join(place.get('types', []))
            
            print(f"Nom: {name}")
            print(f"Types: {place_types}")  # Afficher les types ici
            print("-" * 40)

    def get_optimized_route(self, origin, final_places_list, is_loop, desired_time):
        # Définir l'origine comme point de départ
        start_lat, start_lng = origin[0], origin[1]

        if is_loop:
            destination_lat, destination_lng = start_lat, start_lng
        else:
            destination_lat, destination_lng = final_places_list[-1][2], final_places_list[-1][1]  # Dernier lieu de la liste comme destination

        # Lieux intermédiaires (waypoints)
        waypoints = final_places_list[1:-1] if not is_loop else final_places_list

        # Calculer le temps total actuel
        total_time = self.get_travel_time(waypoints)
        
        # Ajuster les waypoints si le temps total dépasse le temps souhaité
        while waypoints and total_time > desired_time:
            waypoints.pop()  # Retire le dernier waypoint
            total_time = self.get_travel_time(waypoints)

        # Ajouter des lieux supplémentaires si le temps total est trop court
        while total_time < desired_time:
            additional_places = self.get_additional_places(origin, ['restaurant', 'park', 'clothing_store', 'book_store'], 1500)
            
            if additional_places:  # Si des lieux supplémentaires sont disponibles
                for place in additional_places:
                    # Ajouter le lieu et recalculer le temps total
                    waypoints.append((place['name'], place['geometry']['location']['lng'], place['geometry']['location']['lat']))
                    total_time = self.get_travel_time(waypoints)
                    
                    # Vérifier si le temps total a atteint le temps désiré
                    if total_time >= desired_time:
                        break
            else:
                print("Aucun lieu supplémentaire trouvé.")
                break

        # Générer la chaîne de waypoints pour l'URL
        waypoints_str = '|'.join([f"{place[2]},{place[1]}" for place in waypoints])

        # Construire l'URL de la requête à l'API Directions
        url = (
            f"https://maps.googleapis.com/maps/api/directions/json?"
            f"origin={start_lat},{start_lng}&"
            f"destination={destination_lat},{destination_lng}&"
            f"waypoints=optimize:true|{waypoints_str}&"
            f"mode=walking&" 
            f"key={self.API_KEY}"
        )

        # Faire la requête HTTP à l'API Directions
        response = requests.get(url)
        data = response.json()

        # Vérification de la validité de la réponse
        if 'routes' in data and len(data['routes']) > 0:
            route = data['routes'][0]
            return route['legs']
        else:
            print("Erreur dans la récupération de l'itinéraire.")
            return None

    def print_route(self, route_legs):
        if route_legs:
            for leg in route_legs:
                print(f"De {leg['start_address']} à {leg['end_address']}")
                print(f"Distance : {leg['distance']['text']}, Durée : {leg['duration']['text']}")
                print("-" * 40)
        else:
            print("Pas d'itinéraire trouvé.")

    def get_travel_time(self, waypoints):
        total_time = 0
        origin = waypoints[0]

        for i in range(1, len(waypoints)):
            destination = waypoints[i]
            url = (
                f"https://maps.googleapis.com/maps/api/directions/json?"
                f"origin={origin[2]},{origin[1]}&"
                f"destination={destination[2]},{destination[1]}&"
                f"mode=walking&" 
                f"key={self.API_KEY}"
            )

            response = requests.get(url)
            data = response.json()

            # Vérification de la validité de la réponse
            if 'routes' in data and len(data['routes']) > 0:
                leg = data['routes'][0]['legs'][0]
                total_time += leg['duration']['value']  # Temps en secondes
                origin = destination  # Mettre à jour l'origine pour le prochain trajet
            else:
                print(f"Erreur dans la récupération du temps entre {origin[0]} et {destination[0]}.")
                return None

        return total_time / 60  # Retourne le temps total en minutes
    
    def get_additional_places(self, position, types, radius):
        # Récupérer des lieux supplémentaires
        additional_places = self.get_places_list(position, types, radius)
        return additional_places


    def open_google_maps(self,route_legs, is_loop=False):
        # Commencer à construire l'URL
        base_url = "https://www.google.com/maps/dir/?api=1"

        # Ajouter le point de départ
        origin = f"{route_legs[0]['start_location']['lat']},{route_legs[0]['start_location']['lng']}"
        
        # Ajouter les waypoints
        waypoints = []
        for leg in route_legs:
            for step in leg['steps']:
                waypoints.append(f"{step['end_location']['lat']},{step['end_location']['lng']}")
        
        waypoints_str = '|'.join(waypoints)

        # Ajouter la destination
        destination = f"{route_legs[-1]['end_location']['lat']},{route_legs[-1]['end_location']['lng']}"

        # Ajouter les paramètres à l'URL
        url = f"{base_url}&origin={origin}&destination={destination}&waypoints={waypoints_str}&optimize=true"

        # Si is_loop est True, on ajoute le point de départ comme destination finale
        if is_loop:
            url += f"&destination={origin}"

        # Ouvrir l'URL dans le navigateur
        webbrowser.open(url)
                
