# coding: utf-8

"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security <aside class=\"notice\">   Before we begin a reminder that your application will need to adhere to PCI-DSS standards to operate safely   and to meet requirements set out by Visa and MasterCard and the PCI Security Standards Council including: </aside>  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities.   # noqa: E501

    The version of the OpenAPI document: 6.0.0
    Contact: support@citypay.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from citypay.configuration import Configuration


class AirlineAdvice(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'carrier_name': 'str',
        'conjunction_ticket_indicator': 'bool',
        'eticket_indicator': 'bool',
        'no_air_segments': 'int',
        'number_in_party': 'int',
        'original_ticket_no': 'str',
        'passenger_name': 'str',
        'segment1': 'AirlineSegment',
        'segment2': 'AirlineSegment',
        'segment3': 'AirlineSegment',
        'segment4': 'AirlineSegment',
        'ticket_issue_city': 'str',
        'ticket_issue_date': 'date',
        'ticket_issue_name': 'str',
        'ticket_no': 'str',
        'transaction_type': 'str'
    }

    attribute_map = {
        'carrier_name': 'carrier_name',
        'conjunction_ticket_indicator': 'conjunction_ticket_indicator',
        'eticket_indicator': 'eticket_indicator',
        'no_air_segments': 'no_air_segments',
        'number_in_party': 'number_in_party',
        'original_ticket_no': 'original_ticket_no',
        'passenger_name': 'passenger_name',
        'segment1': 'segment1',
        'segment2': 'segment2',
        'segment3': 'segment3',
        'segment4': 'segment4',
        'ticket_issue_city': 'ticket_issue_city',
        'ticket_issue_date': 'ticket_issue_date',
        'ticket_issue_name': 'ticket_issue_name',
        'ticket_no': 'ticket_no',
        'transaction_type': 'transaction_type'
    }

    def __init__(self, carrier_name=None, conjunction_ticket_indicator=None, eticket_indicator=None, no_air_segments=None, number_in_party=None, original_ticket_no=None, passenger_name=None, segment1=None, segment2=None, segment3=None, segment4=None, ticket_issue_city=None, ticket_issue_date=None, ticket_issue_name=None, ticket_no=None, transaction_type=None, local_vars_configuration=None):  # noqa: E501
        """AirlineAdvice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._carrier_name = None
        self._conjunction_ticket_indicator = None
        self._eticket_indicator = None
        self._no_air_segments = None
        self._number_in_party = None
        self._original_ticket_no = None
        self._passenger_name = None
        self._segment1 = None
        self._segment2 = None
        self._segment3 = None
        self._segment4 = None
        self._ticket_issue_city = None
        self._ticket_issue_date = None
        self._ticket_issue_name = None
        self._ticket_no = None
        self._transaction_type = None
        self.discriminator = None

        self.carrier_name = carrier_name
        if conjunction_ticket_indicator is not None:
            self.conjunction_ticket_indicator = conjunction_ticket_indicator
        if eticket_indicator is not None:
            self.eticket_indicator = eticket_indicator
        if no_air_segments is not None:
            self.no_air_segments = no_air_segments
        self.number_in_party = number_in_party
        if original_ticket_no is not None:
            self.original_ticket_no = original_ticket_no
        if passenger_name is not None:
            self.passenger_name = passenger_name
        self.segment1 = segment1
        if segment2 is not None:
            self.segment2 = segment2
        if segment3 is not None:
            self.segment3 = segment3
        if segment4 is not None:
            self.segment4 = segment4
        self.ticket_issue_city = ticket_issue_city
        self.ticket_issue_date = ticket_issue_date
        self.ticket_issue_name = ticket_issue_name
        self.ticket_no = ticket_no
        self.transaction_type = transaction_type

    @property
    def carrier_name(self):
        """Gets the carrier_name of this AirlineAdvice.  # noqa: E501

        The name of the airline carrier that generated the tickets for airline travel.  # noqa: E501

        :return: The carrier_name of this AirlineAdvice.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this AirlineAdvice.

        The name of the airline carrier that generated the tickets for airline travel.  # noqa: E501

        :param carrier_name: The carrier_name of this AirlineAdvice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and carrier_name is None:  # noqa: E501
            raise ValueError("Invalid value for `carrier_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                carrier_name is not None and len(carrier_name) > 25):
            raise ValueError("Invalid value for `carrier_name`, length must be less than or equal to `25`")  # noqa: E501

        self._carrier_name = carrier_name

    @property
    def conjunction_ticket_indicator(self):
        """Gets the conjunction_ticket_indicator of this AirlineAdvice.  # noqa: E501

        true if a conjunction ticket (with additional coupons) was issued for an itinerary with more than four segments. Defaults to false.   # noqa: E501

        :return: The conjunction_ticket_indicator of this AirlineAdvice.  # noqa: E501
        :rtype: bool
        """
        return self._conjunction_ticket_indicator

    @conjunction_ticket_indicator.setter
    def conjunction_ticket_indicator(self, conjunction_ticket_indicator):
        """Sets the conjunction_ticket_indicator of this AirlineAdvice.

        true if a conjunction ticket (with additional coupons) was issued for an itinerary with more than four segments. Defaults to false.   # noqa: E501

        :param conjunction_ticket_indicator: The conjunction_ticket_indicator of this AirlineAdvice.  # noqa: E501
        :type: bool
        """

        self._conjunction_ticket_indicator = conjunction_ticket_indicator

    @property
    def eticket_indicator(self):
        """Gets the eticket_indicator of this AirlineAdvice.  # noqa: E501

        The Electronic Ticket Indicator, a code that indicates if an electronic ticket was issued.  Defaults to true.  # noqa: E501

        :return: The eticket_indicator of this AirlineAdvice.  # noqa: E501
        :rtype: bool
        """
        return self._eticket_indicator

    @eticket_indicator.setter
    def eticket_indicator(self, eticket_indicator):
        """Sets the eticket_indicator of this AirlineAdvice.

        The Electronic Ticket Indicator, a code that indicates if an electronic ticket was issued.  Defaults to true.  # noqa: E501

        :param eticket_indicator: The eticket_indicator of this AirlineAdvice.  # noqa: E501
        :type: bool
        """

        self._eticket_indicator = eticket_indicator

    @property
    def no_air_segments(self):
        """Gets the no_air_segments of this AirlineAdvice.  # noqa: E501

        A value that indicates the number of air travel segments included on this ticket. Valid entries include the numerals “0” through “4”. Required only if the transaction type is TKT or EXC.   # noqa: E501

        :return: The no_air_segments of this AirlineAdvice.  # noqa: E501
        :rtype: int
        """
        return self._no_air_segments

    @no_air_segments.setter
    def no_air_segments(self, no_air_segments):
        """Sets the no_air_segments of this AirlineAdvice.

        A value that indicates the number of air travel segments included on this ticket. Valid entries include the numerals “0” through “4”. Required only if the transaction type is TKT or EXC.   # noqa: E501

        :param no_air_segments: The no_air_segments of this AirlineAdvice.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                no_air_segments is not None and no_air_segments > 4):  # noqa: E501
            raise ValueError("Invalid value for `no_air_segments`, must be a value less than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                no_air_segments is not None and no_air_segments < 0):  # noqa: E501
            raise ValueError("Invalid value for `no_air_segments`, must be a value greater than or equal to `0`")  # noqa: E501

        self._no_air_segments = no_air_segments

    @property
    def number_in_party(self):
        """Gets the number_in_party of this AirlineAdvice.  # noqa: E501

        The number of people in the party.  # noqa: E501

        :return: The number_in_party of this AirlineAdvice.  # noqa: E501
        :rtype: int
        """
        return self._number_in_party

    @number_in_party.setter
    def number_in_party(self, number_in_party):
        """Sets the number_in_party of this AirlineAdvice.

        The number of people in the party.  # noqa: E501

        :param number_in_party: The number_in_party of this AirlineAdvice.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_in_party is None:  # noqa: E501
            raise ValueError("Invalid value for `number_in_party`, must not be `None`")  # noqa: E501

        self._number_in_party = number_in_party

    @property
    def original_ticket_no(self):
        """Gets the original_ticket_no of this AirlineAdvice.  # noqa: E501

        Required if transaction type is EXC.  # noqa: E501

        :return: The original_ticket_no of this AirlineAdvice.  # noqa: E501
        :rtype: str
        """
        return self._original_ticket_no

    @original_ticket_no.setter
    def original_ticket_no(self, original_ticket_no):
        """Sets the original_ticket_no of this AirlineAdvice.

        Required if transaction type is EXC.  # noqa: E501

        :param original_ticket_no: The original_ticket_no of this AirlineAdvice.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                original_ticket_no is not None and len(original_ticket_no) > 14):
            raise ValueError("Invalid value for `original_ticket_no`, length must be less than or equal to `14`")  # noqa: E501

        self._original_ticket_no = original_ticket_no

    @property
    def passenger_name(self):
        """Gets the passenger_name of this AirlineAdvice.  # noqa: E501

        The name of the passenger when the traveller is not the card member that purchased the ticket. Required only if the transaction type is TKT or EXC.  # noqa: E501

        :return: The passenger_name of this AirlineAdvice.  # noqa: E501
        :rtype: str
        """
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, passenger_name):
        """Sets the passenger_name of this AirlineAdvice.

        The name of the passenger when the traveller is not the card member that purchased the ticket. Required only if the transaction type is TKT or EXC.  # noqa: E501

        :param passenger_name: The passenger_name of this AirlineAdvice.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                passenger_name is not None and len(passenger_name) > 25):
            raise ValueError("Invalid value for `passenger_name`, length must be less than or equal to `25`")  # noqa: E501

        self._passenger_name = passenger_name

    @property
    def segment1(self):
        """Gets the segment1 of this AirlineAdvice.  # noqa: E501


        :return: The segment1 of this AirlineAdvice.  # noqa: E501
        :rtype: AirlineSegment
        """
        return self._segment1

    @segment1.setter
    def segment1(self, segment1):
        """Sets the segment1 of this AirlineAdvice.


        :param segment1: The segment1 of this AirlineAdvice.  # noqa: E501
        :type: AirlineSegment
        """
        if self.local_vars_configuration.client_side_validation and segment1 is None:  # noqa: E501
            raise ValueError("Invalid value for `segment1`, must not be `None`")  # noqa: E501

        self._segment1 = segment1

    @property
    def segment2(self):
        """Gets the segment2 of this AirlineAdvice.  # noqa: E501


        :return: The segment2 of this AirlineAdvice.  # noqa: E501
        :rtype: AirlineSegment
        """
        return self._segment2

    @segment2.setter
    def segment2(self, segment2):
        """Sets the segment2 of this AirlineAdvice.


        :param segment2: The segment2 of this AirlineAdvice.  # noqa: E501
        :type: AirlineSegment
        """

        self._segment2 = segment2

    @property
    def segment3(self):
        """Gets the segment3 of this AirlineAdvice.  # noqa: E501


        :return: The segment3 of this AirlineAdvice.  # noqa: E501
        :rtype: AirlineSegment
        """
        return self._segment3

    @segment3.setter
    def segment3(self, segment3):
        """Sets the segment3 of this AirlineAdvice.


        :param segment3: The segment3 of this AirlineAdvice.  # noqa: E501
        :type: AirlineSegment
        """

        self._segment3 = segment3

    @property
    def segment4(self):
        """Gets the segment4 of this AirlineAdvice.  # noqa: E501


        :return: The segment4 of this AirlineAdvice.  # noqa: E501
        :rtype: AirlineSegment
        """
        return self._segment4

    @segment4.setter
    def segment4(self, segment4):
        """Sets the segment4 of this AirlineAdvice.


        :param segment4: The segment4 of this AirlineAdvice.  # noqa: E501
        :type: AirlineSegment
        """

        self._segment4 = segment4

    @property
    def ticket_issue_city(self):
        """Gets the ticket_issue_city of this AirlineAdvice.  # noqa: E501

        The name of the city town or village where the transaction took place.  # noqa: E501

        :return: The ticket_issue_city of this AirlineAdvice.  # noqa: E501
        :rtype: str
        """
        return self._ticket_issue_city

    @ticket_issue_city.setter
    def ticket_issue_city(self, ticket_issue_city):
        """Sets the ticket_issue_city of this AirlineAdvice.

        The name of the city town or village where the transaction took place.  # noqa: E501

        :param ticket_issue_city: The ticket_issue_city of this AirlineAdvice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ticket_issue_city is None:  # noqa: E501
            raise ValueError("Invalid value for `ticket_issue_city`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ticket_issue_city is not None and len(ticket_issue_city) > 18):
            raise ValueError("Invalid value for `ticket_issue_city`, length must be less than or equal to `18`")  # noqa: E501

        self._ticket_issue_city = ticket_issue_city

    @property
    def ticket_issue_date(self):
        """Gets the ticket_issue_date of this AirlineAdvice.  # noqa: E501

        The date the ticket was issued in ISO Date format (yyyy-MM-dd).  # noqa: E501

        :return: The ticket_issue_date of this AirlineAdvice.  # noqa: E501
        :rtype: date
        """
        return self._ticket_issue_date

    @ticket_issue_date.setter
    def ticket_issue_date(self, ticket_issue_date):
        """Sets the ticket_issue_date of this AirlineAdvice.

        The date the ticket was issued in ISO Date format (yyyy-MM-dd).  # noqa: E501

        :param ticket_issue_date: The ticket_issue_date of this AirlineAdvice.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and ticket_issue_date is None:  # noqa: E501
            raise ValueError("Invalid value for `ticket_issue_date`, must not be `None`")  # noqa: E501

        self._ticket_issue_date = ticket_issue_date

    @property
    def ticket_issue_name(self):
        """Gets the ticket_issue_name of this AirlineAdvice.  # noqa: E501

        The name of the agency generating the ticket.  # noqa: E501

        :return: The ticket_issue_name of this AirlineAdvice.  # noqa: E501
        :rtype: str
        """
        return self._ticket_issue_name

    @ticket_issue_name.setter
    def ticket_issue_name(self, ticket_issue_name):
        """Sets the ticket_issue_name of this AirlineAdvice.

        The name of the agency generating the ticket.  # noqa: E501

        :param ticket_issue_name: The ticket_issue_name of this AirlineAdvice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ticket_issue_name is None:  # noqa: E501
            raise ValueError("Invalid value for `ticket_issue_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ticket_issue_name is not None and len(ticket_issue_name) > 26):
            raise ValueError("Invalid value for `ticket_issue_name`, length must be less than or equal to `26`")  # noqa: E501

        self._ticket_issue_name = ticket_issue_name

    @property
    def ticket_no(self):
        """Gets the ticket_no of this AirlineAdvice.  # noqa: E501

        This must be a valid ticket number, i.e. numeric (the first 3 digits must represent the valid IATA plate carrier code). The final check digit should be validated prior to submission. On credit charges, this field should contain the number of the original ticket, and not of a replacement.   # noqa: E501

        :return: The ticket_no of this AirlineAdvice.  # noqa: E501
        :rtype: str
        """
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, ticket_no):
        """Sets the ticket_no of this AirlineAdvice.

        This must be a valid ticket number, i.e. numeric (the first 3 digits must represent the valid IATA plate carrier code). The final check digit should be validated prior to submission. On credit charges, this field should contain the number of the original ticket, and not of a replacement.   # noqa: E501

        :param ticket_no: The ticket_no of this AirlineAdvice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ticket_no is None:  # noqa: E501
            raise ValueError("Invalid value for `ticket_no`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ticket_no is not None and len(ticket_no) > 14):
            raise ValueError("Invalid value for `ticket_no`, length must be less than or equal to `14`")  # noqa: E501

        self._ticket_no = ticket_no

    @property
    def transaction_type(self):
        """Gets the transaction_type of this AirlineAdvice.  # noqa: E501

        This field contains the Transaction Type code assigned to this transaction. Valid codes include:   - `TKT` = Ticket Purchase  - `REF` = Refund  - `EXC` = Exchange Ticket  - `MSC` = Miscellaneous (non-Ticket Purchase- and non-Exchange Ticket-related transactions only).   # noqa: E501

        :return: The transaction_type of this AirlineAdvice.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this AirlineAdvice.

        This field contains the Transaction Type code assigned to this transaction. Valid codes include:   - `TKT` = Ticket Purchase  - `REF` = Refund  - `EXC` = Exchange Ticket  - `MSC` = Miscellaneous (non-Ticket Purchase- and non-Exchange Ticket-related transactions only).   # noqa: E501

        :param transaction_type: The transaction_type of this AirlineAdvice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_type is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_type is not None and len(transaction_type) > 3):
            raise ValueError("Invalid value for `transaction_type`, length must be less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_type is not None and len(transaction_type) < 3):
            raise ValueError("Invalid value for `transaction_type`, length must be greater than or equal to `3`")  # noqa: E501

        self._transaction_type = transaction_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AirlineAdvice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AirlineAdvice):
            return True

        return self.to_dict() != other.to_dict()
