import tkinter as tkr # Pakage de gestion graphique comportant tous les widgets necessaire pour la création d'une interface graphique
from tkinter import Tk,filedialog, messagebox, scrolledtext


class biblioteque:
    def __init__(self, nom_fennetre):
        self.nom_fennetre=nom_fennetre
        self.nom_fennetre.title("Bibliotheque Manager")
        self.nom_fennetre.minsize(740, 520)
        self.nom_fennetre.resizable(False, False)

        self.label_conteneur = tkr.Label(self.nom_fennetre, text="Voici votre livres ci-dessous.", fg="black")
        self.label_conteneur.place(x=500, y=0)
        self.label_fnt = tkr.Label(self.nom_fennetre, text="Voici la liste des fonctions.", fg="black")
        self.label_fnt.place(x=5, y=0)
        
        #Conteneur des livres
        self.books_pack = ["Petit Jo", "La neige", "L'Amour et l'envie"]
        self.taille_books_pack = len(self.books_pack)
        
        #Conteneur des fonctions
        self.fnt_list = ["Ajouter","Afficher", "Modifier","Supprimmer"] 
        self.taille_fnt_list = len(self.fnt_list)
        self.fnt_x =5
        self.fnt_y =25
        
        
        self.afficher_livres()
        self.afficher_menu()
        
    def afficher_menu(self):
        
        i = 0
        while i<self.taille_fnt_list:
            fnt = tkr.Label( self.nom_fennetre, text="("+ str(i+1) + ") " + self.fnt_list[i], fg="blue")
            fnt.place(x=self.fnt_x, y=self.fnt_y)
            i +=1
            self.fnt_y +=20

        cmd = tkr.Label( self.nom_fennetre, text= "Entrez le numero d'une action", fg="black")
        cmd.place(x=self.fnt_x, y=self.fnt_y+30)

        self.cmd_input = tkr.Entry( self.nom_fennetre)
        self.cmd_input.place(x=self.fnt_x+5, y=self.fnt_y+60)

        cmd_btn = tkr.Button( self.nom_fennetre, text="Soumettre", fg="black", bg="gray", command=self.appel_fnt)
        cmd_btn.place(x=self.fnt_x+5, y=self.fnt_y+90)
        
        self.off_btn = tkr.Button( self.nom_fennetre, text="Quitter", font="gras", fg="red", bg="white", width=10, command=self.nom_fennetre.destroy)
        self.off_btn.place(x=360 , y=480)
    
    def appel_fnt(self):
        self.index_fnt = int(self.cmd_input.get())
        if 0 < self.index_fnt < 5 :
            self.w_ajout = Tk()  
            self.w_ajout.minsize(720, 300)
            self.w_ajout.resizable(False, False)
            
            if self.index_fnt == 1:
                self.c1 = tkr.Label(self.w_ajout, font="bold", text="Voulez-vous préciser une position spécifique où inserrer le nouveau livre ?", fg="black")
                self.c1.place(x=20, y=10)

                non = tkr.Button( self.w_ajout, text="NON",width=10, fg="black", bg="gray", command=self.ajouter)
                non.place(x=20, y=60)
                
                oui = tkr.Button( self.w_ajout, text="OUI", width=10, fg="black", bg="gray", command=self.ajouter)
                oui.place(x=120, y=60)

            self.annuler_btn = tkr.Button( self.w_ajout, text="Quitter", font="gras", fg="red", bg="white", width=10,  command=self.w_ajout.destroy)
            self.annuler_btn.place(x=320 , y=260)

    def ajouter():
        print("")
   
    
    def afficher_livres(self):
        #Pour personnaliser la position de chaque livre sur l'écran graphique
        self.book_x =500
        self.book_y =25
        self.compteur = 0
        
        while self.compteur<self.taille_books_pack:
            self.elm_books_pack = tkr.Label(self.nom_fennetre, text="Titre " + str(self.compteur+1) + ":  " + self.books_pack[self.compteur], fg="blue")
            self.elm_books_pack.place(x=self.book_x, y=self.book_y)
            self.compteur +=1
            self.book_y +=20     




def main():
    fenetre = Tk() # La classe principale comportant les widgets parents
    bibli = biblioteque(fenetre)
    fenetre.mainloop()# Démarrage de la fenêtre principale
    
    
if __name__ == "__main__":
    main()