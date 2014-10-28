#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
import unittest
from lxml import html


class TestRozetkaSearch(unittest.TestCase):

    def setUp(self):
        _text = "D-Link DIR-826L"
        params = {'text': _text}
        page = requests.get('http://rozetka.com.ua/search/', params=params)
        self.page_text = page.text
        self.tree = html.fromstring(self.page_text)

    def test_search_d_link_price(self):
        price = self.tree.xpath('//div[@class="g-i-list-price-uah"]/text()')[0].strip()
        price_sign = self.tree.xpath('//span[@class="g-i-list-price-uah-sign"]/text()')[0].strip()
        self.assertEqual('%s %s' % (price, price_sign), u"952 грн.")

    def test_search_d_link_status(self):
        status = self.tree.xpath('//div[@class="g-i-list-status unavailable"]/text()')[0].strip()
        self.assertEqual(status, u"Нет в наличии")

    def test_search_d_link_usd_value(self):
        find_goods_id = re.search(r'id:\ \d+', self.page_text)
        self.goods_id = find_goods_id.group().split()[1]
        page = requests.get('http://rg.rozetka.com.ua/recent_goods_sync/action=getRecentGoodsForStorage;goods_ids=%s/' 
                            % self.goods_id)
        currency = page.json().get('content')[0].get('price_usd')
        self.assertEqual(float(currency), 68.50)


if __name__ == '__main__':
    unittest.main()
