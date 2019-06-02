# -*- coding: utf-8 -*-
"""Chapter 02: Another end world.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherend import config as cnf
THM = cnf.THEMES


# scenes
def sc_intro(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("冒頭",
            w.tag.comment("実はループものになっていて日付は毎回巻き戻る"),
            ak.talk().t("くはっ"),
            ak.do("wake").d("思い切り息を吐き出して両手を突き出しながら上体を起こした"),
            ak.look("彼女の幻"),
            ak.be(w.stage.blackzone, w.day.current),
            ak.look("謎の影の人物"),
            ak.hear(w.zer, "謎の声"),
            w.zer.talk("お主は再び違う世界で目覚めるだろう"),
            )

def sc_onthestreet(w: wd.World):
    ak, zer, ringi = w.akura, w.zer, w.ringi
    return w.scene("街角で目覚めた",
            ak.be("wake", w.stage.town2),
            ak.look(w.ringi),
            ringi.talk().t("何見てんだ？"),
            ak.know(w.ringi, "初対面"),
            ak.think("疑問"),
            ak.ask("亜人"),
            ringi.talk("何言ってんだ？"),
            ak.think("違う世界"),
            ak.look("町を見て歩く"),
            ak.look("人が集まっている"),
            zer.deal("助けを求める"),
            ak.meet(w.zer),
            zer.talk("名前を知ってる"),
            ak.ask("お前誰？"),
            )

def sc_anothertown(w: wd.World):
    ak, zer, minae = w.akura, w.zer, w.minae
    return w.scene("違う異世界の町",
            w.tag.comment("主人公説明と世界観説明"),
            ak.be(w.stage.town2),
            ak.come("河川敷"),
            ak.ask("だから何者？"),
            zer.reply("あんたが雇った妖精"),
            zer.talk(ak, w.i.transfer, THM["transfer"]),
            ak.know("自分の状況"),
            ak.ask("他にもいるのか？"),
            zer.reply("yes"),
            ak.hear(w.killer),
            ak.think("魔王じゃない？"),
            ak.think("どうするか"),
            ak.feel(w.i.hungry.flag()),
            )

def sc_fantasybar(w: wd.World):
    ak, zer, ringi = w.akura, w.zer, w.ringi
    return w.scene("異世界バー",
            ak.come(w.stage.bar2),
            ak.look(ringi),
            ak.ask(ringi, "仕事"),
            ak.know("ギルドの仕組み"),
            ak.know("働いて金を得ることが必要"),
            ringi.ask("働いたことないのか？"),
            ak.remember("何か"),
            )

def sc_fantasyguild(w: wd.World):
    ak, zer, recep = w.akura, w.zer, w.reception2
    return w.scene("異世界ギルド",
            ak.come(w.stage.guild2),
            recep.deal("受付"),
            ak.deal("登録"),
            recep.explain("仕組み"),
            ak.deal("旅芸人"),
            zer.deal("巫女"),
            ak.ask("仕事は？"),
            recep.explain("クエスト説明"),
            ak.look("掲示板"),
            ak.think("無理"),
            ak.look("普通の仕事"),
            )

def sc_mywork(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("そうだ仕事をしよう",
            ak.deal("土木作業"),
            ak.go("現場"),
            ak.deal("壁の補修"),
            ak.go(w.stage.eating2),
            ak.deal("一番安い食事"),
            ak.go(w.stage.stable2),
            ak.deal("並んで睡眠"),
            ak.think("繰り返す日々"),
            ak.think("これでいいのか？"),
            ak.remember(w.minae),
            )

def sc_quest(w: wd.World):
    ak, zer, recep = w.akura, w.zer, w.reception2
    return w.scene("クエスト",
            ak.come(w.stage.guild2),
            recep.ask("何です？"),
            ak.look("誰もやってない"),
            ak.deal("冒険クエスト受注"),
            recep.talk(w.i.killer),
            ak.know(w.i.killer),
            ak.ask(w.minae),
            recep.reply("人探しなら依頼して"),
            )

def sc_shopping(w: wd.World):
    ak, zer, ringi = w.akura, w.zer, w.ringi
    return w.scene("装備調達",
            ak.come(w.stage.weaponshop2),
            ringi.talk("武器トーク"),
            ak.deal("有り金なくなる"),
            zer.talk("稼げばいい"),
            ak.think("その通りだ"),
            )

def sc_gotoout(w: wd.World):
    ak, zer, gatekp = w.akura, w.zer, w.gatekeeper2
    return w.scene("いざフィールドへ",
            ak.come(w.stage.gate2),
            ak.talk(gatekp),
            gatekp.talk(w.i.killer),
            ak.talk("大丈夫"),
            )

def sc_firstbattle(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("最初の戦闘",
            ak.go(w.stage.field2),
            ak.look("巨大蛇"),
            ak.deal("戦闘"),
            )

def sc_blackstreet(w: wd.World):
    ak, zer = w.akura, w.zer
    return w.scene("路地裏の殺人",
            ak.look(w.minae),
            ak.go("追いかける"),
            ak.look(zer, "逸れる"),
            ak.feel(w.i.hungry.deflag()),
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
            sc_fantasybar(w),
            sc_fantasyguild(w),
            sc_mywork(w),
            )

def ep_cheatworld(w: wd.World):
    return (w.chaptertitle("裏切る世界"),
            sc_quest(w),
            sc_shopping(w),
            sc_gotoout(w),
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

