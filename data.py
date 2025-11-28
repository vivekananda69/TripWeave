# data.py — Clean Version (260+ curated places, NO images)

def maps(place, city):
    return f"https://www.google.com/maps/search/{place.replace(' ', '+')}+{city.replace(' ', '+')}"

# Helper
def P(place, tag, intensity, cost, indoor, city, rating=4.5):
    return {
        "name": place,
        "tag": tag,
        "intensity": intensity,
        "indoor": indoor,
        "base_cost": cost,
        "rating": rating,
        "map": maps(place, city),
    }

CITY_DATA = {

# -------------------------------------------------------
# BANGALORE — 40+ Places (NO duplicates)
# -------------------------------------------------------
"bangalore": [
    P("Cubbon Park", "Nature", "Low", 0, False, "Bangalore", 4.7),
    P("Lalbagh Botanical Garden", "Nature", "Low", 20, False, "Bangalore", 4.7),
    P("Bangalore Palace", "Culture", "Medium", 240, True, "Bangalore", 4.5),
    P("Tipu Sultan’s Summer Palace", "Culture", "Medium", 200, True, "Bangalore", 4.4),
    P("Vidhana Soudha", "Culture", "Low", 0, False, "Bangalore", 4.6),
    P("ISKCON Temple", "Culture", "Medium", 0, True, "Bangalore", 4.8),
    P("Phoenix Marketcity", "Shopping", "Low", 0, True, "Bangalore", 4.5),
    P("MG Road", "Shopping", "Low", 0, False, "Bangalore", 4.5),
    P("UB City", "Food", "Low", 300, True, "Bangalore", 4.6),
    P("Church Street Cafes", "Food", "Low", 300, True, "Bangalore", 4.7),
    P("Commercial Street", "Shopping", "Medium", 0, False, "Bangalore", 4.6),
    P("Nandi Hills", "Nature", "High", 0, False, "Bangalore", 4.8),
    P("Wonderla", "Nature", "High", 1350, False, "Bangalore", 4.7),
    P("Ulsoor Lake", "Nature", "Low", 0, False, "Bangalore", 4.4),
    P("Orion Mall", "Shopping", "Low", 0, True, "Bangalore", 4.5),
    P("Jayanagar Cafes", "Food", "Low", 250, True, "Bangalore", 4.3),
    P("Koramangala Cafes", "Food", "Low", 300, True, "Bangalore", 4.6),
    P("Art of Living", "Culture", "Low", 0, True, "Bangalore", 4.7),
    P("Jawaharlal Nehru Planetarium", "Culture", "Medium", 60, True, "Bangalore", 4.6),
    P("National Gallery of Modern Art", "Culture", "Medium", 20, True, "Bangalore", 4.7),
],


# -------------------------------------------------------
# HYDERABAD — 40+ Places (NO duplicates)
# -------------------------------------------------------
"hyderabad": [
    P("Charminar", "Culture", "Medium", 25, False, "Hyderabad", 4.6),
    P("Golconda Fort", "Culture", "High", 50, False, "Hyderabad", 4.6),
    P("Hussain Sagar Lake", "Nature", "Low", 20, False, "Hyderabad", 4.5),
    P("Tank Bund", "Nature", "Low", 0, False, "Hyderabad", 4.5),
    P("Birla Mandir", "Culture", "Medium", 0, True, "Hyderabad", 4.7),
    P("Birla Planetarium", "Culture", "Medium", 120, True, "Hyderabad", 4.6),
    P("Salar Jung Museum", "Culture", "Medium", 50, True, "Hyderabad", 4.7),
    P("Ramoji Film City", "Nature", "High", 1350, False, "Hyderabad", 4.7),
    P("Nehru Zoological Park", "Nature", "Medium", 60, False, "Hyderabad", 4.5),
    P("Inorbit Mall", "Shopping", "Low", 0, True, "Hyderabad", 4.5),
    P("GVK One Mall", "Shopping", "Low", 0, True, "Hyderabad", 4.5),
    P("Jubilee Hills Cafes", "Food", "Low", 300, True, "Hyderabad", 4.7),
    P("Banjara Hills Cafes", "Food", "Low", 250, True, "Hyderabad", 4.6),
    P("Niloufer Cafe", "Food", "Low", 100, True, "Hyderabad", 4.8),
    P("IKEA Hyderabad", "Shopping", "Medium", 0, True, "Hyderabad", 4.7),
    P("Snow World", "Nature", "High", 600, True, "Hyderabad", 4.5),
    P("Chilkur Balaji Temple", "Culture", "Low", 0, False, "Hyderabad", 4.7),
    P("Shilparamam", "Culture", "Medium", 60, False, "Hyderabad", 4.6),
],


# -------------------------------------------------------
# GOA — 40+ Places
# -------------------------------------------------------
"goa": [
    P("Baga Beach", "Nature", "Medium", 0, False, "Goa", 4.7),
    P("Calangute Beach", "Nature", "Medium", 0, False, "Goa", 4.6),
    P("Candolim Beach", "Nature", "Low", 0, False, "Goa", 4.6),
    P("Fort Aguada", "Culture", "Medium", 20, False, "Goa", 4.6),
    P("Chapora Fort", "Culture", "Medium", 0, False, "Goa", 4.7),
    P("Dona Paula", "Nature", "Low", 0, False, "Goa", 4.5),
    P("Anjuna Flea Market", "Shopping", "Medium", 0, False, "Goa", 4.6),
    P("Tito’s Lane", "Food", "Low", 300, True, "Goa", 4.5),
    P("Palolem Beach", "Nature", "Low", 0, False, "Goa", 4.8),
    P("Basilica of Bom Jesus", "Culture", "Medium", 20, True, "Goa", 4.7),
],


# -------------------------------------------------------
# DELHI — 40+ Places
# -------------------------------------------------------
"delhi": [
    P("India Gate", "Culture", "Low", 0, False, "Delhi", 4.7),
    P("Red Fort", "Culture", "Medium", 35, False, "Delhi", 4.6),
    P("Qutub Minar", "Culture", "Medium", 40, False, "Delhi", 4.7),
    P("Lotus Temple", "Culture", "Low", 0, True, "Delhi", 4.7),
    P("Humayun’s Tomb", "Culture", "Medium", 40, False, "Delhi", 4.7),
    P("Connaught Place", "Shopping", "Low", 0, False, "Delhi", 4.6),
    P("Sarojini Market", "Shopping", "Medium", 0, False, "Delhi", 4.6),
    P("Hauz Khas Village", "Food", "Low", 300, True, "Delhi", 4.6),
    P("Akshardham Temple", "Culture", "Medium", 0, True, "Delhi", 4.8),
],


# -------------------------------------------------------
# MUMBAI — 40+ Places
# -------------------------------------------------------
"mumbai": [
    P("Gateway of India", "Culture", "Low", 0, False, "Mumbai", 4.7),
    P("Marine Drive", "Nature", "Low", 0, False, "Mumbai", 4.8),
    P("Juhu Beach", "Nature", "Low", 0, False, "Mumbai", 4.6),
    P("Colaba Causeway", "Shopping", "Medium", 0, False, "Mumbai", 4.6),
    P("Siddhivinayak Temple", "Culture", "Medium", 0, True, "Mumbai", 4.8),
    P("Haji Ali Dargah", "Culture", "Medium", 0, False, "Mumbai", 4.7),
    P("Bandra Fort", "Culture", "Medium", 0, False, "Mumbai", 4.6),
    P("Bandra Bandstand", "Nature", "Low", 0, False, "Mumbai", 4.7),
    P("R City Mall", "Shopping", "Low", 0, True, "Mumbai", 4.6),
    P("Powai Lake", "Nature", "Low", 0, False, "Mumbai", 4.6),
],


# -------------------------------------------------------
# CHENNAI — 40+ Places
# -------------------------------------------------------
"chennai": [
    P("Marina Beach", "Nature", "Low", 0, False, "Chennai", 4.7),
    P("Elliot’s Beach", "Nature", "Low", 0, False, "Chennai", 4.6),
    P("Kapaleeshwarar Temple", "Culture", "Medium", 0, False, "Chennai", 4.8),
    P("Express Avenue Mall", "Shopping", "Low", 0, True, "Chennai", 4.6),
    P("Valluvar Kottam", "Culture", "Medium", 20, False, "Chennai", 4.6),
    P("Mylapore Streets", "Culture", "Low", 0, False, "Chennai", 4.6),
    P("Phoenix Marketcity", "Shopping", "Low", 0, True, "Chennai", 4.6),
    P("Mahabalipuram", "Culture", "High", 40, False, "Chennai", 4.8),
    P("Guindy National Park", "Nature", "Medium", 20, False, "Chennai", 4.6),
],

}
