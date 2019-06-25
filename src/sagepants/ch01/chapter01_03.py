# -*- coding: utf-8 -*-
"""Chapter 01-03: The pants.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf


# scenes
def sc_little_ery(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("小さくなったエリィ",
            hero.be(w.stage.prison, w.day.firstmeet),
            hero.look(ery, "小さい").d("彼女が作り出した鏡のような水面には",
                "パンツとなった$meを履いたままその両端を小さな手でぎゅっと握りしめて立っている",
                "胸元までの長さの紫色の髪を垂らした幼女が映っていた"),
            hero.talk().t("あの……"),
            hero.think().d("泣きそうなところを必死に我慢している彼女に対して",
                "何を言ったものかと思案してみたが",
                "声を出したところでその目が鋭くなったのを確認して",
                "$meはすぐまた黙り込む"),
            hero.look().d("先程まで$meが彼女だと思っていた大人びた体つきの女性が低学年向けパンツを履く姿は",
                "どこかそういう世界観のプレイでもしているように見えて",
                "強烈な違和感が醸し出されていたが",
                "今こうして小さい女の子が$meというパンツを履いている姿として映し出されると",
                "何の抵抗もなく自分がただの幼児向けパンツであることを受け入れられそうな気分になる。",
                "それくらい彼女に$meは似合っていた"),
            hero.look().d("しかし当の本人はそれなりに文句があるようで",
                "口元をぎゅっと結びつけて",
                "何かを必死に堪えている"),
            hero.ask().t("一つ確認なんだが"),
            ery.ask().t("何だ"),
            hero.hear().d("声が不機嫌だ。",
                "ただ先程までのような威圧感がない為か",
                "どこか可愛らしい"),
            hero.ask().t("今$meが見ているこの女の子は",
                "あんたで間違いないんだな？"),
            ery.talk().t("ああそうだが……女の子言うな！"),
            hero.deal().d("眉毛がくっと角度を急にして",
                "彼女の小さな丸い手が$meの目の前に何度も叩きつけられた"),
            hero.feel().d("しかし痛覚を持たない$meにとって",
                "それはただ単に視界を幼女の拳が覆うという現象に過ぎない"),
            hero.think().d("これはこれでいくら叩かれても大丈夫というのは良いものかも知れない"),
            hero.think().d("そんな思いが生まれるくらいパンツ人生に馴染みつつある自分が悲しくなる"),
            hero.ask().t("失言はすまない。",
                "謝るよ。",
                "ただあんたはどうして小さくなったんだ？",
                "何かしたのか？"),
            hero.look().d("だが彼女はじっと水面に映る$meを見たまま",
                "何も言わない"),
            hero.talk().d("ひょっとして……$meの所為なのか？"),
            hero.look().d("その問いかけに渋々といった体で彼女は小さく頷いた"),
            )

def sc_prisoner(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("収監された少女",
                w.hero.know(w.i.her_status, "$want"),
                w.hero.know(w.i.this_world),
                w.hero.talk(w.ery, w.i.her_status),
            hero.talk().t("ちょっと待て。",
                "$meは何もしてないし",
                "そもそもただのパンツだぞ。",
                "そいつに何が出来るって言うんだ？"),
            hero.think().d("自分の所為と彼女に言われて慌てたが",
                "よくよく考えてみれば$meを履いた大人の女性が幼女になっただけだ。",
                "そのよく分からない現象の責任をパンツである$meに押し付けてもらっても困る"),
            ery.talk().t("力が……出せないのだ"),
            hero.ask().t("力って何の？"),
            ery.talk().t("$i_energyと呼ばれておるものだ。",
                "重い石を手を使わずに持ち上げたり",
                "炎を出したり",
                "水を鏡にしたり",
                "お主にやってやったように物体に視覚や聴覚を与えるなどといったことも可能だ"),
            hero.think().d("手品とは違う",
                "ということだけは分かった"),
            hero.think().d("こんな状況でもなければ$meはあまりそういった迷信じみたことに理解を示さないが",
                "流石に自分がパンツになってしまっていて",
                "そんな$meに目と耳を与えてくれたらしい彼女の言葉を信用しない訳にもいかないだろう"),
            hero.talk().t("それがどうして出せなくなったんだ？"),
            hero.hear().d("彼女は一際大きな溜息を落としてから",
                "小さく首を振ってこう続ける"),
            ery.talk(w.i.destroy_sage.flag()).t("だからお主の所為だと言っておる。",
                "どういう理屈かは分からんが",
                "パンツとやらを履いたら$i_energyが急激に萎んでいき",
                "見事に育ったはずだった$Iの体があの頃の軟弱な自分に戻ってしまった。",
                "世界を破滅に追いやった大賢者様がこんなちんちくりんじゃ", "良い笑いものだぞ"),
            hero.think().d("パンツを履くと力が失われる",
                "という発言に",
                "$meは小さい頃に楽しんだあるＴＶ番組の再放送を思い出した。",
                "あれはパンツではなく金の輪っかだったが",
                "それを付けられた粗忽者の猿男は経典を求めて旅をする僧侶に戒められる度に呪文によりその輪を締められる。",
                "痛みによって力を制御される様は",
                "子供心にも体育会系の肉体派指導ここにあり",
                "と刻み込まれたが",
                "人というのは言葉では何も教えられないのかも知れないという諦めも同時に$meの心の中に植え付けていった"),
            hero.ask().t("それなら$meを脱げばいいんじゃないのか？"),
            hero.think().d("$meを履いて縮んだというなら", "それで問題は解決するはずだ。",
                "もし仮にそれでも元に戻らない場合は",
                "これはもう$meが原因ではないということになる"),
            ery.talk().t("それでもそうだの。",
                "何故そんな簡単なことに思い至らなかったのだろうか……",
                "よし分かった。",
                "脱ぐぞ？"),
            hero.think().d("そんな確認は要らないと思ったが$meは一応「おう」と頷いてやると",
                "彼女は$meの両端を掴み",
                "勢いよくそれを下ろした"),
            ery.talk().t("ん！？"),
            hero.look().d("勢いよくそれを"),
            ery.talk().t("おい！",
                    "お主今度は何をしておるんだ！"),
            hero.talk().t("いや$meは何も。",
                    "そもそも何か出来るならあんたに言われる前にしてるよ"),
            hero.think().d("ただのパンツに無理言わないでくれと思いつつも",
                    "何故彼女はさっさと$meを脱がないのだろうと不思議に感じた"),
            hero.talk().t("どうしたんだ？"),
            ery.talk().t("脱げん"),
            hero.think().d("はあ？",
                    "である"),
            hero.talk().t("パンツが履けたのなら脱ぐことも出来るだろう？",
                    "それとも誰かにしてもらわないとパンツすらまともに脱げないくらい退化してしまったのか？"),
            ery.talk().t("ええいうるさい！",
                    "$Iだってパンツくらい一人でどうとでも出来るわ！",
                    "侮るでないぞ！"),
            hero.look().d("しかし一向に$meの視界は変わらない"),
            hero.feel().d("そればかりか",
                    "触覚がないはずなのに体の内側にピッタリフィット感があった。",
                    "それが存外心地良い。",
                    "これが収まっているという満足感なのだろうか"),
            hero.think().d("パンツの満足感て何だよ……"),
            ery.talk().t("んーんー！",
                    "脱がして！",
                    "パンツ脱がして！"),
            hero.look().d("そんなことを考えている間にも",
                    "彼女を$meを引っ張って無理やり自分の足から引き抜こうとしているが",
                    "どういう訳か皮膚の一部にでもなったのかのように",
                    "パンツは彼女の臀部をしっかり覆ったまま離れようとしない"),
            hero.think().d("仮に$meが人間であったなら",
                    "幼女の下腹部に抱きついたまま殴られても蹴られてもしっかりと抱き締めたままでいるといった感じかも知れないが",
                    "生憎と$meにはそんな趣味はないし",
                    "何より$meはパンツだ。",
                    "彼女を掴む手すら持ち合わせていない"),
            hero.think().d("$meがどうこうして解決する問題とは思えなかった"),
            hero.talk().t("なあ",
                    "もう諦めたらどうだ？",
                    "パンツ", "脱げないんだろ？"),
            ery.talk().t("分かった。",
                    "壊す"),
            hero.think().d("何？"),
            ery.talk().t("いくら$Iの$i_energyが失われたからといっても",
                    "こんな布切れ一枚破壊するのは造作もない"),
            hero.talk().t("おい。",
                    "やめろ。",
                    "パンツは大事なんだぞ？",
                    "$meがいないとお前は一生丸裸で暮らすことになるんだぞ？",
                    "それでもいいのか？"),
            hero.think().d("無茶苦茶な理論だと思ったが", "背に腹は変えられない。",
                    "いや今はパンツだから背も腹も表も裏も変え放題な気がするけれど",
                    "とにかくそんな悠長なことを言っている場合ではない"),
            hero.look().d("彼女のしっかりと握りしめた右手が光を放ち",
                    "その手を開くと",
                    "輝きが一気に広がった"),
            hero.hear().d("一瞬の間の後で",
                    "大きな地響きを聞いた"),
            hero.think().d("耳がツンとするような張り詰めた静寂を感じると",
                    "次第に視界がはっきりとしてくる"),
            hero.look().d("そこには彼女の手が光を放つ前とほぼ同じ空間が広がっていることが確認できた"),
            hero.talk().t("あれ……大丈夫", "なのか？"),
            ery.talk().t("なぜだ……なぜ壊れぬ！"),
            hero.hear().d("彼女の驚きの声も", "幼いままだ"),
            ery.talk().t("なんで壊れてくれないの！",
                    "そうか。",
                    "ひょっとしたら$Iの力そのものが弱っていてお主を破壊できないのか？"),
            hero.look().d("そう言うと今度はその手を鏡にした水面へと向け",
                    "光を放った"),
            hero.feel().d("空間そのものが震える衝撃の後で",
                    "水面は見事に水滴すら残さずに消滅してしまう"),
            ery.talk().t("おかしいな……。",
                    "何故お主は壊れんのだ？"),
            hero.talk().t("$meに聞かれても知らないよ。",
                    "それよりもこんだけ出来るのにそれでも力が無くなったって言うのか？"),
            ery.talk().t("ここが普通の檻なら",
                    "本来の$Iの力であれば全てを塵にまで分解してしまえる。",
                    "しかしここは特別製でな。",
                    "まあ見てみろ"),
            hero.look().d("そう言うと",
                    "彼女は体を鉄格子に向けて$meにはっきりと見えるようにした。",
                    "それから手を翳して一撃",
                    "光の銃を放つ"),
            )

def sc_thesage(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("世界を滅ぼす大賢者",
            hero.look().d("彼女の手から発射された小さな光の弾は幅広な鉄格子の間をすり抜けるかと思われたが",
                "その隙間に入りかけたところで何かに弾かれたかのように角度を変え",
                "そのまま地面に落ちて爆発した"),
            ery.talk().t("こういう訳だ"),
            hero.think().d("$i_energeyを検知してそのベクトルを変えるような高度な装置なのだろうか"),
            ery.talk().d("よく分からないことを言っておるが",
                "あれは$i_metalと呼ばれるもので造られた特別な格子でな",
                "接近する$i_energyを容赦なく弾くのだ。",
                "ちなみにこの檻は天井も壁も床も全てがその素材を混ぜた土で覆われておる"),
            hero.talk().t("仕組みは分からないけど",
                "あんたを閉じ込めておく為の特製の檻って訳か"),
            ery.talk().t("$Iを", "という訳ではなかったが……まあそうだな"),
            hero.think().d("何か含みのある言い方だったが", "そう言って彼女は少し笑った"),
            hero.ask(w.i.destroy_sage.deflag()).t("そういやあんた",
                "さっき自分は世界を滅ぼしかけた大賢者だと言ったが",
                "$meの知識では賢者と言えばそんな風に世界を滅ぼしたりはしないもんだ。",
                "寧ろ逆にそういった脅威に対して何か対抗手段を講じたり助言をしたり",
                "戦ってくれたりと",
                "他の人間から感謝されるような立場にある存在だと思うんだが？"),
            ery.talk().t("お主の世界のことはよう知らんが",
                "ここで賢者と言えば数千という智を修めて$i_energyの真理を極めた最高クラスの魔道士のことだ。",
                "その中でも当代で一番優れた者のみが大賢者を名乗ることを許される。",
                "この意味が分からんということはあるまい"),
            hero.think().d("ついさっきまで泣きそうに顔を赤くしていた女の子の口ぶりからは一転",
                "自信に満ち溢れた当初の彼女らしさが戻っていた"),
            hero.ask().t("で",
                "その大賢者様がどうしてこんな場所に閉じ込められているんだ？",
                "いやそもそも",
                "なんでパンツなんて呼び出してるんだ？",
                "そっちの方が大いに謎だぞ"),
            ery.talk().t("お主を呼び出したかった訳ではない。",
                "そもそもこの脱出不可能な箱の中から出る為に",
                "世界そのものに穴を開けようとしておったのだ……。",
                "だが何故かその結果としてお主が現れた。",
                "$Iにも理屈はよう分からん"),
            hero.think().d("ひょっとしてそれは何かの手違い",
                "あるいはとばっちりなんじゃないだろうか"),
            hero.think().d("そんな思考が過って行ったが",
                "ともかく$i_energyと呼ばれる不思議な力を操ることが出来る人間が彼女以外にもいるらしい",
                "ということだけは分かった"),
            hero.ask().t("しかし疑問なんだが",
                "その$i_energyを弾くという檻でもあんたが$i_energyを使わなければ出られるんじゃないのか？"),
            ery.talk().t("は？"),
            hero.hear().d("明らかに$meを馬鹿にした「は？」だった"),
            hero.talk().t("今のあんたの説明からは近づく$i_energyを弾くって言ってただろ？",
                "つまりその$i_energyがない", "あるいはごく低出力だったなら",
                "簡単に出られるんじゃないのか", "ってこと"),
            ery.ask().t("それは……ホントか！？"),
            hero.think().d("訊かれても知らんぞ", "とは思ったが$meは彼女を焚き付けるように「そうだそうだ」と適当に頷くと",
                "彼女は喉の奥でクルクルとした笑い声を漏らし始め、"),
            ery.talk().t("やっと……ここから……出られるのか"),
            hero.hear().d("そう呟いてから",
                    "鼻水を啜った"),
            )

def sc_outprison(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("脱獄できる！？",
            hero.think().d("泣いているのだろうか"),
            hero.think().d("だがそれを確かめる為の術を今の$meは持っていない。",
                "ただその声や雰囲気から感じ取るしかない"),
            hero.think().d("そう思っていたのだが"),
            hero.ask().t("ん？"),
            ery.ask().t("何だ"),
            hero.talk().t("いやその……気の所為だ"),
            ery.ask().t("おかしなことを言う奴だな……$Iが何かしたのかと"),
            hero.hear().d("だがそこで彼女の言葉が停止した"),
            hero.ask().t("どうした？"),
            ery.talk().t("何でもない……"),
            hero.think().d("明らかに何かある。",
                "そしてそれは今$meが感じているある異変に関連したものだと直感した"),
            hero.deal().d("それについては何も言及しないまま",
                "彼女の足が動き出す。",
                "鉄格子へと近づいていく"),
            hero.feel().d("だがそれに伴って$meの体の内側を",
                "何とも冷たい感覚が抜けていく"),
            hero.think().d("ちょうど真夏の営業の合間に立ち寄ったコンビニで購入したアイスを構わずに喉に押し込んだ",
                "その冷気が胃袋まで落ちていく様を思い出すようだ"),
            ery.talk().d("本当に大丈夫……だろうか"),
            hero.hear().d("そんな$meのことなど構わず",
                "鉄格子の前まで到達した彼女は呟きを漏らすと",
                "両手を前へと伸ばした。",
                "その様が何とか視界の上端に見える"),
            hero.look().d("その指の先が震えながら鉄の棒と棒の合間の空間へと伸ばされていく"),
            hero.think().d("何も起こらない。",
                "そう期待しつつ", "$meは自身の内側の冷たい感覚にむずむずとしていた"),
            ery.talk().t("ほお……これはこれは"),
            hero.look().d("彼女の愛らしい手が二つとも鉄格子の外へと出されている。",
                "何ともない。",
                "弾かれたり",
                "妙な光も現れずに",
                "その上腕の部分まで外へと出すことが出来ていた"),
            )

def sc_namedtaro(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("お前はタロウ",
                w.hero.deal("名付けられた"),
            ery.talk().t("これで出られるぞ！",
                "でかした$hero！"),
            hero.ask().t("タロウ？",
                "$meはそんな名前じゃないぞ"),
            ery.talk().t("何を言っておるか。",
                "$heroというのは$i_mean_taroという意味で",
                "非常に名誉ある呼称なのだぞ？"),
            hero.think().d("これこそ本来の意味での価値観の相違というものだろうが",
                "そんな瑣末な問題よりも$meは肝心なことに気づいた"),
            hero.talk().t("$meの名前は……何だ？",
                "思い出せない"),
            ery.ask().t("それなら$heroで良いではないか。",
                "そもそも物に名前が無いのは当たり前のことだ"),
            hero.talk().t("いやいや。",
                "名前がないんじゃなくて$meには元からあったんだよ"),
            ery.ask().t("ではお主。",
                "何と言うのだ？"),
            hero.think().d("それが思い出せない。",
                "全てを思い出せないというならまだ納得もいくが",
                "あんなに鮮明に事故死する直前の映像を覚えているのに",
                "最も単純で馴染みの深いはずの己の名前を",
                "一文字として$meは思い出すことができなかった"),
            ery.talk().t("もうそれなら$heroで良いではないか。",
                "$i_realnameさえ知られていないのであれば何も問題なかろう"),
            hero.think().d("また意味の分からないことを言われたが",
                "それよりも$meは自分の名前が思い出せないショックの方がずっと大きかった"),
            ery.talk().t("ところで$hero"),
            hero.ask().t("何だ？"),
            ery.ask().t("手だけ出て体の方を外に出せないんだが",
                "どうすれば良いかな？"),
            hero.talk().t("そんなこと$meが知るか！",
                "隙間から出るなり鍵を開けるなり何なりして出てくれよ！"),
            ery.talk().t("ああ", "なるほど"),
            hero.think().d("$meが心の中で大量の溜息を零し終えた頃、"),
            hero.hear().d("カチリ"),
            hero.deal().d("と音が聴こえて",
                "彼女は開いた部分から外に足を踏み出した"),
            )

# episodes
def ep_littlegirl(w: wd.World):
    return (w.chaptertitle("小さな女の子"),
            sc_little_ery(w),
            )

def ep_abouther(w: wd.World):
    return (w.chaptertitle("彼女とこの世界について"),
            sc_prisoner(w),
            sc_thesage(w),
            sc_outprison(w),
            sc_namedtaro(w),
            )

# outline
def baseinfo(w: wd.World):
    return [
            ("chapter 1-03", story(w), w.hero, w.ery),
            ]

def outline(w: wd.World):
    return [
            ("chapter 1-03", story(w),
                w.hero.know(w.i.her_status, "$want"),
                w.hero.know(w.i.this_world),
                w.hero.talk(w.ery, w.i.her_status),
                w.hero.deal("名付けられた"),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle("三枚目：パンツの名は"),
            ep_littlegirl(w),
            ep_abouther(w),
            )

def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

