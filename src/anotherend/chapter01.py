# -*- coding: utf-8 -*-
"""Chapter 01: Another end world.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherend import config as cnf


# scenes
def sc_intro(w: wd.World):
    ak = w.akura
    return w.scene("冒頭",
            ak.be(w.stage.field1, w.day.current),
            )

# episodes
def ep_avant(w: wd.World):
    return (w.chaptertitle("1.1 気づいたら異世界"),
            sc_intro(w),
            )

def ep_partA(w: wd.World):
    return (w.chaptertitle("1.2 A"),
            )

def ep_partB(w: wd.World):
    return (w.chaptertitle("1.3 B"),
            )

# main
def story(w: wd.World):
    return (w.maintitle("World.1：１からやり直す異世界生活"),
            ep_avant(w),
            ep_partA(w),
            ep_partB(w),
            )


def main(): # pragma: no cover
    from src.anotherend.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

