import sys

from noodle_extensions import Editor, Animator
from noodle_extensions.constants import EventType, Animations

editor = Editor(r"C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomWIPLevels\ExampleLevel\EasyStandard.dat")
animator = Animator(editor)


def test_createDummyEvent():
    animator.animate("AnimateTrack", "_position", [[0, 0]], "DummyTrach", 0, 3)
    assert True
def test_UpdateReqs():
    assert "Noodle Extensions" in editor.updateDependencies("Noodle Extensions") 
    
def test_editNote():
    beat = 14
    pos = (2,0)
    track = "TestTrack"
    assert editor.editBlock(beat, pos, track) == {
            "_time": 14,
            "_lineIndex": 2,
            "_lineLayer": 0,
            "_type": 1,
            "_cutDirection": 1,
            "_customData" : {
                "_track":track,
                "_fake":False,
                "_interactable":True
            }
        }
def test_editWall():
    beat = 18
    length = 18+6 # start beat + length of wall
    index = 3
    assert editor.editWall(beat, length, index, "TestTrack") == {
        
            "_time": 18,
            "_lineIndex": 3,
            "_type": 0,
            "_duration": 6,
            "_width": 1,
            "_customData": {
                "_track": "TestTrack",
                "_fake": False,
                "_interactable": True
            }
        }

def test_getBlock():
    beat = 14
    pos = (2,0)
    track = "TestTrack"
    block = editor.getBlock(beat, pos)
    assert block == {
            "_time": 14,
            "_lineIndex": 2,
            "_lineLayer": 0,
            "_type": 1,
            "_cutDirection": 1,
            "_customData" : {
                "_track":track,
                "_fake":False,
                "_interactable":True
            }
        }

def test_getWall():
    beat = 18
    length = 18+6 # start beat + length of wall
    index = 3
    wall = editor.getWall(beat, index, length)
    assert wall == {
            "_time": 18,
            "_lineIndex": 3,
            "_type": 0,
            "_duration": 6,
            "_width": 1,
            "_customData": {
                "_track": "TestTrack",
                "_fake": False,
                "_interactable": True
            }
        }

def test_removeEvent():
    assert editor.removeEvent(0, "AnimateTrack", "DummyTrach") == {
                "_time": 0,
                "_type": "AnimateTrack",
                "_data": {
                    "_track": "DummyTrach",
                    "_duration": 3,
                    "_position": [
                        [
                            0,
                            0
                        ]
                    ]
                }
            }