# -*- coding: utf-8 -*-
"""Chapter 03-B: Another end world.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherend import config as cnf

# scenes
def sc_battlefield(w: wd.World):
    ak, zer, minae = w.akura, w.zer, w.minae
    return w.scene("戦場",
            ak.come(w.stage.tower3, w.day.current),
            ak.think("逃亡"),
            ak.talk("このままだと死ぬ"),
            ak.go("外へ"),
            )

def sc_organized(w: wd.World):
    ak, zer, minae, matsu = w.akura, w.zer, w.minae, w.matsuda
    return w.scene("死神討伐団結成",
            ak.come(w.stage.floor3),
            ak.deal("相談"),
            matsu.come("登場"),
            ak.look(matsu),
            ak.think("どこかで見た気が"),
            matsu.ask("協力して欲しいか？", w.i.coordinate.flag()),
            ak.deal(matsu, "断る"),
            ak.deal(w.i.zeroforce, "参加しない"),
            ak.look("見送る"),
            )

def sc_alone(w: wd.World):
    ak, zer, minae, matsu, akane = w.akura, w.zer, w.minae, w.matsuda, w.akane
    return w.scene("孤高と孤独",
            ak.remember("教室の風景"),
            ak.talk(matsu, "いつもオチに使われた"),
            akane.come(w.stage.room3),
            akane.deal("助けて"),
            ak.think("自分じゃ力にならない"),
            akane.explain(ak, "あなたが必要"),
            akane.talk("交換材料なの"),
            )

def sc_lawlesszone(w: wd.World):
    ak, zer, minae, matsu, akane = w.akura, w.zer, w.minae, w.matsuda, w.akane
    return w.scene("無法地帯",
            ak.deal("守る", w.minae),
            ak.come(w.stage.toproom3),
            ak.look(minae),
            ak.ask("何故？"),
            minae.reply("あなた以外を皆殺しにするため"),
            )

def sc_showdown(w: wd.World):
    ak, zer, minae, matsu, akane = w.akura, w.zer, w.minae, w.matsuda, w.akane
    return w.scene("対決",
            minae.talk("あなたは何も覚えてない"),
            ak.talk(matsu, "みんなで逃げろ", w.i.coordinate.deflag()),
            ak.go(minae, "一緒に逃げる"),
            ak.deal("殺される"),
            ak.look("眠る自分の姿"),
            )

# episodes
def ep_thewar(w: wd.World):
    return (w.chaptertitle("戦争になる"),
            sc_battlefield(w),
            )

def ep_zforce(w: wd.World):
    return (w.chaptertitle("ゼロ部隊"),
            sc_organized(w),
            sc_alone(w),
            sc_lawlesszone(w),
            )

def ep_conclusion(w: wd.World):
    ak, zer, minae = w.akura, w.zer, w.minae
    return (w.chaptertitle("暗殺者との決着"),
            sc_showdown(w),
            )

# main
def story(w: wd.World):
    return (w.maintitle("World.3-B：デスゲーム後編"),
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
