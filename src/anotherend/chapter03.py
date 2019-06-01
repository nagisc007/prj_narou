# -*- coding: utf-8 -*-
"""Chapter 03: Another end world.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherend import config as cnf


# scenes
def sc_intro(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("メインフロア",
            ak.be(w.stage.floor3, w.day.current),
            ak.look(zer),
            ak.look("フロア状況"),
            ak.know("ロボの世界"),
            )

def sc_robotown(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("ロボの町",
            ak.come(w.stage.town3),
            ak.know(w.minae, "この世界にもいる"),
            ak.look(w.minae),
            ak.know(w.stage.castle3),
            )

def sc_declaration(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("開始宣言",
            w.killer.talk("デスゲーム開始宣言"),
            )

def sc_battlefield(w: wd.World):
    return w.scene("戦場",
            )

def sc_organized(w: wd.World):
    return w.scene("ゼロ団結成",
            )

def sc_lawlesszone(w: wd.World):
    ak, zer, minae = w.akura, w.zer, w.minae
    return w.scene("無法地帯",
            ak.deal("守る", w.minae),
            )

def sc_showdown(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("対決",
            ak.deal("殺される"),
            ak.look("眠る自分の姿"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("ゲームに似た世界"),
            sc_intro(w),
            )

def ep_roboworld(w: wd.World):
    return (w.chaptertitle("ロボたちの世界"),
            sc_robotown(w),
            )

def ep_deathgame(w: wd.World):
    return (w.chaptertitle("デスゲームの始まり"),
            sc_declaration(w),
            )

def ep_thewar(w: wd.World):
    return (w.chaptertitle("戦争になる"),
            sc_battlefield(w),
            )

def ep_zforce(w: wd.World):
    return (w.chaptertitle("ゼロ部隊"),
            sc_organized(w),
            sc_lawlesszone(w),
            )

def ep_conclusion(w: wd.World):
    ak, zer, minae = w.akura, w.zer, w.minae
    return (w.chaptertitle("暗殺者との決着"),
            ak.go(minae, "一緒に逃げる"),
            sc_showdown(w),
            )

# main
def story(w: wd.World):
    return (w.maintitle("World.3：サード・ロボット・オンライン"),
            ep_intro(w),# 01 avant
            ep_roboworld(w),
            ep_deathgame(w),
            ep_thewar(w),# 02 avant
            ep_zforce(w),
            ep_conclusion(w),
            )


def main(): # pragma: no cover
    from src.anotherend.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

