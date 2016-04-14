from page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):

    @property
    def line_articles_block(self):
        return self.driver.find_element_by_css_selector(".front-articles .line-articles")

    @property
    def first_article_block(self):
        return self.driver_find_element_by_css_selector(".first-article")

    @property
    def second_article_block(self):
        return self.driver_find_element_by_css_selector(".second-article")

    @property
    def rest_articles_block(self):
        return self.driver_find_element_by_css_selector(".rest-articles")

    @property
    def openx_special_block(self):
        return self.driver_find_element_by_css_selector(".openx-special")

    @property
    def last_articles_block(self):
        return self.driver.find_element_by_css_selector(".last-articles")

    @property
    def all_articles_button(self):
        return self.driver.find_element_by_css_selector(".all-articles")

    @property
    def all_special_projects_button(self):
        return self.driver.find_element_by_css_selector(".all-spec")

    @property
    def last_articles_load_more_button(self):
        return self.driver.find_element_by_css_selector("#last-articles-load-more")

    @property
    def fastbot_block(self):
        return self.driver.find_element_by_css_selector(".reforum-fastbot-links")

    @property
    def first_aticle_title(self):
        return self.driver.find_element_by_css_selector(".first-article a:nth-child(1)").text
