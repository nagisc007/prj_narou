# -*- coding: utf-8 -*-
"""Chapter 03-A: Another end world.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherend import config as cnf


# scenes
def sc_intro(w: wd.World):
    ak, zer, ringi = w.akura, w.zer, w.ringi
    return w.scene("メインフロア",
            ak.be(w.stage.floor3, w.day.current),
            ak.do("wake"),
            ak.look("沢山のSF的人物たち"),
            ak.look(zer),
            ak.ask(zer, "知ってるか？"),
            zer.reply("覚えてる"),
            ak.ask("この世界"),
            ak.look("フロア状況"),
            ak.know("ロボの世界？"),
            ak.ask(w.i.transfer, "他にも？"),
            zer.talk("可能性は"),
            ak.think(w.minae, "彼女を探す"),
            ringi.talk("初心者か？"),
            ak.deal("教わる"),
            ak.look("暗くなる"),
            )

def sc_declaration(w: wd.World):
    ak, zer, ringi = w.akura, w.zer, w.ringi
    return w.scene("開始宣言",
            ak.hear("謎の声"),
            w.killer.talk("デスゲーム開始宣言"),
            ringi.talk("デス"),
            ak.ask(w.i.killer),
            ak.look("デスの画像"),
            ak.know(w.i.killer, w.minae),
            )

def sc_robotown(w: wd.World):
    ak, zer, ringi = w.akura, w.zer, w.ringi
    return w.scene("ロボの町",
            ringi.deal("案内"),
            ak.come(w.stage.town3),
            ringi.talk(w.stage.castle3),
            ak.look("クラッド"),
            ak.know(w.stage.castle3),
            )

def sc_weapons(w: wd.World):
    ak, zer, ringi = w.akura, w.zer, w.ringi
    return w.scene("装備",
            ak.come(w.stage.shop3),
            ak.have("装備"),
            ringi.talk("出世払いだ"),
            ringi.talk("見どころある"),
            )

def sc_lookforher(w: wd.World):
    ak, zer, ringi = w.akura, w.zer, w.ringi
    return w.scene("彼女探し",
            ak.come(w.stage.tower3),
            ak.look("見上げる", "外観"),
            ak.know(w.minae, "この世界にもいる"),
            ak.look(w.minae, "探す"),
            ak.go("入り口"),
            )

def sc_slaughters(w: wd.World):
    ak, zer, ringi = w.akura, w.zer, w.ringi
    return w.scene("始まる虐殺",
            ak.come("一階"),
            ak.look("屍の山"),
            ak.hear("死神にやられた"),
            )

def sc_meetdeath(w: wd.World):
    ak, zer, ringi, minae = w.akura, w.zer, w.ringi, w.minae
    return w.scene("死神との対面",
            ak.come("十三階"),
            ak.meet(w.minae),
            ak.look(minae),
            minae.talk("全部殺してあげる"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("ゲームに似た世界"),
            sc_intro(w),
            )

def ep_roboworld(w: wd.World):
    return (w.chaptertitle("ロボたちの世界"),
            sc_declaration(w),
            sc_robotown(w),
            sc_weapons(w),
            )

def ep_deathgame(w: wd.World):
    return (w.chaptertitle("デスゲームの始まり"),
            sc_lookforher(w),
            sc_slaughters(w),
            sc_meetdeath(w),
            )

# main
def story(w: wd.World):
    return (w.maintitle("World.3-A：デスゲーム前編"),
            ep_intro(w),# 01 avant
            ep_roboworld(w),
            ep_deathgame(w),
            )


def main(): # pragma: no cover
    from src.anotherend.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

