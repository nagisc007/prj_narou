# -*- coding: utf-8 -*-
"""Chapter 03: The pants.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf

# scenes

# episodes

# outline
def baseinfo(w: wd.World):
    return [
            ("chapter 3", story(w), w.hero, w.ery),
            ]

def outline(w: wd.World):
    return [
            ("chapter 3", story(w),
                w.hero.go(w.stage.herhome),
                w.hero.know(w.i.ery_home),
                w.hero.move(w.stage.forest1),
                w.hero.meet(w.lily),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle("三枚目：パンツ、戦うもん！"),
            w.hero.be(w.stage.forest1, w.day.firstmeet, w.ery),
            w.hero.go(w.stage.herhome),
            w.hero.know(w.i.ery_home),
            w.hero.move(w.stage.forest1),
            w.hero.meet(w.lily),
            )

def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

