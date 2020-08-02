# coding: utf-8

"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security <aside class=\"notice\">   Before we begin a reminder that your application will need to adhere to PCI-DSS standards to operate safely   and to meet requirements set out by Visa and MasterCard and the PCI Security Standards Council including: </aside>  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities.   # noqa: E501

    The version of the OpenAPI document: 6.0.0
    Contact: support@citypay.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import citypay
from citypay.models.airline_advice import AirlineAdvice  # noqa: E501
from citypay.rest import ApiException

class TestAirlineAdvice(unittest.TestCase):
    """AirlineAdvice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AirlineAdvice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = citypay.models.airline_advice.AirlineAdvice()  # noqa: E501
        if include_optional :
            return AirlineAdvice(
                carrier_name = 'EG Air', 
                conjunction_ticket_indicator = False, 
                eticket_indicator = True, 
                no_air_segments = 2, 
                number_in_party = 2, 
                original_ticket_no = '0', 
                passenger_name = 'NE Person', 
                segment1 = citypay.models.airline_segment.AirlineSegment(
                    arrival_location_code = 'SOU', 
                    carrier_code = 'ZZ', 
                    class_service_code = 'CC', 
                    departure_date = 'Sat Aug 01 00:00:00 GMT 2020', 
                    departure_location_code = 'JER', 
                    flight_number = '772', 
                    segment_fare = 7500, 
                    stop_over_indicator = '1', ), 
                segment2 = citypay.models.airline_segment.AirlineSegment(
                    arrival_location_code = 'SOU', 
                    carrier_code = 'ZZ', 
                    class_service_code = 'CC', 
                    departure_date = 'Sat Aug 01 00:00:00 GMT 2020', 
                    departure_location_code = 'JER', 
                    flight_number = '772', 
                    segment_fare = 7500, 
                    stop_over_indicator = '1', ), 
                segment3 = citypay.models.airline_segment.AirlineSegment(
                    arrival_location_code = 'SOU', 
                    carrier_code = 'ZZ', 
                    class_service_code = 'CC', 
                    departure_date = 'Sat Aug 01 00:00:00 GMT 2020', 
                    departure_location_code = 'JER', 
                    flight_number = '772', 
                    segment_fare = 7500, 
                    stop_over_indicator = '1', ), 
                segment4 = citypay.models.airline_segment.AirlineSegment(
                    arrival_location_code = 'SOU', 
                    carrier_code = 'ZZ', 
                    class_service_code = 'CC', 
                    departure_date = 'Sat Aug 01 00:00:00 GMT 2020', 
                    departure_location_code = 'JER', 
                    flight_number = '772', 
                    segment_fare = 7500, 
                    stop_over_indicator = '1', ), 
                ticket_issue_city = 'London', 
                ticket_issue_date = 'Sat Aug 01 00:00:00 GMT 2020', 
                ticket_issue_name = 'Issue Name', 
                ticket_no = 'A112233', 
                transaction_type = 'TKT'
            )
        else :
            return AirlineAdvice(
                carrier_name = 'EG Air',
                number_in_party = 2,
                segment1 = citypay.models.airline_segment.AirlineSegment(
                    arrival_location_code = 'SOU', 
                    carrier_code = 'ZZ', 
                    class_service_code = 'CC', 
                    departure_date = 'Sat Aug 01 00:00:00 GMT 2020', 
                    departure_location_code = 'JER', 
                    flight_number = '772', 
                    segment_fare = 7500, 
                    stop_over_indicator = '1', ),
                ticket_issue_city = 'London',
                ticket_issue_date = 'Sat Aug 01 00:00:00 GMT 2020',
                ticket_issue_name = 'Issue Name',
                ticket_no = 'A112233',
                transaction_type = 'TKT',
        )

    def testAirlineAdvice(self):
        """Test AirlineAdvice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
