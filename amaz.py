
# import requests
# from bs4 import BeautifulSoup
# import cloudscraper

# # url = "https://standards.globalspec.com/"




# def link_generator(name):
#     product_req = name
#     new_pro_req = product_req.replace(" ", "+")

#     url = 'https://www.amazon.in/s?k=' + new_pro_req + '&crid=2ZL677QUVV68Q&sprefix=' + new_pro_req + '%2Caps%2C246&ref=nb_sb_ss_ts-doa-p_1_4'
#         # https://www.amazon.in/s?k=  boat+earbuds  &i=electronics  &crid=Q7RDSESDSFUK&sprefix= boat+earbuds %2Celectronics %2C429&ref=nb_sb_noss_1
#         # https://www.amazon.in/s?k=  tiffin+box+for+office+for+men   &crid=12PD45NS1CROW&sprefix= tiffin+box+for+office+for+men %2Caps%2C226&ref=nb_sb_noss_2
#         # https://www.amazon.in/s?k=  noise+earbuds  &crid=3RN0GPIWR12KV&sprefix=%2Caps%2C243&ref=nb_sb_ss_recent_1_0_recent
#         # https://www.amazon.in/s?k= oneplus+earphones+bluetooth &crid=N2F9LXG3H4GS&sprefix=oneplus+ear%2Caps%2C300&ref=nb_sb_ss_ts-doa-p_2_11
#         # https://www.amazon.in/s?k= boat+bluetooth+earphone &crid=2ZL677QUVV68Q&sprefix=boat%2Caps%2C246&ref=nb_sb_ss_ts-doa-p_1_4
#     print(url)
#     links = []
    
#     scraper = cloudscraper.create_scraper()
#     req_html = scraper.get(url)
#     print(req_html)
#     if (req_html):
#         req_content = BeautifulSoup(req_html.content, 'html.parser')

#         data_cont_imp = req_content.find_all(
#             'div', {'class': 'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})
#         if (data_cont_imp):
#             # print(data_cont_imp)
#             # links = []
#             for items in data_cont_imp:
#                 rest_link = items.find(
#                     'a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
#                 if rest_link is not None and 'href' in rest_link.attrs:
#                     href_link = 'https://www.amazon.in/'+rest_link['href']
#                     links.append(href_link)
#                     # print(href_link)
#         else:
#             data_cont_imp = req_content.find_all(
#                 'div', {'class': 'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right'})
#             if (data_cont_imp):
#                 # print(data_cont_imp)
#                 # links = []
#                 for items in data_cont_imp:
#                     rest_link = items.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
#                     if rest_link is not None and 'href' in rest_link.attrs:
#                         href_link = 'https://www.amazon.in/'+rest_link['href']
#                         links.append(href_link)
#                         # print(href_link)
#             else:
#                 print("HTML PARSING ERROR")
#     else:
#         print("URL ERROR")

#     print("flip done sucessfully", len(links))
#     return links


# # print(link_generator(input("enter")))













from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup

def link_generator(name):
    product_req = name
    new_pro_req = product_req.replace(" ", "+")

    url = 'https://www.amazon.in/s?k=' + new_pro_req + '&crid=2ZL677QUVV68Q&sprefix=' + new_pro_req + '%2Caps%2C246&ref=nb_sb_ss_ts-doa-p_1_4'
    print(url)
    links = []

    # Set up Microsoft Edge WebDriver
    edge_options = Options()
    edge_options.use_chromium = True
    edge_options.add_argument('--headless') 
    # Replace 'path_to_edgedriver' with the actual path to the downloaded Edge WebDriver executable
    driver = webdriver.Edge(service=Service('C:/Users/PATIDAR_G_/edgedriver_win64'), options=edge_options)

    # Use the WebDriver to navigate to the URL
    driver.get(url)

    # Wait for the page to load (you can use explicit waits here if needed)
    driver.implicitly_wait(10)

    # Get the page source after the JavaScript has executed
    page_source = driver.page_source

    # Parse the page source with BeautifulSoup
    req_content = BeautifulSoup(page_source, 'html.parser')

    # Find links using BeautifulSoup
    data_cont_imp = req_content.find_all('div', {'class': 'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})
    if data_cont_imp:
        for items in data_cont_imp:
            rest_link = items.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
            if rest_link is not None and 'href' in rest_link.attrs:
                href_link = 'https://www.amazon.in/' + rest_link['href']
                links.append(href_link)
    else:
        data_cont_imp = req_content.find_all('div', {'class': 'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right'})
        if data_cont_imp:
            for items in data_cont_imp:
                rest_link = items.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
                if rest_link is not None and 'href' in rest_link.attrs:
                    href_link = 'https://www.amazon.in/' + rest_link['href']
                    links.append(href_link)
        else:
            print("HTML PARSING ERROR")

    # Close the WebDriver
    driver.quit()

    print("Scraping done successfully. Found", len(links), "links.")
    return links

# Call the function and pass the product name as an argument
# product_name = input("Enter product name: ")
# print(link_generator(product_name))
