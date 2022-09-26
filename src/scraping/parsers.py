import requests
import codecs
from bs4 import BeautifulSoup as BS
import random

__all__ = ('work', 'djinni')

headers =   {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            }




def work(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://www.work.ua'
    # url = 'https://www.work.ua/jobs-kyiv-python/'
    # url='https://krasnoyarsk.hh.ru/search/vacancy?text=python&from=suggest_post&area=54'

    if url:

        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='pjax-job-list')
            if main_div:

                div_list = main_div.find_all('div', attrs={'class': 'job-link'})
                for div in div_list:
                    title = div.find('h2')
                    href = title.a['href']
                    content = div.p.text
                    company = 'No name'
                    logo = div.find('img')
                    if logo:
                        company = logo['alt']
                    jobs.append({'title': title.text, 'url': domain + href, 'description': content, 'company': company,
                                 'city_id':city, 'language_id':language})

            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page not response"})
    return jobs, errors


# def rabota(url):
#     jobs = []
#     errors = []
#     domain = 'https://rabota.ua'
#     # url = 'https://www.work.ua/jobs-kyiv-python/'
#     # url='https://krasnoyarsk.hh.ru/search/vacancy?text=python&from=suggest_post&area=54'
#
#     resp = requests.get(url, headers=headers)
#     if resp.status_code == 200:
#         soup = BS(resp.content, 'html.parser')
#         table = soup.find('div', id='pjax-job-list')
#         if table:
#
#             div_list = table.find_all('div', attrs={'class': 'job-link'})
#             for div in div_list:
#                 title = div.find('h2')
#                 href = title.a['href']
#                 content = div.p.text
#                 company = 'No name'
#                 logo = div.find('img')
#                 if logo:
#                     company = logo['alt']
#                 jobs.append({'title': title.text, 'url': domain + href, 'description': content, 'company': company})
#
#         else:
#             errors.append({'url': url, 'title': "Table does not exists"})
#     else:
#         errors.append({'url': url, 'title': "Page not response"})
#     return jobs, errors


def djinni(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://djinni.co'
    # url='https://krasnoyarsk.hh.ru/search/vacancy?text=python&from=suggest_post&area=54'

    if url:

        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_ul = soup.find('ul', attrs={'class': 'list-jobs'})
            if main_ul:

                li_list = main_ul.find_all('li', attrs={'class': 'list-jobs__item'})
                for li in li_list:
                    title = li.find('div', attrs={'class': 'list-jobs__title'})
                    href = title.a['href']
                    cont = li.find('div', attrs={'class': 'list-jobs__description'})
                    content = cont.text
                    company = 'No name'
                    comp = li.find('div', attrs={'class': 'list-jobs__details__info'})

                    if comp:
                        company = comp.a.text
                    jobs.append({'title': title.text, 'url': domain + href, 'description': content, 'company': company,
                                 'city_id':city, 'language_id':language})

            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page not response"})
    return jobs, errors


if __name__ == '__main__':
    url = 'https://djinni.co/jobs/?keywords=Python'
    jobs, errors = djinni(url)
    h = codecs.open('../work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()
