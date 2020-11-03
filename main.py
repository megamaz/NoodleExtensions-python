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
# This code is awful. Please improve it.

import json, os
from pathlib import Path

def GetLocalPath(filename):
    return Path(__file__).parents[0] / filename # I still don't understand how this trick works. but it works. im fine with that.


if not os.path.exists(GetLocalPath('data.json')):
    with open('data.json', 'w', encoding="utf-8") as CreateDataJson:
        print(r"""Please insert your Beat Saber install directory. Here are some locations for you to try;
Steam
- C:\Program Files (x86)\Steam\steamapps\common\Beat Saber

Oculus
- C:\OculusApps\Software\hyperbolic-magnematism-beat-saber

IF YOU ARE USING QUEST / STANDALONE HEADSETS.
Just input NONE. You can also use this if you'd rather have a separate WIP levels location than the ingame one.
""")
        data = {}
        beatSaberDir = input(r"> ")
        if beatSaberDir.lower() != 'none': 
            if os.path.exists(beatSaberDir + '\\Beat Saber.exe'): # shit way of checking if that's a beat saber install. I hate it. but it works.
                data["customWIPLevelsPath"] = beatSaberDir + '\\Beat Saber_data\\CustomWIPLevels'
            else:
                raise FileNotFoundError("Not a Beat Saber install path.")
        else:
            data["customWIPLevelsPath"] = input("insert a path for your custom levels: ")
        

        json.dump(data, CreateDataJson)
            
