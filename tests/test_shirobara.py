# -*- coding: utf-8 -*-
"""Test: shirobara.py
"""
import unittest
from storybuilder.builder import testutils as utl
from src.shirobara.story import world, story


_FILENAME = "shirobara.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "shirobara knight project")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    def test_exists_looking(self):
        pass

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags(self.story))

    @unittest.skip("wip")
    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self,
                [
                    ("story", self.story, self.w.mariel, self.w.ruire),
                ])

    @unittest.skip('wip')
    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                    ("story", self.story,
                        w.mariel.be(),
                        w.mariel.be(),
                        w.mariel.be(),
                        w.mariel.be(),
                        True),
                ])

    @unittest.skip('wip')
    def test_exists_keywords(self):
        utl.exists_keywords_by_data(self,
                [
                    "test",
                ])

