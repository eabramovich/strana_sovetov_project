# -*- coding: utf-8 -*-
from selenium import webdriver
from strana_sovetov.model.page_model import PageModel

def test_check_main_page(app):
    app.goto_main_page()
    assert app.is_page_title_correct(PageModel.MainPage())
    assert app.is_logo_visible
    assert app.is_main_menu_visible
    assert app.is_search_block_visible
    assert app.is_line_articles_block_visible
    assert app.is_first_article_block_visible
    assert app.is_second_article_block_visible
    assert app.is_rest_articles_block_visible
    assert app.is_openx_special_block_visible
    assert app.is_last_articles_block
    assert app.is_all_articles_button
    assert app.is_all_special_projects_button
    assert app.is_last_articles_load_more_button_visible
    assert app.is_fastbot_block_visible
    assert app.is_footer_block_visible

