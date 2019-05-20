# -*- coding: utf-8 -*-
"""Story: Another end world.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherend import config as cnf


# episodes


# main
def world():
    w = wd.World("Another end world project")
    w.set_db(cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS,
            cnf.ITEMS,
            cnf.INFOS,
            cnf.FLAGS,
            )
    return w


def story(w: wd.World):
    return (w.maintitle("あから始まり異世界終了"),
            w.akura.be("die"),
            w.akura.think(w.i.anotherworld),
            w.akura.look("wake"),
            w.akura.be(w.stage.world1, w.day.first),
            w.akura.be("忘れてしまった"),
            w.akura.remember("大事なこと"),
            w.akura.do("何度も死ぬ"),
            w.akura.meet(w.minae),
            w.akura.deal("伝える", w.minae, "自分の本音"),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

