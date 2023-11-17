
Name = input('Ingrese su nombre (tiene que tener mas de dos caracteres y ningun simbolo): ')
Surname = input('Ingrese su apellido (tiene que tener mas de dos caracteres y ningun simbolo): ')
Age = int(input('Ingrese su edad: '))
Gender = input('Ingrese su genero (M/F): ')
Ubication = input('Ingrese donde vive: ')

Symbols = [" ", ",", ".", "*"]

Ready = False
NameReady = False
SurnameReady = False
AgeReady = False
GenderReady = False
UbicationReady = False

while not Ready:
    if len(Name) > 2 and Name != Symbols:
        print("- Nombre: ", Name)
        NameReady = True
    else:
        print("Error, el nombre no cumple con los requisitos")
        Name = input('Ingrese su nombre (tiene que tener mas de dos caracteres y ningun simbolo): ')

    if len(Surname) > 2 and Surname != Symbols:
        print("- Apellido: ", Surname)
        SurnameReady = True
    else:
        print("Error, el apellido no cumple con los requisitos")
        Surname = input('Ingrese su apellido (tiene que tener mas de dos caracteres y ningun simbolo): ')

    if Age > 0:
        print("- Edad: ", Age)
        AgeReady = True

    if Gender == "M":
        print("- Genero: Masculino")
        GenderReady = True
    elif Gender == "F":
        print("- Genero: Femenino")
        GenderReady = True
    else:
        Gender = input('Ingrese su genero (M/F): ')

    if Ubication != ' ':
        print("- Ubicacion: ", Ubication)
        UbicationReady = True
    else:
        print("Error, la ubicacion no es valida")
        Ubication = input('Ingrese donde vive: ')

    if NameReady and SurnameReady and AgeReady and GenderReady and UbicationReady:
        Ready = True




