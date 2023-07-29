from aifc import Error
import random
from random import randint
from django.utils import timezone

from datetime import timedelta, datetime


from AppliDjango.models import Clients,Operateur,TypeChambre,Ville,Aeroport,Compagnie,Vol,Escales,MarqueVoiture,ModeleVoiture,Hotel,Chambres


# # list_aeroport=['Aeroport de Cap Skirring','Aeroport international Léopold-Sédar-Senghor',
# #         'Aéroport international Blaise-Diagne','Aéroport de Ziguinchor',
# #         'Aérodrome de Tambacounda','Aéroport de Saint-Louis',"Aéroport de Paris-Charles-de-Gaulle (CDG)",
# #         "Aéroport de Paris-Orly (ORY)",
# #         "Aéroport de Paris-Le Bourget (LBG)",
# #         "Aéroport de Paris-Vatry (XCR)",
# #         "Aéroport de Paris-Beauvais-Tillé (BVA)",
# #         "Aéroport de Paris-Chalons-Vatry (XCR)",
# #         "Aéroport de Paris-Creil (CSF)",
# #         "Aéroport de Paris-Pontoise-Cormeilles-en-Vexin (POX)",
# #         "Aéroport de Paris-Vélizy-Villacoublay (VIY)",
# #         "Aéroport de Paris-La Défense Heliport (JPU)",
# #         "Aéroport de Marseille-Provence (MRS)",
# #         "Aéroport de Nice-Côte d'Azur (NCE)",
# #         "Aéroport de Lyon-Saint-Exupéry (LYS)",
# #         "Aéroport de Toulouse-Blagnac (TLS)",
# #         "Aéroport de Bordeaux-Mérignac (BOD)",
# #         "Aéroport de Nantes-Atlantique (NTE)",
# #         "Aéroport de Strasbourg-Entzheim (SXB)",
# #         "Aéroport de Lille-Lesquin (LIL)",
# #         "Aéroport de Bâle-Mulhouse-Fribourg (MLH)",
# #         "Aéroport de Rennes-Bretagne (RNS)",
# #         "Aéroport de Montpellier-Méditerranée (MPL)",
# #         "Aéroport international Hartsfield-Jackson d'Atlanta (ATL)",
# #         "Aéroport international de Los Angeles (LAX)",
# #         "Aéroport international de Chicago O'Hare (ORD)",
# #         "Aéroport international de Dallas/Fort Worth (DFW)",
# #         "Aéroport international de Denver (DEN)",
# #         "Aéroport international John F. Kennedy de New York (JFK)",
# #         "Aéroport international de San Francisco (SFO)",
# #         "Aéroport international de Seattle-Tacoma (SEA)",
# #         "Aéroport international de Miami (MIA)",
# #         "Aéroport international de Las Vegas-McCarran (LAS)",
# #         "Aéroport de Londres Heathrow (LHR)",
# #         "Aéroport de Londres Gatwick (LGW)",
# #         "Aéroport de Londres Stansted (STN)",
# #         "Aéroport de Manchester (MAN)",
# #         "Aéroport de Birmingham (BHX)",
# #         "Aéroport de Glasgow (GLA)",
# #         "Aéroport de Édimbourg (EDI)",
# #         "Aéroport de Bristol (BRS)",
# #         "Aéroport de Liverpool John Lennon (LPL)",
# #         "Aéroport de Belfast International (BFS)",
# #         "Aéroport de Francfort (FRA)",
# #         "Aéroport de Munich (MUC)",
# #         "Aéroport de Berlin-Tegel (TXL)",
# #         "Aéroport de Berlin-Schönefeld (SXF)",
# #         "Aéroport de Hambourg (HAM)",
# #         "Aéroport de Düsseldorf (DUS)",
# #         "Aéroport de Cologne-Bonn (CGN)",
# #         "Aéroport de Stuttgart (STR)",
# #         "Aéroport de Hanovre (HAJ)",
# #         "Aéroport de Nuremberg (NUE)",
# #         "Aéroport international de Pékin (PEK)",
# #         "Aéroport international de Shanghai-Pudong (PVG)",
# #         "Aéroport international de Guangzhou Baiyun (CAN)",
# #         "Aéroport international de Hong Kong (HKG)",
# #         "Aéroport international de Chengdu Shuangliu (CTU)",
# #         "Aéroport international de Shenzhen Bao'an (SZX)",
# #         "Aéroport international de Kunming Changshui (KMG)",
# #         "Aéroport international de Xi'an Xianyang (XIY)",
# #         "Aéroport international de Hangzhou Xiaoshan (HGH)",
# #         "Aéroport international de Chongqing Jiangbei (CKG)","Aéroport de Madrid-Barajas (MAD)",
# #         "Aéroport de Barcelone-El Prat (BCN)",
# #         "Aéroport de Palma de Majorque (PMI)",
# #         "Aéroport de Malaga-Costa del Sol (AGP)",
# #         "Aéroport de Valence (VLC)",
# #         "Aéroport de Séville (SVQ)",
# #         "Aéroport d'Alicante-Elche (ALC)",
# #         "Aéroport de Bilbao (BIO)",
# #         "Aéroport de Tenerife Sud (TFS)",
# #         "Aéroport de Gran Canaria (LPA)",
# #         "Aéroport de Rome Fiumicino (FCO)",
# #         "Aéroport de Milan Malpensa (MXP)",
# #         "Aéroport de Venise-Marco Polo (VCE)",
# #         "Aéroport de Naples-Capodichino (NAP)",
# #         "Aéroport de Florence-Peretola (FLR)",
# #         "Aéroport de Palerme-Punta Raisi (PMO)",
# #         "Aéroport de Bologne-Guglielmo Marconi (BLQ)",
# #         "Aéroport de Turin-Caselle (TRN)",
# #         "Aéroport de Catane-Fontanarossa (CTA)",
# #         "Aéroport de Pise-Galileo Galilei (PSA)",

# #         "Aéroport international de Toronto Pearson (YYZ)",
# #         "Aéroport international de Vancouver (YVR)",
# #         "Aéroport international de Montréal-Trudeau (YUL)",
# #         "Aéroport international de Calgary (YYC)",
# #         "Aéroport international d'Ottawa Macdonald-Cartier (YOW)",
# #         "Aéroport international d'Edmonton (YEG)",
# #         "Aéroport international de Winnipeg James Armstrong Richardson (YWG)",
# #         "Aéroport international de Québec Jean Lesage (YQB)",
# #         "Aéroport international de Halifax Stanfield (YHZ)",
# #         "Aéroport international de Victoria (YYJ)",
# #         "Aéroport de Sydney-Kingsford Smith (SYD)",
# #         "Aéroport de Melbourne-Tullamarine (MEL)",
# #         "Aéroport de Brisbane (BNE)",
# #         "Aéroport de Perth (PER)",
# #         "Aéroport de Gold Coast (OOL)",
# #         "Aéroport d'Adélaïde (ADL)",
# #         "Aéroport de Canberra (CBR)",
# #         "Aéroport de Cairns (CNS)",
# #         "Aéroport de Darwin (DRW)",
# #         "Aéroport de Hobart (HBA)",
# #         "Aéroport international OR Tambo (JNB)",
# #         "Aéroport international du Cap (CPT)",
# #         "Aéroport international de Durban-King Shaka (DUR)",
# #         "Aéroport international de Johannesbourg-Lanseria (HLA)",
# #         "Aéroport international de Port Elizabeth (PLZ)",
# #         "Aéroport international de Bloemfontein (BFN)",
# #         "Aéroport international de George (GRJ)",
# #         "Aéroport international d'East London (ELS)",
# #         "Aéroport international de Kimberley (KIM)",
# #         "Aéroport international de Nelspruit-Kruger Mpumalanga (MQP)",
# #         "Aéroport international Mohammed V (CMN)",
# #         "Aéroport Marrakech-Ménara (RAK)",
# #         "Aéroport Agadir-Al Massira (AGA)",
# #         "Aéroport Fès-Saïss (FEZ)",
# #         "Aéroport Tanger-Ibn Battuta (TNG)",
# #         "Aéroport Rabat-Salé (RBA)",
# #         "Aéroport Casablanca-Anfa (CAS)",
# #         "Aéroport Ouarzazate (OZZ)",
# #         "Aéroport Nador-Al Aroui (NDR)",
# #         "Aéroport Essaouira-Mogador (ESU)",
# #         "Aéroport international Jomo Kenyatta (NBO)",
# #         "Aéroport international Moi de Mombasa (MBA)",
# #         "Aéroport de Kisumu (KIS)",
# #         "Aéroport de Eldoret (EDL)",
# #         "Aéroport de Malindi (MYD)",
# #         "Aéroport de Ukunda-Diani Beach (UKA)",
# #         "Aéroport de Lamu-Manda (LAU)",
# #         "Aéroport de Nanyuki (NYK)",
# #         "Aéroport de Lokichoggio (LKG)",
# #         "Aéroport de Wajir (WJR)",
# #         "Aéroport international du Caire (CAI)",
# #         "Aéroport de Charm el-Cheikh (SSH)",
# #         "Aéroport de Louxor (LXR)",
# #         "Aéroport de Hurghada (HRG)",
# #         "Aéroport de Sharm el-Sheikh (RAS)",
# #         "Aéroport de Marsa Alam (RMF)",
# #         "Aéroport de Alexandrie-Borg el-Arab (HBE)",
# #         "Aéroport de Assouan (ASW)",
# #         "Aéroport de Taba (TCP)",
# #         "Aéroport de Suez (SKV)",
# #         "Aéroport international Murtala Muhammed de Lagos (LOS)",
# #         "Aéroport international Nnamdi Azikiwe d'Abuja (ABV)",
# #         "Aéroport international de Port Harcourt (PHC)",
# #         "Aéroport international de Kano (KAN)",
# #         "Aéroport international de Lagos (LOS)",
# #         "Aéroport international de Calabar",

# # ]
# # for i in range(len(list_aeroport)):
# #     aerepo=aeroport(
# #         name=list_aeroport[i]
# #     )
# #     aerepo.save()



# # compagnies_aeriennes = [
# #     "American Airlines",
# #     "Delta Air Lines",
# #     "United Airlines",
# #     "Southwest Airlines",
# #     "British Airways",
# #     "Lufthansa",
# #     "Air France",
# #     "KLM Royal Dutch Airlines",
# #     "Ryanair",
# #     "EasyJet",
# #     "Emirates",
# #     "Qatar Airways",
# #     "Ethiopian Airlines",
# #     "South African Airways",
# #     "EgyptAir",
# #     "Kenya Airways",
# #     "Air Zimbabwe",
# #     "Air Botswana",
# #     "Air Mauritania",
# #     "Air Burkina",
# #     "Air Senegal",
# #     "Air Tanzania",
# #     "Air Côte d'Ivoire",
# #     "Air Malawi",
# #     "Air Madagascar",
# #     "Air Peace (Nigeria)",
# #     "Dana Air (Nigeria)",
# #     "EgyptAir Express",
# #     "Fastjet (Tanzanie)",
# #     "Fastjet (Zimbabwe)",
# #     "Jambojet (Kenya)",
# #     "Aeroflot (Russie)",
# #     "Turkish Airlines",
# #     "Gulf Air",
# #     "Singapore Airlines",
# #     "Cathay Pacific",
# #     "Japan Airlines",
# #     "China Eastern Airlines",
# #     "Air India",
# #     "IndiGo",
# #     "Qantas Airways",
# #     "Air New Zealand",
# #     "LATAM Airlines",
# #     "Avianca",
# #     "Copa Airlines",
# #     "Aeroméxico",
# #     "Interjet (Mexique)",
# #     "Volaris (Mexique)",
# #     "Saudia",
# #     "Emirates",
# #     "Etihad Airways",
# #     "Oman Air",
# #     "AirAsia",
# #     "Vietnam Airlines",
# #     "Philippine Airlines",
# #     "Garuda Indonesia",
# #     "Thai Airways",
# #     "Korean Air",
# #     "Asiana Airlines",
# #     "EVA Air",
# #     "Air Canada",
# #     "WestJet",
# #     "LATAM Airlines",
# #     "Qantas Airways",
# #     "Air New Zealand",
# #     "Virgin Australia",
# #     "Fiji Airways",
# #     "South African Airways",
# #     "Ethiopian Airlines",
# #     "EgyptAir",
# #     "Royal Air Maroc",
# #     "Kenya Airways",
# #     "TAAG Angola Airlines",
# #     "Air Mauritius",
# #     "Air Seychelles",
# #     "RwandAir",
# #     "Tunisair",
# #     "Air Algérie",
# #     "Air Austral",
# #     "Air Botswana",
# #     "Air Burkina",
# #     "Air Côte d'Ivoire",
# #     "Air Madagascar",
# #     "Air Malawi",
# #     "Air Namibia",
# #     "Air Senegal",
# #     "Air Tanzania",
# #     "Air Zimbabwe",
# #     "ASKY Airlines",
# #     "Fastjet (Tanzanie)",
# #     "Fastjet (Zimbabwe)",
# #     "Jambojet (Kenya)",
# #     "Mango (Afrique du Sud)"
# # ]

# # for i in range(len(compagnies_aeriennes)):
# #     comp=compagnie(
# #         name=compagnies_aeriennes[i]
# #     )
# #     comp.save()




# # # Insérer les données dans la table Clients
# # clients_data = [
# #     {'nom': 'Martin', 'prenom': 'Sophie', 'telephone': '555111111', 'mail': 'sophie.martin@example.com'},
# #     {'nom': 'Dupont', 'prenom': 'Luc', 'telephone': '555222222', 'mail': 'luc.dupont@example.com'},
# #     {'nom': 'Petit', 'prenom': 'Laura', 'telephone': '555333333', 'mail': 'laura.petit@example.com'},
# #     {'nom': 'Robert', 'prenom': 'Antoine', 'telephone': '555444444', 'mail': 'antoine.robert@example.com'},
# #     {'nom': 'Durand', 'prenom': 'Pauline', 'telephone': '555555555', 'mail': 'pauline.durand@example.com'},
# #     {'nom': 'Leroy', 'prenom': 'Alexandre', 'telephone': '555666666', 'mail': 'alexandre.leroy@example.com'},
# #     {'nom': 'Morel', 'prenom': 'Julia', 'telephone': '555777777', 'mail': 'julia.morel@example.com'},
# #     {'nom': 'Girard', 'prenom': 'Nicolas', 'telephone': '555888888', 'mail': 'nicolas.girard@example.com'},
# #     {'nom': 'Robin', 'prenom': 'Charlotte', 'telephone': '555999999', 'mail': 'charlotte.robin@example.com'},
# #     {'nom': 'Chevalier', 'prenom': 'Hugo', 'telephone': '555101010', 'mail': 'hugo.chevalier@example.com'},
# #     {'nom': 'Marchand', 'prenom': 'Emma', 'telephone': '555121212', 'mail': 'emma.marchand@example.com'},
# #     {'nom': 'Lemoine', 'prenom': 'Alexis', 'telephone': '555131313', 'mail': 'alexis.lemoine@example.com'},
# #     {'nom': 'Mercier', 'prenom': 'Juliette', 'telephone': '555141414', 'mail': 'juliette.mercier@example.com'},
# #     {'nom': 'Dufour', 'prenom': 'Maxime', 'telephone': '555151515', 'mail': 'maxime.dufour@example.com'},
# #     {'nom': 'Simon', 'prenom': 'Éléonore', 'telephone': '555161616', 'mail': 'eleonore.simon@example.com'},
# #     {'nom': 'Rousseau', 'prenom': 'Mathieu', 'telephone': '555171717', 'mail': 'mathieu.rousseau@example.com'},
# #     {'nom': 'Gauthier', 'prenom': 'Céline', 'telephone': '555181818', 'mail': 'celine.gauthier@example.com'},
# #     {'nom': 'Lefevre', 'prenom': 'Thomas', 'telephone': '555191919', 'mail': 'thomas.lefevre@example.com'},
# #     {'nom': 'Meunier', 'prenom': 'Camille', 'telephone': '555202020', 'mail': 'camille.meunier@example.com'},
# #     {'nom': 'Laurent', 'prenom': 'Julie', 'telephone': '555212121', 'mail': 'julie.laurent@example.com'},
# # ]

# # for data in clients_data:
# #     client = Clients(**data)
# #     client.save()


# # operateurs_paiement = [
# #     "PayPal",
# #     "Stripe",
# #     "Square",
# #     "Skrill",
# #     "Payoneer",
# #     "Payza",
# #     "2Checkout",
# #     "Authorize.Net",
# #     "Alipay",
# #     "WeChat Pay",
# #     "Apple Pay",
# #     "Google Pay",
# #     "Amazon Pay",
# #     "PayU",
# #     "Paytm",
# #     "M-Pesa",
# #     "Orange Money",
# #     "Joni Joni",
# #     "Wizall Money",
# #     "Free Money",
# #     "Wave"
# # ]

# # for i in operateurs_paiement:
# #     ope=Operateur(
# #         nom=i
# #     )
# #     ope.save()

# # type_chambre=["Adulte","Enfant"]
# # for i in type_chambre:
# #     typ=TypeChambre(
# #        type=i
# #     )
# #     typ.save()
# # timezone.now()
# # villes = [
# #     'New York',
# #     'Londres',
# #     'Paris',
# #     'Tokyo',
# #     'Dubaï',
# #     'Sydney',
# #     'Pékin',
# #     'Istanbul',
# #     'Rome',
# #     'Mexico',
# #     'Dakar',
# #     'Le Caire',
# #     'Johannesburg',
# #     'Nairobi',
# #     'Casablanca',
# #     'Moscou',
# #     'Berlin',
# #     'Toronto',
# #     'São Paulo',
# #     'Mumbai',
# #     'Amsterdam',
# #     'Buenos Aires',
# #     'Singapour',
# #     'Bangkok',
# #     'Barcelone'
# # ]


# # # for i in villes:
# # #     Vi=Ville(
# # #        nom=i
# # #     )
# # #     Vi.save()

# # aeroports = [
# #     # New York
# #     ['Aéroport international John F. Kennedy (JFK)', 'Aéroport de LaGuardia (LGA)', 'Aéroport de Newark Liberty (EWR)'],
    
# #     # Londres
# #     ['Aéroport de Heathrow (LHR)', 'Aéroport de Gatwick (LGW)', 'Aéroport de London City (LCY)'],
    
# #     # Paris
# #     ['Aéroport de Paris-Charles-de-Gaulle (CDG)', 'Aéroport de Paris-Orly (ORY)', 'Aéroport de Beauvais-Tillé (BVA)'],
    
# #     # Tokyo
# #     ['Aéroport de Haneda (HND)', 'Aéroport de Narita (NRT)'],
    
# #     # Dubaï
# #     ['Aéroport international de Dubaï (DXB)', 'Aéroport international Al Maktoum (DWC)'],
    
# #     # Sydney
# #     ['Aéroport de Sydney-Kingsford Smith (SYD)'],
    
# #     # Pékin
# #     ['Aéroport international de Pékin (PEK)'],
    
# #     # Istanbul
# #     ["Aéroport international d'Istanbul (IST)", 'Aéroport Sabiha Gökçen (SAW)'],
    
# #     # Rome
# #     ['Aéroport de Rome Fiumicino (FCO)', 'Aéroport de Rome Ciampino (CIA)'],
    
# #     # Mexico
# #     ['Aéroport international de Mexico (MEX)'],
    
# #     # Dakar
# #     ['Aéroport international Blaise-Diagne (DSS)', 'Aéroport de Dakar-Yoff (DKR)'],
    
# #     # Le Caire
# #     ['Aéroport international du Caire (CAI)'],
    
# #     # Johannesburg
# #     ['Aéroport international OR Tambo (JNB)', 'Aéroport de Lanseria (HLA)'],
    
# #     # Nairobi
# #     ['Aéroport international Jomo Kenyatta (NBO)'],
    
# #     # Casablanca
# #     ['Aéroport international Mohammed V (CMN)', "Aéroport d'Anfa (CAS)"],
    
# #     # Moscou
# #     ['Aéroport international de Moscou-Domodedovo (DME)', 'Aéroport international de Moscou-Cheremetievo (SVO)', 'Aéroport international de Moscou-Vnoukovo (VKO)'],
    
# #     # Berlin
# #     ['Aéroport de Berlin-Tegel (TXL)', 'Aéroport de Berlin-Schönefeld (SXF)'],
    
# #     # Toronto
# #     ['Aéroport international Pearson de Toronto (YYZ)'],
    
# #     # São Paulo
# #     ['Aéroport international de São Paulo-Guarulhos (GRU)', 'Aéroport de Congonhas (CGH)'],
    
# #     # Mumbai
# #     ['Aéroport international Chhatrapati-Shivaji de Mumbai (BOM)'],
    
# #     # Amsterdam
# #     ['Aéroport d\'Amsterdam-Schiphol (AMS)'],
    
# #     # Buenos Aires
# #     ['Aéroport international Ministro-Pistarini d\'Ezeiza (EZE)', 'Aéroport Jorge-Newbery (AEP)'],
    
# #     # Singapour
# #     ['Aéroport de Singapour-Changi (SIN)'],
    
# #     # Bangkok
# #     ['Aéroport international de Suvarnabhumi (BKK)', 'Aéroport de Don Muang (DMK)'],
    
# #     # Barcelone
# #     ['Aéroport de Barcelone-El Prat (BCN)']
# # ]
# # from django.core.exceptions import ObjectDoesNotExist
# # for i in range( len(aeroports)):
# #     try:
# #         ville = Ville.objects.get(id_ville=i+1)
# #         for j in aeroports[i]:
# #             aere = Aeroport(
# #                 nom=j,
# #                 id_ville=ville
# #             )
# #             aere.save()
# #     except ObjectDoesNotExist:
# #         print(f"La ville avec l'ID {i} n'existe pas.")

# # compagnies = [
# #     "Royal Air Maroc",
# #     "Kenya Airways",
# #     "American Airlines",
# #     "Air France",
# #     "Air Senegal",
# #     "Emirates",
# #     "Etihad Airways",
# #     "British Airways",
# #     "Air India",
# #     "Qatar Airways",   
# #     "South African Airways",
# #     "AirAsia",
# #     "Volaris",
# #     "Asiana Airlines",
# #     "Singapore Airlines",
# #     "Etihad Airways"
# # ]
# # for i in compagnies:
# #     comp=Compagnie(
# #         nom = i
# #     )
# #     comp.save()


# # Install the Python library from https://pypi.org/project/amadeus
# # import json
# # from amadeus import Client, ResponseError

# # amadeus = Client(
# #     client_id='34cJnESJwBncYy6G4BC8w3ljQYAxCSs3',
# #     client_secret='m23t2aAiwQSO1n5A'
# # )


# # try:
# #     '''
# #     Find the cheapest flights from SYD to BKK
# #     '''
# #     response = amadeus.shopping.flight_offers_search.get(
# #         originLocationCode='SYD', destinationLocationCode='BKK', departureDate='2023-06-01', adults=1)
# #     data = response.data  # Utilisez .data au lieu de .json()
# #     with open('data.json', 'w') as file:
# #         json.dump(data, file)
# # except ResponseError as error:
# #     raise error

# # import json
# # import os
# # json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")

# # with open(json_file_path) as fichier_json:
# #     data=json.load(fichier_json)



# # for item in data['data']:
# #     vol=Vol(
# #         type=item['type'],
# #         subtype=item['subtype'],
# #         name=item['name'],
# #         iataCode=item['iataCode']

# #     )
# #     vol.save()
# # import random
# # from datetime import datetime, timedelta
# # from django.utils import timezone
# # from AppliDjango.models import Vol, Aeroport, Compagnie

# # compagnie_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# # aeroport_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
# #                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
# #                 39, 40, 41, 42, 43, 44]

# # # Insertion de 20 lignes dans la table Vol
# # for _ in range(20):
# #     random_date = timezone.make_aware(datetime.now() + timedelta(days=random.randint(1, 30)))
# #     random_departure = random.choice(aeroport_ids)
# #     random_arrival = random.choice(aeroport_ids)
# #     random_compagnie = random.choice(compagnie_ids)

# #     aeroport_depart = Aeroport.objects.get(id_aeroport=random_departure)
# #     aeroport_arrivee = Aeroport.objects.get(id_aeroport=random_arrival)
# #     compagnie = Compagnie.objects.get(id_compagnie=random_compagnie)

# #     random_hours = random.randint(0, 23)
# #     random_minutes = random.randint(0, 59)

# #     date_depart = random_date.replace(hour=random_hours, minute=random_minutes, second=0, microsecond=0)
# #     date_arrive = date_depart + timedelta(hours=random.randint(1, 10))

#     # vol = Vol(
#     #     date_depart=date_depart,
#     #     date_arrive=date_arrive,
#     #     aeroport_depart=aeroport_depart,
#     #     aeroport_arrivee=aeroport_arrivee,
#     #     id_compagnie=compagnie
#     # )
#     # vol.save()


   
# # marques_voitures = [
# #     "Toyota",
# #     "Hyundai",
# #     "Nissan",
# #     "Renault",
# #     "Peugeot",
# #     "Mercedes-Benz",
# #     "BMW",
# #     "Volkswagen",
# #     "Ford",
# #     "Mitsubishi",
# #     "Kia",
# #     "Honda",
# #     "Chevrolet",
# #     "Audi",
# #     "Land Rover"
# # ]

# # for i in marques_voitures:
# #     marques=MarqueVoiture(
# #         nom=i
# #     )
# #     marques.save()
    
 
# # models_voitures = [
# #         ["Corolla", "Hilux", "Land Cruiser", "RAV4"],
# #         ["i10", "Accent", "Tucson", "Santa Fe"],
# #         ["Micra", "Qashqai", "X-Trail", "Patrol"],
# #         ["Clio", "Megane", "Duster", "Kadjar"],
# #         ["208", "301", "308", "5008"],
# #         ["Classe A", "Classe C", "Classe E", "GLC"],
# #         ["Série 1", "Série 3", "X3", "X5"],
# #         ["Polo", "Golf", "Tiguan", "Touareg"],
# #         ["Fiesta", "Focus", "Ranger", "Everest"],
# #         ["L200", "Pajero", "Outlander", "ASX"],
# #         ["Picanto", "Rio", "Sportage", "Sorento"],
# #         ["Civic", "Accord", "CR-V", "HR-V"],
# #         ["Spark", "Cruze", "Captiva", "Trailblazer"],
# #         ["A3", "A4", "Q5", "Q7"],
# #         ["Range Rover", "Discovery", "Defender", "Range Rover Sport"]
# # ]

# # for i in range(len(models_voitures)):
# #     try:
# #         marque=MarqueVoiture.objects.get(id_marque=i+1)
# #         for j in models_voitures[i]:
# #             models=ModeleVoiture(
# #                 nom=j,
# #                 id_marque=marque
# #             )
# #             models.save()
    
# #     except MarqueVoiture.DoesNotExist :
# #         print(f"La marque avec l'ID {i} n'existe pas.")







# # for i in range( len(aeroports)):
# #     try:
# #         ville = Ville.objects.get(id_ville=i+1)
# #         for j in aeroports[i]:
# #             aere = Aeroport(
# #                 nom=j,
# #                 id_ville=ville
# #             )
# #             aere.save()
# #     except ObjectDoesNotExist:
# #  


# # from amadeus import ResponseError, Client

# # amadeus = Client(
# #     client_id='34cJnESJwBncYy6G4BC8w3ljQYAxCSs3',
# #     client_secret='m23t2aAiwQSO1n5A'
# # )

# # try:
# #     '''
# #     Get list of hotels by city code
# #     '''
# #     response = amadeus.reference_data.locations.hotels.by_city.get(cityCode='PAR')
    
# #     try:
# #         ville = Ville.objects.get(id_ville=3)
# #         for i in range(10) :
# #             hotel=Hotel(
# #                 nom=response.data[i]['name'],
# #                   id_ville=ville
# #                 )
# #             hotel.save()
# #     except ville.DoesNotExist :
# #         raise Error

# # except ResponseError as error:
# #     raise error



# for i in  range(300):
#     try:
#         hotel = Hotel.objects.get(id_hotel=randint(1,17))
#         TypeChamb=TypeChambre.objects.get(id_typeChambre=randint(1,2))
#         chambre=Chambres(
#             montant=randint(20000,500000),
#             id_hotel=hotel,
#             id_typeChambre=TypeChamb
        
#         )
#         chambre.save()
#     except Hotel.DoesNotExist and TypeChambre.DoesNotExist : 
#         raise Error



# import random
# from datetime import timedelta,datetime

# Insertion dans la table Escale
# heure_depart = datetime.now()
# for i in range(10):
#     heure_arrivee = datetime.now() + timedelta(minutes=random.randint(0, 1440))
#     heure_depart = heure_depart + timedelta(minutes=random.randint(30, 240))

#     id_aeroport = random.randint(1, 44)  # Sélection aléatoire de l'identifiant d'aéroport
#     id_vol = random.randint(1, 20)  # Sélection aléatoire de l'identifiant de vol

#     escale = Escales.objects.create(
#         heure_arrivee=heure_arrivee,
#         heure_depart=heure_depart,
#         id_aeroport=Aeroport.objects.get(id_aeroport=id_aeroport),
#         id_vol=Vol.objects.get(id_vol=id_vol)
#     )

#     escale.save()
# societes_location_voiture = [
#     "Europcar Sénégal",
#     "Avis Sénégal",
#     "Hertz Sénégal",
#     "Budget Sénégal",
#     "Sixt Sénégal",
#     "Allo Location",
#     "Senegal Auto Location",
#     "Adja Location",
#     "SenDrive",
#     "Senegal Car Rental",
#     "Tam Tam Location",
#     "Continental Location",
#     "Allo Voiture",
#     "Senegal Auto Service",
#     "Speed Car Rental",
#     "West Africa Car Rental",
#     "Sun Location",
#     "Mame Fall Location",
#     "Boune Car",
#     "Senegal Travel Car"
# ]

# try:
#     ville = Ville.objects.get(id_ville=11)
#     for i in societes_location_voiture :
#         hotel=Hotel(
#             nom=i,
#             id_ville=ville
#             )
#         hotel.save()
# except ville.DoesNotExist :
#     raise Error




# societes_location_voiture = [
#     "Europcar Sénégal",
#     "Avis Sénégal",
#     "Hertz Sénégal",
#     "Budget Sénégal",
#     "Sixt Sénégal",
#     "Allo Location",
#     "Senegal Auto Location",
#     "Adja Location",
#     "SenDrive",
#     "Senegal Car Rental",
#     "Tam Tam Location",
#     "Continental Location",
#     "Allo Voiture",
#     "Senegal Auto Service",
#     "Speed Car Rental",
#     "West Africa Car Rental",
#     "Sun Location",
#     "Mame Fall Location",
#     "Boune Car",
#     "Senegal Travel Car"
# ]

# try:
#     ville = Ville.objects.get(id_ville=11)
#     for i in societes_location_voiture :
#         socit=Societe(
#             nom=i,
#             id_ville=ville
#             )
#         socit.save()
# except Societe.DoesNotExist :
#     print('y aerreur')

# import random
# from .models import Voiture,Societe

# def insertions_aleatoires():
#     modeles_voiture_ids = ModeleVoiture.objects.values_list('id_modele', flat=True)
#     societes_ids = Societe.objects.values_list('id_societe', flat=True)

#     for _ in range(30):
#         modele_voiture_id = random.choice(modeles_voiture_ids)
#         societe_id = random.choice(societes_ids)
#         montant = random.randint(1000, 5000)

#         voiture = Voiture(
#             montant=montant,
#             id_modele=modele_voiture_id,
#             id_societe=societe_id
#         )
#         voiture.save()
# chemin_image='../static/img/chambre'

# liste_images=['chambre1.webp','chambre2.jpeg','chambre3.jpe','chambre4.jpg','chambre5.jpg',
#              'chambre6.jpg','chambre7.jpg','chambre8.jpg','chambre9.jpg','chambre10.jpg','chambre11.jpg','chambre12.jpg',
#              'chambre13.jpeg','chambre14.jpg','chambre15.jpg','chambre16.jpg','chambre17.jpg','chambre18.jpg','chambre19.jpg','chambre20.webp']
            
            
# from django.core.files import File
# from random import randint


# from django.core.files import File
# from random import randint

# chemin_image = 'img/chambre'


# for i in  range(300):
#     try:
#         nom_fichier_image = random.choice(liste_images)
#         chemin_complet_image = chemin_image+'/'+ nom_fichier_image

        

        

#         hotel = Hotel.objects.get(id_hotel=randint(1, 17))
#         type_chambre = TypeChambre.objects.get(id_typeChambre=randint(1, 2))
#         chambre = Chambres(
#             montant=randint(20000, 500000),
#             id_hotel=hotel,
#             id_typeChambre=type_chambre,
#             image=chemin_complet_image
#         )

#         chambre.save()
#     except Hotel.DoesNotExist and TypeChambre.DoesNotExist : 
#         raise Error

# # for i in  range(300):
#     try:
#         nom_fichier_image = random.choice(liste_image)
#         chemin_complet_image = os.path.join(chemin_image, nom_fichier_image)
#         hotel = Hotel.objects.get(id_hotel=random.randint(1,17))
#         TypeChamb=TypeChambre.objects.get(id_typeChambre=random.randint(1,2))
        
#         if os.path.exists(chemin_complet_image):
#             with open(chemin_complet_image, 'rb') as f:
               
#                 fichier_image = File(f)
                
#                 chambre=Chambres(
#                     montant=random.randint(20000,500000),
#                     id_hotel=hotel,
#                     id_typeChambre=TypeChamb
                    
# #                 )
# #                 chambre.save()
# #                 Chambres.image.save(nom_fichier_image, fichier_image, save=True)
# #     except Hotel.DoesNotExist and TypeChambre.DoesNotExist : 
# #         raise Error




# from datetime import datetime
# from django.db import connection

# def recherche_vols(request):
#     destination = request.GET.get('destination')
#     date_depart = request.GET.get('date_depart')

#     # Convertir la date de départ en objet datetime si nécessaire
#     date_depart = datetime.strptime(date_depart, '%Y-%m-%d').date()

#     # Exécuter la requête SQL
#     with connection.cursor() as cursor:
#         query = """
#         SELECT * FROM vol
#         WHERE aeroport_arrivee_id IN (
#             SELECT id FROM aeroport WHERE nom = %s
#         )
#         AND DATE(date_depart) = %s
#         """
#         cursor.execute(query, [destination, date_depart])

#         # Récupérer les résultats de la requête
#         vols_disponibles = cursor.fetchall()

#     # Afficher les résultats
#     context = {
#         'vols_disponibles': vols_disponibles
#     }
#     return render(request, 'recherche.html', context)

# SELECT ac.id_chambre,ac.montant,ah.nom 
# FROM AppliDjango_chambres ac
# INNER JOIN AppliDjango_hotel ah ON ah.id_hotel=ac.id_hotel_id 
# INNER JOIN AppliDjango_ville av ON av.id_ville=ah.id_ville_id 
# WHERE av.nom='Dakar' 


# list_voiture=['v1.jpg','v2.jpg','v3.jpg','v4.jpg','v5.jpg','v6.jpg','v7.jpg','v8.jpg','v9.jpg','v10.jpg','v11.jpg','v12.jpg','v13.jpg','v14.jpg','v15.jpg','v16.jpg','v17.jpg','v18.jpg','v19.jpg','v20.jpg','v21.jpg','v22.jpg','v23.jpg','v24.jpg','v25.jpg','v26.jpg',
#               'v27.jpg','v28.jpg','v29.jpg','v30.jpg','v31.jpg','v32.jpg','v33.jpg','v34.jpg','v35.jpg','v36.jpg','v37.jpg','v38.jpg','v39.jpg','v40.jpg','v41.jpg','v42.jpg','v43.jpg','v44.jpg','v45.jpg','v46.jpg','v47.jpg','v48.jpg','v49.jpg','v50.jpg','v51.jpg','v52.jpg','v53.jpg',
#               'v54.jpg','v55.jpg','v56.jpg','v57.jpg','v58.jpg','v59.jpg','v60.jpg']  

# chemin_voiture = 'img/voitures'

     
# from random import randint, choice
# for _ in range(100):
#     nom_fichier_voiture = random.choice(list_voiture)
#     chemin_complet_voiture = chemin_voiture+'/'+ nom_fichier_voiture
#     modele_voiture_id = randint(1, 60)
#     societe_id = randint(1, 80)
#     montant = randint(50000, 700000)

#     voiture = Voiture(
#         montant=montant,
#         id_modele_id=modele_voiture_id,
#         id_societe_id=societe_id,
#         image=chemin_complet_voiture
#     )
# voiture.save()

# list_voiture=["Corolla.jpg", "Hilux.jpg", "Land Cruiser.jpg", "RAV4.jpg", "i10.jpg", "Accent.jpg", "Tucson.jpg", "Santa Fe.jpg",
#          "Micra.jpg", "Qashqai.jpg", "X-Trail.jpg", "Patrol.jpg","Clio.jpg", "Megane.jpg", "Duster.jpg", "Kadjar.jpg",
#          "208.jpg", "301.jpg", "308.jpg", "5008.jpg","Classe A.jpg", "Classe C.jpg", "Classe E.jpg", "GLC.jpg",
#          "Série 1.jpg", "Série 3.jpg", "X3.jpg", "X5.jpg","Polo.jpg", "Golf.jpg", "Tiguan.jpg", "Touareg.jpg",
#          "Fiesta.jpg", "Focus.jpg", "Ranger.jpg", "Everest.jpg","L200.jpg", "Pajero.jpg", "Outlander.jpg", 
#          "ASX.jpg","Picanto.jpg", "Rio.jpg", "Sportage.jpg", "Sorento.jpg","Civic.jpg", "Accord.jpg", "CR-V.jpg", 
#          "HR-V.jpg","Spark.jpg", "Cruze.jpg", "Captiva.jpg", "Trailblazer.jpg","A3.jpg", "A4.jpg", "Q5.jpg", "Q7.jpg",
#          "Range Rover.jpg", "Discovery.jpg", "Defender.jpg", "Range Rover Sport.jpg"]

# chemin_voiture = 'img/voitures'

     
# from random import randint, choice
# for i in range(len(list_voiture)):
#     nom_fichier_voiture = list_voiture[i]
#     chemin_complet_voiture = chemin_voiture+'/'+ nom_fichier_voiture
#     modele_voiture_id = i+1
#     societe_id = randint(1, 40)
#     montant = randint(50000, 700000)

#     voiture = Voiture(
#         montant=montant,
#         id_modele_id=modele_voiture_id,
#         id_societe_id=societe_id,
#         image=chemin_complet_voiture
#     )
#     voiture.save() 

# <!DOCTYPE html>
# <html>
# <head>
#   <title>Formulaire de réservation</title>
#   <link rel="stylesheet" type="text/css" href="style.css">
# </head>
# <body>
#   <h1>Formulaire de réservation</h1>

#   <form id="reservation-form">
#     <div class="form-group">
#       <label for="name">Nom :</label>
#       <input type="text" id="name" name="name" required>
#     </div>
#     <div class="form-group">
#       <label for="email">Email :</label>
#       <input type="email" id="email" name="email" required>
#     </div>
#     <div class="form-group">
#       <label for="hotel">Hôtel :</label>
#       <select id="hotel" name="hotel" required>
#         <option value="" disabled selected hidden>Choisir un hôtel</option>
#         <option value="hotel1">Hôtel 1</option>
#         <option value="hotel2">Hôtel 2</option>
#         <option value="hotel3">Hôtel 3</option>
#       </select>
#     </div>
#     <div class="form-group">
#       <label for="checkin">Date d'arrivée :</label>
#       <input type="date" id="checkin" name="checkin" required>
#     </div>
#     <div class="form-group">
#       <label for="checkout">Date de départ :</label>
#       <input type="date" id="checkout" name="checkout" required>
#     </div>
#     <div class="form-group">
#       <label for="comments">Commentaires :</label>
#       <textarea id="comments" name="comments"></textarea>
#     </div>
#     <button type="submit">Réserver</button>
#   </form>

#   <script src="script.js"></script>
# </body>
# </html>

# body {
#   font-family: Arial, sans-serif;
#   padding: 20px;
# }

# h1 {
#   text-align:

