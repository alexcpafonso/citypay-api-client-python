# coding: utf-8

"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security <aside class=\"notice\">   Before we begin a reminder that your application will need to adhere to PCI-DSS standards to operate safely   and to meet requirements set out by Visa and MasterCard and the PCI Security Standards Council including: </aside>  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities.   # noqa: E501

    Contact: support@citypay.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import citypay
from citypay.api.card_holder_account_api import CardHolderAccountApi  # noqa: E501


class TestCardHolderAccountApi(unittest.TestCase):
    """CardHolderAccountApi unit test stubs"""

    def setUp(self):
        self.api = citypay.api.card_holder_account_api.CardHolderAccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_account_card_delete_request(self):
        """Test case for account_card_delete_request

        Card Deletion  # noqa: E501
        """
        pass

    def test_account_card_register_request(self):
        """Test case for account_card_register_request

        Card Registration  # noqa: E501
        """
        pass

    def test_account_card_status_request(self):
        """Test case for account_card_status_request

        Card Status  # noqa: E501
        """
        pass

    def test_account_change_contact_request(self):
        """Test case for account_change_contact_request

        Contact Details Update  # noqa: E501
        """
        pass

    def test_account_create(self):
        """Test case for account_create

        Account Create  # noqa: E501
        """
        pass

    def test_account_delete_request(self):
        """Test case for account_delete_request

        Account Deletion  # noqa: E501
        """
        pass

    def test_account_retrieve_request(self):
        """Test case for account_retrieve_request

        Account Retrieval  # noqa: E501
        """
        pass

    def test_account_status_request(self):
        """Test case for account_status_request

        Account Status  # noqa: E501
        """
        pass

    def test_charge_request(self):
        """Test case for charge_request

        Charge  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
