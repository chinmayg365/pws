from tld import get_tld


def get_dname(url):
    dname=get_tld(url)
    return str(dname)

