import os

from selene.support.shared import browser

from demoqa_tests.model.user.user_data import User
from selene_in_action_py13.conditions import match


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def register(self, value: User):
        browser.element('#firstName').should(match.blank).type('Lucy')

        browser.element('#lastName').should(match.blank).type('Bechtel')

        browser.element('#userEmail').should(match.blank).type('aslavret87@gmail.com')

        browser.element('[for=gender-radio-2]').click()

        browser.element('#userNumber').should(match.blank).type('0123456789')

        # ---------------

        browser.element('#dateOfBirthInput').click()

        browser.element('.react-datepicker__month-select').click()

        browser.element('.react-datepicker__month-select').element('[value = "6"]').should(match.text('July')).click()

        browser.element('.react-datepicker__year-select').click()

        browser.element('.react-datepicker__year-select').element('[value = "2005"]').should(match.text('2005')).click()

        browser.element('.react-datepicker__day--020').should(match.text('20')).click()

        # ---------------

        browser.element('#subjectsInput').type('Arts').press_enter()
        browser.element('#subjectsInput').type('En').press_enter()

        browser.element('[for=hobbies-checkbox-2]').click()

        # ---------------

        browser.element('#uploadPicture').send_keys(os.path.abspath('resources/original.jpg'))

        # ----------------

        browser.element('#currentAddress').should(match.blank).type('426 Jordy Lodge Cartwrightshire, SC 88120-6700')

        browser.element('#state').click()

        browser.all('#state div').element_by(match.text('Haryana')).click()

        browser.element('#city').click()

        browser.all('#city div').element_by(match.text('Panipat')).click()

        # ---------------

        browser.element('#submit').click()

    def should_have_registered(self, student: User):
        browser.element('#example-modal-sizes-title-lg').should(match.text('Thanks for submitting the form'))
        browser.all('tbody tr').should(match.exact_texts([
            'Student Name Lucy Bechtel',
            'Student Email aslavret87@gmail.com',
            'Gender Female',
            'Mobile 0123456789',
            'Date of Birth 20 July,2005',
            'Subjects Arts, English',
            'Hobbies Reading',
            'Picture original.jpg',
            'Address 426 Jordy Lodge Cartwrightshire, SC 88120-6700',
            'State and City Haryana Panipat']))
        browser.element('#closeLargeModal').click()
