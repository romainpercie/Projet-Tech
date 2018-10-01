import numpy as np

map = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
       [0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
       [0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
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

            liste_enfant.append(nouv_noeud)

        for enfant in liste_enfant:

            for n in liste_fermee:
                if enfant.position == n.position:
                    continue

            for m in liste_ouverte:
                if m.position == nouv_noeud.position and nouv_noeud.f < n.f:
                    liste_ouverte.remove(m)
                if m.position == nouv_noeud.position and nouv_noeud.f > n.f:
                    continue

            liste_ouverte.append(enfant)

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
        
    for path in liste_fermee:
        if path == parent:
            parent = path.parent
            map[path.position[0]][path.position[1]] = 2

    return print(map)

            
                                                                                                
                    
                    
                        
                    
            
                
            
        
        
