# PPPPPPPPPPPPPPPPP   NNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# P::::::::::::::::P  N:::::::N       N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
# P::::::PPPPPP:::::P N::::::::N      N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
# PP:::::P     P:::::PN:::::::::N     N::::::NEE::::::EEEEEEEEE::::EEE::::::EEEEEEEEE::::E
#   P::::P     P:::::PN::::::::::N    N::::::N  E:::::E       EEEEEE  E:::::E       EEEEEE
#   P::::P     P:::::PN:::::::::::N   N::::::N  E:::::E               E:::::E             
#   P::::PPPPPP:::::P N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE     E::::::EEEEEEEEEE   
#   P:::::::::::::PP  N::::::N N::::N N::::::N  E:::::::::::::::E     E:::::::::::::::E   
#   P::::PPPPPPPPP    N::::::N  N::::N:::::::N  E:::::::::::::::E     E:::::::::::::::E   
#   P::::P            N::::::N   N:::::::::::N  E::::::EEEEEEEEEE     E::::::EEEEEEEEEE   
#   P::::P            N::::::N    N::::::::::N  E:::::E               E:::::E             
#   P::::P            N::::::N     N:::::::::N  E:::::E       EEEEEE  E:::::E       EEEEEE
# PP::::::PP          N::::::N      N::::::::NEE::::::EEEEEEEE:::::EEE::::::EEEEEEEE:::::E
# P::::::::P          N::::::N       N:::::::NE::::::::::::::::::::EE::::::::::::::::::::E
# P::::::::P          N::::::N        N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
# PPPPPPPPPP          NNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE    
#                       
# Python Noodle Extensions Editor. (Great name, I know.) I can't do ASCII, so I used http://patorjk.com/software/taag/#p=testall&h=0&v=0&f=Alpha&t=PNEE "Doh" (Pronounced the same as Knee, /nē/)
# This code is awfully simple. Please improve it.

import json, os
from pathlib import Path
def GetLocalPath(filename):
    return Path(__file__).parents[0] / filename

# Setup area
needs_setup = not os.path.exists(GetLocalPath('data.json'))

if needs_setup:
    while needs_setup:
        install_loc = input("Insert Beat Saber install location: ")
        while not os.path.exists(install_loc):
            print("This folder does not exist. ")
            install_loc = input("Insert Beat Saber install location: ")
        
        if not os.path.exists(install_loc + '\\Beat Saber.exe'): # bad way to check, but at least it works.
            print("that is not a beat saber install directory.")
        
        else:
            data = {
                'CustomWIPLevelsPath':install_loc + '\\Beat Saber_data\\CustomWIPLevels',
                "promptType":False,
                'NoodleExtensionsLevels':[]
            }
            with open(GetLocalPath('data.json'), 'w') as SetupData:
                json.dump(data, SetupData)
                print("Setup Successfull.")
                needs_setup = False
with open(GetLocalPath('data.json'), 'r') as GetData:
    data = json.load(GetData)


if not os.path.exists(GetLocalPath('levels.json')): # Since if you don't have a levels.json, it would mean your first time using the editor (they contain info such as tracks)
    with open(GetLocalPath('levels.json'), 'w') as create:
        json.dump({}, create)
        print("First time using the editor! Welcome! Documentation found on the GitHub as the README.md (https://github.com/megamaz/NoodleExtensions-python/blob/master/README.md)")
# Editor time!
def OpenLevel(wipLevelFolder, difficulty, charact='Standard'):
    # Found out lately that functions use MarkDown for their description. I'm a god now.
    '''
    # OpenLevel
    .dat files are just renamed .json files.
    returns: `LEVEL.dat` as a Dictionary
    - wipLevelFolder\n
    Not the `CustomWIPLevels`, but the folder containing the `LEVEL.dat` and `info.dat`. 
    - difficulty\n
    The difficulty (ranging from Easy to ExpertPlus)
    type: `str`
    - charact
    The type (Defaults to 'standard')
    '''
    global data
    if not os.path.exists(rf'{data["CustomWIPLevelsPath"]}\{wipLevelFolder}'):
        raise FileNotFoundError("This level does not exist.")
    else:
        with open(f'{data["CustomWIPLevelsPath"]}\\{wipLevelFolder}\\info.dat', 'r') as GetReq:
            reqs = json.load(GetReq)
        
        with open(f'{data["CustomWIPLevelsPath"]}\\{wipLevelFolder}\\info.dat', 'w') as AddReq:
            for levels in range(len(reqs["_difficultyBeatmapSets"])):
                if reqs["_difficultyBeatmapSets"][levels]["_beatmapCharacteristicName"] == charact:
                    for diffs in range(len(reqs["_difficultyBeatmapSets"][levels]["_difficultyBeatmaps"])):
                        if reqs["_difficultyBeatmapSets"][levels]["_difficultyBeatmaps"][diffs]["_difficulty"] ==  difficulty: # jesus fuck
                            if 'Noodle Extensions' not in reqs["_difficultyBeatmapSets"][levels]["_difficultyBeatmaps"][diffs]["_customData"]["_requirements"]:
                                reqs["_difficultyBeatmapSets"][levels]["_difficultyBeatmaps"][diffs]["_customData"]["_requirements"].append('Noodle Extensions') # Do note this is JUST to add the requirement of Noodle Extensions automatically.
                                break
            json.dump(reqs, AddReq)
        
        diffic_path = rf'{data["CustomWIPLevelsPath"]}\{wipLevelFolder}\{difficulty}'
        if not os.path.exists(f'{diffic_path}.dat'):
            if not os.path.exists(f'{diffic_path}{charact}.dat'):
                raise FileNotFoundError("This difficulty does not exist.")
            else:
                with open(f'{diffic_path}{charact}.dat', 'r') as GetDiff:
                    return json.load(GetDiff)
        else:
            with open(f'{diffic_path}.dat', 'r') as GetDiff:
                return json.load(GetDiff)

# User Interface (UI) or rather, the actual editor the user will be using to animate and stuff. 

# The editor isn't an actual 3D thing or whatever. It's a CMD - although it quickly gets annoying
# To edit, at least it's faster than manually editing a JSON file. 
def Editor(leveldata, levelfolder):
    '''
    The actual editor where the user will be able to... well edit.
    - leveldata\n
    The data gained from `OpenLevel`
    - levelpath\n
    The level difficulty path. not the folder, the difficulty (StandardExpertPlus.dat)
    '''
        






print(f'''
PPPPPPPPPPPPPPPPP   NNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
P::::::::::::::::P  N:::::::N       N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
P::::::PPPPPP:::::P N::::::::N      N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
PP:::::P     P:::::PN:::::::::N     N::::::NEE::::::EEEEEEEEE::::EEE::::::EEEEEEEEE::::E
  P::::P     P:::::PN::::::::::N    N::::::N  E:::::E       EEEEEE  E:::::E       EEEEEE
  P::::P     P:::::PN:::::::::::N   N::::::N  E:::::E               E:::::E             
  P::::PPPPPP:::::P N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE     E::::::EEEEEEEEEE   
  P:::::::::::::PP  N::::::N N::::N N::::::N  E:::::::::::::::E     E:::::::::::::::E   
  P::::PPPPPPPPP    N::::::N  N::::N:::::::N  E:::::::::::::::E     E:::::::::::::::E   
  P::::P            N::::::N   N:::::::::::N  E::::::EEEEEEEEEE     E::::::EEEEEEEEEE   
  P::::P            N::::::N    N::::::::::N  E:::::E               E:::::E             
  P::::P            N::::::N     N:::::::::N  E:::::E       EEEEEE  E:::::E       EEEEEE
PP::::::PP          N::::::N      N::::::::NEE::::::EEEEEEEE:::::EEE::::::EEEEEEEE:::::E
P::::::::P          N::::::N       N:::::::NE::::::::::::::::::::EE::::::::::::::::::::E
P::::::::P          N::::::N        N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
PPPPPPPPPP          NNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE 

A Python based Beat Saber Noodle Extensions Editor (Python Noodle Extensions Editor)
''')
# print("Warning! it is REQUIRED that you have your level already mapped for this! Block positions don't have to be perfect, you can edit those directly in here.") 
# You can now directly place blocks in PNEE.
level = input("\nInsert level name: ").lower()
match = False
matches = []
for x in os.listdir(data["CustomWIPLevelsPath"]):
    if level in x.lower():
        match = True
        matches.append(x)
if match:
    print("Here is a list with levels similar to what you entered:")
    for y in range(len(matches)):
        print(f'{y+1}. {matches[y]} ')
    print("Insert the number to quickly open that level\n")
    try:
        level = int(input('> '))

    except:
        raise TypeError("Not a number.")

    if level > len(matches):
        raise OverflowError("Item exited the bounds of the level list.")
    else:
        diff =input("Insert Difficulty (ExpertPlus, not Expert+): ")
        lvltype = 'Standard'
        if bool(data["promptType"]):
            lvltype = input("Insert Level type (default is Standard.): ")
        print("Loading Level...")
        EditorLevel = OpenLevel(matches[level-1], difficulty=diff, charact=lvltype)
        print("Loading Editor...")
        print('\n'*100) # Clear the terminal. (user can still scroll up.)
        Editor(EditorLevel, f'{data["CustomWIPLevelsPath"]}\\{matches[y-1]}')
else:
    print("No levels matched your input. ")