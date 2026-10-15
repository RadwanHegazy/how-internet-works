"""

google.com

tld name : com
domain name : google 

"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Domain :
    name : str
    ipv4 : str


@dataclass
class TLD :
    name : str
    domains : list[Domain]


class RootServer :

    def __init__(self, tld_group : list[TLD]):
        self.tld_group = tld_group

    def search_tld (self, tld_name : str) -> Optional[TLD] :  
        for tld in self.tld_group:
            if tld.name == tld_name :
                return tld

        return None


class TLDServer :

    def __init__(self, tld : TLD):
        self.tld = tld

    def get_domain_by_name(self, domain_name) -> Optional[Domain] : 
        for domain in self.tld.domains:
            if domain.name == domain_name:
                return domain

        return None


class DNS :

    def __init__(self, root_server : RootServer):
        self.root_server = root_server

    def search (self, full_domain_name : str) -> Optional[Domain]: 
        domain_name, tld_name = full_domain_name.split('.', maxsplit=1)

        tld = self.root_server.search_tld(tld_name)

        if not tld:
            return None

        tld_server = TLDServer(tld)
        domain = tld_server.get_domain_by_name(domain_name)

        return domain


root_server = RootServer(
    tld_group=[
        TLD(
            name='com',
            domains=[
                Domain(
                    name="google",
                    ipv4="127.0.0.1"
                ),
                Domain(
                    name="facebook",
                    ipv4="127.0.0.1"
                ),
            ]
        ),
        TLD(
            name='org',
            domains=[
                Domain(
                    name='python',
                    ipv4='2.2.2.3'
                )
            ]
        )
    ]
)


if __name__ == "__main__" : 
    dns = DNS(root_server)
    domain_name = 'test.com'
    domain = dns.search(full_domain_name=domain_name)

    if domain:
        print(f"[+] IP For {domain_name} is : {domain.ipv4}")
    else:
        print(f"[-] This Domain Not Exists")

