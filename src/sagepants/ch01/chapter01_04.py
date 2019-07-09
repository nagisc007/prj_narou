# -*- coding: utf-8 -*-
"""Chapter 01-04: The pants.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf


# scenes
def sc_outjail(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("牢の外",
            hero.be(w.stage.prison, w.day.firstmeet),
            ery.talk().t("フフフ……アハハハハハ！"),
            hero.hear().d("檻の外へと出た彼女は",
                "突如高笑いを始めた"),
            hero.think().d("確かに五百年だか何だか知らないがそれだけの長期に渡って閉じ込められていたのだ。",
                "そういう気分になるのも分かる。",
                "だから$meは敢えて何も言わずにそのまま放置した"),
            hero.look().d("五分くらいにも感じたその可愛らしい笑い声が急に止まると",
                "$meの右目に彼女の拳が降ってくる"),
            hero.ask().t("何だよ"),
            ery.talk().t("何故止めん！？"),
            hero.talk().t("だって気持ちよさそうに笑ってるところを邪魔しちゃ悪いだろ？",
                "元彼女にも言われたんだよ。",
                "$heroword005", "って"),
            hero.think().d("そう聞いてからは",
                "あれこれ思っていても口に出さないことが増えた。",
                "ただそれが良かったことなのかどうかは",
                "その後彼女の不機嫌が増えて別れてしまった今となってはよく分からない"),
            ery.ask().t("モトカノジョとは", "何だ？"),
            hero.talk().t("彼女だった女性のことだよ。",
                "ああ。彼女っていうのは付き合っていたって意味な。",
                "それくらいは分かるだろう？"),
            hero.hear().d("しかし何を考え込んでいるのか返答がない"),
            hero.talk().t("そんなことよりもさ",
                "これからどうするんだ？",
                "閉じ込められていたってことは",
                "牢から出ただけで簡単に自由になれるという訳でもないんだろう？"),
            ery.talk().t("あ",
                "そうだったな……"),
            hero.hear().d("そう答えた彼女の声が", "前方へと投げやられる"),
            hero.look().d("$meはパンツとして確認できる最大限で真っ直ぐ続く薄暗い通路の先を見たが",
                "何やら足音に続いて複数の人影が徐々に大きくなるのが分かった"),
            hero.ask().t("なあ", "ひょっとするとアレって"),
            ery.talk().t("五百年ぶりの他人どもだ"),
            )

def sc_aboutprison(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("監獄島について",
                w.hero.know(w.i.mystatus),
                w.hero.be(w.ery, "脱げない"),
            # TODO: continue
            )

def sc_notfound(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("見つからないように",
                w.hero.deal("脱出に協力する"),
            )

def sc_beatgatekeeper(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("門番討伐",
            )

def sc_since500year(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("五百年ぶりの外の景色",
                w.hero.go(w.stage.out_prison),
            )

# episodes
def ep_outjail(w: wd.World):
    return (w.chaptertitle("牢獄の外へ"),
            sc_outjail(w),
            )

def ep_escape(w: wd.World):
    return (w.chaptertitle("脱出"),
            sc_aboutprison(w),
            sc_notfound(w),
            sc_beatgatekeeper(w),
            sc_since500year(w),
            )

# outline
def baseinfo(w: wd.World):
    return [
            ("chapter 1-04", story(w), w.hero, w.ery),
            ]

def outline(w: wd.World):
    return [
            ("chapter 1-04", story(w),
                w.hero.know(w.i.mystatus),
                w.hero.be(w.ery, "脱げない"),
                w.hero.deal("脱出に協力する"),
                w.hero.go(w.stage.out_prison),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle("四枚目：あるパンツからの脱出"),
            w.tag.comment("タイトルは映画「アルカトラズからの脱出」より"),
            ep_outjail(w),
            ep_escape(w),
            )

def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

