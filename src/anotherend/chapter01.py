# -*- coding: utf-8 -*-
"""Chapter 01: Another end world.
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
    return w.scene("目覚めたらリンギ",
            ak.be(w.stage.field1, w.day.current),
            ak.be(w.stage.market1),
            ak.look(w.ringi),
            ak.know(w.i.anotherworld),
            ak.think("この世界を調べる"),
            )

def sc_fantasytown(w: wd.World):
    ak = w.akura
    return w.scene("異世界の町",
            ak.look("死んだ原因"),
            ak.look("好みの美女"),
            ak.go("その女性"),
            )

def sc_morekill(w: wd.World):
    ak = w.akura
    return w.scene("再びの殺人",
            ak.meet(w.minae),
            ak.deal("殺された"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("気づいたら異世界"),
            sc_intro(w),
            )

def ep_research(w: wd.World):
    return (w.chaptertitle("異世界調査"),
            sc_fantasytown(w),
            sc_morekill(w),
            )

# main
def story(w: wd.World):
    return (w.maintitle("１からやり直す異世界生活"),
            ep_intro(w),
            ep_research(w),
            )


def main(): # pragma: no cover
    from src.anotherend.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

