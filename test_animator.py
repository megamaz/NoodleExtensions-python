import sys

from noodle_extensions import Editor, Animator
from noodle_extensions.constants import EventType, Animations

editor = Editor(r"C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomWIPLevels\ExampleLevel\EasyStandard.dat")
animator = Animator(editor)


def test_animate():
    assert animator.animate("AnimateTrack", "_position", [[0, 0]], "DummyTrach", 0, 3) == {
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

def test_animateBlock():
    # pos = Animations().position
    assert animator.animateBlock(14, (2, 0), Animations().position, [[0, 0]]).get("_position") is not None

def test_animateWall():
    assert animator.animateWall(18, 6, 3, Animations().position, [[0, 0]]).get("_position") is not None

def test_editTrack():
    #AssignPlayerToTrack
    data = animator.editTrack("AssignPlayerToTrack", 5, "TestTrack")
    assert data == {
        "_time":5,
        "_type":"AssignPlayerToTrack",
        "_data":{
            "_track":"TestTrack"
        }
    }

def test_editTrack2():
    #AssignTrackParent
    data = animator.editTrack("AssignTrackParent", 5, "TestTrack", "ParentTrack")
    assert data == {
        "_time":5,
        "_type":"AssignTrackParent",
        "_data":{
            "_childrenTracks":["TestTrack"],
            "_parentTrack":"ParentTrack"
        }
    }