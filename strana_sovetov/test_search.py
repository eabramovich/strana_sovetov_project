# -*- coding: utf-8 -*-
from selenium import webdriver
from strana_sovetov.model.page_model import PageModel

def test_check_search(app):
    # Если всплывает банер, закрываем его
    app.close_baner()
    app.goto_main_page()
    # Если всплывает банер, закрываем его
    app.close_baner()
    search_word = app.get_first_article_title()
    app.search_button_click()
    assert app.is_search_input_visible()
    app.type_text_into_search_input(search_word)
    app.execute_search()
    # Если всплывает банер, закрываем его
    app.close_baner()
    # Ждем пока появятся результаты поиска
    app.wait_visibily_of_search_result()
    app.is_search_result_visible()
