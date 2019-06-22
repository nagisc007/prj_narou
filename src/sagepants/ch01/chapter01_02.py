# -*- coding: utf-8 -*-
"""Chapter 01-02: The pants.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf


# scenes
def sc_Iampants(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("俺はパンツだった！？",
            hero.be(w.stage.prison, w.day.firstmeet),
            ery.ask("パンツとは何だ"),
            hero.explain("パンツ説明"),
            hero.know(w.pants),
            hero.remember("彼女の格言"),
            )

def sc_herstatus(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("彼女の状況",
            hero.deal("状況を理解したい"),
            hero.ask(ery, "色々"),
            ery.explain("閉じ込められたこと等"),
            ery.talk("大賢者"),
            ery.deal("パンツ履こうとする"),
            )

def sc_equippants(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("パンツ装着",
            ery.deal(hero, "装着"),
            )

def sc_named_taro(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("名前はタロウ",
            ery.deal(hero, "タロウ"),
            hero.ask("彼女の名前"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_Iampants(w),
            )

def ep_main(w: wd.World):
    return (w.chaptertitle("パンツ装着"),
            sc_herstatus(w),
            sc_equippants(w),
            sc_named_taro(w),
            )

# outline
def baseinfo(w: wd.World):
    return [
            ("chapter 1-02", story(w), w.hero, w.ery),
            ]

def outline(w: wd.World):
    return [
            ("chapter 1-02", story(w),
                w.hero.deal("状況を理解したい"),
                w.hero.know(w.pants),
                w.hero.ask(w.ery, "色々"),
                w.ery.deal(w.hero, "装着"),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle("ニ枚目：パンツの名は"),
            ep_intro(w),
            ep_main(w),
            )

def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

