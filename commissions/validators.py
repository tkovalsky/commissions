from django.core.exceptions import ValidationError

def validate_content(value):
    fieldA = value
    if fieldA == <some logic>
        raise ValidationError("Error Message to display")
    return value
