# -*- coding: utf-8 -*-
from strana_sovetov.model.page_model import PageModel
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import *
from strana_sovetov.pages.page import Page
from strana_sovetov.pages.main_page import MainPage
from strana_sovetov.pages.category_page import CategoryPage
from strana_sovetov.pages.article_page import ArticlePage
from strana_sovetov.pages.right_sidebar import RightSidebar
from strana_sovetov.model.page_model import PageModel
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
import time


class Application(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        driver.get(base_url)
        self.page = Page(driver, base_url)
        self.main_page = MainPage(driver, base_url)
        self.category_page = CategoryPage(driver, base_url)
        self.article_page = ArticlePage(driver, base_url)
        self.right_sidebar = RightSidebar(driver, base_url)
        self.wait = WebDriverWait(driver, 15)

    @property
    def is_logo_visible_by_locator(self):
        return self.page.is_element_visible((By.CSS_SELECTOR, "#logo"))

    @property
    def is_submenu_visible_by_locator(self):
        return self.page.is_element_visible((By.CSS_SELECTOR, ".menu li:nth-child(1) .submenu"))

    def goto_main_page(self):
        self.page.logo.click()

    def goto_beauty(self):
        self.page.main_menu_beauty_link.click()

    def goto_fashion(self):
        self.page.main_menu_fashion_link.click()

    def goto_rest(self):
        self.page.main_menu_rest_link.click()

    def goto_gifts(self):
        self.page.main_menu_gifts_link.click()

    def goto_celebrity(self):
        self.page.main_menu_celebrity_link.click()

    def goto_recipes(self):
        self.page.main_menu_recipes_link.click()

    def goto_tests(self):
        self.page.main_menu_tests_link.click()

    def goto_compettion(self):
        self.page.main_menu_compettion_link.click()

    def goto_makeup(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_beauty_link, self.page.main_menu_makeup_link)

    def goto_figure(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_beauty_link, self.page.main_menu_figure_link)

    def goto_hair(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_beauty_link, self.page.main_menu_hair_link)

    def goto_manicure(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_beauty_link, self.page.main_menu_manicure_link)

    def goto_soup(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_recipes_link, self.page.main_menu_soup_link)

    def goto_salat_snack(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_recipes_link, self.page.main_menu_salat_snack_link)

    def goto_meat(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_recipes_link, self.page.main_menu_meat_link)

    def goto_fish(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_recipes_link, self.page.main_menu_fish_link)

    def goto_bread(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_recipes_link, self.page.main_menu_bread_link)

    def goto_pasta(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_recipes_link, self.page.main_menu_pasta_link)

    def goto_dessert(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_recipes_link, self.page.main_menu_desert_page)

    def goto_drinkables(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_recipes_link, self.page.main_menu_drinkables)

    def goto_conservation(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_recipes_link, self.page.main_menu_conservation)

    def goto_side_dish(self):
        self.openLinkFromDropDownMenu(self.page.main_menu_recipes_link, self.page.main_menu_side_dish_link)

    def goto_recipes_from_footer(self):
        self.page.footer_recipes_link.click()

    def goto_popular_medicine(self):
        self.page.footer_popular_medicine_link.click()

    def goto_hobby(self):
        self.page.footer_hobby_link.click()

    def goto_renovation(self):
        self.page.footer_renovation_link.click()

    def goto_beauty_from_footer(self):
        self.page.footer_beaty_link.click()

    def goto_health(self):
        self.page.footer_health_link.click()

    def goto_kids(self):
        self.page.footer_kids_link.click()

    def goto_animals(self):
        self.page.footer_animals_link.click()

    def goto_computers(self):
        self.page.footer_computers_link.click()

    def goto_career(self):
        self.page.footer_career_link.click()

    def goto_psyhology(self):
        self.page.footer_psyhology.click()

    def goto_miscellaneous(self):
        self.page.footer_miscellaneous.click()

    def goto_auto(self):
        self.page.footer_auto.click()

    def goto_technique(self):
        self.page.footer_technique.click()

    def goto_cosmetics(self):
        self.page.footer_cosmetics.click()

    def goto_books(self):
        self.page.footer_books.click()

    def goto_cinema(self):
        self.page.footer_cinema.click()

    def goto_celebrity(self):
        self.page.footer_celebrity.click()

    def goto_moda(self):
        self.page.footer_moda.click()

    def goto_aviasales(self):
        self.page.footer_aviasales.click()

    def goto_hotellook(self):
        self.page.footer_hotellook.click()

    def goto_melitta(self):
        self.page.footer_melitta.click()

    def goto_econika(self):
        self.page.footer_econika.click()

    def goto_vivacalze(self):
        self.page.footer_vivacalze.click()

    def goto_lamoda(self):
        self.page.footer_lamoda.click()

    def goto_bwt(self):
        self.page.footer_bwt.click()

    def is_page_title_correct(self, page_model):
        return self.driver.title == page_model.title.decode("utf-8")

    def openLinkFromDropDownMenu(self, dropdownLink, link):
        hover = ActionChains(self.driver).move_to_element(dropdownLink)
        hover.perform()
        link.click()

    def is_logo_visible(self):
        return self.page.is_element_visible(self.page.logo)

    def is_main_menu_visible(self):
        return self.page.is_element_visible(self.page.main_menu)

    def is_search_block_visible(self):
        return self.page.is_element_visible(self.page.top_search)

    def is_line_articles_block_visible(self):
        return self.page.is_element_visible(self.main_page.line_articles_block)

    def is_first_article_block_visible(self):
        return self.page.is_element_visible(self.main_page.first_article_block)

    def is_second_article_block_visible(self):
        return self.page.is_element_visible(self.main_page.second_article_block)

    def is_rest_articles_block_visible(self):
        return self.page.is_element_visible((self.main_page.rest_articles_block))

    def is_openx_special_block_visible(self):
        return self.page.is_element_visible(self.main_page.openx_special_block)

    def is_last_articles_block(self):
        return self.page.is_element_visible(self.main_page.last_articles_block)

    def is_all_articles_button(self):
        return self.page.is_element_visible(self.main_page.all_articles_button)

    def is_all_special_projects_button(self):
        return self.page.is_element_visible(self.main_page.all_articles_button)

    def is_last_articles_load_more_button_visible(self):
        return self.page.is_element_visible(self.main_page.last_articles_load_more_button)

    def is_fastbot_block_visible(self):
        return self.page.is_element_visible((self.main_page.fastbot_block))

    def is_footer_block_visible(self):
        return self.page.is_element_visible(self.page.footer_block)

    def goto_about_project_page(self):
        return self.page.footer_about_project_link.click()

    def goto_advertising_page(self):
        return self.page.footer_advertising_link.click()

    def goto_feedback_page(self):
        return self.page.footer_feedback_link.click()

    def is_advertasing_page(self):
        return self.wait.until(title_contains(PageModel.AdvertasingPage().title.decode("utf-8")))

    # Переключаемся на страницу, которая открылась в новой вкладке
    def switch_to_new_opened_window(self):
        self.driver.switch_to_window(self.driver.window_handles[1])

    # Переключаемся обратно на страницу, с которой открыли страницу в новой вкладке
    def switch_to_old_window(self):
        self.driver.switch_to_window(self.driver.window_handles[0])

    def close_current_tab(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

    # Переходим на первую статью из списка
    def goto_first_arcticle(self):
        self.category_page.first_article_title.click()

    # Проверяем, что первая статья из списка открывается и не отдаёт никаких ошибок
    def is_article_excist(self):
        return self.page.is_element_visible(self.article_page.article)

    def close_baner(self):
        if self.page.is_baner_present():
            self.driver.find_element_by_css_selector(".nf-header-close").click()

    def is_bread_crumbs_visible(self):
        return self.page.is_element_visible(self.page.bread_crumbs)

    def is_title_visible(self):
        return self.page.is_element_visible(self.category_page.title)

    def is_scopes_visible(self):
        return self.page.is_element_visible(self.category_page.scopes)

    def is_article_list_visible(self):
        return self.page.is_element_visible(self.category_page.article_list)

    # Отображение яндекс директа после 2-ой статьи в списке
    def is_ya_sync_1_visible(self):
        return self.page.is_element_visible((self.category_page.ya_sync_1))

    # Отображение яндекс директа после 4-ой статьи в списке
    def is_ya_sync_2_visible(self):
        return self.page.is_element_visible((self.category_page.ya_sync_2))

    # Отображение яндекс директа после 6-ой статьи в списке
    def is_ya_sync_3_visible(self):
        return self.page.is_element_visible((self.category_page.ya_sync_3))

    # Отображение яндекс директа после 8-ой статьи в списке
    def is_ya_sync_4_visible(self):
        return self.page.is_element_visible((self.category_page.ya_sync_4))

    def is_pagination_visible(self):
        return self.page.is_element_visible(self.category_page.pagination)

    def is_openx_zone_869_visible(self):
        return self.page.is_element_visible(self.right_sidebar.openx_zone_869)

    def is_best_articles_visible(self):
        return self.page.is_element_visible(self.right_sidebar.best_articles)

    def is_mostread_articles_visible(self):
        return self.page.is_element_visible((self.right_sidebar.mostread_articles))

    def is_teaser_block_visible(self):
        return self.page.is_element_visible(self.right_sidebar.teaser_block)

    def is_new_comments_block_visible(self):
        return self.page.is_element_visible(self.right_sidebar.new_comments_block)

    def is_see_also_block_visible(self):
        return self.page.is_element_visible(self.right_sidebar.see_also_block)

    # Отображение яндекс директа в правом сайдбаре
    def is_ya_sync_0_visible(self):
        return self.page.is_element_visible((self.right_sidebar.ya_sync_0))

    def is_article_title_visible(self):
        return self.article_page.is_element_visible(self.article_page.acticle_title())

    def is_article_rating_visible(self):
        return self.article_page.is_element_visible(self.article_page.article_rating())

    # Яндекс директ после заголовка
    def is_article_ya_sync_1_visible(self):
        return self.page.is_element_visible(self.article_page.ya_sync_1())

    # Яндекс директ в блоке "Читайте также" после первой статьи
    def is_article_ya_sync_2_visible(self):
        return self.page.is_element_visible(self.article_page.ya_sync_2())

    def read_more_article(self):
        self.driver.execute_script("window.scrollTo(0, 1500);")
        self.article_page.article_readmore_button().click()
        self.wait.until(visibility_of(self.article_page.connect_discussion()))

    def is_connect_discussion_visible(self):
        return self.page.is_element_visible(self.article_page.connect_discussion())

    def is_share_block_visible(self):
        return  self.page.is_element_visible(self.article_page.share_block())

    def is_read_also_block_visible(self):
        return self.page.is_element_visible((self.article_page.read_also()))

    # Рекламный тизерный блок после блока "Читайте также"
    def is_tizer_block_visible(self):
        return self.page.is_element_visible(self.article_page.tizer_block())

    def is_article_comments_block_visible(self):
        return self.page.is_element_visible(self.article_page.article_comments_block())

    def is_new_new_materials_block_visible(self):
        return self.page.is_element_visible(self.article_page.new_materials_block())

    def get_first_article_title(self):
        print ("\n" + self.main_page.first_aticle_title)
        return self.main_page.first_aticle_title

    def search_button_click(self):
        self.page.search_button.click()

    def is_search_input_visible(self):
        return self.page.is_element_visible(self.page.search_input)

    def type_text_into_search_input(self, text):
        self.page.search_input.send_keys(text)

    # Ждем пока появятся результаты поиска
    def wait_visibily_of_search_result(self):
        self.wait.until(visibility_of_element_located((By.CSS_SELECTOR, self.page.search_result)))

    # Проверка подгрузки результатов поиска
    def is_search_result_visible(self):
        return self.page.is_element_visible_by_locator((By.CSS_SELECTOR, self.page.search_result))

    def execute_search(self):
        self.page.search_input.send_keys(Keys.RETURN)






















