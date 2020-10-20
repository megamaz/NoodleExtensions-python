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
# Python Noodle Extensions Editor. I can't do ASCII, so I used http://patorjk.com/software/taag/#p=testall&h=0&v=0&f=Alpha&t=PNEE "Doh" (Pronounced the same as Knee, /nē/)


import json, argparse, os
from pathlib import Path
setupParser = argparse.ArgumentParser(description='Setup')
setupParser.add_argument('--setup', action='store_true', help='Sets up the project')
args = setupParser.parse_args()
def GetLocalPath(filename):
    return Path(__file__).parents[0] / filename

# Setup area
def Setup():
    with open(GetLocalPath('data.json'), 'w') as CreateWrite:
        if not os.path.exists(r'C:\Program Files (x86)\Steam\steamapps\common\Beat Saber'):
            raise FileNotFoundError("Beat Saber is not installed on this PC.")
        elif not os.path.exists(r'C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Plugins\NoodleExtensions.dll'):
            raise FileNotFoundError("Noodle Extensions addon is not installed on this PC. It can be found here: https://github.com/Aeroluna/NoodleExtensions/releases")
        else: # if both NoodleExtensions and Beat Saber are downloaded then no check for CustomWIPLevels / CustomLevels
            data = {
                "CustomWIPLevelsPath":r'C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomWIPLevels',
                "NoodleExtensionsLevels":[]
            }

            print("Everything has been setup. Please restart the project.")
            json.dump(data, CreateWrite)

if args.setup:
    if not os.path.exists(GetLocalPath('data.json')):
        Setup()
    else:
        os.remove(GetLocalPath('data.json')) # Delete the file and do setup again.
        Setup()