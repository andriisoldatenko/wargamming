#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(3)

    def find(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def navigate(self):
        self.driver.get(self.url)


class HomePage(BasePage):
    url = "http://rozetka.com.ua/"

    def get_search_form(self):
        return SearchPage(self.driver)


class SearchPage(BasePage):
    url = "http://rozetka.com.ua/search/"

    search_field = lambda self: self.driver.find_element_by_class_name('header-search-input-text')
    search_button = lambda self: self.driver.find_element_by_class_name('btn-link-i')

    def search(self, value):
        self.search_field().send_keys(value)

    def submit(self):
        self.search_button().click()
        return SearchResultsPage(self.driver)


class SearchResultsPage(SearchPage):

    h1 = lambda self: self.driver.find_element_by_tag_name('h1')

    goods_title = lambda self: self.driver.find_element_by_class_name('g-i-list-title')
    goods_status = lambda self: self.driver.find_element_by_class_name('g-i-list-status')
    goods_price = lambda self: self.driver.find_element_by_class_name('g-i-list-price-uah')

    def h1_element(self):
        return self.h1()

    def goods_title_text(self):
        return self.goods_title().text

    def goods_status_text(self):
        return self.goods_status().text

    def goods_price_text(self):
        return self.goods_price().text
