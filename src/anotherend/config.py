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
            "me:俺"),
        ("minae", "水無本,美綯", 25, "female", "謎の女性",
            "me:わたし"),
        ("zer", "ゼル", 99, "female", "妖精", "me:アタシ"),
        ("master", "マスター", 99, "male", "世界管理者", "me:ワタシ"),
        # sub
        ("ringi", "星,リンギ", 45, "male", "商人", "me:オレ"),
        # mob
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
        ## chapter 1
        ("market1", "市場その１"),
        )


DAYS = (
        ("current", "現在"),
        ("first", "最初に死んだ日"),
        )


ITEMS = (
        )


INFOS = (
        ("anotherworld", "異世界"),
        )


FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }
