# coding: utf-8

import unittest

from ..tapioca_hubspot import Hubspot


class TestTapiocaHubspot(unittest.TestCase):

    def setUp(self):
        self.wrapper = Hubspot()


if __name__ == '__main__':
    unittest.main()
