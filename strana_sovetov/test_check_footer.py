# -*- coding: utf-8 -*-
from selenium import webdriver
from strana_sovetov.model.page_model import PageModel
import time

def test_check_advertising_page_from_footer(app):
    window_before = app.driver.window_handles[0]
    app.goto_advertising_page()
    app.switch_to_new_opened_window()
    assert app.is_advertasing_page()
    app.driver.switch_to_window(window_before)
    app.close_current_tab()

def test_check_feedback_page_from_footer(app):
    app.goto_feedback_page()
    assert app.is_page_title_correct(PageModel.FeedBackPage())

def test_check_recipes_page_from_footer(app):
    app.goto_recipes_from_footer()
    assert app.is_page_title_correct(PageModel.RecipesPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_popular_medicine_page_from_footer(app):
    app.goto_popular_medicine()
    assert app.is_page_title_correct(PageModel.PopularMedecinePage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_hobby_page_from_footer(app):
    app.goto_hobby()
    assert app.is_page_title_correct(PageModel.HobbyPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_renovation_page_from_footer(app):
    app.goto_renovation()
    assert app.is_page_title_correct(PageModel.RenovationPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_beauty_page_from_footer(app):
    app.goto_beauty_from_footer()
    assert app.is_page_title_correct(PageModel.BeautyPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_health_page_from_footer(app):
    app.goto_health()
    assert app.is_page_title_correct(PageModel.HealthPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_kids_page_from_footer(app):
    app.goto_kids()
    assert app.is_page_title_correct(PageModel.KidsPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_animals_page_from_footer(app):
    app.goto_animals()
    assert app.is_page_title_correct(PageModel.AnimalPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_computers_page_from_footer(app):
    app.goto_computers()
    assert app.is_page_title_correct(PageModel.ComputersPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_career_page_from_footer(app):
    app.goto_career()
    assert app.is_page_title_correct(PageModel.CareerPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_psyhology_page_from_footer(app):
    app.goto_psyhology()
    assert app.is_page_title_correct(PageModel.Psychology())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_miscellaneous_page_from_footer(app):
    app.goto_miscellaneous()
    assert app.is_page_title_correct(PageModel.Miscellaneous())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_auto_page_from_footer(app):
    app.goto_auto()
    assert app.is_page_title_correct(PageModel.Auto())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_technique_page_from_footer(app):
    app.goto_technique()
    assert app.is_page_title_correct(PageModel.Technique())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_cosmetics_page_from_footer(app):
    app.goto_cosmetics()
    assert app.is_page_title_correct(PageModel.CosmeticsPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_books_page_from_footer(app):
    app.goto_books()
    assert app.is_page_title_correct(PageModel.Books())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_cinema_page_from_footer(app):
    app.goto_cinema()
    assert app.is_page_title_correct(PageModel.Cinema())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_celebrity_page_from_footer(app):
    app.goto_celebrity()
    assert app.is_page_title_correct(PageModel.Celebrity())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_moda_page_from_footer(app):
    app.goto_moda()
    assert app.is_page_title_correct(PageModel.FashionPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_aviasales_page_from_footer(app):
    app.goto_aviasales()
    assert app.is_page_title_correct(PageModel.Aviasales())

def test_check_hotellook_page_from_footer(app):
    app.goto_main_page()
    app.goto_hotellook()
    assert app.is_page_title_correct(PageModel.Hotellook())

def test_check_melitta_page_from_footer(app):
    app.goto_main_page()
    app.goto_melitta()
    assert app.is_page_title_correct(PageModel.Melitta())

def test_check_econika_page_from_footer(app):
    app.goto_main_page()
    app.goto_econika()
    assert app.is_page_title_correct(PageModel.Econika())

def test_check_vivacalze_page_from_footer(app):
    app.goto_main_page()
    app.goto_vivacalze()
    assert app.is_page_title_correct(PageModel.Vivacalze())

def test_check_vivacalze_page_from_footer(app):
    app.goto_main_page()
    app.goto_lamoda()
    assert app.is_page_title_correct(PageModel.Lamoda())

def test_check_bwt_page_from_footer(app):
    app.goto_main_page()
    app.goto_bwt()


