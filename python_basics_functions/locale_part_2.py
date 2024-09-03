import re


def extract_region(locale):
    country = re.split(r"[\W_+]", locale)
    return country[1]


print(extract_region("en_US.UTF-8"))  # US
print(extract_region("en_GB.UTF-8"))  # GB
print(extract_region("ko_KR.UTF-16"))  # KR
