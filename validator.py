def validator(data: dict):
    """Функция, собирающая ошибки"""
    err = []

    if not data.get('recommend_item'):
        err.append('error_bad_request')
    if len(data.keys()) > 1:
        if not data.get("prob_threshold"):
            err.append("error_wrong_threshold_key")
    return err