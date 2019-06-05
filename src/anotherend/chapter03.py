# -*- coding: utf-8 -*-
"""Chapter 03: Another end world.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherend import config as cnf
from src.anotherend import chapter03_a as chap3A
from src.anotherend import chapter03_b as chap3B


# main
def story(w: wd.World):
    return (w.maintitle("World.3：サード・ロボット・オンライン"),
            chap3A.story(w),
            chap3B.story(w),
            )


def main(): # pragma: no cover
    from src.anotherend.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

