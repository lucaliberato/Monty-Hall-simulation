#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:19:25 2024

@author: lucaliberato
"""

import random

class Door:
    def __init__(self, my_game):
        self.my_game = my_game          # car or goat
        self.door_open = False

class Game:
    def __init__(self):
        self.tot_games = 0
        self.tot_wins = 0

    def create_doors(self):
        doors = [Door("goat"), Door("goat"), Door("car")]           # call Door class 
        random.shuffle(doors)
        return doors

    def goat(self, doors, index):
        for i in range(len(doors)):                             # indice porta in doors
            if i != index and doors[i].my_game == "goat":       # verifica indice porta != scelta player e che contiene una capra
                doors[i].door_open = True
                break

    def print_doors(self, doors):
        for i, door in enumerate(doors):        # itera indici e oggetti della porta
            if door.door_open:
                print(f"Door {i + 1}: Door opened. [🐐]")
            else:
                print(f"Door {i + 1}: Door closed")
                

    def play_game(self):
        doors = self.create_doors()                                 # Metodo per creare porte

        print("Welcome to the Let's Make a Deal game!")
        while True:
            self.print_doors(doors)                                     # stampa le porte
            try:
                index = int(input("Choose a door (1, 2, or 3): ")) - 1      # verifica indici relativi alle porte
                if index in range(0,3):
                    break
                else:
                    print("\nEnter a valid number\n")
            except:
                print("\nEnter a valid number\n")

        self.goat(doors, index)                                 # chiama goat per aprire una porta
        self.print_doors(doors)                                 # printa porte aperte e chiuse

        try:
            change_choice = input("Do you want to change your choice? (y/n): ").lower()
            if change_choice not in ["y", "n"]:
                raise ValueError("Invalid choice")
        except ValueError:
            print("\nEnter a valid choice (y/n)\n")
            return False
        
        if change_choice:
            remaining_index = [i for i, door in enumerate(doors) if i != index and not door.door_open][0]
            index = remaining_index

        if doors[index].my_game == "car":
            print("\nCongratulations! You won the car!!! [🏎️]")
            return True
        else:
            print("\nOh... you got a goat. [🐐] Try again if you feel lucky. ")
            return False
        
    def run_game(self):                                 # run game untill different choice
        while True:
            won = self.play_game()
            self.tot_games += 1
            if won:
                self.tot_wins += 1

            while True:
                play_again = input("\nDo you want to play again? (y/n): ").lower()
                if play_again in ["y", "n"]:
                    break
                else:
                    print("\nEnter a valid choice (y/n)\n")
    
            if play_again == "n":
                break
        
        trattino()
        print(f"\nTotal games played: {self.tot_games}")
        print(f"Total cars won: {self.tot_wins} 🏎️")
        
        if self.tot_wins > (self.tot_games - self.tot_wins):                        # Ultimo saluto
            trattino()
            print("\nYou were very lucky today, you won a lot of cars 🏎️!!")
        else:
            trattino()
            print("\nSee you next time to win more cars!!")
                
def trattino():
    print("-----------------------------------------")     
        
game = Game()
game.run_game()


