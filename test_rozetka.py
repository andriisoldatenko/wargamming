#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from base import HomePage


class TestRozetkaSearch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        homepage = HomePage(self.browser)
        homepage.navigate()
        search_form = homepage.get_search_form()
        search_form.search('D-Link DIR-826L')
        self.search_results = search_form.submit()

    def test_rozetka_search_d_link_status(self):
        self.assertEqual(self.search_results.goods_status_text(),
                         u"Нет в наличии")

    def test_rozetka_search_d_link_price(self):
        self.assertEqual(self.search_results.goods_price_text(), u"952 грн.")

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()