# -*- coding: utf-8 -*-
import unittest
from driver import (webdriver_setup,
                        add_paperclips_to_cart,
                        start_checkout_post_add_to_cart,
                        process_checkout_as_guest,
                        complete_billing_info,
                        choose_shipping_method,
                        choose_check_payment_method,
                        complete_checkout,
                        run_test)


class test_ui_functions(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver_setup()
        self.result = False


    def tearDown(self):
        self.driver.close()


    def test_general_country_argentina(self):
        argentina_test_info = {
            'test_type': 'general_country_testing',
            'tests': {
                '1' : { 
                    'billing_firstname' : 'Jason',
                    'billing_lastname' : 'Myers',
                    'billing_company' : 'Home',
                    'billing_email' : 'jason.myers@borderjump.com',
                    'billing_address1' : 'Calle Gral San Martin 230',
                    'billing_address2' : 'Piso 4 DPTO A',
                    'billing_city' : 'Villa Maria',
                    'billing_state' : '',
                    'billing_postal_code' : 'X5900FNF',
                    'billing_country' : 'Argentina',
                    'billing_telephone' : '615-796-6526'
                },
            },
        }

        for test in argentina_test_info['tests']:
            test_type = argentina_test_info['test_type']
            current_test = argentina_test_info['tests'][test]
            self.result = run_test(self.driver, current_test, test_type)
            self.assertTrue(self.result)


    # def test_general_country_australia(self):
    #     australia_test_info = {
    #         'test_type': 'general_country_testing',
    #         'tests' : {
    #             '1' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : '183 Botany Road',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Waterloo',
    #                 'billing_state' : 'NSW',
    #                 'billing_postal_code' : '2017',
    #                 'billing_country' : 'Australia',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #             '2' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : 'PO Box 37',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Springvale',
    #                 'billing_state' : 'VIC',
    #                 'billing_postal_code' : '3171',
    #                 'billing_country' : 'Australia',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #         },
    #     }

    #     for test in australia_test_info['tests']:
    #         test_type = australia_test_info['test_type']
    #         current_test = australia_test_info['tests'][test]
    #         print repr(current_test['billing_firstname'])
    #         self.result = run_test(self.driver, current_test, test_type)
    #         self.assertTrue(self.result)


    # def test_ship_domestic_with_internation_billing(self):
    #     test_info = {
    #         'test_type': 'domestic_shipping_fail',
    #         'tests' : {
    #             '1' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : '183 Botany Road',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Waterloo',
    #                 'billing_state' : 'NSW',
    #                 'billing_postal_code' : '2017',
    #                 'billing_country' : 'Australia',
    #                 'billing_telephone' : '615-796-6526',
    #                 'shipping_firstname' : 'Jason',
    #                 'shipping_lastname' : 'Myers',
    #                 'shipping_company' : 'Work',
    #                 'shipping_address1' : '631 2nd Ave So',
    #                 'shipping_address2' : '',
    #                 'shipping_city' : 'Nashville',
    #                 'shipping_state' : 'Tennessee',
    #                 'shipping_postal_code' : '37128',
    #                 'shipping_country' : 'United States',
    #                 'shipping_telephone' : '615-796-6526'
    #             },
    #         },
    #     }

    #     for test in test_info['tests']:
    #         test_type = test_info['test_type']
    #         current_test = test_info['tests'][test]
    #         print repr(current_test['billing_firstname'])
    #         self.result = run_test(self.driver, current_test, test_type)
    #         self.assertTrue(self.result)


    # def test_ship_domestic_with_internation_billing(self):
    #     test_info = {
    #         'test_type': 'multiple_skus',
    #         'tests' : {
    #             '1' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : 'Mimbreras 4',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Elche',
    #                 'billing_state' : 'Alicante',
    #                 'billing_postal_code' : '03201',
    #                 'billing_country' : 'Spain',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #         },
    #     }

    #     for test in test_info['tests']:
    #         test_type = test_info['test_type']
    #         current_test = test_info['tests'][test]
    #         print repr(current_test['billing_firstname'])
    #         self.result = run_test(self.driver, current_test, test_type)
    #         self.assertTrue(self.result)


    # def test_ship_domestic_with_internation_billing(self):
    #     test_info = {
    #         'test_type': 'invalid_characters',
    #         'tests' : {
    #             '1' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u'Graf-Adolf-Straße 81-87 ',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Dusseldorf',
    #                 'billing_state' : 'Nordrhein-Westfalen',
    #                 'billing_postal_code' : '40210',
    #                 'billing_country' : 'Germany',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #             '2' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u'C/Pescadoro, 22, 3°, 1A izda',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Elche',
    #                 'billing_state' : 'Alicante',
    #                 'billing_postal_code' : '03201',
    #                 'billing_country' : 'Spain',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #             '3' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u'〒 21−18 Shibuya',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Tokyo',
    #                 'billing_state' : '',
    #                 'billing_postal_code' : '150-0002',
    #                 'billing_country' : 'Japan',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #             '4' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : 'Graf-Adolf-Strabe 81-87',
    #                 'billing_address2' : '',
    #                 'billing_city' : u'Düsseldorf',
    #                 'billing_state' : 'Nordrhein-Westfalen',
    #                 'billing_postal_code' : '40210',
    #                 'billing_country' : 'Germany',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #             '5' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u'Carrera San Jerónimo',
    #                 'billing_address2' : '8',
    #                 'billing_city' : 'Madrid',
    #                 'billing_state' : 'Madrid',
    #                 'billing_postal_code' : '28014',
    #                 'billing_country' : 'Spain',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #         },
    #     }

    #     for test in test_info['tests']:
    #         test_type = test_info['test_type']
    #         current_test = test_info['tests'][test]
    #         print repr(current_test['billing_firstname'])
    #         self.result = run_test(self.driver, current_test, test_type)
    #         self.assertTrue(self.result)


    # def test_long_data(self):
    #     test_info = {
    #         'test_type': 'long_data',
    #         'tests' : {
    #             '1' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u' 2391 West I pledge allegiance to the flag of the United States of America to the republic for which it stands one nation under God indivisible with liberty and justice for all 4th Avenue',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Vancouver',
    #                 'billing_state' : 'British Columbia',
    #                 'billing_postal_code' : 'V6K 1P4',
    #                 'billing_country' : 'Canada',
    #                 'billing_telephone' : '615-796-6526'
    #             },

    #         },
    #     }

    #     for test in test_info['tests']:
    #         test_type = test_info['test_type']
    #         current_test = test_info['tests'][test]
    #         print repr(current_test['billing_firstname'])
    #         self.result = run_test(self.driver, current_test, test_type)
    #         self.assertTrue(self.result)


    # def test_incorrect_data(self):
    #     test_info = {
    #         'test_type': 'incorrect_data',
    #         'tests' : {
    #             '1' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u'2391 West 4th Avenue',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Vancouver',
    #                 'billing_state' : 'British Columbia',
    #                 'billing_postal_code' : 'V55 1P4',
    #                 'billing_country' : 'Canada',
    #                 'billing_telephone' : '615-796-6526'
    #             },

    #         },
    #     }

    #     for test in test_info['tests']:
    #         test_type = test_info['test_type']
    #         current_test = test_info['tests'][test]
    #         print repr(current_test['billing_firstname'])
    #         self.result = run_test(self.driver, current_test, test_type)
    #         self.assertTrue(self.result)


    # def test_incorrect_data(self):
    #     test_info = {
    #         'test_type': 'missing_data',
    #         'tests' : {
    #             '1' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u'2391 West 4th Avenue',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'V',
    #                 'billing_state' : 'British Columbia',
    #                 'billing_postal_code' : 'V6K 1P4',
    #                 'billing_country' : 'Canada',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #             '2' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u'West 4th Avenue',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Vancouver',
    #                 'billing_state' : 'British Columbia',
    #                 'billing_postal_code' : 'V6K 1P4',
    #                 'billing_country' : 'Canada',
    #                 'billing_telephone' : '615-796-6526'
    #             },

    #         },
    #     }

    #     for test in test_info['tests']:
    #         test_type = test_info['test_type']
    #         current_test = test_info['tests'][test]
    #         print repr(current_test['billing_firstname'])
    #         self.result = run_test(self.driver, current_test, test_type)
    #         self.assertTrue(self.result)


    # def test_denied_party(self):
    #     test_info = {
    #         'test_type': 'denied_party',
    #         'tests' : {
    #             '1' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u'2465 Cawthra Rd. #203',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Mississauga',
    #                 'billing_state' : 'Ontario',
    #                 'billing_postal_code' : 'L5A 3P2',
    #                 'billing_country' : 'Canada',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #             '2' : { 
    #                 'billing_firstname' : 'Osama',
    #                 'billing_lastname' : 'Bin Laden',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u'West 4th Avenue',
    #                 'billing_address2' : '',
    #                 'billing_city' : 'Vancouver',
    #                 'billing_state' : 'British Columbia',
    #                 'billing_postal_code' : 'V6K 1P4',
    #                 'billing_country' : 'Canada',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #         },
    #     }

    #     for test in test_info['tests']:
    #         test_type = test_info['test_type']
    #         current_test = test_info['tests'][test]
    #         print repr(current_test['billing_firstname'])
    #         self.result = run_test(self.driver, current_test, test_type)
    #         self.assertTrue(self.result)


    # def test_zip_spacing(self):
    #     test_info = {
    #         'test_type': 'zip_spacing',
    #         'tests' : {
    #             '1' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u'Carrera San Jerónimo',
    #                 'billing_address2' : '8',
    #                 'billing_city' : 'Madrid',
    #                 'billing_state' : 'Madrid',
    #                 'billing_postal_code' : ' 28014',
    #                 'billing_country' : 'Spain',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #             '2' : { 
    #                 'billing_firstname' : 'Jason',
    #                 'billing_lastname' : 'Myers',
    #                 'billing_company' : 'Home',
    #                 'billing_email' : 'jason.myers@borderjump.com',
    #                 'billing_address1' : u'Carrera San Jerónimo',
    #                 'billing_address2' : '8',
    #                 'billing_city' : 'Madrid',
    #                 'billing_state' : 'Madrid',
    #                 'billing_postal_code' : '28014 ',
    #                 'billing_country' : 'Spain',
    #                 'billing_telephone' : '615-796-6526'
    #             },
    #         },
    #     }

    #     for test in test_info['tests']:
    #         test_type = test_info['test_type']
    #         current_test = test_info['tests'][test]
    #         print repr(current_test['billing_firstname'])
    #         self.result = run_test(self.driver, current_test, test_type)
    #         self.assertTrue(self.result)

