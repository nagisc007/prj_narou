# -*- coding: utf-8 -*-
"""Chapter 02: Another end world.
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
    return w.scene("冒頭",
            w.tag.comment("実はループものになっていて日付は毎回巻き戻る"),
            ak.be(w.stage.blackzone, w.day.current),
            ak.hear(w.zer, "謎の声"),
            w.zer.talk("お主は再び違う世界で目覚めるだろう"),
            )

def sc_onthestreet(w: wd.World):
    ak = w.akura
    return w.scene("街角で目覚めた",
            ak.be("wake", w.stage.town2),
            ak.look(w.ringi),
            ak.know(w.ringi, "初対面"),
            w.ringi.talk("町の名前"),
            ak.look("町を見て歩く"),
            ak.meet(w.zer),
            )

def sc_anothertown(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("違う異世界の町",
            ak.be(w.stage.town2),
            zer.talk(ak, w.i.transfer),
            ak.know("自分の状況"),
            )

def sc_fantasyguild(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("異世界ギルド",
            ak.come(w.stage.guild2),
            ak.know("ギルドの仕組み"),
            ak.deal("登録"),
            ak.know("働いて金を得ることが必要"),
            )

def sc_mywork(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("そうだ仕事をしよう",
            ak.deal("土木作業"),
            )

def sc_quest(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("クエスト",
            ak.come(w.stage.guild2),
            ak.deal("冒険クエスト受注"),
            ak.know(w.i.killer),
            )

def sc_firstbattle(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("最初の戦闘",
            ak.go(w.stage.field2),
            )

def sc_blackstreet(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("路地裏の殺人",
            ak.look(w.minae),
            ak.go("追いかける"),
            ak.look(zer, "逸れる"),
            ak.deal("殺された"),
            )

# episodes
def ep_avant(w: wd.World):
    return (w.chaptertitle("素晴らしい異世界"),
            sc_intro(w),
            sc_onthestreet(w),
            )

def ep_guild(w: wd.World):
    return (w.chaptertitle("ギルドにて"),
            sc_anothertown(w),
            sc_fantasyguild(w),
            sc_mywork(w),
            )

def ep_cheatworld(w: wd.World):
    return (w.chaptertitle("裏切る世界"),
            sc_quest(w),
            sc_firstbattle(w),
            sc_blackstreet(w),
            )


# main
def story(w: wd.World):
    return (w.maintitle("この素晴らしい２番煎じの異世界に祝福を"),
            ep_avant(w),
            ep_guild(w),
            ep_cheatworld(w),
            )


def main(): # pragma: no cover
    from src.anotherend.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

