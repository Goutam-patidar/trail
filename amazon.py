# # import requests
# # from bs4 import BeautifulSoup
# # import amaz
# # def list_generator(name):
# #     links= amaz.link_generator(name)
# #     names = []
# #     ratings = []
# #     prices = []
# #     imglink=[]
# #     del_li=[]
# #     for item in links:

# #         req_html = requests.get(item)
# #         if (req_html):
# #             req_content = BeautifulSoup(req_html.content, 'html.parser')
# #             data_cont_imp = req_content.find('div', {'id': 'ppd'})
# #             if (data_cont_imp):
                

# #                 name_list = data_cont_imp.find('span', attrs={'class': 'a-size-large product-title-word-break'})
# #                 price_list = data_cont_imp.find('span', attrs={'class': 'a-offscreen'})
# #                 rating_list = data_cont_imp.find('span', attrs={'class': 'reviewCountTextLinkedHistogram noUnderline'})
# #                 img_list = data_cont_imp.find('img', {'class': 'a-dynamic-image a-stretch-vertical'})
# #                 if img_list is not None and 'src' in img_list.attrs:
# #                     href_img = img_list['src']
# #                     print(href_img)
# #                     if href_img is not None:
# #                         imglink.append(href_img)
# #                 #     print(href_img)
# #                 # print(name_list)
# #                 # print(price_list)
# #                 # print(rating_list)
# #                 if(price_list==None  or name_list==None ):
# #                     del_li.append(item)
# #                     continue
                
# #                 names.append(name_list.text.strip() )
# #                 ratings.append(rating_list.text.strip() if rating_list is not None else "")
            
# #                 price_temp=price_list.text.strip()
# #                 price_temp=price_temp.replace('₹','')
# #                 price_temp=price_temp.replace(',','')
# #                 prices.append(float(price_temp) )

# #                 # print(names)
# #                 # print(ratings)
# #                 # print(prices)
# #                 # print(imglink)
# #             else:
# #                 print("HTML PARSING ERROR")
# #                 continue
# #         else:
# #             print("URL ERROR")
# #             continue
    
# #     print(names)
# #     print(ratings)
# #     print(prices)
# #     print(imglink)

# #     for i in del_li:
# #         links.remove(i)

# #     combined_array = []
# #     for index, (element1, element2, element3,element4,element5) in enumerate(zip(names,ratings,prices,links,imglink)):
# #         combined_array.append((index, element1, element2, element3,element4,element5))


# #     sorted_price_list=sorted(combined_array, key=lambda x: x[3])
# #     for i in sorted_price_list:
# #         print(i)
# #     return sorted_price_list

# # # def main(name):
# # print(list_generator(input("enter")))

# import requests
# from bs4 import BeautifulSoup
# import amaz
# def list_generator(name):
#     links= amaz.link_generator(name)
#     names = []
#     ratings = []
#     prices = []
#     imglink=[]
#     del_li=[]
#     for item in links:
#         if item is None:
#             continue
#         req_html = requests.get(item)
#         print(req_html)
#         if (req_html):
#             req_content = BeautifulSoup(req_html.content, 'html.parser')
#             data_cont_imp = req_content.find('div', {'id': 'ppd'})
#             if (data_cont_imp):
                

#                 name_list = data_cont_imp.find('span', attrs={'class': 'a-size-large product-title-word-break'})
#                 price_list = data_cont_imp.find('span', attrs={'class': 'a-offscreen'})
#                 rating_list = data_cont_imp.find('span', attrs={'class': 'reviewCountTextLinkedHistogram noUnderline'})
#                 img_list = data_cont_imp.find('img', {'class': 'a-dynamic-image a-stretch-vertical'})
#                 if img_list is not None and 'src' in img_list.attrs:
#                     href_img = img_list['src']
#                     if href_img is not None:
#                         imglink.append(href_img)
#                 #     print(href_img)
#                 # print(name_list)
#                 # print(price_list)
#                 # print(rating_list)
#                 if(price_list==None  or name_list==None ):
#                     del_li.append(item)
#                     continue
                
#                 names.append(name_list.text.strip() )
#                 ratings.append(rating_list.text.strip() if rating_list is not None else "")
            
#                 price_temp=price_list.text.strip()
#                 price_temp=price_temp.replace('₹','')
#                 price_temp=price_temp.replace(',','')
#                 prices.append(float(price_temp) )

#                 # print(names)
#                 # print(ratings)
#                 # print(prices)
#                 # print(imglink)
#             else:
#                 print("HTML PARSING ERROR")
#                 continue
#         else:
#             print("URL ERROR")
#             continue
        
#     for i in del_li:
#         links.remove(i)

#     combined_array = []
#     for index, (element1, element2, element3,element4,element5) in enumerate(zip(names,ratings,prices,links,imglink)):
#         combined_array.append((index, element1, element2, element3,element4,element5))


#     sorted_price_list=sorted(combined_array, key=lambda x: x[3])
#     for i in sorted_price_list:
#         print(i)
#     return sorted_price_list

# # def main(name):
# #     return list_generator(name)
# #     # print(temp)
# #     # return temp

# print(list_generator(input("enter ")))
# print("done")




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import amaz

def list_generator(name):
    links = amaz.link_generator(name)
    names = []
    ratings = []
    prices = []
    imglink = []
    del_li = []

    # Set up Microsoft Edge WebDriver
    edge_options = Options()
    edge_options.use_chromium = True
    edge_options.add_argument('--headless') 
    # Replace 'path_to_edgedriver' with the actual path to the downloaded Edge WebDriver executable
    driver = webdriver.Edge(service=Service('C:/Users/PATIDAR_G_/edgedriver_win64'), options=edge_options)

    for item in links:
        if item is None:
            continue

        # Use the WebDriver to navigate to the URL
        driver.get(item)

        # Wait for the page to load (you can use explicit waits here if needed)
        driver.implicitly_wait(10)

        # Get the page source after the JavaScript has executed
        page_source = driver.page_source

        # Parse the page source with BeautifulSoup
        req_content = BeautifulSoup(page_source, 'html.parser')

        data_cont_imp = req_content.find('div', {'id': 'ppd'})
        if data_cont_imp:
            name_list = data_cont_imp.find('span', attrs={'class': 'a-size-large product-title-word-break'})
            price_list = data_cont_imp.find('span', attrs={'class': 'a-offscreen'})
            rating_list = data_cont_imp.find('span', attrs={'class': 'reviewCountTextLinkedHistogram noUnderline'})
            img_list = data_cont_imp.find('img', {'class': 'a-dynamic-image a-stretch-vertical'})
            if img_list is not None and 'src' in img_list.attrs:
                href_img = img_list['src']
                if href_img is not None:
                    imglink.append(href_img)

            if price_list is None or name_list is None:
                del_li.append(item)
                continue

            names.append(name_list.text.strip())
            ratings.append(rating_list.text.strip() if rating_list is not None else "")

            price_temp = price_list.text.strip()
            price_temp = price_temp.replace('₹', '')
            price_temp = price_temp.replace(',', '')
            prices.append(float(price_temp))

        else:
            print("HTML PARSING ERROR")
            continue

    # Close the WebDriver
    driver.quit()

    for i in del_li:
        links.remove(i)

    combined_array = []
    for index, (element1, element2, element3, element4, element5) in enumerate(zip(names, ratings, prices, links, imglink)):
        combined_array.append((index, element1, element2, element3, element4, element5))

    sorted_price_list = sorted(combined_array, key=lambda x: x[3])
    for i in sorted_price_list:
        print(i)

    return sorted_price_list

print(list_generator(input("Enter product name: ")))
print("done")
