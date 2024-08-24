import requests
from bs4 import BeautifulSoup

def scrape():
    url = 'https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    res = []
    variables = soup.find_all('tr')
    for variable in variables:
        tdvariable = variable.find('td')
        if tdvariable is not None:
            res.append(tdvariable.text)
    print(res)
    return res
    
""" if __name__ == '__main__':
    scrape() """

def jscrape():
    url = 'https://archive.ics.uci.edu/api/trpc/donated_datasets.findById,keywords.findByDatasetId,variables.findTableByDatasetId,variableInfo.findTupleByDatasetId,edits.findByDatasetId,creators.findByDatasetId,descriptive.findTupleByDatasetId,evals.findByDatasetId,citation.findByDatasetId,notes.findByDatasetId,papers.findByDatasetId,papers.findSummariesByDatasetId,donated_datasets.names,reviews.findByDatasetId,python.findRequestById,users.findById,citation.findCitationRequests?batch=1&input=%7B%220%22%3A%7B%22json%22%3A17%7D%2C%221%22%3A%7B%22json%22%3A17%7D%2C%222%22%3A%7B%22json%22%3A17%7D%2C%223%22%3A%7B%22json%22%3A17%7D%2C%224%22%3A%7B%22json%22%3A%7B%22datasetID%22%3A17%7D%7D%2C%225%22%3A%7B%22json%22%3A17%7D%2C%226%22%3A%7B%22json%22%3A17%7D%2C%227%22%3A%7B%22json%22%3A17%7D%2C%228%22%3A%7B%22json%22%3A17%7D%2C%229%22%3A%7B%22json%22%3A17%7D%2C%2210%22%3A%7B%22json%22%3A17%7D%2C%2211%22%3A%7B%22json%22%3A%7B%22datasetID%22%3A17%2C%22skip%22%3A0%2C%22take%22%3A5%2C%22orderBy%22%3A%22year%22%2C%22sort%22%3A%22desc%22%7D%7D%2C%2212%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%2C%2213%22%3A%7B%22json%22%3A17%7D%2C%2214%22%3A%7B%22json%22%3A17%7D%2C%2215%22%3A%7B%22json%22%3A1%7D%2C%2216%22%3A%7B%22json%22%3A17%7D%7D'
    response = requests.get(url)
    data = response.json()
    variables = data[0]['result']['data']['json']['variables']

    res = []
    for variable in variables:
        res.append(variable['name'])
    print(res)
    return res

jscrape()

""" def scrape():
    url = 'vhttps://archive.ics.uci.edu/api/trpc/donated_datasets.findById,keywords.findByDatasetId,variables.findTableByDatasetId,variableInfo.findTupleByDatasetId,edits.findByDatasetId,creators.findByDatasetId,descriptive.findTupleByDatasetId,evals.findByDatasetId,citation.findByDatasetId,notes.findByDatasetId,papers.findByDatasetId,papers.findSummariesByDatasetId,donated_datasets.names,reviews.findByDatasetId,python.findRequestById,users.findById,citation.findCitationRequests?batch=1&input=%7B%220%22%3A%7B%22json%22%3A17%7D%2C%221%22%3A%7B%22json%22%3A17%7D%2C%222%22%3A%7B%22json%22%3A17%7D%2C%223%22%3A%7B%22json%22%3A17%7D%2C%224%22%3A%7B%22json%22%3A%7B%22datasetID%22%3A17%7D%7D%2C%225%22%3A%7B%22json%22%3A17%7D%2C%226%22%3A%7B%22json%22%3A17%7D%2C%227%22%3A%7B%22json%22%3A17%7D%2C%228%22%3A%7B%22json%22%3A17%7D%2C%229%22%3A%7B%22json%22%3A17%7D%2C%2210%22%3A%7B%22json%22%3A17%7D%2C%2211%22%3A%7B%22json%22%3A%7B%22datasetID%22%3A17%2C%22skip%22%3A0%2C%22take%22%3A5%2C%22orderBy%22%3A%22year%22%2C%22sort%22%3A%22desc%22%7D%7D%2C%2212%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%2C%2213%22%3A%7B%22json%22%3A17%7D%2C%2214%22%3A%7B%22json%22%3A17%7D%2C%2215%22%3A%7B%22json%22%3A1%7D%2C%2216%22%3A%7B%22json%22%3A17%7D%7D'
    response = requests.get(url)

    data = response.json()

    print(data)


scrape()
 """