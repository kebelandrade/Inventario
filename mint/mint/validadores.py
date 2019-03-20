from django.core.exceptions import ValidationError


def validar_alfa(valor):
    if not valor.isalpha():
        raise ValidationError("El campo solo puede contener datos alfabeticos")
