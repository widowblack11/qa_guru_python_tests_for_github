#!/usr/bin/python -tt
import allure
from allure_commons.types import Severity
from selene import be
from selene.support import by
from selene.support.shared import browser


@allure.tag('web')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Проверка наличия таски в репе')
@allure.story('Шаги с декоратором @allure.step')
@allure.link('https://github.com', name='Testing')
def test_to_check_name_issue_with_decorator_allure(open_browser):
    open_main_page()
    click_window_of_search()
    set_search_options()
    start_search()
    search_pull_requests_with_params_of_search()
    click_on_tab()
    check_repo_with_number()


with allure.step('Открыть главную страницу github'):
    def open_main_page():
        browser.open('https://github.com/')

with allure.step('Кликнуть в окно поиска на странице'):
    def click_window_of_search():
        browser.element('.header-search-input').click()

with allure.step('Ввести в поиске нужный репозиторий eroshenkoam/allure-example'):
    def set_search_options():
        browser.element('.header-search-input').type('eroshenkoam/allure-example')

with allure.step('Запустить поиск'):
    def start_search():
        browser.element('.header-search-input').press_enter()

with allure.step('Найти на странице репозиторий, соответсвующий поиску'):
    def search_pull_requests_with_params_of_search():
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

with allure.step('Кликнуть на кнопку Issue'):
    def click_on_tab():
        browser.element('#issues-tab').click()

with allure.step('Проверить наличие issue с номером 53'):
    def check_repo_with_number():
        assert browser.element(by.partial_text("#66")).should(be.visible)
