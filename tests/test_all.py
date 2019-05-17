# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest
import test_shirobara
import test_anotherend


def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    suite.addTests((
        # iris
        unittest.makeSuite(test_shirobara.StoryTest),
        # hj
        unittest.makeSuite(test_anotherend.StoryTest),
        ))

    return suite
