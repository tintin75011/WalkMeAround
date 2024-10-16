
import webbrowser

class Maps_path_generator:
    def __init__(self) -> None:
        # Rien à initialiser pour l'instant dans ce constructeur
        pass

    # Créer l'URL pour l'itinéraire Google Maps
    def create_google_maps_url(self, lieux):
        if len(lieux) < 2:
            return "Il faut au moins un point de départ et un point d'arrivée."
        
        # Récupérer le point de départ
        origin = f"{lieux[0]['latitude']},{lieux[0]['longitude']}"
        
        # Récupérer le point d'arrivée (dernier lieu)
        destination = f"{lieux[-1]['latitude']},{lieux[-1]['longitude']}"
        
        # Ajouter les points intermédiaires s'il y en a
        if len(lieux) > 2:
            waypoints = "|".join([f"{lieu['latitude']},{lieu['longitude']}" for lieu in lieux[1:-1]])
        else:
            waypoints = ""
        
        # Construire l'URL
        url = f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}"
        
        if waypoints:
            url += f"&waypoints={waypoints}"
        
        return url


    def open_url(self,maps_url):
        
        # Afficher l'URL
        print("Itinéraire Google Maps :", maps_url)

        # Ouvrir l'URL dans le navigateur par défaut
        webbrowser.open(maps_url)