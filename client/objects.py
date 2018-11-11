class Structure(object):

    _fields = []

    def _init_arg(self, expected_type, value):
        if value is None:
            return None
        elif isinstance(value, expected_type):
            return value
        elif isinstance(value, list) and not isinstance(expected_type, list):
            return [expected_type(**obj) for obj in value]
        else:
            return expected_type(**value)

    def __init__(self, **kwargs):
        self._verbose = False

        field_names, field_types = zip(*self._fields)
        assert([isinstance(name, str) for name in field_names])
        assert([isinstance(type_, type) for type_ in field_types])

        for name, field_type in self._fields:
            try:
                setattr(self, name, self._init_arg(
                    field_type, kwargs.pop(name)))
            except KeyError:
                if self._verbose:
                    print("could not find attribute %s" % name)

        # Check for any remaining unknown arguments
        if self._verbose and kwargs:
            print('Invalid arguments(s): {}'.format(','.join(kwargs)))


class Attribute(Structure):
    _fields = [
        ("label", str),
        ("description", str),
        ("dataunit", str),
        ('datatype', str),
        ('id', str),
    ]


class Object(Structure):
    _fields = [
        ("label", str),
        ("description", str),
        ("attributes", Attribute),
        ('id', str),
    ]


Attribute._fields.append(("object", Object))


class Schema(Structure):
    _fields = [
        ("label", str),
        ("description", str),
        ("objects", Object),
        ("url", str),
        ('id', str),
    ]


Object._fields.append(("schema", Schema))


class DateTimeAttributeInstance(Structure):
    _fields = [
        ('base', Attribute),
        ('value', str),
    ]


class FloatAttributeInstance(Structure):
    _fields = [
        ('base', Attribute),
        ('value', float),
    ]


class ObjectInstance(Structure):
    _fields = [
        ('base', Object),
        ("floatAttributes", FloatAttributeInstance),
        ('datetimeAttributes', DateTimeAttributeInstance),
        ('id', str),
    ]
