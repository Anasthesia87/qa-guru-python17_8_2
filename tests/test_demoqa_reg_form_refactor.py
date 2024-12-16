from demoqa_tests.model.page.registration_page import RegistrationPage
from demoqa_tests.model.user.user_data import student


def test_student_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
