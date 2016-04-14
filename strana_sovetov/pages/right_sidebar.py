# -*- coding: utf-8 -*-
from strana_sovetov.pages.page import Page
from selenium.webdriver.common.by import By

class RightSidebar(Page):
    
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