from sanatio.array_validator import ArrayValidator
from sanatio.date_validator import DateValidator
from sanatio.document_validator import DocumentValidator
from sanatio.email_validator import EmailValidator
from sanatio.number_validator import NumberValidator
from sanatio.other_validator import OtherValidator
from sanatio.password_validator import PasswordValidator
from sanatio.string_validator import StringValidator
from sanatio.username_validator import UsernameValidator


class Validator(StringValidator, DocumentValidator, UsernameValidator, NumberValidator, 
                DateValidator, EmailValidator, PasswordValidator, OtherValidator):
    """ Validator class for validating the data """
    def __init__(self):
        super().__init__()