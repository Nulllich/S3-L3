# Funzioni
def calcola_perimetro_quadrato(l):
    print("\nIl perimetro del quadrato è: " + str(l * 4) + "\n")

def calcola_circonferenza(r):
    print("\nIl perimetro del cerchio è: " + str(round(2 * 3.1415 * r, 2)) + "\n")

def calcola_perimetro_rettangolo(base, altezza):
    print("\nIl perimetro del rettangolo è: " + str(base * 2 + altezza * 2) + "\n")

# Variabile per la condizione dentro il ciclo while 
opzione = True

# Il programma continuerà a funzionare finche la condizione non sia false
while opzione:

  # input dell'utente, qualsiasi input dell'utente
  scelta = input("Scegli la figura geometrica:\nA) quadrato\nB) cerchio\nC) rettangolo\n\nVuoi uscire dal gioco: Y\n").lower()  

  # Se l'utente seleziona una delle opzioni il gioco da inizio!
  if scelta != 'y':

    # perimetro quadrato
    if scelta == "a":
        lato = float(input("Inserisci il lato del quadrato: "))

        # Controllo degli input
        while lato <= 0:
          lato = float(input("Il lato deve essere un valore positivo, inserisci nuovo valore: "))
          
        calcola_perimetro_quadrato(lato)

    # Circonferenza
    elif scelta == "b":
        raggio = float(input("Inserisci il raggio del cerchio: "))

        # Controllo degli input
        while raggio <= 0:
            raggio = float(input("Il raggio deve essere un valore positivo, inserisci nuovo valore: "))

        calcola_circonferenza(raggio)
        
    # Rettangolo
    elif scelta == "c":
        
        base = float(input("Inserisci la base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))

        # Controllo degli input
        while base <= 0:
          base = float(input("La base deve essere positiva, inserisci nuovo valore: "))
          
        while altezza <= 0:
          altezza = float(input("La altezza deve essere positiva, inserisci nuovo valore: "))

        while altezza == base:
          print("La base e l'altezza devono essere diverse tra loro")
          base = float(input("Inserisci la base del rettangolo: "))
          altezza = float(input("Inserisci l'altezza del rettangolo: "))

        calcola_perimetro_rettangolo(base, altezza)

    else:
        print("Scelta non valida. Riprova.\n")
  else:
      # se la scelta è stata diversa da y il programma finirà
      opzione = False

print("\nVa bene non tornare mai più!\n")