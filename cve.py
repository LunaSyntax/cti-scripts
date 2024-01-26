import requests

from time import sleep
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

cve_list = ['CVE-2022-45868','CVE-2020-36518','CVE-2022-42004']
base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def get_info(cve_id, number):
    url = f"{base_url}?cveId={cve_id}"
    response = requests.get(url)

    ''' No API Key '''
    sheet[f"A{number}"] = f"{cve_id}"
    if "cvssMetricV31" in response.json().get("vulnerabilities")[0].get('cve').get('metrics'):
        sheet[f"B{number}"] = response.json().get("vulnerabilities")[0].get('cve').get('metrics').get('cvssMetricV31')[0].get('cvssData').get('vectorString')
        sheet[f"C{number}"] = response.json().get("vulnerabilities")[0].get('cve').get('metrics').get('cvssMetricV31')[0].get('cvssData').get('baseScore')
        sheet[f"D{number}"] = response.json().get("vulnerabilities")[0].get('cve').get('weaknesses')[0].get('description')[0].get('value')
    else:
        sheet[f"B{number}"] = response.json().get("vulnerabilities")[0].get('cve').get('metrics').get('cvssMetricV30')[0].get('cvssData').get('vectorString')
        sheet[f"C{number}"] = response.json().get("vulnerabilities")[0].get('cve').get('metrics').get('cvssMetricV30')[0].get('cvssData').get('baseScore')
        sheet[f"D{number}"] = response.json().get("vulnerabilities")[0].get('cve').get('weaknesses')[0].get('description')[0].get('value')
    
    print()
    sleep(6)

i = 0

for cve in cve_list:
    i += 1
    get_info(cve, i)

workbook.save(filename="cev.xlsx")