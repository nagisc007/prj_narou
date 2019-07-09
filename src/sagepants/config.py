# -*- coding: utf-8 -*-
"""Config: sage pants project
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("hero", "パンツ,太郎", 30, "male", "パンツ", "me:オレ:I:太郎:ery:エリィ"),
        ("ery", "ステラ,エリザベート", 99, "female", "賢者", "me:我:my:私:I:わし:hero:タロウ:ery:エリィ"),
        ("lily", "ステラ,リリィ", 20, "female", "魔道士", "me:わたし"),
        # sub
        ("robber", "パンティ,三郎", 42, "male", "パンツ", "me:ワシ"),
        ("rey", "ワムザ,レイ", 30, "female", "大賢者", "me:私"),
        ("pery", "ルナ,ペリィ", 27, "female", "公安特別部隊長", "me:ワタシ"),
        ("reiko", "沢森,麗子", 30, "female", "役場職員", "me:私"),
        # chapter 1-1
        ("sufferer1", "痴漢被害者", 27, "female", "会社員"),
        # chapter 2
        ("gater1", "番人1", 28, "female", "番兵"),
        ("gater2", "番人2", 30, "female", "番兵"),
        )

STAGES = (
        # Area
        ("lemurian", "エル・レム・リア"),
        # Place
        ("island_prison", "監獄島"),
        ("prison", "監獄"),
        ("station", "駅"),
        ("forest1", "大森林"),
        ("herhome", "エリィの家"),
        # Part
        ("train", "列車内"),
        ("sta_home", "駅のホーム"),
        ## ch01-04
        ("out_prison", "監獄の外"),
        )

DAYS = (
        # main
        ("deadman", "死んだ日", 8,2, 2019),# パンツの日
        ("firstmeet", "最初の遭遇日"),
        ("current", "現在"),
        # sub
        ("departher", "彼女と別れた日", 6,6, 2016),
        )

ITEMS = (
        # main
        ("pants", "パンツ"),
        ("sagerobe", "聖紫法衣"),
        # sub
        )

INFOS = (
        # main
        ("transfer", "転生"),
        ("pants_life", "パンツの人生"),
        ("myvalue", "己の価値"),
        ("anotherworld", "異世界"),
        ("equip", "装着"),
        ("energy", "エナ"),
        ("metal", "魔鋼"),
        # sub
        ("coope", "協力"),
        # chapter 1
        ("pervert", "痴漢"),
        ("rescue_her", "被害女性を助ける"),
        ("catch_pervert", "痴漢逮捕"),
        ("dead_truck", "トラック事故死"),
        ("knowledge_world", "この世界についての知識"),
        ("myfuture", "自分の未来"),
        # chapter 1-3
        ("destroy_sage", "世界を滅ぼす大賢者"),
        ("her_status", "彼女の状況"),
        ("this_world", "この世界のこと"),
        ("mean_taro", "勤勉な者"),
        ("realname", "真名"),
        # chapter 1-4
        ("mystatus", "己の状況"),
        # chapter 2
        ("ery_home", "エリィの家の場所"),
        ("language1", "レム語"),
        # her phrase
        ("herword001", "パンツは知らない他人に触らせる為のものじゃないのよ"),
        ("herword002", "パンツというのは人類が最初に身に着けた服そのものであって決して下着なんて呼んでいい代物じゃないの"),
        ("herword003", "下着は隠されたもう一つの顔みたいなものなのよ"),
        ("herword004", "あなたが私の為にできることなんか本質的には何もないのよ"),
        ("herword005", "一番最悪な人種は人が楽しんでいるところにわざわざ水を差すような発言をする輩よ"),
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

