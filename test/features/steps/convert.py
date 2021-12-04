from behave import *

use_step_matcher("re")


@given("we are looking at the home page")
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/')


@when("I convert 10 TTD to ZMW")
def step_impl(context):
    context.browser.find_element_by_name('amount').send_keys(10)
    context.browser.find_element_by_name('from_curr').send_keys('TTD')
    context.browser.find_element_by_name('to_curr').send_keys('ZMW')


@step("I click on Convert button")
def step_impl(context):
    context.browser.find_element_by_xpath(f"//input[@type='submit' and @value='Convert']").click()


@then("the following result should be returned")
def step_impl(context):
    result = 26.38
    print(context.browser.find_element_by_name('result'))
    assert result == float(context.browser.find_element_by_name('result').get_attribute("value"))
