from selenium import webdriver
from pages.home.home_page import HomePage
import unittest
import pytest


@pytest.mark.usefixtures('one_time_set_up', 'set_up')
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        self.hp = HomePage(self.driver)

    @pytest.mark.run(order=2)
    # @pytest.mark.skip
    def test_valid_login(self):

        # Home page
        self.hp.login('test.auto@sample.com', 'coding*016')

        # verify title

        # title_result = self.hp.verify_title()
        # assert title_result == True

        # verify success login
        login_result = self.hp.verify_login_success()
        assert login_result == True


    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.hp.login('invalid.auto@sample.com', 'testtest')
        result = self.hp.verify_login_fail()
        assert result == True
