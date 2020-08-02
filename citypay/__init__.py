# coding: utf-8

# flake8: noqa

"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security <aside class=\"notice\">   Before we begin a reminder that your application will need to adhere to PCI-DSS standards to operate safely   and to meet requirements set out by Visa and MasterCard and the PCI Security Standards Council including: </aside>  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities.   # noqa: E501

    The version of the OpenAPI document: 6.0.0
    Contact: support@citypay.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.1"

# import apis into sdk package
from citypay.api.card_holder_account_api import CardHolderAccountApi
from citypay.api.operational_api import OperationalApi
from citypay.api.payment_processing_api import PaymentProcessingApi

# import ApiClient
from citypay.api_client import ApiClient
from citypay.configuration import Configuration
from citypay.exceptions import OpenApiException
from citypay.exceptions import ApiTypeError
from citypay.exceptions import ApiValueError
from citypay.exceptions import ApiKeyError
from citypay.exceptions import ApiAttributeError
from citypay.exceptions import ApiException
# import models into sdk package
from citypay.models.account_create import AccountCreate
from citypay.models.account_status import AccountStatus
from citypay.models.acknowledgement import Acknowledgement
from citypay.models.airline_advice import AirlineAdvice
from citypay.models.airline_segment import AirlineSegment
from citypay.models.auth_reference import AuthReference
from citypay.models.auth_references import AuthReferences
from citypay.models.auth_request import AuthRequest
from citypay.models.auth_response import AuthResponse
from citypay.models.authen_required import AuthenRequired
from citypay.models.c_res_auth_request import CResAuthRequest
from citypay.models.capture_request import CaptureRequest
from citypay.models.card import Card
from citypay.models.card_holder_account import CardHolderAccount
from citypay.models.card_status import CardStatus
from citypay.models.charge_request import ChargeRequest
from citypay.models.contact_details import ContactDetails
from citypay.models.decision import Decision
from citypay.models.error import Error
from citypay.models.external_mpi import ExternalMPI
from citypay.models.list_merchants_response import ListMerchantsResponse
from citypay.models.mcc6012 import MCC6012
from citypay.models.merchant import Merchant
from citypay.models.pa_res_auth_request import PaResAuthRequest
from citypay.models.ping import Ping
from citypay.models.register_card import RegisterCard
from citypay.models.request_challenged import RequestChallenged
from citypay.models.retrieve_request import RetrieveRequest
from citypay.models.three_d_secure import ThreeDSecure
from citypay.models.void_request import VoidRequest

from citypay.models.api_key import api_key_generate
