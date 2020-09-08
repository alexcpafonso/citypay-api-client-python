# coding: utf-8

"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security <aside class=\"notice\">   Before we begin a reminder that your application will need to adhere to PCI-DSS standards to operate safely   and to meet requirements set out by Visa and MasterCard and the PCI Security Standards Council including: </aside>  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities.   # noqa: E501

    Contact: support@citypay.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from citypay.configuration import Configuration


class CardHolderAccount(object):
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
        'account_id': 'str',
        'cards': 'list[Card]',
        'contact': 'ContactDetails',
        'date_created': 'datetime',
        'default_card_id': 'str',
        'default_card_index': 'int',
        'status': 'str',
        'unique_id': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'cards': 'cards',
        'contact': 'contact',
        'date_created': 'date_created',
        'default_card_id': 'default_card_id',
        'default_card_index': 'default_card_index',
        'status': 'status',
        'unique_id': 'unique_id'
    }

    def __init__(self, account_id=None, cards=None, contact=None, date_created=None, default_card_id=None, default_card_index=None, status=None, unique_id=None, local_vars_configuration=None):  # noqa: E501
        """CardHolderAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._cards = None
        self._contact = None
        self._date_created = None
        self._default_card_id = None
        self._default_card_index = None
        self._status = None
        self._unique_id = None
        self.discriminator = None

        self.account_id = account_id
        if cards is not None:
            self.cards = cards
        self.contact = contact
        if date_created is not None:
            self.date_created = date_created
        if default_card_id is not None:
            self.default_card_id = default_card_id
        if default_card_index is not None:
            self.default_card_index = default_card_index
        if status is not None:
            self.status = status
        if unique_id is not None:
            self.unique_id = unique_id

    @property
    def account_id(self):
        """Gets the account_id of this CardHolderAccount.  # noqa: E501

        The account id of the card holder account provided by the merchant which uniquely identifies the account.   # noqa: E501

        :return: The account_id of this CardHolderAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CardHolderAccount.

        The account id of the card holder account provided by the merchant which uniquely identifies the account.   # noqa: E501

        :param account_id: The account_id of this CardHolderAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_id is not None and len(account_id) > 50):
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_id is not None and len(account_id) < 5):
            raise ValueError("Invalid value for `account_id`, length must be greater than or equal to `5`")  # noqa: E501

        self._account_id = account_id

    @property
    def cards(self):
        """Gets the cards of this CardHolderAccount.  # noqa: E501


        :return: The cards of this CardHolderAccount.  # noqa: E501
        :rtype: list[Card]
        """
        return self._cards

    @cards.setter
    def cards(self, cards):
        """Sets the cards of this CardHolderAccount.


        :param cards: The cards of this CardHolderAccount.  # noqa: E501
        :type: list[Card]
        """

        self._cards = cards

    @property
    def contact(self):
        """Gets the contact of this CardHolderAccount.  # noqa: E501


        :return: The contact of this CardHolderAccount.  # noqa: E501
        :rtype: ContactDetails
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this CardHolderAccount.


        :param contact: The contact of this CardHolderAccount.  # noqa: E501
        :type: ContactDetails
        """
        if self.local_vars_configuration.client_side_validation and contact is None:  # noqa: E501
            raise ValueError("Invalid value for `contact`, must not be `None`")  # noqa: E501

        self._contact = contact

    @property
    def date_created(self):
        """Gets the date_created of this CardHolderAccount.  # noqa: E501

        The date and time the account was created.  # noqa: E501

        :return: The date_created of this CardHolderAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this CardHolderAccount.

        The date and time the account was created.  # noqa: E501

        :param date_created: The date_created of this CardHolderAccount.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def default_card_id(self):
        """Gets the default_card_id of this CardHolderAccount.  # noqa: E501

        The id of the default card.  # noqa: E501

        :return: The default_card_id of this CardHolderAccount.  # noqa: E501
        :rtype: str
        """
        return self._default_card_id

    @default_card_id.setter
    def default_card_id(self, default_card_id):
        """Sets the default_card_id of this CardHolderAccount.

        The id of the default card.  # noqa: E501

        :param default_card_id: The default_card_id of this CardHolderAccount.  # noqa: E501
        :type: str
        """

        self._default_card_id = default_card_id

    @property
    def default_card_index(self):
        """Gets the default_card_index of this CardHolderAccount.  # noqa: E501

        The index in the array of the default card.  # noqa: E501

        :return: The default_card_index of this CardHolderAccount.  # noqa: E501
        :rtype: int
        """
        return self._default_card_index

    @default_card_index.setter
    def default_card_index(self, default_card_index):
        """Sets the default_card_index of this CardHolderAccount.

        The index in the array of the default card.  # noqa: E501

        :param default_card_index: The default_card_index of this CardHolderAccount.  # noqa: E501
        :type: int
        """

        self._default_card_index = default_card_index

    @property
    def status(self):
        """Gets the status of this CardHolderAccount.  # noqa: E501

        Defines the status of the account for processing valid values are   - ACTIVE for active accounts that are able to process  - DISABLED for accounts that are currently disabled for processing.   # noqa: E501

        :return: The status of this CardHolderAccount.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CardHolderAccount.

        Defines the status of the account for processing valid values are   - ACTIVE for active accounts that are able to process  - DISABLED for accounts that are currently disabled for processing.   # noqa: E501

        :param status: The status of this CardHolderAccount.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def unique_id(self):
        """Gets the unique_id of this CardHolderAccount.  # noqa: E501

        A unique id of the card holder account which uniquely identifies the stored account. This value is not searchable.  # noqa: E501

        :return: The unique_id of this CardHolderAccount.  # noqa: E501
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this CardHolderAccount.

        A unique id of the card holder account which uniquely identifies the stored account. This value is not searchable.  # noqa: E501

        :param unique_id: The unique_id of this CardHolderAccount.  # noqa: E501
        :type: str
        """

        self._unique_id = unique_id

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
        if not isinstance(other, CardHolderAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CardHolderAccount):
            return True

        return self.to_dict() != other.to_dict()
