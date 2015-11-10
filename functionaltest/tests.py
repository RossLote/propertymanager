#!/usr/bin/env python
from selenium import webdriver
from django.test import TestCase


class NewVisitorTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_signup_button_goes_to_signup_page(self):
        # John goes to the home page
        self.browser.get('http://localhost:8000')

        # he notices that there is a signup button
        signup_button = self.browser.find_element_by_id('signup')

        # he clicks the signup button and goes to the signup page
        signup_button.click()

        # he gets sent to the signup page
        self.assertEqual(
            self.browser.current_url,
            'http://localhost:8000/signup/'
        )

    def test_signup_form_empty_fields(self):
        # John goes to the signup page
        self.browser.get('http://localhost:8000/signup/')

        # he sees the signup button
        signup_button = self.browser.find_element_by_id('signup-form-submit')

        # he tries submitting the form while it's empty
        signup_button.click()

        # he gets an error telling him the the form needs to be filled in
        self.assertIn('This field is required', self.browser.page_source)

    def test_signup_form_invalid_email(self):
        self.browser.get('http://localhost:8000/signup/')

        # he enters an invalid email address
        self.browser.find_element_by_id('id_email').send_keys('invalid email')
        self.browser.find_element_by_id('signup-form-submit').click()
        self.assertIn('Enter a valid email address', self.browser.page_source)

    def test_signup_form_correct(self):

        # John goes to the signup page
        self.browser.get('http://localhost:8000/signup/')

        # he notices that the title mentions signup
        self.assertIn('signup', self.browser.title.lower())

        # He fills out the form correctly and uses the return key to submit the form
        self.browser.find_element_by_id('id_first_name').send_keys('Bruce')
        self.browser.find_element_by_id('id_last_name').send_keys('Wayne')
        self.browser.find_element_by_id('id_email').send_keys('functional_test@email.com')
        self.browser.find_element_by_id('id_password1').send_keys('alfred1')
        self.browser.find_element_by_id('id_password2').send_keys('alfred1\n')

        self.fail('Current stopping point!')
