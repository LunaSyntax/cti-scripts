import requests

from time import sleep

cve_list = []
base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def get_info(cve_id):
    url = f"{base_url}?cveId={cve_id}"
    response = requests.get(url)

    ''' No API Key '''
    print(cve_id)
    if "cvssMetricV31" in response.json().get("vulnerabilities")[0].get('cve').get('metrics'):
        print(response.json().get("vulnerabilities")[0].get('cve').get('metrics').get('cvssMetricV31')[0].get('cvssData').get('vectorString'))
        print(response.json().get("vulnerabilities")[0].get('cve').get('metrics').get('cvssMetricV31')[0].get('cvssData').get('baseScore'))
        print(response.json().get("vulnerabilities")[0].get('cve').get('weaknesses')[0].get('description')[0].get('value'))
    else:
        print(response.json().get("vulnerabilities")[0].get('cve').get('metrics').get('cvssMetricV30')[0].get('cvssData').get('vectorString'))
        print(response.json().get("vulnerabilities")[0].get('cve').get('metrics').get('cvssMetricV30')[0].get('cvssData').get('baseScore'))
        print(response.json().get("vulnerabilities")[0].get('cve').get('weaknesses')[0].get('description')[0].get('value'))
    
    print()
    sleep(6)

for cve in cve_list:
    get_info(cve)