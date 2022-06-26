import tkinter
import webbrowser
from tkinter import *
import webbrowser
import string
from collections import Counter,  OrderedDict
import re
import random
from bs4 import BeautifulSoup
import requests

#######################################################I- CREATION DES DIFFERENTES FONCTIONS #######################################################################


#ouvrir divtionnaire en ligne
def open_larousse():
    webbrowser.open_new('larousse.fr/dictionnaires/francais-monolingue')


#Fonctions d'analyse de texte
def saisi():
    mon_texte.get()
    return  webbrowser.open_new('https://www.larousse.fr/dictionnaires/francais/'+ str(mon_texte.get())+'/')


#fonction de réinitiamisation des entrées et les résultats des sorties de fonctions
def delete():
    text_entry.delete("1.0","end")
    total_mots.delete("1.0","end")
    nb_phrases.delete("1.0", "end")
    mot_rech.delete("1.0", "end")
    text_occurence.delete("1.0", "end")
    nb_espace.delete("1.0", "end")


#Fonction d'analyse de texte
def dico():
    analyse_window = tkinter.Toplevel(center2)
    analyse_window.title("Dictionaire de mots")
    analyse_window.geometry("720x500")
    analyse_window.minsize(360, 272)
    analyse_window.iconbitmap("drapeau_fr.ico")
    analyse_window.config(background='#C5F2F4')
    entrée= tkinter.Entry(analyse_window,font=("Courrier", 12))
    entrée.grid(columnspan=50)
    def definitions():
        if True:
            try:
                res = requests.get('https://www.larousse.fr/dictionnaires/francais/' + str(entrée.get()) + '/')
                soup = BeautifulSoup(res.text, "html.parser")
                items = soup.findAll('article')
                definition_mot = items[0].text.strip('\n').split('.')
                tb.delete('1.0', END)
                tb.insert(INSERT, definition_mot)
            except IndexError:
                tb.delete('1.0', END)
                tb.insert(INSERT, "Mot inexistant , Veuillez en saisir un autre")

    Entrée_btn = Button(analyse_window, text="Valider", command=definitions)
    Entrée_btn.grid(row=3, column=0, sticky="n")
    tb = Text(analyse_window, font=("Arial", 12))
    tb.grid( sticky="nsew")

def dictionnaire_de_mots():
    global center
    center.grid()

#Fonction Aide
def f_aide():
    Aide = '''Ce programme permet d'analyser un texte  \

             en comptant le nombre de mots du texte, en donnant le nombre de mots le plus utilisé\
             
              et le mot le plus long du texte inséré  \

          - Cliquez sur "fichier" puis "Analyse de Texte" pour réinitialiser l espace de saisi de\
           
           la fenetre principale puis saisisser ou copier le texte que vous voulez analyser\
        
          - Cliquez sur"fichier" puis "Dictionnaire de mot" pour rechercher la définition d'un mot \

          - Cliquez sur Quitter pout fermer l appli'''
    aide_window = tkinter.Toplevel(window)
    aide_window.title("Aide")
    aide_window.geometry("720x480")
    aide_window.minsize(360, 272)
    aide_window.iconbitmap("drapeau_fr.ico")
    lb = tkinter.Label(aide_window, text=Aide , font= ("Courrier", 12))
    lb.grid()

def comptage():
    nbre_mot = len(text_entry.get("1.0", "end").split())
    total_mots.delete('1.0', END)
    total_mots.insert('1.0', nbre_mot)

def mots():
    liste_de_mot = list(set(mon_texte.get().split().split()))


#Nombre de phrases
def tot_phrases():
    global text_entry
    nbre_point = text_entry.get("1.0", "end").count('.')
    nbre_point_ex = text_entry.get("1.0", "end").count('!')
    nbre_point_int = text_entry.get("1.0", "end").count('?')
    nbre_phrases = nbre_point + nbre_point_ex + nbre_point_int
    nb_phrases.delete('1.0', END)
    nb_phrases.insert('1.0', nbre_phrases)

#Nombre de caractères espace
def tot_espace():
    global text_entry
    nbre_Espace = text_entry.get("1.0", "end").count(' ')
    nb_espace.delete('1.0', END)
    nb_espace.insert('1.0', nbre_Espace)


#Choisir un mot
def choix_mot():
    global text_entry
    mot_choisi = random.choice(text_entry.get("1.0", "end").split())
    mot_rech.delete('1.0', END)
    mot_rech.insert('1.0', mot_choisi)

#Nombre d'occurence
def occurences():
    global text_entry
    mots = re.findall(r'\w+', mot_rech.get("1.0", "end"))
    # nbre_occurence = Counter(mots)
    nbre_occurence_t = OrderedDict(Counter(re.sub(r"[^a-zA-Z0-9]"," ",text_entry.get("1.0", "end")).split()).most_common())
    nbre_occurence = "\n".join({f'il y a {j} fois le mot : {i}  ' for i, j in nbre_occurence_t.items()})
    text_occurence.delete('1.0', END)
    text_occurence.insert('1.0', nbre_occurence)

#Fonction de calcul du mot le plus utilisé
def Top_mot():
    global text_entry
    #best occurence
    nbre_occurence_t = Counter(text_entry.get("1.0", "end").split())
    maxi= nbre_occurence_t.most_common()[0]
    #nbre de mots
    m=text_entry.get("1.0", "end").split()
    nbre_mot = len([re.sub(r"[^a-zA-Z0-9]"," ",i) for i in m])
    maxi_t= f'-il y a {nbre_mot} mots au total.\n' \
            f'-Le mot apparaissant le plus est: " {maxi[0]}" ; Il apparait  *{maxi[1]}*  fois\n'
    #longest word
    list_mots = text_entry.get("1.0", "end").split()
    sortedwords = sorted(list_mots, key=len)
    long_mot = f'-le plus long mot est "{sortedwords[-1]}" et contient {len(sortedwords[-1])}  caractères'
    result = maxi_t + long_mot
    mot_rech.delete('1.0', END)
    mot_rech.insert('1.0', result )



######################################################  CREATION DE LA FENETRE PRINCIPALE ##############################################################################

window = Tk()

#Personalisation de la fenetre
window.title("Application Dictionnaire")
window.geometry("1080x720")
window.iconbitmap("drapeau_fr.ico")
window.config(background='#55CAFF')


# CREATION DES PRINCIPALES CONTAINERS(FRAME)
top_frame = Frame(window, bg='#55CAFF', width=450, height=50, pady=3)
center2 = Frame(window, bg='grey', width=50, height=40, padx=3, pady=3)
center = Frame(window, bg='#55CAFF', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(window, bg='#55CAFF', width=450, height=45, pady=3)
btm_frame2 = Frame(window, bg='lavender', width=450, height=60, pady=3)


# layout all of the main containers
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

# CREATION DU WIDGET CENTRALE
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

#DEFINITION DE L'AFFICHAGES DES FRAMES
top_frame.grid(row=0, sticky="n")
center2.grid(row=1, sticky="nsew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
btm_frame2.grid(row=4, sticky="ew")

#######################################################  CREATION DES BOUTONS ET DES ZONES D'ENTREES DE TEXTE #############################################
#Création de la zone d'entré du texte
mon_texte = StringVar()
#text_entry=Entry(center, textvariable=mon_texte,width=30,font=('Arial',10),bg='white', fg='#030303')
text_entry = Text(center,height=40,width=50,font=('Arial',10) )
text_entry.grid(row=1,column=0, rowspan=6,columnspan=2, sticky="nsew" )
Entry_btn = Button(btm_frame2, text = "Valider",  command=lambda:[comptage(), tot_phrases(), tot_espace(), Top_mot(),occurences()])
Entry_btn.grid(row=6, column=1, sticky="nw")

#Bouton Total mots
Total_mot_btn = Button(center, text = "Total Mots",width=15,  command=comptage)
Total_mot_btn.grid(row=1, column=2)
total_mots = Text(center,height=2,width=40,font=("Courrier",15) ,bg='#F5E7E7')
total_mots.grid(row=1,column=3,columnspan=2, padx=2,pady=4)


#Bouton Total Phrase
nb_phrases_btn = Button(center, text = "  Nombre de Phrase",width=15, command=tot_phrases)
nb_phrases_btn.grid(row=2, column=2)
nb_phrases = Text(center,height=2,width=40,font=("Courrier",15) ,bg='#F5E7E7')
nb_phrases.grid(row=2,column=3,columnspan=2, padx=2,pady=4)

#Bouton Total Espace
nb_Espace_btn = Button(center, text = "Total espace",width=15,  command=tot_espace)
nb_Espace_btn.grid(row=3, column=2)
nb_espace = Text(center,height=2,width=40,font=("Courrier",15),bg='#F5E7E7' )
nb_espace.grid(row=3,column=3,columnspan=2,padx=2,pady=4)

#Création d'un sous titre
text_title = Label(center,text='Nombre de récurence : ', font= ("Times New Roman", 20), fg='#CB1531',bg='#DAF2E0')
text_title.grid(row=4, column=2,columnspan=2)

#Création du bouton mot recherché
mot_rech_btn = Button(center, text = "Mot recherché ",width=15,command=Top_mot)
mot_rech_btn.grid(row=5, column=2)
mot_rech = Text(center,height=5,width=60,font=("Courrier",13),bg='#F5E7E7')
mot_rech.grid(row=5,column=3,columnspan=2,padx=2,pady=4 )


# #Bouton Récurence
occurences_btn = Button(center, text = "Nombres d'occurences",width=16,command=occurences)
occurences_btn.grid(row=6, column=2, sticky="n")
text_occurence = Text(center,height=15,width=36,font=('Arial',10),bg='#F5E7E7' )
text_occurence.grid(row=6,column=3,columnspan=2, sticky="nsew", padx=4,pady=4 )


################################################################## Création des touches Menu #################################################
# #Création d'une bar menu
menu_bar = Menu(window)
# #creation du premier menu
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Dictionnaire de mots", command=dico)
file_menu.add_command(label=" Analyse de texte", command=delete)
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
# #creation du premier menu Aide
aide_menu = Menu(menu_bar,tearoff=0)
aide_menu.add_command(label="Aide", command=f_aide)
menu_bar.add_cascade(label="Aide", menu=aide_menu)


############################################################# Creation d'une image ###################################################################
width = 300
height=150
image = PhotoImage(file= "Larousse_img.png").zoom(35).subsample(60)
canvas = Canvas(top_frame, width=width, height=height, bg='#55CAFF', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2,image=image)
canvas.grid(row=0, column=3,columnspan=450,sticky='e')

# #Configuration de la fenetre pour ajouter la bar de menu
window.config(menu=menu_bar)

#Affichage de la fenetre
window.mainloop()

