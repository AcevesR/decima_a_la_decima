# List of Artists

list_artist = ['Xoel López', 'Vítor Ramil', 'Fernando Cabrera', 'Martín Buscaglia', 'Jorge Drexler', 'Kevin Johansen', 'Daniel Drexler', 'Kiko Veneno', 'Álex Ferreira', 'René Pérez (Calle 13)']
list_names = []

for i in range(len(list_artist)):
    list_names.append((list_artist[i].split()[0][0] + list_artist[i].split()[1][0]).lower() + str(i))

print(list_names)

#verses_list = []

