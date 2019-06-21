# -*- coding: utf-8 -*-
"""Chapter 01-01: The pants.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf

# scenes
def sc_hardday(w: wd.World):
    hero, robber = w.hero, w.robber
    return w.scene("大変な日",
            w.tag.comment("現代日本かつ現代人で会社員で30程度と知らせるのはここしかない"),
            hero.remember().d("最後にパンツを君に履かせてからもう三年になるのか",
                "とスマートフォンに着信したメールの日付を見て", "唐突に思い出した"),
            hero.be(w.stage.train, w.day.deadman).d("相変わらず満員の電車はカーブに差し掛かり",
                "背中側に引っ張られるのを感じながら$meは上司から送られてきた『辞めないでくれ』という懇願の内容に",
                "一通り目を通す"),
            hero.think().d("ブラックだとは思わない"),
            hero.think().d("仕事内容に不満がある訳でもない"),
            hero.think().d("それでも入社して六年。",
                "一度として自分で何かを成し遂げた",
                "という充実感は得られなかった。",
                "このまま上から流れてきた指示通りにプログラムという小さな部品を作り続けても",
                "自分の人生には何も残らないんじゃないか",
                "そんな問いかけが生まれてしまっただけだ"),
            w.sufferer1.talk().t("……あ"),
                w.hero.look(w.i.pervert),
                w.hero.think(w.i.rescue_her, "$must"),
            hero.look().d("ドア付近に立つ鞄を肩から下げた髪の短い女性だった。",
                "自分よりも少し若いくらいだろう。",
                "ノースリーブに短いスカートから出た脚が少し覗き見えたが",
                "その女性がもぞもぞと体を動かして移動しようとしている"),
            hero.look("痴漢現場").d("けれど周囲に立つ他の客に阻まれ",
                "そこから逃げ出せないでいるようだ"),
            hero.look().d("その彼女の右手側",
                "一人の別の女性を挟んだ先に",
                "暗灰色の帽子をしたマスク姿の男性が",
                "競馬新聞を持っていない方の左手をすっと",
                "その女性のスカートに差し入れたのが見えた"),
            hero.think().d("痴漢",
                "という言葉が真っ先に浮かんで",
                "$meはそっと体を捩りながらそっち足を進める"),
            hero.think().d("$i_herword001"),
            hero.think().d("そう言っていつも憤っていた元彼女は",
                "満員電車のない土地で元気にしているだろうか"),
            hero.look().d("男の手はその女性の臀部をまさぐっているのか",
                "スカートがややまくれ上がり気味になって小さく動いている"),
            hero.look().d("女性の顔は見えないが",
                "じっと我慢しているのかも知れないと考えると",
                "さっさとその苦悶から解放してあげたかった"),
            hero.think().d("もうすぐでその男の手を掴める"),
            hero.look().d("そう思った刹那", "男の手が彼女のスカートから引き抜かれた"),
            hero.look().d("$meはその手が掴んでいたものを目にして思わず心の中で唸ってしまう"),
            hero.look("下着ドロ").d("彼の手には四つの紐がだらりと垂れ下がる",
                "女性ものの布地面積の少ない白の下着が", "握られていたのだ。",
                "彼はそれをスマートフォンでも仕舞うかのような動作で",
                "自分のジャケットの内側へと差し入れる"),
            hero.deal().d("だがそれが完全に彼のものとなる前に",
                "$meの右手がそこから下着ごと引きずり出した"),
            hero.talk().t("この男",
                "痴漢だ"),
            hero.look().d("振り返ったマスクの男は",
                "やたらと血走った目を$meに向けたが",
                "観念したのか",
                "藻掻くことも否定することもせず",
                "ただ大人しくその下着を女性に差し出し",
                "こう言った"),
            robber.talk().t("あんたには似合わないパンツだ。",
                    "だから$meが供養してやろうとしたんだよ"),
            hero.hear().d("喉に下着を詰め込んだような",
                    "潰れた声だった"),
            hero.deal(robber, "捕まえる"),
            hero.deal("拍手される").d("$meの右拳が思い切りそいつの頬に叩きつけられると",
                    "車内から控えめに拍手が起こる"),
            hero.look().d("けれど下着を返してもらった彼女は俯いたままで",
                    "電車が停車してドアが開くと一目散にそこから逃げ出して行ってしまった"),
            )

def sc_accident(w: wd.World):
    hero, robber = w.hero, w.robber
    return w.scene("事故に遭う",
                w.hero.deal(w.i.catch_pervert),
            hero.move(w.stage.sta_home).d("目的の駅ではなかったが",
                "一旦犯罪者を駅員に引き渡そうと思い", "ホームに降り立ったが、"),
            hero.talk().t("おい"),
            hero.deal().d("大人しくしていた痴漢男は$meの右手からするりと身を捻って抜け出すと",
                "そのまま車両の進行方向と反対側へと駆け出した"),
            hero.talk().t("待て！",
                "すみません！",
                "その男痴漢です！"),
            hero.think().d("僅かな油断だった"),
            hero.move().d("とにかく$meも後追いで駆け出したが",
                "人の多いホームではなかなか全速力で走ることもままならない"),
            hero.look().d("だがその痴漢男の方はこういった状況に慣れているのか",
                "上手く人を躱しながら駆け抜けていくと",
                "車両が切れたところで線路へと飛び降りる。",
                "そのまま駅を出ていこうという気だろう"),
            hero.think().d("逃がすかよ"),
            robber.go("逃亡"),
            hero.move().d("$meも後追いで飛び降りると",
                "心臓がどんどん熱くなるのも構わずに思い切り足を蹴る"),
            hero.think().d("もう少し。",
                "あと三メートル……"),
            hero.think().d("届かないか"),
            hero.look().d("踏切の遮断器が上がり",
                "男は道路側へと曲がる"),
            hero.think().d("逃げられる"),
            hero.think().d("そう思った時だった"),
            hero.look().d("$meの目の前を横っ飛びで痴漢男の体が吹き飛んでいく"),
            hero.look().d("続いてトラックの厳ついフロントが頭を覗かせたが",
                "そいつは真っ直ぐに進むことを拒否し",
                "運悪く",
                "$meの方へと向きを変えて",
                "正面からそのまま$meの意識を刈り取っていった"),
            hero.do("dead").d("そう。",
                "$meはちっぽけな正義感を振り回した挙句",
                "この世界を去ったのだ"),
            )

def sc_iampants(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("私はパンツ",
            hero.think().d("人は死んでもその意識というのはずっと消えないものなのだろうか"),
            hero.think().d("最初に感じたのは",
                "そんな疑問だった"),
            hero.think().d("普通なら意識が戻ったと感じることだろうが",
                "今の$meにとてもそんな悠長な思考はない。",
                "何故なら何も見えないし何も感じないからだ"),
            hero.think().d("それは$meが知る数少ない言葉から敢えて選ぶとすれば”無”。",
                "そう。",
                "一切が存在せず",
                "光だ闇だ",
                "男だ女だと騒ぐ必要もない",
                "完全な無の世界が",
                "どこまでも広がっているように感じられた"),
            hero.feel().d("感じる？"),
            hero.think().d("もう死んでしまったのにおかしな話だ。",
                "一体何を感じることができるというのだ。",
                "手を動かそうにも",
                "足を動かそうにも",
                "そんな感覚はどこにも見つけられない"),
            hero.be().d("ただ",
                "何だろう"),
            hero.think().d("何かの圧倒的な存在感が",
                "$meの心の一番奥底に眠るある感情をまさぐっていた"),
            hero.be(w.stage.lemurian, w.day.firstmeet),
            hero.be(w.pants),
            hero.think(w.i.myfuture),
            ery.talk().t("ほお。",
                "そなた",
                "$meが分かるのか"),
            hero.think().d("声",
                "という代物ではなかった。",
                "低く",
                "地面を揺るがすような振動を持っていたが",
                "それでもおそらくは女性のそれだと分かる"),
            hero.think().d("天国だか地獄だか知らないが",
                "その道案内でもしてくれる可愛らしい女性でもいるのか。",
                "それならさっさとその姿を見せて",
                "一瞬だけでいい",
                "自分が死んだことをちゃんと認識させてくれ"),
            hero.hear().d("だがそんなことを考えた$meに浴びせかけられたのは",
                "自分の体ごと震わすような圧倒的な高笑いだった"),
            ery.talk().t("何だ。",
                "お主はは$meに地獄送りにしてもらいたいのか？",
                "造作もないことだが……残念ながら今の$meでは少々それが難しくてな"),
            hero.think().d("何なのだろう", "この女。",
                "いやそれ以前に$meの言葉が通じているなら",
                "ずっと気になっていたことを質問してみるのが先だ"),
            hero.ask().t("なあ。",
                "あんたは$meの言葉が分かるようだから是非一つ確認したいことがあるんだが"),
            ery.ask().t("何だ？"),
            hero.ask().t("今の$me。",
                    "一体どうなっているんだ？",
                    "何も見えないし",
                    "ここは真っ暗なのか？",
                    "それに体を動かそうにも何の感触もない。",
                    "自分で自分のことがさっぱり分からないんだよ"),
            hero.hear().d("今度は噛み殺した笑いだった"),
            hero.ask().t("さっきからあんた何をそんな笑ってるんだ？",
                    "$meってそんな奇妙な格好させられてるのか？"),
            hero.think().d("会社の新入社員歓迎会で上司の命令で当時流行っていたアニメの女子のコスプレをさせられたことを思い出し",
                    "有り得ないほど短い丈のスカートからガーターベルト付きの真っ黒なストッキングの脚を見せてしまったあの恥辱が",
                    "何十回と脳裏を過って行った"),
            ery.ask().t("お主",
                    "自分が何者であるか",
                    "全く分かっておらぬ", "ということか？"),
            hero.reply().t("分かるも分からぬもないよ。",
                    "何も見えない感じない",
                    "そもそも口すらないみたいなのにどうして$meしゃべれてるんだ？"),
            hero.hear().d("小さな溜息だった"),
            hero.feel().d("けれどそれは何かの感触となって$meに伝わり",
                    "次の瞬間",
                    "今まで失われていた感覚が一気に戻ってしまったかのような激しい熱と痛みが襲ってくる"),
            hero.ask().t("あ、あんた",
                    "一体$meに何したんだ！？"),
            hero.think().d("熱いのが全身に広がると",
                    "今度はそれが一気に冷却されたみたいに意識ごと張り手をくらった感じで",
                    "$meは目を覚ました"),
            hero.do().d("そう。",
                    "目を",
                    "覚ますことが出来た",
                    "のだ"),
                w.hero.meet(w.ery),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("痴漢発見"),
            sc_hardday(w),
            )

def ep_goodbyeworld(w: wd.World):
    return (w.chaptertitle("さよなら世界"),
            sc_accident(w),
            sc_iampants(w),
            )

# outline
def baseinfo(w: wd.World):
    return [
            ("chapter 1-01", story(w), w.hero, w.ery),
            ]

def outline(w: wd.World):
    return [
            ("chapter 1-01", story(w),
                w.hero.think(w.i.rescue_her, "$must"),
                w.hero.look(w.i.pervert),
                w.hero.deal(w.i.catch_pervert),
                w.hero.meet(w.ery),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle("一枚目：すべてはパンツから始まる"),
            ep_intro(w),
            ep_goodbyeworld(w),
            )

def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

