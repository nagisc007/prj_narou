# -*- coding: utf-8 -*-
"""Chapter 02: The pants.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf


# scenes
def sc_intheprison(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("檻の中",
            hero.feel("彼女の感触"),
            hero.feel("不思議な感覚"),
            ery.ask("何かした？"),
            hero.look("強烈な光"),
            hero.look("幼女エリィ"),
            w.hero.be(w.stage.prison, w.day.firstmeet, w.ery),
            hero.look("場所確認"),
            w.hero.deal(w.ery, "手伝う"),
            w.hero.deal(w.ery, "装着"),
            ery.ask("どういうこと？"),
            hero.reply("知らん"),
            hero.think("こうなった事情"),
            ery.explain("おそらく、の説明"),
            ery.explain("檻について"),
            hero.look("檻"),
            ery.go("外へ"),
            )

def sc_outtoprison(w: wd.World):
    hero, ery = w.hero, w.ery
    gater1, gater2 = w.gater1, w.gater2
    outprison = w.stage.prison.insided("檻の外")
    return w.scene("檻の外",
            hero.be(outprison),
            hero.look("暗い通路"),
            ery.move("出口へ"),
            hero.ask("閉じ込められた事情"),
            ery.explain("事情"),
            ery.talk("大賢者だった"),
            hero.look("出口"),
            hero.hear("話し声"),
            ery.talk("門番がいる"),
            hero.ask("大丈夫か？"),
            ery.talk("力弱くなってるが"),
            hero.think("自分が脱げれば？"),
            ery.talk("そしたら世界が終わるぞ"),
            )

def sc_herpower(w: wd.World):
    hero, ery = w.hero, w.ery
    gater1, gater2 = w.gater1, w.gater2
    return w.scene("彼女の力",
            ery.deal("ドア開ける"),
            gater1.talk("驚く"),
            gater2.talk("文句"),
            hero.look("二人口論"),
            hero.look("兵士は女で上下鎧"),
            gater1.talk("戻れ"),
            ery.talk("そろそろ外の空気を吸わせてくれ"),
            ery.deal("戦闘"),
            hero.look("一瞬で決着"),
            hero.ask("抑えてこれ？"),
            ery.talk("だから世界が滅ぶ"),
            ery.talk("久々の世界だ"),
            hero.look("広がる森"),
            hero.look("見たことない生き物"),
            )

def sc_letsgo(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("いざ我が家へ",
            w.hero.go("外に出る"),
            w.hero.know(w.i.anotherworld),
            ery.talk("まず我が家に"),
            ery.talk("ここがどこか分からん"),
            ery.talk("知っている世界と違う"),
            ery.have("マント"),
            ery.move("歩き出す"),
            hero.think("見えない"),
            ery.talk("仕方ないな"),
            hero.look("前が開く"),
            hero.have("視界"),
            hero.look("自然は見たことがあるものばかり"),
            )

def sc_mysister(w: wd.World):
    hero, ery, lily = w.hero, w.ery, w.lily
    return w.scene("阻む者は我が妹",
            hero.move("しばらく徒歩"),
            hero.ask("賢者なら飛んだり？"),
            ery.talk("そこまでの力はない"),
            hero.think("簡単な気がする"),
            ery.talk("腹が減っている"),
            hero.talk("何年入ってた？"),
            ery.talk("ざっと五百年ばかり"),
            ery.feel("気配"),
            hero.look("空から落ちてきた"),
            hero.look(lily),
            hero.look("髪色そっくり"),
            hero.look("制服着てる"),
            hero.look("怒ってる"),
            ery.talk("何よ我が妹"),
            hero.ask("妹？"),
            lily.talk("あんたの所為でね"),
            )

# episodes
def ep_mypants(w: wd.World):
    return (w.chaptertitle("私のパンツ"),
            sc_intheprison(w),
            )

def ep_prisonbreak(w: wd.World):
    return (w.chaptertitle("脱獄"),
            sc_outtoprison(w),
            sc_herpower(w),
            )

def ep_outworld(w: wd.World):
    return (w.chaptertitle("外は異世界だった"),
            sc_letsgo(w),
            sc_mysister(w),
            )

# outline
def baseinfo(w: wd.World):
    return [
            ("chapter 2", story(w), w.hero, w.ery),
            ]

def outline(w: wd.World):
    return [
            ("chapter 2", story(w),
                w.hero.deal(w.ery, "手伝う"),
                w.hero.deal(w.ery, "装着"),
                w.hero.go("外に出る"),
                w.hero.know(w.i.anotherworld),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle("二枚目：パンツ、脱獄するもん！"),
            ep_mypants(w),
            ep_prisonbreak(w),
            ep_outworld(w),
            )

def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

