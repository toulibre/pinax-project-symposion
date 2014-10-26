from django.core.exceptions import ValidationError

def validate_3_plus_4(value):
    if value != 7:
        raise ValidationError(u"Erreur sur le champs anti-robot")
