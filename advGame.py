#!/usr/bin/env python3

#WELCOME TO MY ADVENTURE GAME!
#CURRENTLY COMPLETED, BUT THE USE OF FUNCTIONS AND PROCEDURES WILL ALLOW ME TO
#UPGRADE AND EDIT THE GAME IN THE FUTURE. I PLAN TO CONVERT THIS TO AN ACTUAL
#MOBILE/WEB-BASED GAME SOME DAY, BUT NOT FOR NOW (MY PERSONAL WINTER PROJECT MAYBE?)
#BESIDES THAT, HOPE YOU ENJOY THE GAME :)

import time, random, os


StepsTaken = 0 #A variable that will keep track of how many steps the PLAYER has taken

EncounterValue = 0 #Multi-purpose var to let code know if PLAYER encountered monster, is dead, killed monster or ran away

PlayerStats = {"Health": 100,
               "Attack": 20,
               "Defense": 5,
               "Speed": 30} #PLAYER's baseline stats (Dictionary)

ElfStats = {"Health": 100,
            "Attack": 20,
            "Defense": 10,
            "Speed": 25} #Stats of Elf Monster (Dictionary)

GoblinStats = {"Health": 100,
               "Attack": 10,
               "Defense": 40,
               "Speed": 15} #Stats of Goblin Monster (Dictionary)

WolfStats = {"Health": 100,
             "Attack": 25,
             "Defense": 15,
             "Speed": 45} #Stats of Wolf Monster (Dictionary)

DemonStats = {"Health": 200,
              "Attack": 50,
              "Defense": 50,
              "Speed": 100} #Stats of Demon Monster (Dictionary)

Monsters = {"Elf": ElfStats,
            "Goblin": GoblinStats,
            "Wolf": WolfStats,
            "Demon": DemonStats} #Different types of monsters except Demon (List)

Swords = {"Broken Bronze Sword": 10,
          "Broken Steel Sword": 15,
          "Broken Iron Sword": 20,
          "Bronze Sword": 20,
          "Steel Sword": 30,
          "Iron Sword": 40,
          "Samurai's Katana": 80,
          "Useless Needle": 3,
          "Severed Arm": 1,
          "Fallen Branch": 2,
          "Dild- Weird Purple Thing": 1} #Different types of swords (Dictionary)

Armour = {"Cardboard Shoes": ["Shoes",2,0],
          "Cardboard Pants": ["Pants",2,0],
          "Cardboard Chestplate": ["Chestplate",2,0],
          "Cardboard Helmet": ["Helmet",2,0],
          "Chainmail Shoes": ["Shoes",6,2],
          "Chainmail Pants": ["Pants",9,1],
          "Chainmail Chestplate": ["Chestplate",12,1],
          "Chainmail Helmet": ["Helmet",7,1],
          "Steel Shoes": ["Shoes",9,3],
          "Steel Pants": ["Pants",12,2],
          "Steel Chestplate": ["Chestplate",15,2],
          "Steel Helmet": ["Helmet",10,2],
          "Iron Shoes": ["Shoes",19,5],
          "Iron Pants": ["Pants",22,4],
          "Iron Chestplate": ["Chestplate",25,4],
          "Iron Helmet": ["Helmet",20,4],
          "God's Will": ["Special",15,0],
          "Demon's Curse": ["Special",50,20]} #Different types of armour (Dictionary)

Potions = {"Basic Health Potion": {"BHP":25},
           "Advanced Health Potion": {"AHP":50},
           "Speed Potion": {"SPD":5},
           "Strength Potion": {"STR":10}} #Different types of potions that affect PLAYER stats (Dictionary)

CurrentEquipment = {"Sword": "None",
                    "Helmet": "None",
                    "Chestplate": "None",
                    "Pants": "None",
                    "Shoes": "None",
                    "Special": "None"} #The current equipment set of PLAYER (Dictionary)

PlayerBag = {"BHP": 0,
             "AHP": 0,
             "SPD": 0,
             "STR": 0} #Bag of PLAYER that only stores potions (Dictionary)

Thoughts = {1: "You: It's very hot, reminds me of Singapore.",
            2: "You: I hope I don't run into a demon...",
            3: "You: That's the second-biggest monkey I've ever seen!",
            4: "You: Do they have geese in Syria?",
            5: "You: I see a graveyard... Maybe I should just bury myself there.",
            6: "You: *sigh* When am I getting out of here...",
            7: "You: Human, please be careful with your choices...",
            8: "You: Damn, I'm thirsty.",
            9: "You: Starting to get hungry... Should I eat my fingers?"} #Self-thoughts while travelling


def SlowText(Text): #Procedure to print text slowly char-by-char
    for i in Text:
        if i=="\n":
            time.sleep(0.2)
            print()
        if i==".":
            print(i,end='',flush=True)
            time.sleep(0.5)
        else:
            print(i,end='',flush=True)
            time.sleep(0.1)
            
        
def ClearText(): #Procedure to clear the console
    os.system('clear')
    
            
def PromptPlayerReply(): #Function to prompt PLAYER reply to a yes/no question. Returns TRUE if yes, FALSE if no. Will also verify that PLAYER inputs yes/no
    PlayerChoice = input(" ")
    print()
    while PlayerChoice.upper() not in ("YES","NO"):
        SlowText("I NEED A YES/NO ANSWER, NOTHING ELSE.\nWHAT'S THE CHOICE?")
        PlayerChoice = input(" ")
        print()
    if PlayerChoice.upper() == "YES":
        return True
    else:
        return False
    

def InitializeGame(): #Function to initialize the game
    time.sleep(1)
    SlowText("WELCOME TO YUSUF'S ADVENTURE GAME\nDO YOU NEED THE RULES? ['YES'/'NO']")
    return PromptPlayerReply()


def PrintPlayerStats(): #Procedure to print PLAYER's stats. Called in GameRunning() to let PLAYER know their base stats
    SlowText("YOUR CURRENT STATS:\n")
    for i,j in PlayerStats.items():
        print(i, j)
        time.sleep(0.2)
    print()
    
        
def GameRules(): #Function to print game rules
    GameRulesList = ["YOU TRAVEL THROUGH A MONSTER-FILLED FOREST\n",
                     "EVERYTIME YOU CONTINUE FORWARD, SOMETHING WILL HAPPEN\n",
                     "DEPENDING ON THE SITUATION, YOU WILL HAVE CHOICES\n",
                     "YOU CAN ONLY RUN AWAY IF YOUR SPEED IS HIGHER THAN THE MONSTER'S\n",
                     "WHOEVER HAS HIGHER SPEED WILL GET TO ATTACK FIRST\n",
                     "WHEN YOU KILL A MONSTER, YOU RECEIVE +25 HP",
                     "YOUR MISSION IS TO SURVIVE UNTIL YOU EXIT THE FOREST\n",
                     "ITEMS WILL BE PICKED UP RANDOMLY\n",
                     "SWORDS WILL INCREASE YOUR ATTACK STAT\n",
                     "ARMOUR WILL INCREASE YOUR DEFENSE, BUT CAN REDUCE YOUR SPEED\n",
                     "POTIONS WILL AFFECT YOUR STATS DIRECTLY",
                     "BASIC HEALTH POTION (BHP) RESTORES 25 HP",
                     "ADVANCED HEALTH POTION (AHP) RESTORES 50 HP",
                     "SPEED POTION (SPD) ADDS +5 SPEED",
                     "STRENGTH POTION (STR) ADDS +10 STRENGTH\n",
                     "THERE ARE DIFFERENT TYPES OF MONSTERS: ELVES, GOBLINS, WOLVES AND DEMONS\n",
                     "I SUGGEST YOU AVOID THE DEMONS.\n",
                     "BTW, CAPITALIZATION IN YOUR ANSWERS DON'T MATTER\n",
                     "ALL THE BEST, GOOD LUCK\n"]
    for i in GameRulesList:
        print(i)
        time.sleep(0.2)
    time.sleep(1)
    SlowText("READY TO START? [YES/NO]")
    return PromptPlayerReply()


def PromptChangeSword(PickedUp): #Function to prompt PLAYER if they want to replace their sword
    SwordText = "(+" + str(PickedUp[1]) + " ATTACK)"
    SlowText(SwordText)
    SlowText("\nYOUR CURRENT EQUIPMENT SET:\n")
    for i,j in CurrentEquipment.items():
        print(i+":", j)
        time.sleep(0.2)
    print()
    SlowText("CHANGE? [YES/NO]")
    return PromptPlayerReply()


def PickedUpSword(): #Procedure to be called when PLAYER picks up new sword
    SwordsList = list(Swords.items())
    PickedUp = random.choice(SwordsList)
    SwordText = "PICKED UP SWORD: " + PickedUp[0]
    SlowText(SwordText)
    print("\n")
    PlayerStats["Attack"] += PickedUp[1]
    if PromptChangeSword(PickedUp) == True:
        CurrentEquipment["Sword"] = PickedUp[0]
        SlowText("You: Greedy, aren't we?")
        time.sleep(1)
        print("\n")
    else:
        PlayerStats["Attack"] -= PickedUp[1]
    SlowText("CHECK UPDATED STATS? [YES/NO]")
    if PromptPlayerReply() == True:
        PrintPlayerStats()
    else:
        pass
    
    
def ReplaceArmour(PickedUp): #Procedure to change speed of PLAYER if they decide to pick up the found armour
    PlayerStats["Speed"] -= PickedUp[1][2]
    SlowText("You: Uhh.. All I'm hoping for is to not die...")
    time.sleep(1)
    print("\n")
    
    
def PromptChangeArmour(PickedUp): #Function to prompt PLAYER if they want to replace their armour
    ArmourText = "(+" + str(PickedUp[1][1]) + " DEFENSE, -" + str(PickedUp[1][2]) + " SPEED)"
    SlowText(ArmourText)
    SlowText("\nYOUR CURRENT EQUIPMENT SET:\n")
    for i,j in CurrentEquipment.items():
        print(i+":", j)
        time.sleep(0.2)
    print()
    SlowText("CHANGE? [YES/NO]")
    return PromptPlayerReply()


def PickedUpArmour(): #Procedure that calls PromptChangeArmour and ReplaceArmour when PLAYER picks up new armour. If PLAYER defense is already 100, tells user they have max defense and doesn't change stats
    ArmourList = list(Armour.items())
    PickedUp = random.choice(ArmourList)
    ArmourText = "PICKED UP ARMOUR: " + PickedUp[0]
    SlowText(ArmourText)
    print("\n")
    PlayerStats["Defense"] += PickedUp[1][1]
    if PromptChangeArmour(PickedUp) == True:
        ArmourChange = PickedUp[1][0]
        CurrentEquipment[ArmourChange] = PickedUp[0]
        ReplaceArmour(PickedUp)
    else:
        PlayerStats["Defense"] -= PickedUp[1][1]
    SlowText("CHECK UPDATED STATS? [YES/NO]")
    if PromptPlayerReply() == True:
        PrintPlayerStats()
    else:
        pass
    

def PrintPlayerBag(): #Procedure to display contents of PLAYER's bag
    SlowText("YOUR CURRENT ITEMS:\n")
    for i,j in PlayerBag.items():
        print(i,"x"+str(j))
        time.sleep(0.2)
    print()
        

def PickedUpPotion(): #Procedure to be called when PLAYER finds picks up a potion
    PotionsList = list(Potions.items())
    PickedUp = random.choice(PotionsList)
    PotionsText = "PICKED UP POTION: " + PickedUp[0]
    SlowText(PotionsText)
    print("\n")
    PotionsList2 = list(PickedUp[1])
    PlayerBag[PotionsList2[0]] += 1
    SlowText("CHECK YOUR BAG? [YES/NO]")
    if PromptPlayerReply() == True:
        PrintPlayerBag()
    else:
        pass
    

def PromptPotion(): #Function to let PLAYER use potions that have been picked up. If none, tells PLAYER that bag is empty
    NumPotions = sum(PlayerBag.values()) #NumPotions initialized as a temp var to check if bag is empty
    while NumPotions!=0:
        PrintPlayerStats()
        PrintPlayerBag()
        SlowText("WHICH POTION TO USE ([BHP]/[AHP]/[SPD]/[STR]) OR [E]EXIT?")
        PlayerChoice = input(" ")
        print()
        while PlayerChoice.upper() not in ("BHP","AHP","SPD","STR","E"):
            SlowText("THAT'S NOT ONE OF THE OPTIONS.\nWHAT'S THE CHOICE?")
            PlayerChoice = input(" ")
            print()
        if PlayerChoice.upper()=="E":
            return
        while PlayerBag[PlayerChoice.upper()]==0:
            SlowText("YOU DON'T HAVE THAT POTION.\nWHAT'S THE CHOICE?")
            PlayerChoice = input(" ")
            print()
        ExitValue = 0 #Temp var that keeps PLAYER in a loop of using potions. Exits if PLAYER chooses to return to battle
        while ExitValue == 0:
            if PlayerChoice.upper()=="BHP":
                SlowText("RESTORED 10HP!\n")
                PlayerStats["Health"] += Potions["Basic Health Potion"][PlayerChoice.upper()]
                PlayerBag[PlayerChoice.upper()] -= 1
            elif PlayerChoice.upper()=="AHP":
                SlowText("RESTORED 25HP!\n")
                PlayerStats["Health"] += Potions["Advanced Health Potion"][PlayerChoice.upper()]
                PlayerBag[PlayerChoice.upper()] -= 1
            elif PlayerChoice.upper()=="SPD":
                SlowText("ADDED +2 SPEED!\n")
                PlayerStats["Speed"] += Potions["Speed Potion"][PlayerChoice.upper()]
                PlayerBag[PlayerChoice.upper()] -= 1
            else:
                SlowText("ADDED +2 ATTACK!\n")
                PlayerStats["Attack"] += Potions["Strength Potion"][PlayerChoice.upper()]
                PlayerBag[PlayerChoice.upper()] -= 1
            SlowText("RETURN TO BATTLE? [YES/NO]")
            if PromptPlayerReply() == True:
                ClearText()
                return
            else:
                NumPotions -= 1
                ExitValue = -1
                ClearText()
    else:
        SlowText("YOUR BAG IS EMPTY.")  
        return
    
    
def TravellingThoughts(): #Procedure to print one of the nine "self-thoughts"
    RandomThought = Thoughts[random.randint(1,9)]
    SlowText(RandomThought)
    print("\n")
    
    
def PrintMonsterStats(EncounteredMonster): #Procedure to print the stats of the encountered monster
    for i,j in Monsters[EncounteredMonster].items():
        print(i+":", j)
        time.sleep(0.3)
    print()
    
    
def CompareSpeed(EncounteredMonster): #Function to compare the speed of PLAYER and encountered monster
    if PlayerStats["Speed"]>Monsters[EncounteredMonster]["Speed"]:
        return True
    else:
        return False
    

def ResetMonsterStats(EncounteredMonster):
    Monsters[EncounteredMonster]["Health"] = 100
    
    
def EncounterMonster(EncounterValue): #Function to be called when PLAYER encounters a monster
    EncounterValue = 1
    MonsterList = list(Monsters)
    EncounteredMonster = random.choice(MonsterList)
    while EncounteredMonster == "Demon":
        EncounteredMonster = random.choice(MonsterList)
    SlowText("YOU ENCOUNTERED: "+EncounteredMonster+"\n")
    PrintMonsterStats(EncounteredMonster)
    PrintPlayerStats()
    while True:
        BattleChoice = PromptBattleChoice()
        if BattleChoice=="R": #If PLAYER chooses to run, calls CompareSpeed(). If PLAYER spd > monster spd, run away from battle
            if CompareSpeed(EncounteredMonster)==True:
                SlowText("SUCCESSFULLY RAN AWAY!")
                EncounterValue = 2
                break
            else:
                SlowText("SORRY, YOUR SPEED IS LOWER THAN THE MONSTER")
                continue
        elif BattleChoice=="P":
            ClearText()
            PromptPotion()
            ClearText()
            SlowText(EncounteredMonster+" STATS:\n")
            PrintMonsterStats(EncounteredMonster)
            PrintPlayerStats()
        else:
            IsPlayerDead = Attack(EncounteredMonster)
            if IsPlayerDead==False:
                EncounterValue = -1
                break
            else:
                EncounterValue = 0
                break
    ResetMonsterStats(EncounteredMonster)
    return EncounterValue
            

def EncounterDemon(EncounterValue): #Function to be called if PLAYER encounters Demon
    EncounterValue = 1
    SlowText("YOU ENCOUNTERED: Demon\n")
    PrintMonsterStats("Demon")
    PrintPlayerStats()
    while True:
        BattleChoice = PromptBattleChoice()
        if BattleChoice=="R": #If PLAYER chooses to run, calls CompareSpeed(). If PLAYER spd > monster spd, run away from battle
            if CompareSpeed("Demon")==True:
                SlowText("SUCCESSFULLY RAN AWAY!")
                EncounterValue = 2
                break
            else:
                SlowText("SORRY, YOUR SPEED IS LOWER THAN THE MONSTER")
                continue
        elif BattleChoice=="P":
            ClearText()
            PromptPotion()
            ClearText()
            SlowText("Demon STATS:\n")
            PrintMonsterStats("Demon")
            PrintPlayerStats()
        else:
            IsPlayerDead = Attack("Demon")
            if IsPlayerDead==False:
                EncounterValue = -1
                break
            else:
                EncounterValue = 0
                break
    ResetMonsterStats("Demon")
    return EncounterValue
            
    
def Attack(EncounteredMonster): #Function to be called when PLAYER chooses to [A]Attack
    if CompareSpeed(EncounteredMonster)==True:
        Monsters[EncounteredMonster]["Health"]-=(PlayerStats["Attack"]-Monsters[EncounteredMonster]["Defense"])
        SlowText("YOU ATTACKED! YOU DID "+str(PlayerStats["Attack"])+" DAMAGE\n")
        if Monsters[EncounteredMonster]["Health"]<=0:
            SlowText(EncounteredMonster+" DIED! HEALTH RESTORED BY 25HP")
            PlayerStats["Health"] += 25
            return True
        PlayerStats["Health"]-=(Monsters[EncounteredMonster]["Attack"]-PlayerStats["Defense"])
        SlowText(EncounteredMonster+" ATTACKED! IT DID "+str(Monsters[EncounteredMonster]["Attack"])+" DAMAGE\n")
        if PlayerStats["Health"]<=0:
            return False
        time.sleep(2)
        ClearText()
        SlowText(EncounteredMonster+" STATS:\n")
        PrintMonsterStats(EncounteredMonster)
        PrintPlayerStats()
    else:
        PlayerStats["Health"]-=(Monsters[EncounteredMonster]["Attack"]-PlayerStats["Defense"])
        SlowText(EncounteredMonster+" ATTACKED! IT DID "+str(Monsters[EncounteredMonster]["Attack"])+" DAMAGE\n")
        if PlayerStats["Health"]<=0:
            return False
        Monsters[EncounteredMonster]["Health"]-=(PlayerStats["Attack"]-Monsters[EncounteredMonster]["Defense"])
        SlowText("YOU ATTACKED! YOU DID "+str(PlayerStats["Attack"])+" DAMAGE\n")
        if Monsters[EncounteredMonster]["Health"]<=0:
            SlowText(EncounteredMonster+" DIED! HEALTH RESTORED BY 25HP")
            PlayerStats["Health"] += 25
            return True
        time.sleep(2)
        ClearText()
        SlowText(EncounteredMonster+" STATS:\n")
        PrintMonsterStats(EncounteredMonster)
        PrintPlayerStats()
        

def PrintEquipment(): #Procedure to print PLAYER's current equipment
    for i,j in CurrentEquipment.items():
        while j!="None":
            print(i+":", j, end='')
            if i!="Sword":
                print(" (+"+str(Armour[j][1])+" DEFENSE)")
                break
            else:
                print(" (+"+str(Swords[j])+" ATTACK)")
                break
        else:
            print(i+":", j)
        time.sleep(0.3)
    print()
    
    
def PromptBattleChoice(): #Prompts player if they want to attack or run
    SlowText("[A]ATTACK, [R]RUN OR [P]USE POTION?")
    PlayerChoice = input(" ")
    print()
    while PlayerChoice.upper() not in ("A","R","P"):
        SlowText("THAT'S NOT ONE OF THE OPTIONS.\nWHAT'S THE CHOICE?")
        PlayerChoice = input(" ")
        print()
    return PlayerChoice.upper()

    
def PromptPlayerAction(): #Function to prompt PLAYER's choice of action
    PlayerChoice = input(" ")
    print()
    while PlayerChoice.upper() not in ("E","S","F"):
        SlowText("THAT'S NOT ONE OF THE OPTIONS.\nWHAT'S THE CHOICE?")
        PlayerChoice = input(" ")
        print()
    if PlayerChoice.upper() == "E":
        ClearText()
        SlowText("YOUR EQUIPMENT:\n")
        PrintEquipment()
        PrintPlayerBag()
        return
    elif PlayerChoice.upper() == "S":
        ClearText()
        PrintPlayerStats()
        return
    else:
        return True
    
    
def PlayerAction(): #Procedure that asks the PLAYER what they wish to do (if no encounter with a monster)
    SlowText("WHAT WOULD YOU LIKE TO DO?\n[E]SEE YOUR EQUIPMENT, [S]SEE STATS OR [F]CONTINUE FORWARD?")
    PlayerChoice = PromptPlayerAction()
    while PlayerChoice!=True:
        SlowText("WHAT WOULD YOU LIKE TO DO?\n[E]SEE YOUR EQUIPMENT, [S]SEE STATS OR [F]CONTINUE FORWARD?")
        PlayerChoice = PromptPlayerAction()
    else:
        EncounterValue = WalkingThroughForest(StepsTaken)
        if EncounterValue==0:
            SlowText("YOU ARE DEAD. GAME OVER")
        else:
            pass
    

def WalkingThroughForest(StepsTaken): #Procedure to be called if PLAYER chooses to take a step forward
    ClearText()
    StepsTaken += 1
    SlowText("YOU WALK THROUGH THE FOREST AND THINK TO YOURSELF...\n")
    TravellingThoughts()
    time.sleep(5)
    ActionValue = random.randint(1,4)
    if StepsTaken<20:
        if ActionValue==1:
            if StepsTaken%5==0 and random.randint(1,10)==7:
                EncounterValue = EncounterDemon()
                if EncounterValue in (-1,2):
                    pass
                else:
                    return EncounterValue
            else:
                EncounterValue = EncounterMonster(EncounterValue)
                if EncounterValue in (-1,2):
                    pass
                else:
                    return EncounterValue
        elif ActionValue==2:
            PickedUpSword()
        elif ActionValue==3:
            PickedUpArmour()
        else:
            PickedUpPotion()
        

def GameRunning(): #The main game
    ClearText()
    SlowText("LOADING...")
    time.sleep(5)
    ClearText()
    if InitializeGame() == True:
        ClearText()
        if GameRules() == True:
            ClearText()
            pass
        else:
            ClearText()
            SlowText("WELL, THAT'S UNFORTUNATE. YOU MAY CLOSE THE GAME YOURSELF THEN.")
            return
    PrintPlayerStats()
    time.sleep(5)
    ClearText()
    while StepsTaken<20:
        PlayerAction()
    else:
        SlowText("CONGRATULATIONS! YOU SUCCESFULLY EXITED THE FOREST!")
        time.sleep(2)
        SlowText("GAME OVER")
        return
    

GameRunning()