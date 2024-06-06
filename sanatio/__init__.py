from sanatio.array_validator import ArrayValidator
from sanatio.date_validator import DateValidator
from sanatio.document_validator import DocumentValidator
from sanatio.email_validator import EmailValidator
from sanatio.number_validator import NumberValidator
from sanatio.other_validator import OtherValidator
from sanatio.password_validator import PasswordValidator
from sanatio.string_validator import StringValidator
from sanatio.username_validator import UsernameValidator
from sanatio.file_validator import FileValidator
from warnings import warn


class Sanatio(ArrayValidator,
              DateValidator,
              DocumentValidator,
              EmailValidator,
              NumberValidator,
              OtherValidator,
              PasswordValidator,
              StringValidator,
              UsernameValidator,
              FileValidator):
    """ Sanatio class for validating the data """
    def __init__(self):
        super().__init__()


class Validator(Sanatio):
    """ Validator class for validating the data """
    def __init__(self):
        warn("Validator class is deprecated, use Sanatio class instead", DeprecationWarning)
