import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk





image_path = "C:\\Users\\Abdou\\Desktop\\cars\\bmw.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\cars\\bmw.gif"

image_path = "C:\\Users\\Abdou\\Desktop\\cars\\nissan.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\cars\\nissan.gif"

image_path = "C:\\Users\\Abdou\\Desktop\\cars\\jeep.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\cars\\jeep.gif"


image_path = "C:\\Users\\Abdou\\Desktop\\cars\\mercedes.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\cars\\mercedes.gif"


image_path = "C:\\Users\\Abdou\\Desktop\\cars\\tesla.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\cars\\tesla.gif"

image_path = "C:\\Users\\Abdou\\Desktop\\cars\\audi.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\cars\\audi.gif"

image_path = "C:\\Users\\Abdou\\Desktop\\cars\\golf.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\cars\\golf.gif"

image_path = "C:\\Users\\Abdou\\Desktop\\cars\\honda.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\cars\\honda.gif"

image_path = "C:\\Users\\Abdou\\Desktop\\cars\\mustang.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\cars\\mustang.gif"


image_path = "C:\\Users\\Abdou\\Desktop\\cars\\subaru.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\cars\\subaru.gif"
image_path = "C:\\Users\\Abdou\\Desktop\\v1.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\v1.gif"
image_path = "C:\\Users\\Abdou\\Desktop\\cars\\toyota.jpg"
output_path = "C:\\Users\\Abdou\\Desktop\\cars\\toyota.gif"

img = Image.open(image_path)
img = img.convert('RGB')  # Convert the image to 'RGB' mode
img.save(output_path, "GIF")

base_regles_voitures = {
    "couleur": {
        "Rouge": ["Toyota Corolla", "Honda Civic"],
        "Bleu": ["Ford Mustang", "Volkswagen Golf"],
        "Vert": ["Tesla Model 3", "Subaru Outback"],
        "Blanc": ["Nissan Altima", "BMW 3 Series"],
        "Gris": ["Audi A4", "Mercedes-Benz C-Class"],
        "Noir": ["Lexus ES", "Jeep Wrangler"],
        
    },
    "prix": {
        "20000": ["Toyota Corolla", "Ford Mustang"],
        "30000": ["Honda Civic", "Volkswagen Golf"],
        "25000": ["Tesla Model 3", "Subaru Outback"],
        "35000": ["Nissan Altima", "BMW 3 Series"],
        "40000": ["Audi A4", "Mercedes-Benz C-Class"],
        "45000": ["Lexus ES"],
        "50000": ["Jeep Wrangler"],
       
    },
    "type_carburant": {
        "Essence": ["Toyota Corolla", "Honda Civic"],
        "Diesel": ["Ford Mustang", "Volkswagen Golf"],
        "Hybride": ["Tesla Model 3", "Subaru Outback"],
        "Électrique": ["Nissan Altima", "BMW 3 Series"],
        "Hydrogène": ["Audi A4", "Mercedes-Benz C-Class"],
        "GPL": ["Lexus ES","Jeep Wrangler"],
      
    },
    "marque": {
        "Toyota": ["Toyota Corolla", "Tesla Model 3"],
        "Honda": ["Honda Civic"],
        "Ford": ["Ford Mustang"],
        "Volkswagen": ["Volkswagen Golf"],
        "Subaru": ["Subaru Outback"],
        "Nissan": ["Nissan Altima"],
        "BMW": ["BMW 3 Series"],
        "Audi": ["Audi A4"],
        "Mercedes-Benz": ["Mercedes-Benz C-Class"],
        "Lexus": ["Lexus ES"],
        "Jeep": ["Jeep Wrangler"],
       
    },
    "transmission": {
        "Automatique": ["Toyota Corolla", "Ford Mustang", "Nissan Altima", "BMW 3 Series", "Audi A4", "Mercedes-Benz C-Class", "Lexus ES", "Jeep Wrangler"],
        "Manuelle": ["Honda Civic", "Volkswagen Golf", "Tesla Model 3", "Subaru Outback"],
        
    },
    "nombre_portes": {
        2: ["Ford Mustang", "Tesla Model 3", "Nissan Altima", "BMW 3 Series", "Audi A4", "Mercedes-Benz C-Class", "Lexus ES", "Jeep Wrangler"],
        4: ["Toyota Corolla", "Honda Civic", "Volkswagen Golf", "Subaru Outback"],
        
    },
    "type_carrosserie": {
        "Berline": ["Toyota Corolla", "Honda Civic", "Ford Mustang", "Volkswagen Golf", "Nissan Altima", "BMW 3 Series", "Audi A4", "Mercedes-Benz C-Class", "Lexus ES"],
        "SUV": ["Tesla Model 3", "Subaru Outback", "Jeep Wrangler"],
        
    },
    "consommation_carburant": {
        "Faible": ["Toyota Corolla", "Honda Civic", "Ford Mustang", "Volkswagen Golf", "Nissan Altima", "BMW 3 Series", "Audi A4", "Mercedes-Benz C-Class"],
        "Moyenne": ["Tesla Model 3", "Subaru Outback", "Lexus ES"],
        "Élevée": ["Jeep Wrangler"],
       
    },
    "vehicule_neuf": {
        True: ["Toyota Corolla", "Ford Mustang", "Tesla Model 3", "Audi A4", "Lexus ES"],
        False: ["Honda Civic", "Volkswagen Golf", "Subaru Outback", "Nissan Altima", "BMW 3 Series", "Mercedes-Benz C-Class", "Jeep Wrangler"],
       
    },
    "images": {
        "Toyota Corolla": r"C:\\Users\\Abdou\\Desktop\\cars\\toyota.gif",
        "Honda Civic": r"C:\\Users\\Abdou\\Desktop\\cars\honda.gif",
        "Ford Mustang": r"C:\\Users\\Abdou\\Desktop\\cars\\mustang.gif",
        "Tesla Model 3": r"C:\\Users\\Abdou\\Desktop\\cars\\tesla.gif",
        "Jeep Wrangler": r"C:\\Users\\Abdou\\Desktop\\cars\\jeep.gif",
        "Mercedes-Benz C-Class": r"C:\\Users\\Abdou\\Desktop\\cars\\mercedes.gif",
        "Audi A4": r"C:\\Users\\Abdou\\Desktop\\cars\\audi.gif",
        "BMW 3 Series": r"C:\\Users\\Abdou\\Desktop\\cars\\bmw.gif",
        "Volkswagen Golf": r"C:\\Users\\Abdou\\Desktop\\cars\\golf.gif",
        "Nissan Altima": r"C:\\Users\\Abdou\\Desktop\\cars\\nissan.gif",
        "Subaru Outback": r"C:\\Users\\Abdou\\Desktop\\cars\\subaru.gif",
        "Lexus ES": r"C:\\Users\\Abdou\\Desktop\\v1.gif",
        
    }
   
}
class SystemeExpertVoitures:
    def recommander_voiture(self, criteres):
        matching_cars = None

        for critere, valeur in criteres.items():
            if valeur != 'Choisir une option' and critere in base_regles_voitures and valeur in base_regles_voitures[critere]:
                if matching_cars is None:
                    matching_cars = set(base_regles_voitures[critere][valeur])
                else:
                    matching_cars.intersection_update(base_regles_voitures[critere][valeur])

        return list(matching_cars) if matching_cars is not None else []

def afficher_resultats(resultats):
    result_window = tk.Toplevel(root)
    result_window.title("Résultats")

    image_window = tk.Toplevel(root)
    image_window.title("Images")

    if resultats:
        for voiture in resultats:
            image_path = base_regles_voitures.get("images", {}).get(voiture)
            if image_path:
                # Display text in result_window
                result_label = ttk.Label(result_window, text=f"{voiture} - Caractéristiques : {criteres_voiture(voiture)}")
                result_label.pack(padx=10, pady=5)

                # Load and display the image in image_window
                image = Image.open(image_path)
                image.thumbnail((500, 500))  # Adjust the size as needed
                photo = ImageTk.PhotoImage(image)
                image_label = ttk.Label(image_window, image=photo)
                image_label.image = photo  # Keep a reference to the image to avoid garbage collection
                image_label.pack(padx=10, pady=5)
            else:
                # Display text if image path is not available
                result_label = ttk.Label(result_window, text=f"{voiture} - Caractéristiques : {criteres_voiture(voiture)}")
                result_label.pack(padx=10, pady=5)

    else:
        result_label = ttk.Label(result_window, text="Aucune voiture ne correspond à vos critères.")
        result_label.pack(padx=10, pady=10)

def criteres_voiture(voiture):
    # Helper function to get criteria for a specific car
    criteria = []
    for critere, valeurs in base_regles_voitures.items():
        for valeur, voitures in valeurs.items():
            if voiture in voitures:
                criteria.append(f"{critere}: {valeur}")
    return ", ".join(criteria)

def soumettre_formulaire():
    criteres_utilisateur = {critere: valeur.get() for critere, valeur in critere_vars.items() if valeur.get() != 'Choisir une option'}
    resultats = expert_voitures.recommander_voiture(criteres_utilisateur)
    afficher_resultats(resultats)

def clear_champs():
    for critere in critere_vars.values():
        critere.set('Choisir une option')

def create_dropdowns():
    main_frame = ttk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Customize the appearance of the frame to achieve a card view with rounded corners
    style = ttk.Style()
    style.configure("Card.TFrame", background="white", borderwidth=2, relief="groove", bordercolor="lightgray", padding=(5, 5, 5, 5))

    card_frame = ttk.Frame(main_frame, style="Card.TFrame")
    card_frame.pack(fill=tk.X, pady=10, padx=10, ipadx=10, ipady=10)

    for critere, valeurs in base_regles_voitures.items():
        if (critere!="images") :

            label_frame = ttk.LabelFrame(card_frame, text=f"{critere.capitalize()}", padding=(10, 5, 10, 5))
            label_frame.pack(fill=tk.X, pady=10)

            critere_vars[critere] = tk.StringVar(root)
            critere_vars[critere].set('Choisir une option')

            menu_options = list(valeurs.keys())
            menu_options.sort()

            critere_menu = ttk.Combobox(label_frame, textvariable=critere_vars[critere], values=menu_options, state="readonly", width=27)
            critere_menu.grid(row=0, column=0, padx=(0, 10))

    button_frame = ttk.Frame(card_frame, padding=(10, 5, 10, 5))
    button_frame.pack(fill=tk.X)

    submit_button = ttk.Button(button_frame, text="Recommander voiture", command=soumettre_formulaire)
    submit_button.grid(row=0, column=0, padx=(0, 10))

    clear_button = ttk.Button(button_frame, text="Effacer les champs", command=clear_champs)
    clear_button.grid(row=0, column=1)

# Initialisation du thème pour l'interface graphique
root = tk.Tk()
style = ThemedStyle(root)
style.set_theme("clearlooks")  # Choose a light theme, 'clearlooks' is an example

# Initialisation du système expert pour les voitures
expert_voitures = SystemeExpertVoitures()

critere_vars = {}
create_dropdowns()

resultat_label = ttk.Label(root, text="", font=('Arial', 12))
resultat_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.mainloop()