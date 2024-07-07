import pytest
from pageObjects.dashboard import DashboardPage
from pageObjects.login import LogIn
from pageObjects.signUp import SignUpPage
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestSignUp(BaseClass):

    @pytest.fixture(autouse=True)
    def setup_pages(self, setup):
        self.dashboard_page = DashboardPage(self.driver)
        self.login_page = LogIn(self.driver)
        self.signup_page = SignUpPage(self.driver)
        yield
        self.signup_page.clear_fields()

    def test_e2e(self):
        self.dashboard_page.go_to_dashboard()

    def test_signupClick(self):
        self.login_page.go_to_signup()

    def test_page_title(self):
        self.wait_for_title_contains("Register")
        assert "Register" in self.driver.title

    def test_presence_of_all_fields(self):
        fields = ["username", "email", "gender", "date", "pass", "cpass"]
        for field in fields:
            assert self.signup_page.is_field_displayed(field)

    def test_mandatory_fields_validation(self):
        self.signup_page.submit_form()
        validation_messages = self.signup_page.get_validation_messages()
        assert len(validation_messages) > 0

    def test_email_field_with_invalid_format(self):
        self.signup_page.enter_email("abc")
        self.signup_page.submit_form()
        validation_message = self.signup_page.get_email_validation_message()
        assert "valid email" in validation_message

    def test_password_length_and_strength(self):
        self.signup_page.enter_password("abc")
        self.signup_page.submit_form()
        validation_message = self.signup_page.get_password_validation_message()
        assert "Length must be minimum 8 and combination of uppercase" in validation_message

    def test_password_and_confirm_password_match(self):
        self.signup_page.enter_password("String@123")
        self.signup_page.enter_confirm_password("String@@123")
        self.signup_page.submit_form()
        validation_message = self.signup_page.get_password_mismatch_message()
        assert "Password did not match" in validation_message

    def test_gender_dropdown_functionality(self):
        self.signup_page.select_gender("Male")
        assert self.signup_page.get_selected_gender() == "Male"

    def test_successful_form_submission(self):
        self.signup_page.enter_username("Testing")
        self.signup_page.enter_email("mik@yopmail.com")
        self.signup_page.select_gender("Male")
        self.signup_page.enter_password("String@123")
        self.signup_page.enter_confirm_password("String@123")

        old_url = self.driver.current_url
        self.signup_page.submit_form()
        self.wait_for_url_change(old_url)
        assert "signup" in self.driver.current_url

