# -*- coding: utf-8 -*-
"""Chapter 01: Another end world.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.anotherend import config as cnf


# scenes
def sc_fantasytown(w: wd.World):
    ak, ringi = w.akura, w.ringi
    return w.scene("目覚めたらリンギ",
            ak.do().d("後頭部に痛みを感じて", "ゆっくりと目を開く"),
            ringi.ask().t("あんちゃん大丈夫かい？"),
            ak.think().d("目の前のモヒカン頭に「あんちゃん」呼ばわりされる覚えはなかったが",
                "とにかく「大丈夫だ」と答えて立ち上がる"),
            ak.think().d("そう。", "$meは立ち上がった。",
                "立派な己の二本の足でしっかりと石畳の路地の上に", "立ったのだ"),
            ak.talk().t("痛ってぇなあ、しかし……"),
            ringi.talk().t("そりゃそうだよ。",
                "危うく荷馬車に轢かれかけたんだもんな。",
                "あんちゃんホント運が良いよ"),
            ak.look().d("腕組みをしたその上腕二頭筋の逞しさを眩しく感じながら",
                "笑った髭面モヒカンの男が見た方向に視線をやった"),
            ak.talk().t("おぉ……"),
            ak.think().d("思わずそんな声を漏らしてしまうほど",
                "住居のレンガ壁の前で派手に荷馬車が横転している。",
                "ひっくり返った馬が足をばたつかせ",
                "周りに集まった男たちが何とか押さえようとしていたが",
                "人力ではとても無理だ", "と思えた"),
            ak.be(w.stage.field1, w.day.current),
            ak.be(w.stage.market1),
            ak.look(w.ringi),
            ak.look().d("しかしそこに集まっている男たちが",
                "どう見ても人間ではない者が混ざっているのだ。",
                "爬虫類にも似た緑色の皮膚に不自然に盛り上がった首の後ろの筋肉",
                "何より三本目の足とでも呼べるものがケツの辺りから地面に向かって伸びている"),
            ak.hear().t("ガァア"),
            ak.look().d("そんな濁声と共に馬を掴んだかと思うと",
                "抱え上げて家の壁に投げつけてしまった"),
            ak.think().d("馬はそのまま地面に落下するとぐったりと動かなくなってしまう"),
            ringi.talk().t("こういう時は亜人に頼るに限るぜ。",
                "なああんちゃん"),
            ak.ask().t("え、ええ……ところでその”亜人”て何ですか？"),
            ak.look().d("初めて耳にする言葉について疑問に思っただけなのだが",
                "そんな$meのことを厳ついモヒカンの男は顎髭を撫で付けながら首を捻って見ると、"),
            ringi.ask().t("亜人は亜人だよ。",
                "犬の耳がついてたり", "狼男だったり……", "ほら",
                "あそこを今走っていく猫耳の女の子とか"),
            ak.look().d("モヒカンに指を差されて振り返ると",
                "身長百四十くらいだろうか。",
                "水色っぽい半透明の浴衣にも見えるワンピースの裾をはためかせて",
                "手を左右に振りながら必死に走っていく。",
                "その彼女の頭の上には確かに獣のそれに似た三角形の耳が乗っていたが",
                "それよりも$meはその娘の横顔を見て心臓が止まってしまいそうになった"),
            ak.know(w.i.anotherworld),
            ak.think("この世界を調べる"),
            ak.look("死んだ原因"),
            ak.look("好みの美女", w.minae),
            ak.think().d("学生時代に失恋をした", "$n_minaeによく似ていたからだ"),
            ak.look().d("その猫耳の彼女の後を", "黒マントを着た複数の男が追いかけていく"),
            ringi.talk().t("おい！", "あんちゃん！？"),
            ak.go("その女性").d("気づけば$meは林檎によく似た果実を手にしたまま",
                    "彼女の後を追いかけていた"),
            )

def sc_morekill(w: wd.World):
    ak = w.akura
    return w.scene("再びの殺人",
            ak.talk().t("こっちか？"),
            ak.go().d("商店が並ぶ通りから脇の狭い路地へと曲がったのが辛うじて見えた"),
            ak.go().d("$meもそれに続く"),
            ak.look().d("その路地に入った瞬間", "目の前に真っ黒な布が迫ってきて",
                "とてもじゃないが避けきれなかった"),
            ak.look().d("視界と動きを奪われたまま",
                "何か鋭いものが背中の辺りを貫いていく"),
            ak.meet(w.minae),
            ak.think().d("嘘だろ……また", "なのか"),
            ak.deal("殺された").d("こうして$meは再び死を迎えた"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("気づいたら異世界"),
            sc_fantasytown(w),
            )

def ep_research(w: wd.World):
    return (w.chaptertitle("異世界調査"),
            sc_morekill(w),
            )

# main
def story(w: wd.World):
    return (w.maintitle("１からやり直す異世界生活"),
            ep_intro(w),
            ep_research(w),
            )


def main(): # pragma: no cover
    from src.anotherend.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

