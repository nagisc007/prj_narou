# -*- coding: utf-8 -*-
"""Chapter 02: The pants.
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
            ("chapter 2", story(w), w.hero, w.ery),
            ]

def outline(w: wd.World):
    return [
            ("chapter 2", story(w),
                w.hero.deal(w.ery, "手伝う"),
                w.hero.deal(w.ery, "装着"),
                w.hero.go("外に出る"),
                w.hero.know(w.i.anotherworld),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle("二枚目：パンツ、脱獄するもん！"),
            w.hero.be(w.stage.prison, w.day.firstmeet, w.ery),
            w.hero.deal(w.ery, "手伝う"),
            w.hero.deal(w.ery, "装着"),
            w.hero.go("外に出る"),
            w.hero.know(w.i.anotherworld),
            )

def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

