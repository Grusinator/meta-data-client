
class GqlRequests:
    get_user_info = """
        query userqueue{
            profile{
                language
                birthdate
                audioThreshold
                user {
                    username
                    email
                    lastName
                    firstName
                }
            }
        }
        """

    get_all_instances = """
        {
        allObjectInstances(base_Label: {{object_label}}) {
            edges {
            node {
                id
                base {
                label
                }
                floatAttributes(base_Label: {{float_label}}) {
                edges {
                    node {
                    value
                    base{
                        label
                    }
                    }
                }
                }
                datetimeAttributes(base_Label: {{datetime_label}}){
                edges{
                    node{
                    value
                    base{
                        label
                    }
                    }
                }
                }
            }
            }
        }
        }
        """

    identify_data_from_provider = """
        mutation{identifyDataFromProvider(providerName:{{provider_name}}, endpoint: {{endpoint}}){
            rdfDumpUrl
        }
        }
    """

    export_schema_to_rdf = """
    mutation {
        exportSchema(schemaLabel: {{schema_label}}) {
            schemaFileUrl
            visualizationUrl
            }
        }
    """

    get_all_objects = """
    query{allObjects(schema_Label: {{schema_label}}){
    edges{
        node{
        label
        id
        description
        attributes{
            edges{
            node{
                id
                label
                description
                datatype
                dataunit
            }
            }
        }
        }
    }
    }
    }
    """
