# -*- coding: utf-8 -*-
from strana_sovetov.pages.page import Page
from selenium.webdriver.common.by import By

class CategoryPage(Page):

    @property
    def first_article_title(self):
        return self.driver.find_element_by_css_selector(".article-list article:nth-child(1) .article-title a")

    @property
    def title(self):
        return self.driver.find_element_by_css_selector(".category-title")

    @property
    def scopes(self):
        return self.driver.find_element_by_css_selector("scopes")

    @property
    def article_list(self):
        return self.driver.find_element_by_css_selector(".article-list")

    # Яндекс директ после 2-ой статьи в списке
    @property
    def ya_sync_1(self):
        return self.driver.find_element_by_css_selector("#Ya_sync_1")

    # Яндекс директ после 4-ой статьи в списке
    @property
    def ya_sync_2(self):
        return self.driver.find_element_by_css_selector("#Ya_sync_2")

    # Яндекс директ после 6-ой статьи в списке
    @property
    def ya_sync_3(self):
        return self.driver.find_element_by_css_selector("#Ya_sync_3")

    # Яндекс директ после 8-ой статьи в списке
    @property
    def ya_sync_4(self):
        return self.driver.find_element_by_css_selector("#Ya_sync_4")

    @property
    def pagination(self):
        return self.driver.find_element_by_css_selector(".pagination")

    # Реклама от google в правом сайдбаре
    @property
    def openx_zone_869(self):
        return self.driver.find_element_by_css_selector(".div[data-zoneid='869']")

    # Лучшее в рубрике
    @property
    def best_articles(self):
        return self.driver.find_element_by_css_selector(".best-articles")

    # Читают на стране советов
    @property
    def mostread_articles(self):
        return self.driver.find_element_by_css_selector(".mostread-articles")

    # Тизерный блок в правом сайдбаре
    @property
    def teaser_block(self):
        return self.driver.find_element_by_css_selector("#newsblockn8HE5edAuuTEMbcm97o4")

    # Блок новые комментарии
    @property
    def new_comments_block(self):
        return self.driver.find_element_by_css_selector(".drcontainer")

    # Блок смотрите также
    @property
    def see_also_block(self):
        return self.driver.find_element_by_css_selector(".box")





