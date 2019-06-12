import six


def create_transports(transports, valid_transports):
    if not transports:
        return [create_transport_pair(t) for t in valid_transports]

    if isinstance(transports, six.string_types):
        transports = [transports]
    result = [
        (transport_name, transport_options)
        for transport in transports
        for (transport_name, transport_options) in (create_transport_pair(transport),)
        if transport_name in valid_transports
    ]
    if not result:
        raise ValueError('No valid transports provided')
    return result


def create_transport_pair(data):
    if isinstance(data, tuple) and len(data) == 2 and isinstance(data[0], six.string_types):
        return data
    if isinstance(data, six.string_types):
        return data, None
    else:
        raise ValueError('No valid transport provided: %r; expected name or (name, options dict)', data)
