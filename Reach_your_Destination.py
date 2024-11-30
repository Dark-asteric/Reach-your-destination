# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 08:30:10 2024

@author: shafi.muhammad
"""
import random as rd
BLUE = '\033[94m'
RESET = '\033[0m'
YELLOW = '\033[93m'
RED = "\033[0;31m"
class PLATEAU:
    def __init__(self,nbcx,nbcy):
        self.nbcx = nbcx
        self.nbcy = nbcy
        self.grille = [[0 for j in range(self.nbcy)] for i in range(self.nbcx)]
        self.save = [[False for j in range(self.nbcy)] for i in range(self.nbcx)]
        self.rempli_half()
    def afficher(self,dep_x,dep_y,arr_x,arr_y,curr_x,curr_y,nom):
        for x in range(self.nbcx):
            for y in range(self.nbcy):
                if curr_x == x and curr_y == y:
                    print(BLUE + nom[0].upper() + RESET, end=" ")
                elif dep_x == x and dep_y == y:
                    print(RED + "D" + RESET,end=" ")
                elif arr_x == x and arr_y == y:
                    print(YELLOW + "A" + RESET,end=" ")
                elif self.save[x][y]:
                    print(self.grille[x][y],end=" ")
                else:
                    print("#",end=" ")
            print()
    def rempli_half(self):
        half = (self.nbcx * self.nbcy) // 2
        cnt = 0
        while True:
            x = rd.randint(0, self.nbcx - 1)
            y = rd.randint(0, self.nbcy - 1)
            if cnt < half:
                if self.grille[y][x] == 0:
                    self.grille[y][x] = rd.randint(1, 5)
                    cnt += 1
            else:
                break
    def depart(self):
        x = rd.randint(0,self.nbcx - 1)
        y = rd.randint(0,self.nbcy - 1)
        return x,y
    def arrive(self,x,y):
        while True:
            arr_x = rd.randint(0,self.nbcx - 1)
            arr_y = rd.randint(0,self.nbcy - 1)
            if arr_x != x and arr_y != y :
                return arr_x,arr_y
    def check(self,cur_x,cur_y):
        if self.grille[cur_x][cur_y] == 0:
            self.save[cur_x][cur_y] = True
            return True
        else:
            self.grille[cur_x][cur_y] -= 1
            return False

class JOUEUR:
    def __init__(self, name,life):
        self.name = name
        self.life = life

    def player_coordinate(self,x,y,nbcx,nbcy):
        move = input("Enter your direction towards -> R➡️ , L⬅️ , U⬆️, D⬇️ : ")

        if x >= 0 and x <= nbcx and y >= 0 and y <= nbcy:
            if move == 'D' or move == 'd':
                x += 1
            elif move == 'U' or move == 'u':
                x -= 1
            elif move == 'R' or move == 'r':
                y += 1
            elif move == 'L' or move == 'l':
                y -= 1
        if x < 0:
            x = 0
        elif x >= nbcx:
            x = nbcx - 1
        if y < 0:
            y = 0
        elif y >= nbcy :
            y = nbcy - 1
        return  x,y
    def decrease_life(self):
        self.life -= 1
        return self.life
    def check_win(self,vie,arr_x,arr_y,cur_x,cur_y):
        if vie != 0:
            if arr_x == cur_x and arr_y == cur_y:
                return True
        return False

    def afficher_winner(self,vie,ok):
        if vie != 0 and ok:
            print("Congratulations, You won the Game.")
        else:
            print("Better Luck next Time.")
nbx, nby = 10,10
plt = PLATEAU(10,10)
life = 10
nom = input("Enter your name : ")
dep_x, dep_y = plt.depart()
dest_x,dest_y = plt.arrive(dep_x,dep_y)
jr = JOUEUR(nom,life)
plt.afficher(dep_x,dep_y,dest_x,dest_y,dep_x,dep_y,nom)
#plt.rempli_half()
cur_pos_x, cur_pos_y = dep_x,dep_y
while True:
    cur_pos_x,cur_pos_y = jr.player_coordinate(cur_pos_x,cur_pos_y,nbx,nby)
    ok = plt.check(cur_pos_x,cur_pos_y)
    if not ok:
        cur_pos_x,cur_pos_y = dep_x,dep_y
        life = jr.decrease_life()
    plt.afficher(dep_x, dep_y, dest_x, dest_y, cur_pos_x, cur_pos_y, nom)
    ok_2 = jr.check_win(life,dest_x,dest_y,cur_pos_x,cur_pos_y)
    if life <= 0 or ok_2 == True:
        jr.afficher_winner(life,ok_2)
        break

#print()
#plt.afficher(dep_x,dep_y,dest_x,dest_y,cur_pos_x,cur_pos_y,nom)

