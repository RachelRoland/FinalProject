import random 

#list of favorite family restaurants 
names = ["Plum Bistro," "Chipotle", "Oto Sushi", "Spicy Talk", "Mediterranian Kitchen", "Aarya's Place", "McDonalds", "Papa Johns", "Mod", "PCC", "Potbelly", "Ooba Tuba", "Agave", "Panera", "Yummy Pho", "JJ Mahoneys", "Bai Tong", "Spark Pizza", "Woodblock", "Tipsy Cow", "Dough Zone", "Yummy Teriyaki", "Blazing Bagels", "Noodleland", "Bankok Basil" ]

#format the list of names 
print(f"All names: {names}\n")

#choose a random selection from the list 
idx = random.randint(0, len(names) - 1)
print(f"The random restaurant generator has chosen {names[idx]} today.")
