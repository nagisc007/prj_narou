# -*- coding: utf-8 -*-
"""Chapter 01-09: The pants.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf


# scenes

# episodes

# outline
def baseinfo(w: wd.World):
    return [
            ("chapter 1-09", story(w), w.hero, w.ery),
            ]

def outline(w: wd.World):
    return [
            ("chapter 1-09", story(w),
                w.hero.be(),
                w.hero.be(),
                w.hero.be(),
                w.hero.be(),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle("九枚目：パンツと魔衣"),
            )

def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

