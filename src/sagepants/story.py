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


# chapters

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story", story(w), w.hero, w.ery),
            ] + ch1.baseinfo(w) \
                + ch2.baseinfo(w)

def story_outlineinfo(w: wd.World):
    return [
            ("story", story(w),
                w.hero.think(w.i.pants_life),
                w.hero.be(w.pants),
                w.hero.deal(w.i.coope, w.ery),
                w.hero.know(w.i.myvalue),
                True),
            ] + ch1.outline(w) \
                + ch2.outline(w)

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

