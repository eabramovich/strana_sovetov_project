# -*- coding: utf-8 -*-
from strana_sovetov.model.page_model import PageModel
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

def test_check_menu(app):
    app.goto_main_page()
    # Если всплывает банер, закрываем его
    app.close_baner()
    assert app.is_page_title_correct(PageModel.MainPage())

def test_check_beauty(app):
    app.goto_beauty()
    assert app.is_page_title_correct(PageModel.BeautyPage())
    app.goto_first_arcticle()
    # Если всплывает банер, закрываем его
    app.close_baner()
    assert app.is_article_excist()

def test_check_fashion(app):
    app.goto_fashion()
    assert app.is_page_title_correct(PageModel.FashionPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_rest(app):
    app.goto_rest()
    assert app.is_page_title_correct(PageModel.RestPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_gifts(app):
    app.goto_gifts()
    assert app.is_page_title_correct(PageModel.GiftsPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_celebrity(app):
    app.goto_celebrity()
    assert app.is_page_title_correct(PageModel.CelebrityPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_recipes(app):
    app.goto_recipes()
    assert app.is_page_title_correct(PageModel.RecipesPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_tests(app):
    app.goto_tests()
    assert app.is_page_title_correct(PageModel.TestsPage())

def test_check_compettion(app):
    app.goto_compettion()
    assert app.is_page_title_correct(PageModel.CompettionPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_makeup(app):
    app.goto_makeup()
    assert app.is_page_title_correct(PageModel.MakeupPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_figure(app):
    app.goto_figure()
    assert app.is_page_title_correct(PageModel.FigurePage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_hair(app):
    app.goto_hair()
    assert app.is_page_title_correct(PageModel.HairPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_manicure(app):
    app.goto_manicure()
    assert app.is_page_title_correct(PageModel.ManicurePage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_soup(app):
    app.goto_soup()
    assert app.is_page_title_correct(PageModel.SoupPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_snack(app):
    app.goto_salat_snack()
    assert app.is_page_title_correct(PageModel.SalatSnaksPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_meat(app):
    app.goto_meat()
    assert app.is_page_title_correct(PageModel.MeatPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_bread(app):
    app.goto_bread()
    assert app.is_page_title_correct(PageModel.BreadPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_pasta(app):
    app.goto_pasta()
    assert app.is_page_title_correct(PageModel.PastaPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_dessert(app):
    app.goto_dessert()
    assert app.is_page_title_correct(PageModel.DessertPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_drinkables(app):
    app.goto_drinkables()
    assert app.is_page_title_correct(PageModel.DrinkablesPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()

def test_check_conservation(app):
    app.goto_conservation()
    assert app.is_page_title_correct(PageModel.ConservationPage())
    app.goto_first_arcticle()
    app.close_baner()
    assert app.is_article_excist()









