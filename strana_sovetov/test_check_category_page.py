# -*- coding: utf-8 -*-
from selenium import webdriver
from strana_sovetov.model.page_model import PageModel

def test_check_category_page(app):
    app.goto_main_page()
    # Если всплывает банер, закрываем его
    app.close_baner()
    app.goto_beauty()
    app.close_baner()
    assert app.is_logo_visible
    assert app.is_main_menu_visible
    assert app.is_search_block_visible
    assert app.is_bread_crumbs_visible
    assert app.is_title_visible
    assert app.is_scopes_visible
    assert app.is_article_list_visible
    assert app.is_ya_sync_1_visible
    assert app.is_ya_sync_2_visible
    assert app.is_ya_sync_3_visible
    assert app.is_ya_sync_4_visible
    assert app.is_pagination_visible
    assert app.is_openx_zone_869_visible
    assert app.is_best_articles_visible
    assert app.is_mostread_articles_visible
    assert app.is_new_comments_block_visible
    assert app.is_see_also_block_visible
    assert app.is_ya_sync_0_visible
    assert app.is_footer_block_visible
