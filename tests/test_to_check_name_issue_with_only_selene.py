import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser


@allure.tag('web')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Проверка наличия таски в репе')
@allure.story('1. Чистый Selene (без шагов)')
@allure.link('https://github.com', name='Testing')
def test_to_check_name_issue_with_only_selene(open_browser):
    browser.open('https://github.com/')
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('eroshenkoam/allure-example')
    browser.element('.header-search-input').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    assert browser.element(by.partial_text("#66")).should(be.visible)
