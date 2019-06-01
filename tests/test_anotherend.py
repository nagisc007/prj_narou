# -*- coding: utf-8 -*-
"""Test: Another end world
"""
import unittest
from storybuilder.builder import testutils as utl
from src.anotherend.story import world, story
from src.anotherend.config import THEMES, MOTIFS
from src.anotherend import chapter00 as chap0
from src.anotherend import chapter01 as chap1
from src.anotherend import chapter02 as chap2
from src.anotherend import chapter03 as chap3
from src.anotherend import chapter04 as chap4
from src.anotherend import chapter05 as chap5
from src.anotherend import chapter06 as chap6
from src.anotherend import chapter07 as chap7
from src.anotherend import chapter08 as chap8
from src.anotherend import chapter09 as chap9
from src.anotherend import chapter10 as chap10


_FILENAME = "anotherend.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "Another end world project")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)
        self.ch0 = chap0.story(self.w)
        self.ch1 = chap1.story(self.w)
        self.ch2 = chap2.story(self.w)
        self.ch3 = chap3.story(self.w)
        self.ch4 = chap4.story(self.w)
        self.ch5 = chap5.story(self.w)
        self.ch6 = chap6.story(self.w)
        self.ch7 = chap7.story(self.w)
        self.ch8 = chap8.story(self.w)
        self.ch9 = chap9.story(self.w)
        self.ch10 = chap10.story(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags_with_error_info(self, self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self,
                [
                    ("story", self.story, self.w.akura, self.w.minae),
                    # chapter 00
                    ("chapter 00", self.ch0, self.w.akura, self.w.master),
                    # chapter 01
                    ("chapter 01", self.ch1, self.w.akura, self.w.minae),
                    # chapter 02
                    ("chapter 02", self.ch2, self.w.akura, self.w.zer),
                    # chapter 03
                    ("chapter 03", self.ch3, self.w.akura, self.w.minae),
                    # chapter 04
                    ("chapter 04", self.ch4, self.w.akura, self.w.akura),
                    # chapter 05
                    ("chapter 05", self.ch5, self.w.akura, self.w.akura),
                    # chapter 06
                    ("chapter 06", self.ch6, self.w.akura, self.w.akura),
                    # chapter 07
                    ("chapter 07", self.ch7, self.w.akura, self.w.akura),
                    # chapter 08
                    ("chapter 08", self.ch8, self.w.akura, self.w.akura),
                    # chapter 09
                    ("chapter 09", self.ch9, self.w.akura, self.w.akura),
                    # chapter 10
                    ("chapter 10", self.ch10, self.w.akura, self.w.akura),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                    ("story", self.story,
                        w.akura.remember("大事なこと"),
                        w.akura.be("忘れてしまった"),
                        w.akura.do("何度も死ぬ"),
                        w.akura.deal("伝える", w.minae, "自分の本音"),
                        True),
                    # chapter 00
                    ("chapter 00", self.ch0,
                        w.akura.know("自分が何者か"),
                        w.akura.be("何も覚えていない"),
                        w.akura.do("wake"),
                        w.akura.deal("殺された"),
                        True),
                    # chapter 01
                    ("chapter 01", self.ch1,
                        w.akura.think("この世界を調べる"),
                        w.akura.know(w.i.anotherworld),
                        w.akura.look("死んだ原因"),
                        w.akura.deal("殺された"),
                        True),
                    # chapter 02
                    ("chapter 02", self.ch2,
                        w.akura.know("自分の状況"),
                        w.akura.meet(w.zer),
                        w.akura.go(w.stage.field2),
                        w.akura.deal("殺された"),
                        True),
                    # chapter 03
                    ("chapter 03", self.ch3,
                        w.akura.look(w.minae),
                        w.akura.know(w.minae, "この世界にもいる"),
                        w.akura.deal("守る", w.minae),
                        w.akura.look("眠る自分の姿"),
                        True),
                    # chapter 04
                    ("chapter 04", self.ch4,
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        True),
                    # chapter 05
                    ("chapter 05", self.ch5,
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        True),
                    # chapter 06
                    ("chapter 06", self.ch6,
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        True),
                    # chapter 07
                    ("chapter 07", self.ch7,
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        True),
                    # chapter 08
                    ("chapter 08", self.ch8,
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        True),
                    # chapter 09
                    ("chapter 09", self.ch9,
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        True),
                    # chapter 10
                    ("chapter 10", self.ch10,
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        w.akura.be(),
                        True),
                ])

    def test_has_themes(self):
        for k, v in THEMES.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in(self.story, THEMES[k]))

    def test_has_motifs(self):
        for k, v in MOTIFS.items():
            with self.subTest(k=k, v=v):
                self.assertTrue(utl.has_the_keyword_in_description_in(self.story, MOTIFS[k]))
