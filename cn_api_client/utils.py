def _make_url(api_house=None, base_url= None, params=None):
    """
    It builds the url based on the house webservice and parameters
    Args:
        api_house: str:: 'camara' or 'senado'
        webservice: str:: specify a webservice such as 'deputados', '
        params: dict::  parameters that compose the url

    Returns: str
        The API url
    """

    if api_house == None:
        raise ReferenceError ('No API House Specified')

    if base_url == None:
        raise ReferenceError ('No Base Url Specified')

    elif api_house == 'camara':

        # EndPoints
        for i, items in enumerate(params.items()):
            key, value = [_treat_inputs(i) for i in items]

            if value == None:
                value = ''

            base_url += key + '=' + value

            if len(params) - i > 1:

                base_url += '&'

    print(base_url)
    return base_url

def _treat_inputs(value):
    """
    Make sure that inputs are in the right type

    Args:
        value: value input

    Returns:

    """

    if isinstance(value, (int, float)):
        value = str(value)

    return value