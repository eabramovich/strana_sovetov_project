# -*- coding: utf-8 -*-
from selenium import webdriver
from strana_sovetov.model.page_model import PageModel

def test_check_article_page(app):
    app.goto_main_page()
    # Если всплывает банер, закрываем его
    app.close_baner()
    app.goto_beauty()
    app.close_baner()
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_bread_crumbs_visible
    assert app.is_openx_zone_869_visible
    assert app.is_best_articles_visible
    assert app.is_mostread_articles_visible
    assert app.is_new_comments_block_visible
    assert app.is_see_also_block_visible
    assert app.is_ya_sync_0_visible
    assert app.is_footer_block_visible
    assert app.is_article_title_visible
    assert app.is_article_excist()
    assert app.is_article_rating_visible()
    assert app.is_article_ya_sync_1_visible()

    # Нажимаем на кнопку "Читать полностью"
    app.read_more_article()
    assert app.is_connect_discussion_visible()
    assert app.is_share_block_visible()

    assert app.is_read_also_block_visible()
    assert app.is_article_ya_sync_2_visible()
    assert app.is_article_comments_block_visible()
    assert app.is_new_new_materials_block_visible()
    assert app.is_footer_block_visible

