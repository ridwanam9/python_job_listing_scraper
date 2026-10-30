import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
response = requests.get(url)
print(response)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())  # prints well-formatted HTML


job_titles = soup.find_all('h2', class_='title is-5')
company_names = soup.find_all('h3', class_='subtitle is-6 company')
locations = soup.find_all('p', class_='location')
# job_urls = soup.find_all('a', class_='card-footer-item')
job_urls = soup.find_all('a', body_ = '')

# print('Job Titles')
# number = 1
# for job_title in job_titles:
#     print(f"{number} : {job_title.text}")
#     number += 1

# print('-'*30)
# print('company_names')
# number = 1
# for company_name in company_names:
#     print(f"{number} : {company_name.text}")
#     number += 1

# print('-'*30)
# print('locations')
# number = 1
# for location in locations:
#     print(f"{number} : {location.text}")
#     number += 1


print('-'*30)
print('job_urls')
number = 1
for job_url in job_urls:
    href = job_url.get('href')
    print(f"{number} : {href}")
    number += 1

