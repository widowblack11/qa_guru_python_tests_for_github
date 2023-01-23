import allure
from allure_commons.types import Severity
from selene import be
from selene.support import by
from selene.support.shared import browser


@allure.tag('web')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Проверка наличия таски в репе')
@allure.story('1. Чистый Selene (без шагов)')
@allure.link('https://github.com', name='Testing')
def test_to_check_name_issue_with_allure_step(open_browser):
    with allure.step('Открыть главную страницу github'):
        browser.open('https://github.com/')

    with allure.step('Кликнуть в окно поиска на старнице'):
        browser.element('.header-search-input').click()

    with allure.step('Ввести в поиске нужный репозиторий eroshenkoam/allure-example'):
     browser.element('.header-search-input').type('eroshenkoam/allure-example')

    with allure.step('Запустить поиск'):
        browser.element('.header-search-input').press_enter()

    with allure.step('Найти на странице репозиторий, соответсвующий поиску'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Кликнуть на кнопку Issue'):
        browser.element('#issues-tab').click()

    with allure.step('Проверить наличие issue с номером 53'):
        assert browser.element(by.partial_text("#66")).should(be.visible)