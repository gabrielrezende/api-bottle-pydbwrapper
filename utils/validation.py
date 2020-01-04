def required_fields(json, *fields):
    errors = []
    for field in fields:
        if field not in json or json[field] == '':
            errors.append(field)
    if not errors:
        return
    if len(errors) > 2:
        message = 'Os campos {} e {} são obrigatórios.'.format(', '.join(errors[:-1]), errors[-1])
    elif len(errors) == 2:
        message = 'Os campos {} e {} são obrigatório.'.format(errors[0], errors[1])
    elif len(errors) == 1:
        message = 'O campo {} é obrigatório.'.format(errors[0])
    raise ValueError(message)
