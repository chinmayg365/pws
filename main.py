from dname import *
from gen import *
from get_nmap import *
from ip_address import *
from whois import *
from robots import *
ROOT_Dir = 'companies'
create_directory(ROOT_Dir)


def gather_info(name, url):
    domain_name = get_dname(url)
    ip_address = get_ip(domain_name)
    nmap = gets_nmap('-F', ip_address)
    whois = get_whois(domain_name)
    robo = robots(url)
    create_report(name, url, domain_name, ip_address, nmap, robo, whois)


def create_report(name, fullurl , domain_name, ip_address , nmap , robo , whois ):
    project_dir = ROOT_Dir + '/' + name
    create_directory(project_dir)
    write_file(project_dir+'/full-url.txt',fullurl)
    write_file(project_dir+'/domainname.txt',domain_name)
    write_file(project_dir+'/nmap.txt', nmap)
    write_file(project_dir+'/robots.txt',robo)
    write_file(project_dir+'/whois.txt',whois)

gather_info('yahoo','https://www.yahoo.com')