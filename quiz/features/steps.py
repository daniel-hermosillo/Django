# -*- coding: utf-8 -*-

import time

from lettuce import step, world, before
from lettuce.django import django_url

from selenium import webdriver


@before.all
def prepare_tests():
    world.browser = webdriver.Chrome()


@step('Given I go to the "(.*)" page')
def given_i_go_to_the_group1_page(step, page):
    world.browser.get(page)


@step('When I insert the lanid "(.*)" and try to go to the next screen')
def when_i_insert_the_lanid_group1_and_try_to_go_to_the_next_screen(step, lanid):
    lanid_input = world.browser.find_element_by_id('id_lanid')
    lanid_input.send_keys(lanid)

    xpath = '//button[contains(text(), "Next")]'
    next_button = world.browser.find_element_by_xpath(xpath)
    next_button.click()


@step('Then the error message "(.*)" is shown')
def then_the_error_message_group1_is_shown(step, expected_error):
    time.sleep(2)

    xpath = '//div[@class="red-text"]'
    error_message = world.browser.find_element_by_xpath(xpath)

    assert expected_error == error_message.text,\
        expected_error + ", " + error_message.text


@step('the url should be "(.*)" page')
def then_url_should_be_group1_page(step, expected_url):
    time.sleep(2)
    good_value = world.browser.current_url
    assert expected_url == good_value, expected_url + ", " + good_value


@step('the page should contain one question')
def then_page_should_contain_one_question(step):
    time.sleep(2)

    xpath = '//div[@class="input-field"]'
    good_value = world.browser.find_element_by_xpath(xpath)

    assert good_value, good_value

