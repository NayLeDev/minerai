import random

mineraux = ["Aluminium", "Américium", "Argentium", "Béryllium", "Bohrium", "Cadmium", "Calcium", "Cérium", "Césium", "Chromite", "Cobaltite", "Copernicium", "Corindon", "Curium", "Darmstadtium", "Dubnium", "Dysprosium", "Einsteinium", "Erbium", "Europium", "Fermium", "Flerovium", "Gallium", "Germanium", "Hafnium", "Hassium", "Hélium", "Holmium", "Indium", "Iridium", "Lanthanum", "Lawrencium", "Lithium", "Livermorium", "Lutécium", "Magnésium", "Manganite", "Meitnerium", "Molybdène", "Neptunium", "Niobium", "Nobélium", "Osmium", "Palladium", "Platine", "Plutonium", "Polonium", "Potassium", "Praséodyme", "Prométhium", "Radon", "Rhodium", "Rubidium", "Ruthénium", "Rutherfordium", "Scandium", "Sélénium", "Silicium", "Sodium", "Strontium", "Tantale", "Technétium", "Tellure", "Terbium", "Thallium", "Thorium", "Thulium", "Titane", "Tungstène", "Uranium", "Vanadium", "Xénon", "Ytterbium", "Yttrium", "Zinc", "Zirconium"]
serveur = input("Entrez le nom de votre serveur: ")
lettres = "".join(random.sample(serveur, 3))
trouvé = False
for minéral in mineraux:
  if len(minéral) <= len(serveur):
    for lettre in lettres:
      if lettre in minéral:
        trouvé = True
        break
    if trouvé:
      break
if trouvé:
  print(f"Voici un minéral nommé {minéral}.")
else:
  print(f"Aucun minérai ne cohere avec le nom de votre serveur et ne contient aucun des lettres {lettres} et n'a une longueur inférieure ou égale à celle du serveur.")
