import re
import string

LICENSE_PLATE_RE = [
    re.compile("^([a-zA-Z]{2})([\d]{2})([\d]{2})$"), # 1 XX-99-99 11
    re.compile("^([\d]{2})([\d]{2})([a-zA-Z]{2})$"), # 2 99-99-XX 12
    re.compile("^([\d]{2})([a-zA-Z]{2})([\d]{2})$"), # 3 99-XX-99
    re.compile("^([a-zA-Z]{2})([\d]{2})([a-zA-Z]{2})$"), # 4 XX-99-XX
    re.compile("^([a-zA-Z]{2})([a-zA-Z]{2})([\d]{2})$"), # 5 XX-XX-99
    re.compile("^([\d]{2})([a-zA-Z]{2})([a-zA-Z]{2})$"), # 6 99-XX-XX
    re.compile("^([\d]{2})([a-zA-Z]{3})([\d]{1})$"), # 7 99-XXX-9
    re.compile("^([\d]{1})([a-zA-Z]{3})([\d]{2})$"), # 8 9-XXX-99
    re.compile("^([a-zA-Z]{2})([\d]{3})([a-zA-Z]{1})$"), # 9 XX-999-X 19
    re.compile("^([a-zA-Z]{1})([\d]{3})([a-zA-Z]{2})$"), # 10 X-999-XX
    re.compile("^(CD[ABFJNST][0-9]{1,3})$") # 11 license plate for diplomats
]

class LicensePlate():
    def __init__(self, number):
        self.normalized = re.sub('-', '', number.upper())

        for r in LICENSE_PLATE_RE:
            match = r.match(self.normalized)
            if match:
                self.formatted = string.join(match.groups(), '-')
                return None

        raise ValueError('Not a valid license plate')

    def __str__(self):
        return self.formatted
