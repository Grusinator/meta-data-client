from .objects import *


class CreateInstances():

    def __init__(self, *args, **kwargs):
        self.created_list = []

    def _iterate_create_instances(self, input_data):
        if input_data is None:
            return
        if isinstance(input_data, list):

            cleaned_list = []
            for elm in input_data:
                if isinstance(elm, dict):
                    if "node" in elm.keys():
                        elm = elm["node"]

                elm = self._iterate_create_instances(elm)
                cleaned_list.append(elm)

            return cleaned_list

        elif isinstance(input_data, dict):
            for key, value in input_data.items():

                meta_type = None
                # if any edges appear skip one level
                if isinstance(value, list):
                    if "object" in key.lower():
                        meta_type = ObjectInstance
                    elif "attribute" in key.lower():
                        meta_type = AttributeInstance

                input_data[key] = self._iterate_create_instances(value)

        return input_data

    def create_instances(self, data):

        instances = self.iterate_create_instances(data)
        return instances
