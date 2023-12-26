from django.db.models import ManyToManyField

def get_field_values(instance):
  field_values = {}
  fields = instance._meta.get_fields(include_hidden=True)

  for field in fields:
    try:
      if isinstance(field, ManyToManyField):
        # If the field is a many-to-many field, get all related objects
        related_objects = getattr(instance, field.name).all()
        field_values[field.name] = ", ".join(
          str(obj) for obj in related_objects
        )
        continue

      field_values[field.name] = getattr(instance, field.name)

    except Exception:
      pass

  return field_values
