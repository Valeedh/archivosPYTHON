print ("¿que tabla deseas jugar?")

numero=int (input("introduce numero:"))
for i in range(1,10):
    resultado=i*numero
    print (("%d x %d = %d")%(numero,i,resultado))
    

