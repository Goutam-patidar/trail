
import requests
from bs4 import BeautifulSoup
def link_generator(name):
    # product_req = input("Enter product detail: ")
    product_req=name
    new_pro_req = product_req.replace(" ", "%20")

    url = 'https://www.flipkart.com/search?q=' + new_pro_req + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
           
        
    print(url)

    req_html = requests.get(url)
    if (req_html):
        req_content = BeautifulSoup(req_html.content, 'html.parser')

        data_cont_imp = req_content.find_all('div', {'class': '_4ddWXP'})
        if (data_cont_imp):
            # print(data_cont_imp)
            links = []
            for items in data_cont_imp:
                rest_link = items.find('a', {'class': '_2rpwqI'})
                if rest_link is not None and 'href' in rest_link.attrs:
                    href_link = 'https://www.flipkart.com'+rest_link['href']
                    links.append(href_link)
                    # print(href_link)
        else:
            data_cont_imp = req_content.find_all('div', {'class': '_2kHMtA'})
            if (data_cont_imp):
                # print(data_cont_imp)
                links = []
                for items in data_cont_imp:
                    rest_link = items.find('a', {'class': '_1fQZEK'})
                    if rest_link is not None and 'href' in rest_link.attrs:
                        href_link = 'https://www.flipkart.com'+rest_link['href']
                        links.append(href_link)
                        # print(href_link)
            else:
                print("HTML PARSING ERROR")
    else:
        print("URL ERROR")

    print("flip done sucessfully")
    return links


# print(link_generator(input("enter")))
