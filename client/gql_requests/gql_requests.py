
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
