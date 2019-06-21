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
        ("rei", "ワムザ,レイ", 30, "female", "大賢者", "me:私"),
        ("pery", "ルナ,ペリィ", 27, "female", "公安特別部隊長", "me:ワタシ"),
        ("steady", "沢森,麗子", 30, "female", "役場職員", "me:私"),
        # chapter 1
        ("sufferer1", "痴漢被害者", 27, "female", "会社員"),
        # chapter 2
        ("gater1", "番人1", 28, "female", "番兵"),
        ("gater2", "番人2", 30, "female", "番兵"),
        )

STAGES = (
        # Area
        ("lemurian", "エル・レム・リア"),
        # Place
        ("prison", "監獄"),
        ("station", "駅"),
        ("forest1", "大森林"),
        ("herhome", "エリィの家"),
        # Part
        ("train", "列車内"),
        ("sta_home", "駅のホーム"),
        )

DAYS = (
        # main
        ("deadman", "死んだ日", 6,6, 2019),
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
        # sub
        ("coope", "協力"),
        # chapter 1
        ("myfuture", "自分の未来"),
        # chapter 2
        ("ery_home", "エリィの家の場所"),
        ("language1", "レム語"),
        # her phrase
        ("herword001", "パンツは知らない他人に触らせる為のものじゃないのよ"),
        ("herword002", "パンツというのは人類が最初に身に着けた服そのものであって決して下着なんて呼んでいい代物じゃないの"),
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

