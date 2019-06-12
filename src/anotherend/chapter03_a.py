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
            ak.talk().t("あぁ！！！"),
            ak.do("wake").d("思い切り叫び声を上げたと思って目を開けると",
                "自分の声が聞こえないくらい大勢の喧騒の中で",
                "$meは突っ立っていた"),
            ak.think().d("何だこのおかしげなコスプレ連中は"),
            ak.explain().d("コスプレ。",
                "つまりコスチュームプレイとは何かしらのキャラクターと同じ衣装を着て",
                "時にカツラやメイクなどで見た目をそのキャラクターへと近づけて",
                "自分を捨て", "その人物に成り切る",
                "という一種のロールプレイだ"),
            ak.look("沢山のSF的人物たち").d("今までに$meが見た連中は",
                "どちらかといえばまだそれなりの統一感があった。",
                "だが今目にしている有象無象な",
                "人間と呼んでいいかどうかすら分からない者まで混ざった群衆を目にして",
                "$meは圧倒されていた"),
            zer.talk().t("ここではみんな自分が好きな格好ができるみたいだよぉ"),
            ak.look(zer).t("$zer？"),
            ak.look().d("後ろからの声に振り返ると",
                "スカイブルーの瞳の少女が笑って立っていた。",
                "彼女は変わらずに水兵っぽい白のセーラー服姿で",
                "怪訝に眉を顰めた$meに対して旧知の仲のように右隣にやってきて肩を寄せた"),
            ak.ask(zer, "知ってるか？").t("おい。",
                "お前は$meの知ってるお前か？"),
            ak.look().d("彼女はその意味が理解できたのか",
                "コクン", "と頷きを見せると声を潜めて耳元でこう囁いた"),
            zer.reply("覚えてる").t("また死んじゃったんでしょ？"),
            ak.feel().d("それから脇腹を軽く突く"),
            ak.think().d("あれは夢じゃなかったってことなのか"),
            ak.look().d("$meはシャツを捲り上げて脇腹を見たが",
                "血は流れていない"),
            ak.look().d("ただそこにベルトのように真っ直ぐ腹回りに沿って",
                "赤い痣が付いていた"),
            ak.think().d("本当に斬られたのか？"),
            ak.look().d("$zerを見たが彼女は小首を傾げただけだ"),
            ak.think().d("考えても仕方ないが", "こいつもまた居るのか"),
            ak.deal().d("$meは足元に落ちていた林檎を拾い上げると",
                "それを齧ってみる。", "固い。", "味もしない。",
                "ただの玩具だ"),
            ak.ask("この世界"),
            ak.look("フロア状況").d("現実に戻った$meは改めて",
                "この騒々しさの正体を知る為に視線を巡らせた"),
            ak.look().d("一番手前の奴は黒革のロングジャケットなのに",
                "背中に長い剣を背負っているし",
                "そこから先にある壇上に登っている女は白のロングニーソに赤いスカート",
                "上は金糸で刺繍された白い肩出しの厚手の上着だ。",
                "手もロンググローブをしていて", "暑苦しいとしか感じられない"),
            ak.look().d("他にも目元だけを覆う仮面を付けている金髪の男性や",
                "腕がドリルになった大柄の男", "背中にロケットを背負ったり全身金属に包まれた者までいる"),
            ak.think().d("何でもありなのか？"),
            ak.look().d("$meはひょっとしたら", "という思いでその集団の中に彼女がいないか",
                    "視線を巡らせた。",
                    "けれど身長百四十程度の小柄な女性は何人も混ざっていたが",
                    "その中に$n_minaeらしき容姿を持つ者は見当たらない"),
            ak.know("ロボの世界？"),
            ak.ask(w.i.transfer, "他にも？").t("なあ$zer。",
                    "前に$meが$i_transferだって言ったよな？"),
            zer.reply().t("うん", "そおだよぉ。",
                    "$akuraは$meとの契約で$i_transferになったの"),
            ak.ask().t("その$i_transferってのは$me以外にも存在するのか？"),
            w.tag.comment("実は林檎がその別の次元妖精で、美綯の妖精"),
            zer.talk("可能性は", w.i.another_fairy.flag()).t("$meとの契約者は他にいないけどぉ",
                    "でも$i_fairyは$meだけじゃないからね。",
                    "もしかしたらどこかで別の世界で$i_transferになった誰かと遭遇する……かも？"),
            ak.look().d("$zerは楽しげにコロコロとした笑い声を上げる"),
            ak.think(w.minae, "彼女を探す").d("今までに二度",
                    "$meは彼女を目撃した。",
                    "あれは幻影なんかじゃなく",
                    "確かに$n_minaeだった。",
                    "だとすれば", "彼女もまた$i_transferだということなのだろうか"),
            ringi.talk("初心者か？"),
            ak.deal("教わる"),
            ak.ask().t("仮にもう一人の$i_transferがいたとして",
                    "そいつも$meと同じ世界に移動するのか？",
                    "だが$meは殺されたから転生したんだろう？",
                    "じゃあそいつも死んだのかってことになる"),
            ak.look().d("そんなぼやきに「何の話ぃ？」と苦笑する$zerは",
                    "突然その顔の向きを変えた"),
            ak.ask().t("どうした？"),
            zer.reply().t("あそこのモニタ"),
            ak.look().d("言われてから初めて$meはここが巨大なドーム状の室内で",
                    "天井から吊り下げられた壁のようなモニタがあることに気づいた"),
            ak.look("暗くなる"),
            )

def sc_declaration(w: wd.World):
    ak, zer, ringi, killer, matsu, akane = w.akura, w.zer, w.ringi, w.killer, w.matsuda, w.akane
    return w.scene("開始宣言",
            ak.look().d("その巨大モニタが全面ブルーに染まり",
                "天井から降り注ぐように照らしていた無数のライトが一斉に消えた"),
            ak.hear().d("おぉ……といったざわめきが広がり",
                "誰もがそのモニタに注意を向けた"),
            ak.look().d("ざ、ざ、という雑音。",
                "それに続いてモニタも真っ黒になり", "一瞬の間の後",
                "それが鈍く光った"),
            ak.talk().t("……何だ"),
            ak.look().d("カメラが一気に引きの絵になると",
                "その黒が単なるブラックスクリーンではなく",
                "黒いマントの一部だったと判明する"),
            killer.talk().t("諸君……"),
            ak.hear("謎の声").d("それは出来の悪い合成音声のような声だった"),
            w.killer.talk("デスゲーム開始宣言").t("今ここに集う者たちは皆それぞれ",
                "己の力を過信する者ばかりだろう"),
            matsu.talk().t("過信じゃねえよ。",
                "難攻不落と言われたこの$st_castle3まで到達した$meたちだぞ！"),
            akane.talk().t("そやで！"),
            ak.look().d("声を上げたのはどうやら黒革ジャケットの男と白ニーソの女のカップルのようだ。",
                "その二人に追随して",
                "周囲の者もそれぞれの手を突き上げて騒ぎ出す"),
            ak.look().d("一陣の風だった"),
            ak.look().d("巨漢の首がずり落ち", "そこから鮮血の噴水が上がる"),
            akane.talk().t("きゃぁぁぁ！！"),
            killer.talk().t("大人しく話を聞けない人は嫌いだ"),
            ak.hear().d("その感情のない合成音声に", "少々の苛立ちを感じたのを$meだけじゃなかったようだ。",
                "誰もが息を呑み", "一斉に口を噤んだ"),
            ak.feel().d("辺りを静寂が支配する中で", "その黒マントはゆっくり話を続ける"),
            killer.talk().t("力はより強い力によって制御される。",
                "それなのに大した力を持たないことを自覚せずに強いと勘違いし",
                "他者を虐げる者たちがいる。",
                "お前らのことだ"),
            ak.look().d("お前ら", "という言葉と共に黒マントは画面の方へと向き直る。",
                "翻ったマントの裾は何か赤いもので汚されていたが",
                "彼は気にしていないようだ。",
                "メシメシと奇妙な足音をさせて振り返ると",
                "全身が黒のメタリックなフルプレートで覆われている",
                "特撮なんかで見かけるヒーローや悪役幹部のような姿をはっきり捉えることができた"),
            ringi.talk().t("……あいつは"),
            ak.look().d("$meの右手の方でそう呟いたのは",
                "あのモヒカン男だった。",
                "いや本当に同一人物かは分からないが",
                "モヒカンの艶といい厳つい顔の造形といい",
                "実によく似ている。",
                "但し首から下が全てサイボーグのような機械の体になっているのがスケルトン状になって見えていた"),
            killer.talk().t("偽りの力は世界を混沌に陥れる。",
                "故に$meはお前らを削除しなければならない。",
                "削除とはつまり",
                "死のことだ"),
            ak.hear().d("再び悲鳴が上がる。",
                    "今度は一つじゃなく二つも三つも同時だった"),
            ak.talk().t("一体どうやって殺してるんだ？"),
            ringi.talk("デス").t("$meの聞いた噂が本当なら",
                    "奴は目が合った奴の首を飛ばすことができるそうだ"),
            ak.think().d("それはもう世界が世界ならチートと呼ばれてもおかしくない能力だろう。",
                    "少なくとも物理法則は当てにできない"),
            ringi.talk().t("とにかくアイツが通った後には大量の首なし死体が転がっているところから",
                    "こんな風に呼ばれてるんだぜ"),
            killer.talk().t("さて",
                    "虐殺を始めようか"),
            ringi.talk().t("$i_killnameと"),
            ak.look().d("その声を聞いた", "と思った次の瞬間には",
                    "フロア全体に血の雨が降り注いでいた"),
            ak.talk().t("に、逃げるぞ"),
            ak.move().d("$meはとにかく$zerの小さな手を掴むと",
                    "背を向けて走り出していた。",
                    "決して振り返らず",
                    "フロアの入り口なのか出口なのか",
                    "それすら分からないぱっくりと開いた真っ黒なそこへと",
                    "体を投げ出すようにして飛び込んだ"),
            ak.ask(w.i.killer),
            ak.look("デスの画像"),
            ak.know(w.i.killer, w.minae),
            )

def sc_robotown(w: wd.World):
    ak, zer, ringi = w.akura, w.zer, w.ringi
    matsu, akane = w.matsuda, w.akane
    return w.scene("ロボの町",
            ak.behav().t("ハァハァハァ……"),
            ak.think().d("荒い息と共に飛び出た場所は",
                "見渡す限りの雲海が広がる世界だった"),
            ak.feel().d("不意な強烈な突風に慌てて両腕を前にやって堪えるが",
                "$zerはしっかりと$meの腰に手を回して抱きつき",
                "その柔らかい体を頬から押し付けた"),
            ak.talk().t("おい。", "もう大丈夫だぞ"),
            ak.look().d("いつまでもくっついて離れようとしないものだからそう言ったが",
                "彼女は笑みを浮かべたまま子猫のように頭を擦り付け",
                "何だか気持ち良さそうにする"),
            ak.deal().d("その頭に", "思わず手が伸びそうになったが、"),
            ak.hear().d("ソウイウノハ", "ヤメテ"),
            ak.deal().d("何かが聴こえた気がして",
                "自分の胸の前にその手を戻した"),
            zer.ask().t("ん？",
                "なでなでしてくれてもぉ", "良かったのに"),
            ak.talk().t("さっきの奴が来ないうちにどうするか決めないといけないだろ？",
                "そんなふざけてる場合じゃない"),
            zer.talk().t("あっそ"),
            ak.look().d("つまらなさそうに言って彼女は手を離す"),
            ak.hear().d("半球状の真っ白な建物の中からつい先程まで聴こえてきた阿鼻叫喚は",
                "既に静寂へと変わっていた"),
            ak.think().d("全てが終わってしまったのだろうか"),
            ak.think().d("けれどそれを確かめる為に再びあの恐怖が支配する空間に戻ろうとはとても思えない"),
            zer.ask().t("どうせ死んでもまた転生するだけだから", "気にする必要ないのにぃ"),
            ak.talk().t("$meは転生したい訳じゃないし",
                "ここが嫌だからじゃあ死んで次に行きましょうって",
                "そんなゲーム脳みたいな考えはできない"),
            ak.think().d("そもそも転生って何だ。",
                "$meは本当に殺されたのか？",
                "そして本当に違う世界でまた$meとして生まれ変わったのか？"),
            zer.talk().t("そんな深く考えることないのにぃ。",
                "今までに$i_transferにした人は誰も$akuraみたいなこと言わなかったよ？"),
            ak.ask().t("$me以外にも何人も$i_transferがいたのか？"),
            ak.look().d("妙なことを口走ったのはどうも$meの方のようで",
                "$zerは三十度くらい顎を傾けて大きく目を開けている"),
            ak.think().d("言われてみれば自分一人だけが特別だった", "ということはないだろう。",
                "$i_fairyが何者かは知らないが", "彼女たちはただ与えられた仕事をこなしている程度の感覚なのだ。",
                "ただそれが転生とか転移とかといった人間の$meからすれば訳の分からないものだから",
                "奇異なことのように見える", "というだけだ"),
            ak.ask().t("なあ", "お前ら$i_fairyって何の為にいるんだ？", "確か誰かに呼び出されたとか言ってたけど"),
            ak.look().d("だがその質問に彼女が答えるよりも早く",
                "建物から数名が束になって転がるようにして駆け出てくる"),
            matsu.talk().t("な、何なんだよアイツは！"),
            akane.talk().t("$matsu", "あれ絶対ヤバイ奴やで。",
                "もしかして$meらがチートしてるのバレて$i_masterが抹殺しようとしてるんちゃうの？"),
            ak.look().d("それはあの黒革ジャケットと白ニーソのカップルだった。",
                "彼らには自分のものではないと思われる血が飛び散って付着していて",
                "中で起こった惨状がどんなものだったのか容易に想像することができた"),
            matsu.talk().t("おう。",
                    "$me以外にも無事な奴がいたとは驚きだ"),
            ak.look().d("その黒革ジャケットは$meを見ると",
                    "右頬に血飛沫が広がる顔で笑みを作り",
                    "血でべっとりとした右手を差し出してきた"),
            ak.ask().t("それ"),
            matsu.ask().t("あん？",
                    "何だよ。",
                    "この$i_castle3まで来た奴がこんな血くらいでどうこう言うのか？"),
            ak.think().d("その感覚は全く理解出来なかったが",
                    "$meはとにかく握手を拒否して中がどうなったのか尋ねる"),
            ak.ask().t("全員あいつに殺られたのか？"),
            matsu.reply().t("流石に全員てことはないだろ。",
                    "ただとても他の奴らまで構ってる余裕なかったから",
                    "$i_barrier3張るのも自分とこいつの分で精一杯だったよ"),
            ak.think().d("$i_barrier3？", "何だそれは"),
            ak.look().d("$meは$zerを見たが彼女もよく分からないようで首を捻っている。",
                    "言葉の響きから考えれば何かしらのバリアのようなものなのだろうが",
                    "そんな便利な能力があるなら一つくらい$meにも分けてもらいたい"),
            akane.talk().t("けどどうすんのよ", "$matsu。",
                    "このままじゃ$meら$i_lastcastle3まで行けへんよ？"),
            ak.ask().t("その$i_lastcastle3ってのは何だ？",
                    "というかそもそもここはどこなんだ？",
                    "雲が下に見えるってことは相当高い場所なのか？"),
            ak.think().d("そこまで考えて", "自分が高所恐怖症だったことを思い出す"),
            ak.look().d("だがどちらを見ても$meの質問に対して何か答えてくれるといった表情をしていない。",
                    "それどころか奇異なものを見るような目で見たかと思うと",
                    "こそこそと二人で打ち合わせをするように耳打ちをし合った"),
            ak.ask().t("何だよ？"),
            matsu.talk().t("お前",
                    "本当に何も知らないままここまで上がって来たのか？"),
            ak.ask().t("だとしたら何だって言うんだ？"),
            ak.look().d("そう質問した$meを", "奴らは鼻で笑う"),
            matsu.talk().t("なら相当運が良かったんだろうな。",
                    "ここは$i_castle3。",
                    "この世界の第三番目の階層にして",
                    "最強の者じゃなきゃとても生きていけない場所だ。",
                    "さっきみたいなチート野郎は別として",
                    "$meやこの$akaneのようにレベル九十九まで必死に上げて",
                    "それでようやく辿り着ける",
                    "そんな場所なんだよ。",
                    "それが何だお前は。",
                    "見たところレベルも一桁",
                    "装備もない",
                    "魔力も感じない",
                    "何かチートしている訳でもなさそうだし",
                    "ただの馬鹿か？"),
            ak.think().d("言われるがままになっていたが",
                    "明らかに馬鹿にしている上",
                    "$me自身はこの世界では相当カスな能力の部類なのだと自覚できた"),
            ak.think().d("けれど何だろう。",
                    "多少酷い言われようをしたところで",
                    "$meは何も感じなかった"),
            ak.ask().t("ただの馬鹿でも阿呆でもいいが",
                    "あんたらが言ってたその$i_lastcastle3ってところまで行けば何か良いことがあるのか？"),
            ak.look().d("その質問がまた彼らには愉快だったらしい。",
                    "二人して仰け反ってまで笑うと",
                    "惨めに感じたのか", "ご丁寧に教えてくれた"),
            matsu.talk().t("最上層$i_lastcastle3。",
                    "そこにはこの世界の叡智が全て揃っていると云われている。",
                    "何より$i_masterの称号が得られ",
                    "何をするのも思いのまま。",
                    "世界を作り変えることすら可能と云われているんだ。",
                    "分かったかな", "低能君"),
            ak.think().d("世界が思い通りに作り変えられる。",
                    "そんなことに一体何の意味があるのだろう。",
                    "$meにとっては彼の勝ち誇った顔が",
                    "何とも滑稽で",
                    "散々課金して貴重なカードを手に入れた子供のそれにしか思えなかった"),
            ak.ask().t("じゃあ", "あんたらって相当強いってことでいいんだな？"),
            akane.reply().t("そうやで。", "ここまでに出会った中で$meと$matsuほどの猛者は一人しかおらへんかったわ"),
            ak.ask().t("誰だ？"),
            matsu.reply().t("名前は知らん。",
                    "ただその女はこう左の目の下に大きな痣があった"),
            ak.think().d("痣じゃない。", "それは彼女の黒子だ。",
                    "今の発言から黒革ジャケットたちが見た女とは$n_minaeの転生した姿なのだと確信した"),
            matsu.ask().t("おい", "お前まさか"),
            ak.reply().t("中に戻るつもりだが", "何か？"),
            matsu.talk().t("馬鹿なのか？",
                    "何の準備もなく戻れば無駄死にするだけだぞ"),
            ak.think().d("強いと言う割には臆病なんだな", "とその二人に対して感じた"),
            ak.talk().t("それじゃああんたらはこんな場所でじっと嵐が静まるのを待ってるつもりなのか？"),
            ak.look().d("見たところ半球状の建物以外", "どこにも行けそうにない。",
                    "今$meたちが立っている場所だってベランダのように突き出た構造になっているだけで",
                    "そこから飛び出せば雲の中にダイブすることになるだろう"),
            ak.think().d("それじゃあ建物の壁を登るか？"),
            ak.look().d("見上げれば半球の真ん中から頂上が見えないくらいずっと伸びる塔がある。",
                    "そこを登ることで更に上の階層を目指せるなら",
                    "彼女もあそこにいるかも知れない"),
            matsu.talk().t("なあ", "$meが今から攻略法を探すから",
                    "それからなら一緒に行ってやってもいいぞ？"),
            ak.talk().t("低能馬鹿に随分優しいんだな。", "それともさっきの奴が恐いから",
                    "一つでも多く手駒が欲しいのか？"),
            akane.talk().t("あんたなあ"),
            ak.think().d("どうやら図星のようだ"),
            ak.talk().t("おい$zer行くぞ"),
            zer.talk().t("はぁーい"),
            ak.move().d("そのカップルは何か言い訳を並べ始めたが",
                    "$meと$zerは聞く耳を持たずにさっさと建物の中へと戻ってしまった"),
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
            ).omit()

def sc_lookforher(w: wd.World):
    ak, zer, ringi = w.akura, w.zer, w.ringi
    return w.scene("彼女探し",
            ak.come(w.stage.tower3).d("血生臭い惨状が広がっている",
                "と覚悟して中に入ったが", "まるでゲームの死骸のように綺麗サッパリ消えてしまっていた"),
            ak.look().d("大理石のような真っ白な床と天井", "それに巨大な数本の意匠を施した柱が突っ立っているだけだ"),
            ak.look().d("天井から吊り下げられた大型モニタこそ", "血飛沫が飛び散った跡が見て取れたが",
                "そこにはブルースクリーンが表示されているだけで", "もうあの$i_killernameの姿は映っていなかった"),
            ak.ask().t("なあ$zer。",
                "どういうことだと思う？"),
            zer.reply().t("お片付けが好きなのかなぁ"),
            ak.think().d("知っているが答える気がないのか", "それとも本当に知らないだけか分からないが",
                "彼女はとぼけた振りをして見せると",
                "一人で先に歩き出す"),
            ak.ask().t("おい。", "大丈夫なのか？"),
            zer.reply().t("大丈夫よぉ。",
                "だって$i_fairyは死という概念がないから"),
            ak.think().d("つまり死なないから恐怖も何もないということか"),
            ak.think().d("そんな便利な存在なら自分もなってみたいと一瞬考えたが",
                "死がない", "つまり永遠に終わりの来ない人生を", "$meは楽しむことができる自信がなかった"),
            ak.look().d("$meも彼女に続いて歩き出すが", "さっきの最強（笑）カップルはどうしただろうかと気になり",
                "一度後ろを振り返った。",
                "中に戻ってくる気配はない。",
                "ただ入り口付近に小さな林檎が転がっているのだけが見えた"),
            ak.think().d("また林檎か"),
            ak.remember().d("リンゴジュースならまだ良いが", "林檎そのものとなるとどうにもあの香りと臭みが気に入らない。",
                "そうだ。",
                "$meは林檎嫌いだったんだ"),
            zer.talk().t("$akura"),
            ak.talk().t("おう"),
            ak.move().d("階段の前まで行って立ち止まった彼女に応え",
                "$meは小走りで向かった"),
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
            # NOTE: flags
            ak.look(w.i.minae_hight.deflag()),
            ak.look(w.i.minae_point.deflag()),
            ak.look(w.i.needtosay_word.deflag()),
            ak.be(w.i.another_fairy.deflag()),
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
