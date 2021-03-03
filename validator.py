def validator(data: dict):
    """Функция, собирающая ошибки"""
    err = []
    if not data.get('recommend_item'):
        err.append('error_bad_request')
    return err