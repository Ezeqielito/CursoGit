
contador=0
miEmail=input("introduce tu direccion de email: ")

# Comprobar si un email es correcto
for i in miEmail:
    if (i=="@" or i=="."):
        contador = contador+1
        
if contador >=2 and contador >=3 :
    print("Email correcto")
else:
    print("El email es incorrecto")              

