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
                'CustomWIPLevelsPath':install_loc + '\\BeatSaber_data\\CustomWIPLevels',
                'NoodleExtensionsLevels':[]
            }
            with open(GetLocalPath('data.json'), 'w') as SetupData:
                json.dump(data, SetupData)
                print("Setup Successfull.")
                needs_setup = False
with open(GetLocalPath('data.json'), 'r') as GetData:
    data = json.load(GetData)
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
        
        if not os.path.exists(rf'{data["CustomWIPLevelsPath"]}\{wipLevelFolder}\{difficulty}{charact}.dat'):
            if not os.path.exists(rf'{data["CustomWIPLevelsPath"]}\{wipLevelFolder}\{difficulty}.dat'):
                if not os.path.exists(rf'{data["CustomWIPLevelsPath"]}\{wipLevelFolder}\{difficulty}Standard.dat'):
                    raise FileNotFoundError("This difficulty does not exist.")
                else:
                    with open(rf'{data["CustomWIPLevelsPath"]}\{wipLevelFolder}\{difficulty}Standard.dat', 'r') as GetDiff:
                        return json.load(GetDiff)
            else:
                with open(rf'{data["CustomWIPLevelsPath"]}\{wipLevelFolder}\{difficulty}.dat', 'r') as GetDiff:
                    return json.load(GetDiff)
        else:
            with open(rf'{data["CustomWIPLevelsPath"]}\{wipLevelFolder}\{difficulty}{charact}.dat', 'r') as GetDiff:
                return json.load(GetDiff)
print('''
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