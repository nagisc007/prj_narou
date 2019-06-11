# -*- coding: utf-8 -*-
"""Config: sage pants project
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("hero", "パンツ,太郎", 30, "male", "パンツ", "me:オレ"),
        ("ery", "エリザベート,ステラ", 99, "female", "賢者", "me:私"),
        )

STAGES = (
        # Area
        ("lemurian", "エル・レム・リア"),
        # Place
        ("prison", "監獄"),
        # Part
        )


DAYS = (
        # main
        ("firstmeet", "最初の遭遇日"),
        # sub
        )


ITEMS = (
        # main
        ("pants", "パンツ"),
        # sub
        )


INFOS = (
        # main
        ("transfer", "転生"),
        ("pants_life", "パンツの人生"),
        ("myvalue", "己の価値"),
        # sub
        ("coope", "協力"),
        )


FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

