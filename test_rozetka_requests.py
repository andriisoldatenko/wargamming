#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
import unittest
from lxml import html


class Rozetka(object):

    def __init__(self, url, text=''):
        self.text = text
        self.url = url
        self.request = requests.get(url, params={'text': text})

    def json_response(self):
        return self.request.json()

    def page_source(self):
        return self.request.text

    def html_tree(self):
        pass


class TestRozetkaSearch(unittest.TestCase):

    def setUp(self):
        page = Rozetka('http://rozetka.com.ua/search/', text="D-Link DIR-826L")
        self.tree = html.fromstring(page.page_source())

    def test_search_d_link_price(self):
        price = self.tree.find_class("g-i-list-price-uah")[0].text
        price_sign = self.tree.find_class("g-i-list-price-uah-sign")[0].text

        self.assertEqual('%s%s' % (price, price_sign), u"952\u2009грн.")

    def test_search_d_link_status(self):
        status = self.tree.find_class("g-i-list-status unavailable")[0].text.strip()

        self.assertEqual(status, u"Нет в наличии")

    def test_search_d_link_usd_value(self):
        find_goods_id = re.search(r'id:\ \d+', self.page.page_source())
        goods_id = find_goods_id.group().split()[1]
        rest_url = "http://rg.rozetka.com.ua/recent_goods_sync/" \
                   "action=getRecentGoodsForStorage;goods_ids=%s/" % goods_id

        page = Rozetka(rest_url)
        currency = page.json_response().get('content')[0].get('price_usd')

        self.assertEqual(float(currency), 68.50)


if __name__ == '__main__':
    unittest.main()
