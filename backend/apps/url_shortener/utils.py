import requests


def check_request(url: str):
    """
    Utility function to check the status code of a URL. All responses not 200 are false.
    :param url:
    :return bool:
    """
    r = requests.get(url)

    if r.status_code == 200:
        return True
    else:
        return False
