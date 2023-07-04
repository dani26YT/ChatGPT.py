import random

def saluta():
    saluti = ["Ciao!", "Salve!", "Buongiorno!"]
    return random.choice(saluti)

def rispondi(domanda):
    risposte = {
        "come stai?": "Sto bene, grazie!",
        "qual è il tuo nome?": "Mi chiamo Dani26GPT.",
        "che tempo fa oggi?": "Non sono in grado di controllare il meteo, mi dispiace.",
        "cosa fai?": "Sono qui per rispondere alle tue domande!",
        "chatgpt": "Ecco il link di chatGPT: https://chat.openai.com/",
        "Che cos'è windows?": "Windows è un sistema operativo per computer sviluppato da Microsoft. È uno dei sistemi operativi più diffusi al mondo ed è utilizzato su una vasta gamma di dispositivi, inclusi personal computer, laptop, tablet e dispositivi mobili. Windows offre un'interfaccia grafica utente (GUI) che consente agli utenti di interagire con il computer utilizzando icone, finestre e menu."
        
    }
    risposta = risposte.get(domanda.lower())
    if risposta:
        return risposta
    else:
        return "Mi dispiace, ma non ho capito questa domanda, se ti serve aiuto scrivi 'Help' "

def main():
    print(saluta())
    while True:
        domanda = input("Fammi una domanda: ")
        if domanda.lower() == "exit":
            print(rispondi(domanda))
            break
        print(rispondi(domanda))

if __name__ == "__main__":
    main()
