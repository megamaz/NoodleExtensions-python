import NoodleExtensions

# As always, set up and editor and an animator
editor = NoodleExtensions.Editor(r"C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomWIPLevels\ExampleLevel\EasyStandard.dat")
animator = NoodleExtensions.Animator(editor)

# Python tip! 
# If you want to make the animating process be less repetitive, you can do this;
editor.editBlock(12, (1, 0), "RotateTrack")
editor.editBlock(12, (2, 0), "RotateTrack")
def Animation(data, track, start, end):
    animator.animate("AnimateTrack", NoodleExtensions.Animations.rotation, data, track, start, end)

# then just call the function!
Animation([
    [0, 0, 0, 0],
    [0, 0, 180, 1, "easeInOutBack"]
], "RotateTrack", 11, 12)

# of course, in this case the function is useless. 