# -*- coding: utf-8 -*-
"""Chapter 07: Another end world.
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
    return (w.chaptertitle("2.0 素晴らしい異世界"),
            sc_intro(w),
            )


# main
def story(w: wd.World):
    return (w.maintitle("World.7：七宮ナツヒの消失"),
            ep_avant(w),
            )


def main(): # pragma: no cover
    from src.anotherend.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

