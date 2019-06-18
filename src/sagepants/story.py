# -*- coding: utf-8 -*-
"""Story: the sage pants project.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf
from src.sagepants import chapter01 as ch1
from src.sagepants import chapter02 as ch2
from src.sagepants import chapter03 as ch3


# chapters
def chapter04_story(w: wd.World):
    return (w.maintitle("四枚目：弟子を取るもん！"),
            w.hero.be(w.stage.lemurian, w.day.current, w.ery),
            )

def chapter05_story(w: wd.World):
    return (w.maintitle("五枚目：脱がされるもん！"),
            w.hero.be(w.stage.lemurian, w.day.current, w.ery),
            )

def chapter06_story(w: wd.World):
    return (w.maintitle("六枚目：捨てられるもん！"),
            w.hero.be(w.stage.lemurian, w.day.current, w.ery),
            )

def chapter07_story(w: wd.World):
    return (w.maintitle("七枚目：拾われるもん！"),
            w.hero.be(w.stage.lemurian, w.day.current, w.ery),
            )

def chapter08_story(w: wd.World):
    return (w.maintitle("八枚目：破れるもん！"),
            w.hero.be(w.stage.lemurian, w.day.current, w.ery),
            )

def chapter09_story(w: wd.World):
    return (w.maintitle("九枚目：新生するもん！"),
            w.hero.be(w.stage.lemurian, w.day.current, w.ery),
            )

def chapter10_story(w: wd.World):
    return (w.maintitle("十枚目：履かれるもん！"),
            w.hero.be(w.stage.lemurian, w.day.current, w.ery),
            )

def chapter11_story(w: wd.World):
    return (w.maintitle("十一枚目：突撃するもん！"),
            w.hero.be(w.stage.lemurian, w.day.current, w.ery),
            )

def chapter12_story(w: wd.World):
    return (w.maintitle("十二枚目：散るもん……"),
            w.hero.be(w.stage.lemurian, w.day.current, w.ery),
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story", story(w), w.hero, w.ery),
            ] + ch1.baseinfo(w) \
                + ch2.baseinfo(w) \
                + ch3.baseinfo(w) \
            + [
                ("chapter 4", chapter04_story(w), w.hero, w.ery),
                ("chapter 5", chapter05_story(w), w.hero, w.ery),
                ("chapter 6", chapter06_story(w), w.hero, w.ery),
                ("chapter 7", chapter07_story(w), w.hero, w.ery),
                ("chapter 8", chapter08_story(w), w.hero, w.ery),
                ("chapter 9", chapter09_story(w), w.hero, w.ery),
                ("chapter 10", chapter10_story(w), w.hero, w.ery),
                ("chapter 11", chapter11_story(w), w.hero, w.ery),
                ("chapter 12", chapter12_story(w), w.hero, w.ery),
            ]

def story_outlineinfo(w: wd.World):
    return [
            ("story", story(w),
                w.hero.think(w.i.pants_life),
                w.hero.be(w.pants),
                w.hero.deal(w.i.coope, w.ery),
                w.hero.know(w.i.myvalue),
                True),
            ] + ch1.outline(w) \
                + ch2.outline(w) \
                + ch3.outline(w)

# main
def world():
    w = wd.World("shirobara knight project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS,
            )
    return w


def story(w: wd.World):
    return (w.maintitle("大賢者さまのパンツ！"),
            ch1.story(w),
            ch2.story(w),
            ch3.story(w),
            w.hero.go(w.stage.lemurian, w.day.firstmeet),
            w.hero.deal(w.i.transfer, w.pants),
            w.hero.think(w.i.pants_life),
            w.hero.deal(w.i.coope, w.ery),
            w.hero.know(w.i.myvalue),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

