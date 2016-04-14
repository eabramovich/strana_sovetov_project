# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *


class Page(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    @property
    def logo(self):
        return self.driver.find_element_by_css_selector("#logo")

    @property
    def bread_crumbs(self):
        return self.driver.find_element_by_css_selector(".breadcrumbs")

    @property
    def main_menu(self):
        return self.driver.find_element_by_css_selector("nav menu")

    @property
    def top_search(self):
        return self.driver.find_element_by_css_selector("nav .top-search")

    @property
    def search_button(self):
        return self.driver.find_element_by_css_selector("nav .top-search")

    @property
    def search_input(self):
        return self.driver.find_element_by_css_selector(".searchform input[type='search']")

    @property
    def search_loader_progress(self):
        return ".results__loading"

    @property
    def search_result(self):
        return "#ya-site-results .b-body-items"

    @property
    def main_menu_beauty_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(1).dropdown > a")

    @property
    def main_menu_fashion_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(2).dropdown > a")

    @property
    def main_menu_rest_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(3).dropdown > a")

    @property
    def main_menu_gifts_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(4).dropdown > a")

    @property
    def main_menu_celebrity_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(5).dropdown > a")

    @property
    def main_menu_recipes_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(6).dropdown > a")

    @property
    def main_menu_tests_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(7).dropdown > a")

    @property
    def main_menu_compettion_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(8).dropdown > a")

    @property
    def main_menu_makeup_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(1) .submenu li:nth-child(1) a")

    @property
    def main_menu_figure_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(1) .submenu li:nth-child(2) a")

    @property
    def main_menu_hair_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(1) .submenu li:nth-child(3) a")

    @property
    def main_menu_soup_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(6) .submenu ul:nth-child(1) li:nth-child(1) a")

    @property
    def main_menu_salat_snack_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(6) .submenu ul:nth-child(1) li:nth-child(2) a")

    @property
    def main_menu_meat_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(6) .submenu ul:nth-child(1) li:nth-child(3) a")

    @property
    def main_menu_fish_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(6) .submenu ul:nth-child(1) li:nth-child(3) a")

    @property
    def main_menu_bread_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(6) .submenu ul:nth-child(2) li:nth-child(1) a")

    @property
    def main_menu_pasta_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(6) .submenu ul:nth-child(2) li:nth-child(2) a")

    @property
    def main_menu_desert_page(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(6) .submenu ul:nth-child(2) li:nth-child(3) a")

    @property
    def main_menu_drinkables(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(6) .submenu ul:nth-child(2) li:nth-child(4) a")

    @property
    def main_menu_conservation(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(6) .submenu ul:nth-child(3) li:nth-child(1) a")

    @property
    def main_menu_side_dish_link(self):
        return  self.driver.find_element_by_css_selector("menu li:nth-child(6) .submenu ul:nth-child(3) li:nth-child(2) a")

    @property
    def main_menu_manicure_link(self):
        return self.driver.find_element_by_css_selector("menu li:nth-child(1) .submenu li:nth-child(4) a")

    @property
    def footer_block(self):
        return self.driver.find_element_by_css_selector("footer")

    @property
    def footer_about_project_link(self):
        return self.driver.find_element_by_css_selector("footer a[href='/about.html']")

    @property
    def footer_advertising_link(self):
        return self.driver.find_element_by_css_selector("footer a[href='http://wp-media.ru/women.html']")

    @property
    def footer_feedback_link(self):
        return self.driver.find_element_by_css_selector("footer a[href='/index.php?option=com_rsform&formId=5&Itemid=99999']")

    @property
    def footer_recipes_link(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(1) a")

    @property
    def footer_popular_medicine_link(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(2) a")

    @property
    def footer_hobby_link(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(3) a")

    @property
    def footer_renovation_link(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(4) a")

    @property
    def footer_beaty_link(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(5) a")

    @property
    def footer_health_link(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(6) a")

    @property
    def footer_kids_link(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(7) a")

    @property
    def footer_animals_link(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(8) a")

    @property
    def footer_computers_link(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(9) a")

    @property
    def footer_career_link(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(10) a")

    @property
    def footer_psyhology(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(11) a")

    @property
    def footer_miscellaneous(self):
        return  self.driver.find_element_by_css_selector("footer .column:nth-child(1) ul li:nth-child(12) a")

    @property
    def footer_auto(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(2) ul li:nth-child(1) a")

    @property
    def footer_technique(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(2) ul li:nth-child(2) a")

    @property
    def footer_cosmetics(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(2) ul li:nth-child(3) a")

    @property
    def footer_books(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(2) ul li:nth-child(4) a")

    @property
    def footer_cinema(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(2) ul li:nth-child(5) a")

    @property
    def footer_celebrity(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(3) ul li:nth-child(1) a")

    @property
    def footer_moda(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(3) ul li:nth-child(2) a")

    @property
    def footer_aviasales(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(4) ul li:nth-child(1) a")

    @property
    def footer_hotellook(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(4) ul li:nth-child(2) a")

    @property
    def footer_melitta(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(4) ul li:nth-child(3) a")

    @property
    def footer_econika(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(4) ul li:nth-child(4) a")

    @property
    def footer_vivacalze(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(4) ul li:nth-child(5) a")

    @property
    def footer_lamoda(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(4) ul li:nth-child(6) a")

    @property
    def footer_bwt(self):
        return self.driver.find_element_by_css_selector("footer .column:nth-child(4) ul li:nth-child(7) a")

    def is_element_visible_by_locator(self, locator):
        try:
            return self.wait.until(visibility_of_element_located(locator))
        except WebDriverException:
            return False

    def is_element_visible(self, element):
        try:
            return self.wait.until(visibility_of(element))
        except WebDriverException:
            return False

    def is_baner_present(self):
        self.driver.implicitly_wait(0)
        try:
            banner = self.driver.find_element_by_css_selector(".nf-b-big-banner")
            if banner.is_displayed():
                return True
        except WebDriverException:
            return False








