# -*- coding: utf-8 -*-
"""Chapter 00: Another end world.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherend import config as cnf


# scenes
def sc_intro(w: wd.World):
    ak, ma = w.akura, w.master
    return w.scene("突然の死",
            w.tag.comment("全てのきっかけだが、何も分からない。最大の謎となる殺害場面。実はヒロインにより殺された"),
            w.akura.be("die"),
            w.akura.think(w.i.anotherworld),
            w.akura.look("wake"),
            w.akura.be(w.stage.world1, w.day.first),
            w.akura.be("忘れてしまった"),
            w.akura.remember("大事なこと"),
            w.akura.do("何度も死ぬ"),
            w.akura.meet(w.minae),
            w.akura.deal("伝える", w.minae, "自分の本音"),
            #
            ak.be(w.stage.world0, w.day.current),
            ak.look("暗黒の世界"),
            ak.be("何も覚えていない"),
            ak.know("自分が何者か"),
            ak.do("wake"),
            ak.hear(ma, "誰かの声"),
            ak.deal("殺された"),
            )

# episodes
def ep_first(w: wd.World):
    return (w.chaptertitle("全ての始まり"),
            sc_intro(w),
            )


# main
def story(w: wd.World):
    return (w.maintitle("World.0：始まりと終わりの０の執行人"),
            ep_first(w),
            )


def main(): # pragma: no cover
    from src.anotherend.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

