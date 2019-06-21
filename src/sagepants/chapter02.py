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
            hero.think().d("自分がパンツとして彼女に履かれている"),
            hero.think().d("という衝撃の事実に思い至った瞬間の出来事だった"),
            ery.talk().t("な、何だというのだ"),
            hero.hear().d("彼女の驚く声が響き",
                "次いで$meの視界がどんどん低くなっていく"),
            hero.feel("彼女の感触").d("またそれに伴って",
                "何というのか",
                "$meが包み込んでいる彼女の下腹部が最初のしっかりと張りがあるものから",
                "もっと柔らかいそれへと感覚が変わっていくのに気づいた"),
            hero.ask().t("なあ", "あんた今度は何をしたんだ？"),
            ery.talk().t("知らん"),
            hero.hear().d("けれどそう答えた彼女の声は先程までとは明らかに違い",
                "動揺からか", "随分と甲高い声へと変容している"),
            hero.ask().t("やっぱり何か変だぞ？"),
            ery.talk().t("知らんたら知らんのだ！"),
            hero.think().d("先程までの泰然と構えていた様子から一転",
                "明らかに彼女は慌てていた"),
            hero.ask().t("なあ", "ちょっとさっきの鏡で今の姿を見せてくれないか？"),
            hero.think().d("自分で見られれば苦労しないのだが",
                "今は他人の一部みたいなものだ。", "視界に入るのは部屋の床や壁だけだった"),
            ery.talk().t("だ、駄目だ"),
            hero.ask().t("どうして？"),
            hero.think().d("そういえば彼女の声が響いてくるその位置もまた",
                "先程より近くなっている気がする。",
                "彼女が縮んでいる……のだろうか"),
            ery.ask("何かした？").t("お主こそ何かしたのではなかろうな？"),
            hero.feel("不思議な感覚").d("少し泣きそうな声にも聞こえる。",
                "それに$meの視界にちらちらと映り込む彼女の手も",
                "何だろう", "もっとしゅっとしていたはずなのに",
                "今のそれは太ってしまったのか", "指が短く見える"),
            hero.talk().t("あ……"),
            hero.look().d("何より今までとの決定的な違いに気づいた。",
                "あれほど大量にあった髪が", "一切見えないのだ"),
            hero.ask().t("やっぱあんた変だ。",
                "大丈夫なのか？"),
            ery.talk().t("知らん知らん知らん！",
                "あぁもう！",
                "どうしてこんなことに"),
            hero.think().d("よく分からないが彼女は困っているようだった"),
            hero.think().d("$meは内心で溜息を零し",
                "それから自分の体があったならその向きを少しばかり変えて姿を確認できるのに",
                "と思考した"),
            ery.talk().t("あ"),
            hero.hear().d("という彼女の吐息に続いて",
                "その視界が僅かに動いた"),
            hero.look("強烈な光").d("足元の水面に向かった視界に",
                "一瞬立ちくらみを覚えるような強烈な光を見た気がした"),
            hero.talk().t("これは……"),
            hero.look().d("それからゆっくりと自分の視界を確認すると",
                "鏡となった水面には代わり映えのしない$meという犬プリントのパンツと、"),
            ery.talk().t("だから見るなと言うただろうが！"),
            hero.look("幼女エリィ").d("モデルのような八頭身美女とはあまりにもかけ離れた",
                    "身長百三十センチ程度の", "まるで子供と呼んで差し支えのない幼女が",
                    "そこには映り込んでいた。",
                    "髪は彼女の小さな胸を隠す程度まで短くなり",
                    "その大きな瞳には涙が蓄えられていた"),
            ery.ask().t("$Iがこのような姿になって笑わぬのか？"),
            hero.hear().d("今し方までの落ち着いた威圧感のある物言いとは打って変わり",
                    "若干舌足らずの可愛げな声で話す"),
            hero.talk().t("笑われるなら$meの方だろう？",
                    "だって$meの姿なんてパンツなんだぜ？"),
            hero.look().d("彼女の小さな手は",
                    "$meの両サイドを掴んでぎゅっと握られていた"),
            hero.think().d("痛みはない。",
                    "というか痛覚はないのだろう。",
                    "ただ彼女のぷっくりとした指で触れられていることだけは分かる"),
            w.hero.be(w.stage.prison, w.day.firstmeet, w.ery),
            ery.ask().t("このような弱々しい姿を見ても",
                    "お主は笑わぬというのか！？"),
            hero.talk().t("一つ尋ねるが",
                    "このちっこい姿というのは弱々しいのか？",
                    "$meの価値観でいえば",
                    "ただの子供だ。",
                    "子供というのは確かに力も弱く知識も乏しいかも知れないが",
                    "$meたち大人にはない可能性を秘めている。",
                    "その可能性を笑うような歪んだ精神は持ち合わせていないつもりだぜ"),
            ery.talk().t("そうか", "笑わぬのか"),
            hero.look().d("彼女は考え込むようにしながら水面に映った$meである自身の履くパンツを見やると",
                    "笑顔になる"),
            ery.talk().t("そうか。",
                    "お主は好い奴だな。",
                    "気に入ったぞ", "$hero"),
            hero.ask().t("た、太郎！？"),
            hero.think().d("何だその安直かつ名前を思いつかないから適当に命名されてしまった犬や猫のような扱いは"),
            ery.talk().t("気に入らぬのか？",
                    "$heroとは$i_language1で”優しき者”という意味があるのだぞ？"),
            hero.talk().t("お前の世界では良い名前だというのは分かったが",
                    "$meにだって立派な名前があって……"),
            ery.ask().t("ほお。",
                    "それで名は何と言うのだ？"),
            hero.think().d("おかしい。",
                    "自分が事故死したことは思い出せたのに",
                    "それ以外のことがさっぱりだ。",
                    "頭がどうかしてしまったのだろうか。",
                    "それともパンツになったショックか……"),
            hero.talk().t("$meの名は……"),
            ery.ask().t("名は？"),
            hero.talk().t("名前は……$Iだ"),
            hero.think().d("そう答えてしまった瞬間に$meの中の何かがポキリと折れたような気がしたが",
                    "彼女は特に気が付かなかったようで、"),
            ery.talk().t("そうか。", "元からお主は$heroであったか"),
            hero.think().d("と一人頷いている"),
            hero.look().d("しかし改めてパンツとなった自分を履く幼女が両手を腰にやって満足そうにコクコクと顎を上下させている姿を目の当たりにすると",
                    "何ともやるせない気分になってしまう"),
            hero.think().d("$meは死んでパンツになったのか？",
                    "それも会話が出来るパンツって何だ。",
                    "これまで生きてきた中で史上最高に受け入れがたい事態に既に馴染みそうになっていることに",
                    "$Iである$meは戦々恐々とした"),
            hero.talk().t("ああ、そうだ。",
                    "まだあんたの名前を教わっていなかったな。",
                    "で、その大賢者様のお名前は何と呼ぶので？"),
            hero.look().d("もうその面影が無くなってしまったただの小学生低学年に見える彼女は",
                    "それでもすっと口元を結んで目つきを鋭くすると",
                    "鼻で笑ってから$meにこう言った"),
            ery.talk().t("大事な真名をそう易々とは教えられぬな。",
                    "だから$eryと呼ぶことを許してやろう"),
            hero.talk().t("$eryだな？", "分かった。",
                    "で、その$eryちゃんはさ"),
            ery.ask().t("ちゃん……だと！"),
            hero.think().d("何が引っかかったのか", "彼女は表情を歪めた"),
            ery.talk().t("ちゃん……ちゃん！"),
            hero.talk().t("その、すまないが", "ちゃんは悪かった"),
            hero.think().d("よく分からなかったが", "ひとまず謝っておく"),
            ery.talk().t("な、何故謝るのだ？"),
            hero.talk().t("いやだってちゃん付けは嫌なんだろう？"),
            hero.look().d("彼女は首を高速で左右に振ってぷにっとした頬をふるふるさせた"),
            hero.talk().t("いいのか？"),
            ery.talk().t("その、特別だぞ。",
                    "特別に$Iをちゃん付けで呼ぶことを許可してやる"),
            hero.look().d("とても許してやろうという高圧的な態度ではなく",
                    "ひくひくとした鼻の穴とその笑いを堪えている様からは",
                    "明らかに喜んでいるのが見て取れた"),
            hero.talk().t("それで$eryちゃんさ"),
            ery.talk().t("な、何だ？"),
            hero.look().d("実に嬉しそうだ"),
            hero.talk().t("それだけ強大な力を持ちながら",
                    "どうしてこんなちっぽけな檻一つ壊せないんだ？"),
            )

def sc_breakprison(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("脱獄しよう",
            hero.look("場所確認").d("目の前には腕を余裕で外に出せそうな幅広の鉄格子が見えていた"),
            hero.ask().t("あれを少し曲げれば外に出られるんじゃないのか？"),
            hero.think().d("映画なんかでよく見る怪力を持ったヒーローや超能力を持った極悪人は",
                "クイと捻じ曲げてすぐに脱出口を作って見せる。",
                "仮にも世界を滅ぼしかけたという大賢者ならそれくらい造作も無いことのように思えるのだが"),
            ery.talk().t("あれがただの鉄格子ならな"),
            hero.talk().t("何か特殊加工がされている", "というのか？"),
            hero.look().d("見た目は何の変哲もないものに見えたが",
                "閉じ込められていた本人が言うのだから間違いないのだろう"),
            ery.talk().t("そもそも",
                "何百年も掛けて次元に穴を開けようとしている中でお主が現れたくらいだ。",
                "力が強大であればあるほど", "ここは外界へは繋がることはない"),
            hero.think().d("正直何を言っているのか理解できない"),
            hero.think().d("だがそもそも$meはパンツなのだ。",
                "既に常識で考えることは間違っているのだろうと思い",
                "いつものような癖は心のポケットに仕舞っておくことにした"),
            hero.talk().t("理屈は分からないが",
                "$meが現れたってことは何かしら変化があったかも知れないだろう？",
                "試してみたらどうだ？"),
            hero.think().d("ここでこのまま$eryのパンツとして過ごすというのも悪くないかも知れない",
                "という既に正常な判断力を失いつつある$meではあったが",
                "流石に何百年も変わらない景色を眺めて過ごしたいとは思わない。",
                "そこまでいかれてもいない"),
            hero.think().d("いや案外そうでもないのだろうか。",
                "自分がパンツであることを受け入れている時点で",
                "内心で「どうにでもなれ」という魔法の呪文を唱えてしまった気がする"),
            ery.talk().t("そこまで言うなら試してやらんこともないが",
                "$heroは大丈夫だろうな？",
                "弾け飛んでも知らぬぞ"),
            hero.talk().t("え？"),
            hero.think().d("聞き捨てならないことを言われた気がするが",
                "それを制止するより早く彼女はすたすたと歩いて鉄格子の前まで行くと",
                "その棒に右手を伸ばした"),
            hero.talk().t("弾け飛ぶとか", "言わなかったか？"),
            ery.talk().t("これは魔力を跳ね返す特殊な金属で出来ておってな",
                "こうして触れると……"),
            hero.look().d("彼女の小さな手が", "棒を掴む。",
                "しっかりと握るには少し太いようで",
                "一周ぐるりと掴む訳にはいかないようだったが",
                "ぴたりと吸い付くようにそれを握り締めた"),
            hero.talk().t("触れると", "何だ？"),
            ery.talk().t("……何も起こらんな"),# TODO
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
            sc_breakprison(w),
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

