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


class ExternalMPI(object):
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
        'authen_result': 'str',
        'cavv': 'str',
        'eci': 'int',
        'enrolled': 'str',
        'xid': 'str'
    }

    attribute_map = {
        'authen_result': 'authen_result',
        'cavv': 'cavv',
        'eci': 'eci',
        'enrolled': 'enrolled',
        'xid': 'xid'
    }

    def __init__(self, authen_result=None, cavv=None, eci=None, enrolled=None, xid=None, local_vars_configuration=None):  # noqa: E501
        """ExternalMPI - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authen_result = None
        self._cavv = None
        self._eci = None
        self._enrolled = None
        self._xid = None
        self.discriminator = None

        if authen_result is not None:
            self.authen_result = authen_result
        if cavv is not None:
            self.cavv = cavv
        if eci is not None:
            self.eci = eci
        if enrolled is not None:
            self.enrolled = enrolled
        if xid is not None:
            self.xid = xid

    @property
    def authen_result(self):
        """Gets the authen_result of this ExternalMPI.  # noqa: E501

        The authentication result available from the MPI.  # noqa: E501

        :return: The authen_result of this ExternalMPI.  # noqa: E501
        :rtype: str
        """
        return self._authen_result

    @authen_result.setter
    def authen_result(self, authen_result):
        """Sets the authen_result of this ExternalMPI.

        The authentication result available from the MPI.  # noqa: E501

        :param authen_result: The authen_result of this ExternalMPI.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                authen_result is not None and len(authen_result) > 1):
            raise ValueError("Invalid value for `authen_result`, length must be less than or equal to `1`")  # noqa: E501

        self._authen_result = authen_result

    @property
    def cavv(self):
        """Gets the cavv of this ExternalMPI.  # noqa: E501

        A value determining the cardholder verification value supplied by the card scheme.  # noqa: E501

        :return: The cavv of this ExternalMPI.  # noqa: E501
        :rtype: str
        """
        return self._cavv

    @cavv.setter
    def cavv(self, cavv):
        """Sets the cavv of this ExternalMPI.

        A value determining the cardholder verification value supplied by the card scheme.  # noqa: E501

        :param cavv: The cavv of this ExternalMPI.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cavv is not None and len(cavv) > 20):
            raise ValueError("Invalid value for `cavv`, length must be less than or equal to `20`")  # noqa: E501

        self._cavv = cavv

    @property
    def eci(self):
        """Gets the eci of this ExternalMPI.  # noqa: E501

        The obtained e-commerce indicator from the MPI.  # noqa: E501

        :return: The eci of this ExternalMPI.  # noqa: E501
        :rtype: int
        """
        return self._eci

    @eci.setter
    def eci(self, eci):
        """Sets the eci of this ExternalMPI.

        The obtained e-commerce indicator from the MPI.  # noqa: E501

        :param eci: The eci of this ExternalMPI.  # noqa: E501
        :type: int
        """

        self._eci = eci

    @property
    def enrolled(self):
        """Gets the enrolled of this ExternalMPI.  # noqa: E501

        A value determining whether the card holder was enrolled.  # noqa: E501

        :return: The enrolled of this ExternalMPI.  # noqa: E501
        :rtype: str
        """
        return self._enrolled

    @enrolled.setter
    def enrolled(self, enrolled):
        """Sets the enrolled of this ExternalMPI.

        A value determining whether the card holder was enrolled.  # noqa: E501

        :param enrolled: The enrolled of this ExternalMPI.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                enrolled is not None and len(enrolled) > 1):
            raise ValueError("Invalid value for `enrolled`, length must be less than or equal to `1`")  # noqa: E501

        self._enrolled = enrolled

    @property
    def xid(self):
        """Gets the xid of this ExternalMPI.  # noqa: E501

        The XID used for processing with the MPI.  # noqa: E501

        :return: The xid of this ExternalMPI.  # noqa: E501
        :rtype: str
        """
        return self._xid

    @xid.setter
    def xid(self, xid):
        """Sets the xid of this ExternalMPI.

        The XID used for processing with the MPI.  # noqa: E501

        :param xid: The xid of this ExternalMPI.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                xid is not None and len(xid) > 20):
            raise ValueError("Invalid value for `xid`, length must be less than or equal to `20`")  # noqa: E501

        self._xid = xid

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
        if not isinstance(other, ExternalMPI):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalMPI):
            return True

        return self.to_dict() != other.to_dict()
