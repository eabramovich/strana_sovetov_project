# -*- coding: utf-8 -*-
class PageModel(object):

    def __init__(self, url="", title="", h1="", h2=""):
        self.url = url
        self.title = title
        self.h1 = h1

    @classmethod
    def MainPage(cls):
        return cls(url="http://strana-sovetov.com",
                   title="Страна Советов: полезные советы, ответы на вопросы, практические рекомендации и отзывы потребителей о товарах",
                   h1="")
    @classmethod
    def BeautyPage(cls):
        return cls(url="http://strana-sovetov.com/fashion.html",
                   title="Красота и мода: полезные советы стилистов по выбору одежды и аксессуаров",
                   h1="Красота и мода")

    @classmethod
    def FashionPage(cls):
        return cls(url="http://strana-sovetov.com/moda.html",
                   title="Мода",
                   h1="Мода")

    @classmethod
    def RestPage(cls):
        return cls(url="http://strana-sovetov.com/miscellaneous.html?format=html&scope=138",
                   title="Самые полезные советы, рекомендации и житейские хитрости на все случаи жизни",
                   h1="Разное")

    @classmethod
    def GiftsPage(cls):
        return cls(url="http://strana-sovetov.com/gifts-and-souvenirs.html",
                   title="Подарки и сувениры: советы по выбору, общие рекомендации, полезная информация",
                   h1="Подарки и сувениры")

    @classmethod
    def CelebrityPage(cls):
        return cls(url="http://strana-sovetov.com/celebrity.html",
                   title="Звезды",
                   h1="Звезды")

    @classmethod
    def RecipesPage(cls):
        return cls(url="http://strana-sovetov.com/recipes.html",
                   title="Рецепты, полезные советы по приготовлению вкусных блюд, инструкции, фото и видео",
                   h1="Рецепты")

    @classmethod
    def TestsPage(cls):
        return cls(url="http://strana-sovetov.com/test.html",
                   title="Тесты",
                   h2="Психологические тесты")

    @classmethod
    def CompettionPage(cls):
        return cls(url="http://strana-sovetov.com/contests.html",
                   title="Конкурсы",
                   h1="Конкурсы")

    @classmethod
    def MakeupPage(cls):
        return cls(url="http://strana-sovetov.com/fashion/cosmetics.html",
                   title="Всё о косметике: секреты, правила нанесения, полезные советы и фирменные хитрости",
                   h1="Лицо")

    @classmethod
    def FigurePage(cls):
        return cls(url="http://strana-sovetov.com/fashion/figure.html",
                   title="Фигура: уход за собой, советы по диетам, упражнения, лучшие методики похудения",
                   h1="Фигура")

    @classmethod
    def HairPage(cls):
        return cls(url="http://strana-sovetov.com/fashion/hair.html",
                   title="Волосы: советы по уходу, завивка и покраска, секреты профессиональных стилистов",
                   h1="Волосы")

    @classmethod
    def ManicurePage(cls):
        return cls(url="http://strana-sovetov.com/fashion/nais.html",
                   title="Ногти: советы по правильному уходу, секреты качественного маникюра и педикюра",
                   h1="Ногти")

    @classmethod
    def SoupPage(cls):
        return cls(url="http://strana-sovetov.com/recipes/soups.html",
                   title="Супы: рецепты разных супов, общие советы и рекомендации, фото и многое другое",
                   h1="Супы")

    @classmethod
    def SalatSnaksPage(cls):
        return cls(url="http://strana-sovetov.com/recipes/salads.html",
                   title="Салаты и закуски: лучшие рецепты, полезные советы, фото и рекомендации",
                   h1="Салаты, закуски")

    @classmethod
    def MeatPage(cls):
        return cls(url="http://strana-sovetov.com/recipes/meat.html",
                   title="Мясо и птица: рецепты лучших блюд, ценные советы по приготовлению, фото",
                   h1="Мясо, птица")

    @classmethod
    def FishPage(cls):
        return cls(url="http://strana-sovetov.com/recipes/meat.html",
                   title="Рыба и морепродукты: рецепты, ценные советы и рекомендации, фотографии",
                   h1="Рыба, морепродукты")

    @classmethod
    def BreadPage(cls):
        return cls(url="http://strana-sovetov.com/recipes/bread.html",
                   title="Хлеб и выпечка: рецепты приготовления, создание пиццы и других блюд из теста",
                   h1="Хлеб, выпечка")

    @classmethod
    def PastaPage(cls):
        return cls(url="http://strana-sovetov.com/recipes/pasta.html",
                   title="Макароны и ризотто: популярные рецепты, советы по приготовлению, фото и другое",
                   h1="Макароны, ризотто")

    @classmethod
    def DessertPage(cls):
        return cls(url="http://strana-sovetov.com/recipes/desserts.html",
                   title="Десерты: рецепты, полезные советы, секреты приготовления, фотографии и статьи",
                   h1="Десерты")

    @classmethod
    def DrinkablesPage(cls):
        return cls(url="http://strana-sovetov.com/recipes/drinks.html",
                   title="Напитки: рецепты, ценные советы и рекомендации, статьи и фото приготовления",
                   h1="Напитки")

    @classmethod
    def ConservationPage(cls):
        return cls(url="http://strana-sovetov.com/recipes/conservation.html",
                   title="Консервирование: полезные советы, общие рекомендации, статьи и рецепты",
                   h1="Консервирование")

    @classmethod
    def SideDishPage(cls):
        return cls(url="http://strana-sovetov.com/recipes/garniry-sousy.html",
                   title="Гарниры и соусы: рецепты приготовления, ценные статьи, советы и рекомендации",
                   h1="Гарниры, соусы")

    @classmethod
    def AdvertasingPage(cls):
        return cls(url="http://wp-media.ru/women.html",
                   title="WP Media - реклама на женских сайтах",
                   h1="")

    @classmethod
    def FeedBackPage(cls):
        return cls(url="http://strana-sovetov.com/index.php?option=com_rsform&formId=5&Itemid=99999",
                   title="Страна Советов: полезные советы, ответы на вопросы, практические рекомендации и отзывы потребителей о товарах",
                   h1="")

    @classmethod
    def PopularMedecinePage(cls):
        return cls(url="http://strana-sovetov.com/popular-medicine.html",
                   title="Народная медицина: рецепты применения трав народными средствами",
                   h1="Народная медицина")

    @classmethod
    def HobbyPage(cls):
        return cls(url="http://strana-sovetov.com/hobbies.html",
                   title="Хобби: полезные советы, уроки Хэнд Мэйд, уход за растениями и многое другое",
                   h1="Хобби")


    @classmethod
    def RenovationPage(cls):
        return cls(url="http://strana-sovetov.com/renovation.html",
                   title="Ремонт: ценные советы, инструкции, фото и видео, полезные статьи, описания",
                   h1="Ремонт")

    @classmethod
    def HealthPage(cls):
        return cls(url="http://strana-sovetov.com/health.html",
                   title="Здоровье: полезные советы врачей, питание, витамины и другая информация",
                   h1="Здоровье")

    @classmethod
    def KidsPage(cls):
        return cls(url="http://strana-sovetov.com/kids.html",
                   title="Дети: полезные советы по уходу за детьми любого возраста, от 0 до 14 лет",
                   h1="Дети")

    @classmethod
    def AnimalPage(cls):
        return cls(url="http://strana-sovetov.com/animals.html",
                   title="Советы по уходу за домашними животными: кормление, лечение и рекомендации",
                   h1="Домашние животные")

    @classmethod
    def ComputersPage(cls):
        return cls(url="http://strana-sovetov.com/computers.html",
                   title="Компьютеры: полезные советы и хитрости для пользователей, обзоры и информация",
                   h1="Компьютеры")

    @classmethod
    def CareerPage(cls):
        return cls(url="http://strana-sovetov.com/career.html",
                   title="Советы: Карьера",
                   h1="Карьера")

    @classmethod
    def Psychology(cls):
        return cls(url="http://strana-sovetov.com/psychology.html",
                   title="Психология: советы профессионалов, полезные рекомендации, интересные статьи",
                   h1="Психология")

    @classmethod
    def Miscellaneous(cls):
        return cls(url="http://strana-sovetov.com/miscellaneous.html",
                   title="Самые полезные советы, рекомендации и житейские хитрости на все случаи жизни",
                   h1="Разное")

    @classmethod
    def Auto(cls):
        return cls(url="http://strana-sovetov.com/auto.html",
                   title="Отзывы о новинках автомобильного и мототранспорта, советы и свежие обзоры",
                   h1="Авто")

    @classmethod
    def Technique(cls):
        return cls(url="http://strana-sovetov.com/appliances.html",
                   title="Отзывы о технике: мобильные телефоны, бытовая техника, компьютеры и другое",
                   h1="Техника")

    @classmethod
    def CosmeticsPage(cls):
        return cls(url="http://strana-sovetov.com/beauty.html",
                   title="Отзывы о косметике, описание средств по уходу за собой, фото и видео материалы",
                   h1="Косметика")

    @classmethod
    def Books(cls):
        return cls(url="http://strana-sovetov.com/books.html",
                   title="Отзывы о книгах, обзоры и рецензии лучших мировых литературных произведений",
                   h1="Книги")

    @classmethod
    def Cinema(cls):
        return cls(url="http://strana-sovetov.com/movies.html",
                   title="Кино: отзывы зрителей, полезные рекомендации, советы, что можно посмотреть",
                   h1="Кино")

    @classmethod
    def Celebrity(cls):
        return cls(url="http://strana-sovetov.com/celebrity.html",
                   title="Звезды",
                   h1="Звезды")

    @classmethod
    def Aviasales(cls):
        return cls(url="http://strana-sovetov.com/aviasales.html",
                   title="Aviasales",
                   h1="")

    @classmethod
    def Hotellook(cls):
        return cls(url="http://strana-sovetov.com/hotellook.html",
                   title="Hotellook",
                   h1="")

    @classmethod
    def Melitta(cls):
        return cls(url="http://strana-sovetov.com/melitta-special.html",
                   title="Melitta",
                   h1="")

    @classmethod
    def Econika(cls):
        return cls(url="http://strana-sovetov.com/econika.html",
                   title="Econika",
                   h1="")

    @classmethod
    def Vivacalze(cls):
        return cls(url="http://strana-sovetov.com/vivacalze.html",
                   title="Viva Calze",
                   h1="")

    @classmethod
    def Lamoda(cls):
        return cls(url="http://strana-sovetov.com/lamoda.html",
                   title="lamoda.ru",
                   h1="")

    @classmethod
    def BWT(cls):
        return cls(url="http://strana-sovetov.com/bwt.html",
                   title="BWT",
                   h1="")















