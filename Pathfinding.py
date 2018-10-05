import numpy as np

map = np.array([[0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
       [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
       [0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
       [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
       [0,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

start = (3,3)
end = (6,12)


class Noeud:
    """Classe définissant un noeud"""

    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        
        self.f = 0
        self.g = 0
        self.h = 0

    
def A_star(map, start, end):
    
    noeud_start = Noeud(None, start)
    noeud_end = Noeud(None, end)

    liste_ouverte = [noeud_start]
    liste_fermee = [noeud_start]
    

    while len(liste_ouverte) > 0:

        
        
        noeud_actuel = liste_fermee[-1]
        liste_enfant = []

        if noeud_actuel.position == noeud_end.position:
              break
        
        for enfant in [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            
            nouv_pos = (enfant[0] + noeud_actuel.position[0], enfant[1] + noeud_actuel.position[1])

            #est en dehors de la map
            if nouv_pos[0]<0 or nouv_pos[1]<0 or nouv_pos[0]>=len(map) or nouv_pos[1]>=len(map[0]):
                continue
            
            #est un obstacle
            if map[nouv_pos[0]][nouv_pos[1]] == 1:
                continue

            nouv_noeud = Noeud(noeud_actuel,nouv_pos)
            nouv_noeud.g = noeud_actuel.g + (noeud_actuel.position[0] - nouv_pos[0])**2 + (noeud_actuel.position[1] - nouv_pos[1])**2
            nouv_noeud.h = (noeud_end.position[0] - nouv_noeud.position[0])**2 + (noeud_end.position[1] - nouv_noeud.position[1])**2
            nouv_noeud.f = nouv_noeud.g + nouv_noeud.h

            #On ne garde pas un noeud qui a la même position et le même parent qu'un noeud de la liste fermée
            est_dans_liste_fermee = False

            for n in liste_fermee:
                if nouv_noeud.parent != None and n.parent != None :
                    if nouv_noeud.parent.position == n.parent.position and nouv_noeud.position == n.position:
                        est_dans_liste_fermee = True
                        
            if not(est_dans_liste_fermee):
                liste_enfant.append(nouv_noeud)

        for enfant in liste_enfant:            

            for m in liste_ouverte:
                if m.position == enfant.position and enfant.f < m.f:
                    liste_ouverte.remove(m)

            liste_ouverte.append(enfant)

        #On sélectionne le meilleur noeud de la liste ouverte pour le mettre dans la liste fermée
        maximum = liste_ouverte[0].f
        meilleur_noeud = liste_ouverte[0]

        for i in liste_ouverte:
            if i.f < maximum:
                meilleur_noeud = i
                maximum = i.f

        liste_ouverte.remove(meilleur_noeud)
        liste_fermee.append(meilleur_noeud)

    liste_fermee.reverse()    
    parent = liste_fermee[0]

    if parent.position != end:
        return "Pas de chemin possible"
        
    for path in liste_fermee:
        if path == parent:
            parent = path.parent
            map[path.position[0]][path.position[1]] = 2

    return print(map)

            
                                                                                                
                    
                    
                        
                    
            
                
            
        
        
