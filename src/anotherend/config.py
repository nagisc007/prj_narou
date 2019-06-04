# -*- coding: utf-8 -*-
"""Config: Another end world
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("akura", "悪鞍,汚悪", 25, "male", "無職",
            "me:俺:zer:ゼル"),
        ("minae", "水無本,美綯", 25, "female", "謎の女性",
            "me:わたし"),
        ("zer", "ゼル", 99, "female", "妖精", "me:アタシ:akura:アックン"),
        ("master", "マスター", 99, "male", "世界管理者", "me:ワタシ"),
        ("killer", "暗殺者", 99, "male", "暗殺者", "me:ワタシ",
            "実は世界管理者"),
        # sub
        ("ringi", "星,リンギ", 45, "male", "商人", "me:オレ"),
        # mob
        ## chapter 2
        ### sub
        ("reception2", "受付嬢", 30, "female", "受付嬢", "me:アタシ"),
        ### mob
        ("gatekeeper2", "門番", 28, "male", "門番", "me:私"),
        )


STAGES = (
        # Area
        ("world0", "レイナール"),
        ("world1", "異世界１"),
        ("world2", "異世界２"),
        ("world3", "異世界３"),
        ("world4", "異世界４"),
        ("world5", "異世界５"),
        ("world6", "異世界６"),
        ("world7", "異世界７"),
        ("world8", "異世界８"),
        ("world9", "異世界９"),
        ("world10", "異世界１０"),
        # Place
        ("apart", "アパート"),
        # Part
        ("field1", "大地"),
        ("blackzone", "暗黒の場所"),
        ## chapter 1
        ("market1", "市場その１"),
        ## chapte 2
        ("town2", "アクセク"),
        ("guild2", "ギルド"),
        ("bar2", "居酒屋"),
        ("weaponshop2", "武器屋"),
        ("eating2", "大衆食堂"),
        ("stable2", "馬小屋"),
        ("gate2", "外門"),
        ("field2", "フィールド２"),
        ("street2", "路地"),
        ## chapter 3
        ("floor3", "メインフロア"),
        ("town3", "サード・タウン"),
        ("castle3", "サードクラッド"),
        )


DAYS = (
        ("current", "現在"),
        ("first", "最初に死んだ日"),
        )


ITEMS = (
        )


INFOS = (
        ("anotherworld", "異世界"),
        ("killer", "謎の殺人者"),
        ("transfer", "転生体"),
        ("transnovel", "異世界転生物"),
        ## chapter 0
        ("feeling", "感覚"),
        ## chapter 1
        ("checkstatus", "状況確認"), # NOTE: theme1
        ("apple1", "林檎に似た果実"),
        ## chapter 2
        ("hungry", "空腹"), # NOTE: theme2
        ("minae_exist2", "彼女の存在")
        ## chapter 3
        ## chapter 4
        )


FLAGS = (
        )

THEMES = {
        "transfer": "転生",
        }

MOTIFS = {
        }
