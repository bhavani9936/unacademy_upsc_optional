import time

from behave import *
from features.pages.Courseclasspage import UPSC_Optional
from hamcrest import *

# Launch Chrome and open the UPSC course page
@given("chrome is opened and UPSC course page is launched")
def step_impl(context):
    time.sleep(2)
    expectedTitle = "UPSC Optional | Unacademy"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

# Click the "Got it" button
@step("user clicks Got it button")
def step_impl(context):
    gotIt= UPSC_Optional(context.driver)
    gotIt.click_Got_It()

#  Click the "Success Stories" button
@then("user clicks success stories")
def step_impl(context):
    click_Stories= UPSC_Optional(context.driver)
    click_Stories.click_success_stories()

#  Verify that the user is in the "Success Stories" field
@step("user is in success stories field")
def step_impl(context):
    time.sleep(2)
    expectedTitle = "Unacademy - India's largest learning platform"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

#  Click the "Subscription" button
@step("user clicks subsciption button")
def step_impl(context):
    click_Subscription= UPSC_Optional(context.driver)
    click_Subscription.click_subscripiton()
    time.sleep(5)

# Verify that the user is in the "Subscription" field
@step("user is in subscription field")
def step_impl(context):
    time.sleep(2)
    expectedTitle = "Unacademy - India's largest learning platform"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

#  Click the "Store New" button
@then("user clicks store new button")
def step_impl(context):
    store= UPSC_Optional(context.driver)
    store.click_store_new()

#  Verify that the user is in the "Store New" field
@step("user is in store new field")
def step_impl(context):
    time.sleep(2)
    expectedTitle = "Unacademy - India's largest learning platform"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

# Click the "Store New" button again
@when("user clicks store new button")
def step_impl(context):
    store= UPSC_Optional(context.driver)
    store.click_store_new()

#  Click the "Batch" button
@then("user clicks batch button")
def step_impl(context):
   click_Batch= UPSC_Optional(context.driver)
   click_Batch.click_batch()

#  Verify that the user is in the "Batch" field
@step("user is in batch feild")
def step_impl(context):
    expectedTitle = "Unacademy - India's largest learning platform"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
