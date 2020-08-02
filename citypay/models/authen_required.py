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


class AuthenRequired(object):
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
        'acs_url': 'str',
        'md': 'str',
        'pareq': 'str'
    }

    attribute_map = {
        'acs_url': 'acs_url',
        'md': 'md',
        'pareq': 'pareq'
    }

    def __init__(self, acs_url=None, md=None, pareq=None, local_vars_configuration=None):  # noqa: E501
        """AuthenRequired - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._acs_url = None
        self._md = None
        self._pareq = None
        self.discriminator = None

        if acs_url is not None:
            self.acs_url = acs_url
        if md is not None:
            self.md = md
        if pareq is not None:
            self.pareq = pareq

    @property
    def acs_url(self):
        """Gets the acs_url of this AuthenRequired.  # noqa: E501

        The url of the Access Control Server (ACS) to forward the user to.   # noqa: E501

        :return: The acs_url of this AuthenRequired.  # noqa: E501
        :rtype: str
        """
        return self._acs_url

    @acs_url.setter
    def acs_url(self, acs_url):
        """Sets the acs_url of this AuthenRequired.

        The url of the Access Control Server (ACS) to forward the user to.   # noqa: E501

        :param acs_url: The acs_url of this AuthenRequired.  # noqa: E501
        :type: str
        """

        self._acs_url = acs_url

    @property
    def md(self):
        """Gets the md of this AuthenRequired.  # noqa: E501

        Merchant Data (MD) which should be sent to the ACS to establish and reference the authentication session.   # noqa: E501

        :return: The md of this AuthenRequired.  # noqa: E501
        :rtype: str
        """
        return self._md

    @md.setter
    def md(self, md):
        """Sets the md of this AuthenRequired.

        Merchant Data (MD) which should be sent to the ACS to establish and reference the authentication session.   # noqa: E501

        :param md: The md of this AuthenRequired.  # noqa: E501
        :type: str
        """

        self._md = md

    @property
    def pareq(self):
        """Gets the pareq of this AuthenRequired.  # noqa: E501

        The Payer Authentication Request packet which should be `POSTed` to the Url of the ACS to establish the authentication session. Data should be sent untouched.   # noqa: E501

        :return: The pareq of this AuthenRequired.  # noqa: E501
        :rtype: str
        """
        return self._pareq

    @pareq.setter
    def pareq(self, pareq):
        """Sets the pareq of this AuthenRequired.

        The Payer Authentication Request packet which should be `POSTed` to the Url of the ACS to establish the authentication session. Data should be sent untouched.   # noqa: E501

        :param pareq: The pareq of this AuthenRequired.  # noqa: E501
        :type: str
        """

        self._pareq = pareq

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
        if not isinstance(other, AuthenRequired):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthenRequired):
            return True

        return self.to_dict() != other.to_dict()
