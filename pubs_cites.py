"""Citation metadata for every entry on the Publications page.

This is the single source of truth for the "Cite" widgets build_pubs.py
inserts into each <li> in pubs.md's rendered output. Entries must appear
in the same order as their corresponding list items in pubs.md.

Author names are given exactly as they appear in the visible citation on
pubs.md (full names or initials) - nothing here is invented, just
reformatted into BibTeX "Last, First" order and abbreviated-initial form
for the plain-text citation.

To add a new publication: add its citation line to pubs.md, then add a
matching add(...) call here in the same position, then run build_pubs.py.
"""
import re

def split_authors(s):
    s = s.strip().rstrip('.').rstrip(',')
    s = s.replace(' and ', ', ')
    parts = [p.strip() for p in s.split(',') if p.strip()]
    return parts

COMPOUND_SURNAMES = ["La Porta", "St. Clair", "St.Clair"]

def split_name(name):
    name = name.strip()
    for surname in COMPOUND_SURNAMES:
        if name.endswith(surname):
            first = name[: -len(surname)].strip()
            return first, surname
    toks = name.split()
    if len(toks) == 1:
        return '', toks[0]
    return ' '.join(toks[:-1]), toks[-1]

def to_bibtex_name(name):
    first, last = split_name(name)
    if not first:
        return last
    return f"{last}, {first}"

def to_plain_name(name):
    first, last = split_name(name)
    if not first:
        return last
    initials = []
    for t in first.split():
        t = t.strip('.')
        initials.append(t[0] + '.')
    return f"{last}, {''.join(initials)}"

def plain_author_list(names):
    plain = [to_plain_name(n) for n in names]
    if len(plain) == 1:
        return plain[0]
    return ', '.join(plain[:-1]) + ', & ' + plain[-1]

def bibtex_author_field(names):
    return ' and '.join(to_bibtex_name(n) for n in names)

entries = []

def add(key, kind, authors_str, title, fields, plain_venue):
    authors = split_authors(authors_str)
    entries.append(dict(key=key, kind=kind, authors=authors, title=title, fields=fields, plain_venue=plain_venue))

# JOURNALS
add('moyer2011scalable', 'article', "Thomas Moyer, Kevin Butler, Joshua Schiffman, Patrick McDaniel, and Trent Jaeger",
    "Scalable Web Content Attestation",
    {"journal": "IEEE Transactions on Computers", "year": "2011"},
    "IEEE Transactions on Computers (2011)")

add('schiffman2011network', 'article', "Joshua Schiffman, Thomas Moyer, Trent Jaeger, and Patrick McDaniel",
    "Network-based Root of Trust for Installation",
    {"journal": "IEEE Security \\& Privacy", "volume": "9", "number": "1", "pages": "40--48", "year": "2011"},
    "IEEE Security & Privacy, 9(1), 40-48 (2011)")

add('muthukumaran2011protecting', 'article', "Divya Muthukumaran, Joshua Schiffman, Mohamed Hassan, Anuj Sawani, Vikhyath Rao, Trent Jaeger",
    "Protecting the Integrity of Trusted Applications in Mobile Phone Systems",
    {"journal": "Security and Communication Networks", "volume": "4", "number": "6", "pages": "633--650", "year": "2011"},
    "Security and Communication Networks, 4(6), 633-650 (2011)")

add('jaeger2010outlook', 'article', "Trent Jaeger and Joshua Schiffman",
    "Outlook: Cloudy with a Chance of Security Challenges and Improvements",
    {"journal": "IEEE Security \\& Privacy", "volume": "8", "number": "1", "pages": "77--80", "year": "2010"},
    "IEEE Security & Privacy, 8(1), 77-80 (2010)")

add('lee2007roundeye', 'article', "Ken C.K. Lee, Joshua Schiffman, Baihua Zheng, Wang-Chien Lee, Hong Va Leong",
    "Round-Eye: A System for Tracking Nearest Surrounders in Moving Object Environments",
    {"journal": "The Journal of Systems and Software", "volume": "80", "pages": "2063--2076", "year": "2007"},
    "The Journal of Systems and Software, 80, 2063-2076 (2007)")

# CONFERENCES
add('laing2022symbolon', 'inproceedings', "Thalia Laing, Eduard Marin, Mark D. Ryan, Joshua Schiffman, and Gaëtan Wattiau",
    "Symbolon: Enabling Flexible Multi-device-based User Authentication",
    {"booktitle": "2022 IEEE Conference on Dependable and Secure Computing (DSC)", "year": "2022"},
    "2022 IEEE Conference on Dependable and Secure Computing (DSC)")

add('sun2015cloudarmor', 'inproceedings', "Yuqiong Sun, Giuseppe Petracca, Trent Jaeger, Hayawardh Vijayakumar, and Joshua Schiffman",
    "CloudArmor: Protecting Cloud Commands from Compromised Cloud Services",
    {"booktitle": "8th IEEE International Conference on Cloud Computing (IEEE CLOUD '15)", "year": "2015"},
    "8th IEEE International Conference on Cloud Computing (IEEE CLOUD '15)")

add('schiffman2013cloudverifier', 'inproceedings', "Joshua Schiffman, Yuqiong Sun, Hayawardh Vijayakumar, and Trent Jaeger",
    "Cloud Verifier: Verifiable Auditing Service for IaaS Clouds",
    {"booktitle": "2013 IEEE Ninth World Congress on Services (SERVICES '13)", "year": "2013"},
    "2013 IEEE Ninth World Congress on Services (SERVICES '13)")

add('vijayakumar2013process', 'inproceedings', "Hayawardh Vijayakumar, Joshua Schiffman, and Trent Jaeger",
    "Process Firewalls: Enforcing Safe Resource Access with Attack-Specific Invariants",
    {"booktitle": "8th ACM European Conference on Computer Systems", "year": "2013"},
    "8th ACM European Conference on Computer Systems (2013)")

add('lorch2013shroud', 'inproceedings', "J. Lorch, B. Parno, J. Mickens, M. Raykova, and J. Schiffman",
    "Shroud: Ensuring Private Access to Large-Scale Data in the Data Center",
    {"booktitle": "11th USENIX Conference on File and Storage Technologies (FAST '13)", "pages": "199--213", "year": "2013"},
    "11th USENIX Conference on File and Storage Technologies (FAST '13), pp. 199-213")

add('vijayakumar2012sting', 'inproceedings', "H. Vijayakumar, J. Schiffman, and T. Jaeger",
    "STING: Finding Name Resolution Vulnerabilities in Programs",
    {"booktitle": "21st USENIX Security Symposium (USENIX Security '12)", "year": "2012"},
    "21st USENIX Security Symposium (USENIX Security '12)")

add('schiffman2012verifying', 'inproceedings', "J. Schiffman, H. Vijayakumar, T. Jaeger",
    "Verifying System Integrity by Proxy",
    {"booktitle": "5th International Conference on Trust and Trustworthy Computing (TRUST 2012)", "year": "2012"},
    "5th International Conference on Trust and Trustworthy Computing (TRUST 2012)")

add('vijayakumar2012integrity', 'inproceedings', "H. Vijayakumar, G. Jakka, S. Rueda, J. Schiffman, and T. Jaeger",
    "Integrity Walls: Finding Attack Surfaces from Mandatory Access Control Policies",
    {"booktitle": "7th ACM Symposium on Information, Computer, and Communications Security (AsiaCCS)", "year": "2012"},
    "7th ACM Symposium on Information, Computer, and Communications Security (AsiaCCS)")

add('vijayakumar2011rose', 'inproceedings', "Hayawardh Vijayakumar, Joshua Schiffman, and Trent Jaeger",
    "A Rose by Any Other Name or an Insane Root? Adventures in Name Resolution",
    {"booktitle": "7th European Conference on Computer Network Defense", "address": "Gothenburg, Sweden", "year": "2011"},
    "7th European Conference on Computer Network Defense, Gothenburg, Sweden (2011)")

add('traynor2010constructing', 'inproceedings', "P. Traynor, J. Schiffman, T. La Porta, P. McDaniel and A. Ghosh",
    "Constructing Secure Localization Systems with Adjustable Granularity",
    {"booktitle": "IEEE Global Communications Conference (GLOBECOM)", "year": "2010"},
    "IEEE Global Communications Conference (GLOBECOM) (2010)")

add('hicks2010architecture', 'inproceedings', "Boniface Hicks, Sandra Rueda, Dave King, Thomas Moyer, Joshua Schiffman, Yogesh Sreenivasan, Patrick McDaniel, and Trent Jaeger",
    "An Architecture for Enforcing End-to-End Access Control Over Web Applications",
    {"booktitle": "15th ACM Symposium on Access Control Models and Technologies (SACMAT)", "year": "2010"},
    "15th ACM Symposium on Access Control Models and Technologies (SACMAT '10)")

add('schiffman2010dauth', 'inproceedings', "Joshua Schiffman, Xinwen Zhang and Simon Gibbs",
    "DAuth: Fine-grained Authorization Delegation for Distributed Web Application Consumers",
    {"booktitle": "2010 IEEE International Symposium on Policies for Distributed Systems and Networks (POLICY '10)", "address": "Washington, DC", "year": "2010"},
    "2010 IEEE International Symposium on Policies for Distributed Systems and Networks (POLICY '10), Washington, DC")

add('schiffman2009justifying', 'inproceedings', "Joshua Schiffman, Thomas Moyer, Christopher Shal, Trent Jaeger, and Patrick McDaniel",
    "Justifying Integrity Using a Virtual Machine Verifier",
    {"booktitle": "Annual Computer Security Applications Conference (ACSAC '09)", "address": "Honolulu, HI", "year": "2009"},
    "Annual Computer Security Applications Conference (ACSAC '09), Honolulu, HI")

add('moyer2009scalable', 'inproceedings', "Thomas Moyer, Kevin Butler, Joshua Schiffman, Patrick McDaniel, and Trent Jaeger",
    "Scalable Web Content Attestation",
    {"booktitle": "Annual Computer Security Applications Conference (ACSAC '09)", "address": "Honolulu, HI", "year": "2009"},
    "Annual Computer Security Applications Conference (ACSAC '09), Honolulu, HI")

add('lee2008validscope', 'inproceedings', "Ken C. K. Lee, Josh Schiffman, Baihua Zheng, Wang-chien Lee",
    "Valid Scope Computation for Location-Dependent Spatial Query in Mobile Broadcast Environments",
    {"booktitle": "17th ACM Conference on Information and Knowledge Management (CIKM)", "year": "2008"},
    "17th ACM Conference on Information and Knowledge Management (CIKM '08)")

add('muthukumaran2008measuring', 'inproceedings', "Divya Muthukumaran, Anuj Sawani, Joshua Schiffman, Brian M. Jung, Trent Jaeger",
    "Measuring Integrity on Mobile Phone Systems",
    {"booktitle": "13th ACM Symposium on Access Control Models and Technologies (SACMAT '08)", "year": "2008"},
    "13th ACM Symposium on Access Control Models and Technologies (SACMAT '08)")

add('stclair2007establishing', 'inproceedings', "Luke St.Clair, Joshua Schiffman, Trent Jaeger, and Patrick McDaniel",
    "Establishing and Sustaining System Integrity via Root of Trust Installation",
    {"booktitle": "23rd Annual Computer Security Applications Conference (ACSAC '07)", "year": "2007"},
    "23rd Annual Computer Security Applications Conference (ACSAC '07)")

add('lee2006tracking', 'inproceedings', "Ken C. K. Lee, Josh Schiffman, Baihua Zheng, Wang-Chien Lee and Hong Va Leong",
    "Tracking Nearest Surrounders in Moving Object Environments",
    {"booktitle": "IEEE International Conference on Pervasive Services", "year": "2006"},
    "IEEE International Conference on Pervasive Services (2006)")

# WORKSHOPS
add('schiffman2014smm', 'inproceedings', "Joshua Schiffman and David Kaplan",
    "The SMM Rootkit Revisited: Fun with USB",
    {"booktitle": "2nd International Workshop on Emerging Cyberthreats and Countermeasures (ECTCM '14)", "year": "2014"},
    "2nd International Workshop on Emerging Cyberthreats and Countermeasures (ECTCM '14)")

add('schiffman2010seeding', 'inproceedings', "Joshua Schiffman, Thomas Moyer, Hayawardh Vijayakumar, Trent Jaeger, Patrick McDaniel",
    "Seeding Clouds with Trust Anchors",
    {"booktitle": "2010 ACM Workshop on Cloud Computing Security Workshop (CCSW '10)", "year": "2010"},
    "2010 ACM Workshop on Cloud Computing Security Workshop (CCSW '10)")

add('zhang2009securing', 'inproceedings', "Xinwen Zhang, Joshua Schiffman, Simon Gibbs, Anugeetha Kunjithapatham, and Sangoh Jeong",
    "Securing Elastic Applications on Mobile Devices for Cloud Computing",
    {"booktitle": "1st ACM Cloud Computing Security Workshop (CCSW '09)", "year": "2009"},
    "1st ACM Cloud Computing Security Workshop (CCSW '09)")

add('enck2007protecting', 'inproceedings', "William Enck, Sandra Rueda, Yogesh Sreenivasan, Joshua Schiffman, Luke St. Clair, Trent Jaeger, and Patrick McDaniel",
    "Protecting Users from 'Themselves'",
    {"booktitle": "1st ACM Computer Security Architectures Workshop (CSAW '07)", "address": "Alexandria, VA", "year": "2007"},
    "1st ACM Computer Security Architectures Workshop (CSAW '07), Alexandria, VA")

# MISC
add('schiffman2010usenixreport', 'misc', "Joshua Schiffman",
    "19th USENIX Security Symposium Conference Summaries",
    {"howpublished": "USENIX ;login: Magazine", "year": "2010"},
    "USENIX ;login: Magazine (December 2010)")

add('schiffman2008usenixreport', 'misc', "Joshua Schiffman",
    "17th USENIX Security Symposium Conference Summaries",
    {"howpublished": "USENIX ;login: Magazine", "year": "2008"},
    "USENIX ;login: Magazine (December 2008)")

# TECH REPORT
add('butler2009firma', 'techreport', "Kevin Butler, Stephen McLaughlin, Thomas Moyer, Joshua Schiffman, Patrick McDaniel, and Trent Jaeger",
    "Firma: Disk-Based Foundations for Trusted Operating Systems",
    {"institution": "Networking and Security Research Center, Pennsylvania State University", "number": "NAS-TR-0114-2009", "year": "2009"},
    "Technical Report NAS-TR-0114-2009, Pennsylvania State University (2009)")


def render_bibtex(e):
    lines = [f"@{e['kind']}{{{e['key']},"]
    lines.append(f"  author = {{{bibtex_author_field(e['authors'])}}},")
    lines.append(f"  title  = {{{e['title']}}},")
    for k, v in e['fields'].items():
        lines.append(f"  {k} = {{{v}}},")
    lines.append("}")
    return "\n".join(lines)


def render_plain(e):
    authors = plain_author_list(e['authors'])
    venue = re.sub(r'\s*\(\d{4}\)\s*$', '', e['plain_venue']).rstrip('.')
    return f"{authors} ({e['fields'].get('year')}). {e['title']}. {venue}."
