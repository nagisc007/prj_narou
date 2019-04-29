# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest

import test_shirobara

def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    suite.addTests((
        unittest.makeSuite(test_shirobara.StoryTest),
        ))

    return suite
