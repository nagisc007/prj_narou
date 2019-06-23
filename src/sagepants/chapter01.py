# -*- coding: utf-8 -*-
"""Chapter 01: The pants.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf
from src.sagepants.ch01 import chapter01_01 as chap01
from src.sagepants.ch01 import chapter01_02 as chap02


# scenes
def sc_mypants(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("パンツ装着",
            hero.think().d("パンツとは何なのか"),
            hero.think().d("それを$meは即座に「下着のことだ」とは言えなかった。",
                "何故なら三年前に別れた彼女の遺言にも似た最後の言葉が、"),
            hero.hear().emphasis("$i_herword002"),
            hero.think().d("だったからだ"),
            ery.ask().t("どうした？",
                "何か答えるのに不都合でもあるのか？"),
            hero.talk().t("あんたはパンツを身に着けていない。",
                "それに加えて裸のようだ。",
                "だからひょっとしたら下着を含めた衣類を身に着けるという文化がないのかも知れない。",
                "そういう前提で話させてもらうが",
                "いいか？"),
            hero.look().d("彼女はその言葉に眉を顰めていたが",
                "ゆっくりと縦に首を振ったのを確認すると",
                "$meは滔々とパンツについて語り始めた"),
            hero.talk().t("パンツとは股間を含めた下腹部の一部を覆う着衣の一種だ。",
                "着衣",
                "つまり服を着ることで様々な恩恵を受けることができる。",
                "中でも下着と呼ばれるものは肌着とも呼ばれ",
                "皮膚の上に直接身に着けるように設計されている"),
            hero.look().d("最初は首を傾げ気味だった彼女も",
                "$meが仕事の時のような語り口になったからか",
                "集中して聞き入っているように見えた"),
            hero.talk().t("人間というのは思っている以上に日々汚れ",
                "またその常在菌と呼ばれる微生物は皮膚の上で老廃物となり蓄積する。",
                "そういう体表上の汚れ", "あるいは汗のような分泌物を下着は吸収し",
                "それを付け替えることで人間は己の体を清潔に保つという手段を手に入れたんだ"),
            hero.look().d("長い髪で覆い隠されていたが",
                "彼女はその一部を持ち上げ", "自分の体を確かめるように見始める"),
            hero.talk().t("その肌着の内で主に股の部分を中心に覆うようになっているものがパンツだ。",
                "あんたがさっきした",
                "その",
                "おしっこのように",
                "人は食べたもの飲んだものを排出する。",
                "そこはとても不衛生となる。",
                "だからこそ普段パンツで覆い",
                "生活することで",
                "自分を", "そして周りを汚染せずに済むという訳だ"),
            hero.think().d("もっと言えばデザインやオシャレといった精神性の問題もあるが",
                "目の前の女にそういった説明をしても混乱を招くだけだろうと思って敢えて省いた"),
            hero.talk().t("パンツが何か", "分かったか？"),
            ery.talk().t("そうだな……つまりだ。",
                "パンツとは身に着けるものであり",
                "$meは今裸だ。",
                "本来であれば$sagerobeという法衣を身に着けておったのだが",
                "事情があって今", "$meの手元にはないのだ"),
            hero.look().d("彼女は$meの端を両手で持ったままにっこりと笑みを向ける"),
            hero.talk().t("わ、分かってくれたなら良かったよ"),
            hero.feel().d("ぞわり", "という妙な悪寒に$meの警戒心が顔を覗かせた"),
            hero.look().d("何だろう。",
                    "目の前の女性は紫の髪で胸元から下までを覆い隠して立っていたが",
                    "その片方の足が不意に持ち上がる"),
            hero.look().d("右足だ"),
            hero.look().d("続いて少し背を曲げるようにして屈み込むと",
                    "$meの視界はぐんぐんと下降していき",
                    "ほど良い二つの丘から",
                    "肉付きのよい腹部",
                    "形の良い臍を経て",
                    "何もないつるりとした彼女の下腹と",
                    "その先に存在するであろう女性の排泄器官までが見えてしまう"),
            hero.look().d("そう思った瞬間だった"),
            ery.ask().t("ところでお前には前と後ろがあるのか？"),
            hero.talk().t("パンツの前後ろのことだったら",
                    "確かに存在する。",
                    "犬のイラストが付いている方が前だ"),
            hero.think().d("そう答えながらも$meは何を言っているのだろう",
                    "という意識がどうしても脳裏から離れてくれない。",
                    "そればかりか",
                    "彼女の質問からはどう考えても",
                    "ある結果しか導かれないではないか"),
            ery.talk().t("そうか。",
                    "ならばこういうことか"),
            hero.look().d("刹那",
                    "$meの視界は横回りで百八十度振り回され",
                    "この薄暗い空間の壁へと向けられる"),
            hero.feel().d("それに続いて自分のお腹が内部から広げられたような",
                    "何とも胸苦しさを覚える感覚が湧き上がり",
                    "もそもそと何かが動く気配を背中側に強烈に感じさせられた"),
            hero.talk().t("あぅ！？"),
            hero.feel().d("何かが",
                    "$meの右半身を貫いていった"),
            hero.think().d("痛みを伴った衝撃ではないが",
                    "何と表現したものだろう。",
                    "ムズムズとするような", "痛痒感とでも呼べばいいのだろうか。",
                    "それがずっと右半分に張り付いている"),
            hero.feel().d("けれどそれはすぐ残りの左半分にもやってきた"),
            hero.talk().t("ひゃう！"),
            ery.talk().t("妙な声を上げるでない"),
            hero.talk().t("け、けどな。",
                    "あんた一体何をしたんだ？"),
            hero.look().d("一瞬潰れたように歪んだ視界は",
                    "今は明瞭だった。",
                    "少しは目も慣れてきたのだろう。",
                    "壁は岩肌で",
                    "視界の切れ端に鉄の棒のようなものが見える"),
            ery.talk().t("ほお……これは", "なかなかに"),
            hero.feel().d("彼女の手が",
                    "$meに触れる。",
                    "それは分かる。",
                    "けれどその内側にあるものは一体何だ"),
            hero.think().d("考えろ。",
                    "今どういう状況なんだ"),
            ery.talk().t("何をごちゃごちゃと言っておる。",
                    "お主はパンツ。",
                    "そして$meは外見上は人間の姿をしておる。",
                    "ならば自ずと答えは導かれよう"),
            hero.talk().t("嘘、だろ……"),
            hero.hear().d("彼女は声を殺して笑う"),
            hero.look().d("確かに少し考えれば分かることだった。",
                    "さっき彼女に持たれていた時よりも随分と視界が低い。",
                    "それは彼女の顔の高さより低い位置だということだ。",
                    "それに目の前には部屋の様子が広がっていることから",
                    "彼女の方を見ていないということになる"),
            hero.think().d("自明", "というやつだ"),
            hero.think().d("そうだ。",
                    "つまり$meは彼女に……"),
            hero.talk().t("履かれているのか！？"),
            ery.talk().t("お主が言ったではないか。",
                    "パンツは履くものだと"),
            hero.think().d("そう認識した瞬間",
                    "自分の内側に女性のアレやソレやコレが密着しているのだということに気づいて",
                    "$meは思考に急ブレーキを掛けた"),
            ery.deal("身に着ける", hero),
            hero.feel("衝撃"),
            )

def sc_outofprison(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("監獄の外は異世界でした",
            hero.know(w.i.anotherworld),
            ).omit()

def sc_herpower(w: wd.World):
    hero, ery = w.hero, w.ery
    gater1 = w.gater1
    return w.scene("彼女の力",
            ery.deal("battle", gater1),
            hero.know("彼女の強さ"),
            ).omit()

# outline
def baseinfo(w: wd.World):
    return [("chapter 1", story(w), w.hero, w.ery),] \
            + chap01.baseinfo(w) \
            + chap02.baseinfo(w)

def outline(w: wd.World):
    return [
            ("chapter 1", story(w),
                w.hero.know(w.i.mystatus, "$want"),
                w.hero.be(w.i.transfer, w.pants),
                w.hero.deal(w.ery, w.i.knowledge_world),
                w.hero.deal(w.ery, w.i.equip),
                True),
            ] \
                + chap01.outline(w) \
                + chap02.outline(w)

# NOTE
# c01 出会い（パンツ転生）
# c02 パンツ自認、命名
# c03 パンツ装着
# c04 脱獄
# c05 妹遭遇
# c06 自宅
# c07 その後の世界情勢
# c08 逮捕事情
# c09 魔衣
# c10 特殊部隊

# main
def story(w: wd.World):
    return (w.maintitle("第一章：パンツ、大地に立つ！"),
            chap01.story(w),
            w.hero.know(w.i.mystatus, "$want"),
            w.hero.be(w.i.transfer, w.pants),
            w.hero.deal(w.ery, w.i.knowledge_world),
            w.hero.deal(w.ery, w.i.equip),
            )


def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

