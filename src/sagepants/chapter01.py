# -*- coding: utf-8 -*-
"""Chapter 01: The pants.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf
from src.sagepants.ch01 import chapter01_01 as chap01
from src.sagepants.ch01 import chapter01_02 as chap02
from src.sagepants.ch01 import chapter01_03 as chap03
from src.sagepants.ch01 import chapter01_04 as chap04


# outline
def baseinfo(w: wd.World):
    return [("chapter 1", story(w), w.hero, w.ery),] \
            + chap01.baseinfo(w) \
            + chap02.baseinfo(w) \
            + chap03.baseinfo(w) \
            + chap04.baseinfo(w)

def outline(w: wd.World):
    return [
            ("chapter 1", story(w),
                w.hero.know(w.i.mystatus, "$want"),
                w.hero.be(w.i.transfer, w.pants),
                w.hero.deal(w.ery, w.i.knowledge_world),
                w.hero.deal(w.ery, w.i.equip),
                True),
            ] \
                + chap01.outline(w) \
                + chap02.outline(w) \
                + chap03.outline(w) \
                + chap04.outline(w)

# NOTE
# c01 出会い（パンツ転生）
# c02 パンツ装着、幼女化
# c03 世界観、命名
# c04 脱獄
# c05 妹遭遇
# c06 自宅
# c07 その後の世界情勢
# c08 逮捕事情
# c09 魔衣
# c10 特殊部隊

# main
def story(w: wd.World):
    return (w.maintitle("第一章：パンツ、大地に立つ！"),
            chap01.story(w),
            chap02.story(w),
            chap03.story(w),
            chap04.story(w),
            )


def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

