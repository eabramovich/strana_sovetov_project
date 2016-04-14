# -*- coding: utf-8 -*-
from strana_sovetov.pages.page import Page
from selenium.webdriver.common.by import By

class ArticlePage(Page):

    @property
    def article(self):
        return self.driver.find_element_by_css_selector(".read-more-article")

    def acticle_title(self):
        return self.driver.find_element_by_css_selector(".read-more-article h1")

    def article_rating(self):
        return self.driver.find_element_by_css_selector(".article-rating")

    def ya_sync_1(self):
        return self.driver.find_element_by_css_selector("#Ya_sync_1")

    def ya_sync_2(self):
        return self.driver.find_element_by_css_selector("#Ya_sync_2")

    def article_readmore_button(self):
        return self.driver.find_element_by_css_selector(".article-readmore-button")

    def connect_discussion(self):
        return self.driver.find_element_by_css_selector(".article-readmore-button-wrapper .article-social .red-button")

    def share_block(self):
        return self.driver.find_element_by_css_selector(".article-readmore-button-wrapper .article-social .share-block")

    def read_also(self):
        return self.driver.find_element_by_css_selector(".article-readmore")

    # Рекламный тизерный блок после блока "Читайте также"
    def tizer_block(self):
        return self.driver.find_element_by_css_selector("#cb1Zm6VnJ5H8D4TVOWeURG")

    def article_comments_block(self):
        return self.driver.find_element_by_css_selector(".article-comments")

    def new_materials_block(self):
        return self.driver.find_element_by_css_selector("section .drcontainer")
