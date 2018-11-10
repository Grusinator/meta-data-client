class Structure(object):

    _fields = []

    def _init_arg(self, expected_type, value):
        if isinstance(value, expected_type):
            return value
        elif isinstance(value, list) and not isinstance(expected_type, list):
            return [expected_type(**obj) for obj in value]
        else:
            return expected_type(**value)

    def __init__(self, **kwargs):
        field_names, field_types = zip(*self._fields)
        assert([isinstance(name, str) for name in field_names])
        assert([isinstance(type_, type) for type_ in field_types])

        for name, field_type in self._fields:
            try:
                setattr(self, name, self._init_arg(
                    field_type, kwargs.pop(name)))
            except KeyError:
                print("could not find attribute %s" % name)

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError(
                'Invalid arguments(s): {}'.format(','.join(kwargs)))


class base(Structure):
    _fields = [
        ('label', str),
    ]


class DateTimeAttributeInstance(Structure):
    _fields = [
        ('base', base),
        ('value', str),
    ]


class FloatAttributeInstance(Structure):
    _fields = [
        ('base', base),
        ('value', float),
    ]


class ObjectInstance(Structure):
    _fields = [
        ('base', base),
        ("floatAttributes", FloatAttributeInstance),
        ('datetimeAttributes', DateTimeAttributeInstance),
        ('id', str), ]
