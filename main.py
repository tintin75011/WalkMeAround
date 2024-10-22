
from Maps import Maps
from OpenAI import OpenAI_request


#définition des envie de l'utilsiateur
latitude = 48.8566
longitude = 2.3522
radius = 1500
desired_time = 120
position = [latitude,longitude]
is_loop = False # booléen pour déterminer si l'utilisateur veut faire une boucle # True si on veut revenir au point de départ, False sinon
types = ['restaurant','park','clothing_store','book_store']

#####################################
#### ECHANGE AVEC MAPS    ###########
#####################################
maps = Maps() # Déclaration d'un object pour gérer les échanges avec maps
places = maps.get_places_list(position,types,radius) # réccupération de tous les lieux

#####################################
#### ECHANGE AVEC OPEN AI ###########
#####################################
openAI = OpenAI_request()# Déclaration d'un object pour gérer les échanges avec gpt4
response = openAI.ask_chatgpt(places,types) # envoie de la requête à gpt4 pour qu'il fasse la sélection dans la liste
final_places_list = openAI.extract_data_from_response(response) #extraction des donnée de la réponse de gpt4 à partir d'un aptern défini
print(final_places_list) # affichage de la liste finale

#####################################
#### GENERATION DU PATH   ###########
#####################################
route_legs = maps.get_optimized_route(position, final_places_list,is_loop,desired_time)
maps.print_route(route_legs)
maps.open_google_maps(route_legs, is_loop)