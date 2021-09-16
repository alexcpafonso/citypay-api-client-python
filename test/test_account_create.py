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
from citypay.model.account_create import AccountCreate  # noqa: E501


class TestAccountCreate(unittest.TestCase):
    """AccountCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return AccountCreate(
                account_id='aaabbb-cccddd-eee',
                contact=citypay.ContactDetails(
                    address1='79 Parliament St',
                    address2='Westminster',
                    address3='0',
                    area='London',
                    company='Acme Ltd',
                    country='GB',
                    email='card.holder@citypay.com',
                    firstname='John',
                    lastname='Smith',
                    mobile_no='447790123456',
                    postcode='L1 789',
                    telephone_no='442030123456',
                    title='Mr', )
            )
        else:
            return AccountCreate(
                account_id='aaabbb-cccddd-eee',
            )

    def testAccountCreate(self):
        """Test AccountCreate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
