# -*- coding: utf-8 -*-
"""Chapter 01: The pants.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf


# scenes
def sc_accident(w: wd.World):
    hero = w.hero
    return w.scene("事故に遭う",
            hero.look(w.stage.train),
            hero.move(w.stage.station, w.day.deadman),
            hero.do("dead"),
            )

def sc_iampants(w: wd.World):
    hero = w.hero
    return w.scene("私はパンツ",
            hero.be(w.stage.lemurian, w.day.firstmeet),
            hero.be(w.pants),
            hero.think(w.i.myfuture),
            )

def sc_prisoner(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("監獄の女",
            hero.be(w.stage.prison),
            hero.meet(ery),
            )

def sc_mypants(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("パンツ装着",
            ery.deal("身に着ける", hero),
            hero.feel("衝撃"),
            )

def sc_outofprison(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("監獄の外は異世界でした",
            hero.know(w.i.anotherworld),
            )

def sc_herpower(w: wd.World):
    hero, ery = w.hero, w.ery
    gater1 = w.gater1
    return w.scene("彼女の力",
            ery.deal("battle", gater1),
            hero.know("彼女の強さ"),
            )

# episodes
def ep_herodead(w: wd.World):
    return (w.chaptertitle("太郎、死す"),
            sc_accident(w),
            )

def ep_wonderworld(w: wd.World):
    return (w.chaptertitle("不可思議な世界で"),
            sc_iampants(w),
            sc_prisoner(w),
            sc_mypants(w),
            )

def ep_meetpants(w: wd.World):
    return (w.chaptertitle("そしてパンツは出会った"),
            sc_outofprison(w),
            sc_herpower(w),
            )

# outline
def baseinfo(w: wd.World):
    return [("chapter 1", story(w), w.hero, w.ery),]

def outline(w: wd.World):
    return [
            ("chapter 1", story(w),
                w.hero.think(w.i.myfuture),
                w.hero.be(w.pants),
                w.hero.know(w.i.anotherworld),
                w.hero.meet(w.ery),
                True),
            ]
# main
def story(w: wd.World):
    return (w.maintitle("１枚目：パンツ、大地に立つ！"),
            ep_herodead(w),
            ep_wonderworld(w),
            ep_meetpants(w),
            )


def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

