# -*- coding: utf-8 -*-
"""Story: Another end world.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherend import config as cnf
from src.anotherend import chapter00 as chap0
from src.anotherend import chapter01 as chap1
from src.anotherend import chapter02 as chap2
from src.anotherend import chapter03 as chap3
from src.anotherend import chapter04 as chap4
from src.anotherend import chapter05 as chap5
from src.anotherend import chapter06 as chap6
from src.anotherend import chapter07 as chap7
from src.anotherend import chapter08 as chap8
from src.anotherend import chapter09 as chap9
from src.anotherend import chapter10 as chap10


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
            chap0.story(w),
            chap1.story(w),
            chap2.story(w),
            chap3.story(w),
            chap4.story(w),
            chap5.story(w),
            chap6.story(w),
            chap7.story(w),
            chap8.story(w),
            chap9.story(w),
            chap10.story(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

