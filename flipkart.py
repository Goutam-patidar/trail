import requests
from bs4 import BeautifulSoup
import flip
def list_generator(name):
    links= flip.link_generator(name)
    # links = flip.links
    names = []
    ratings = []
    prices = []
    imglink=[]
    for item in links:
        req_html = requests.get(item)
        if (req_html):
            req_content = BeautifulSoup(req_html.content, 'html.parser')
            data_cont_imp = req_content.find('div', {'class': '_1YokD2 _2GoDe3'})
            if (data_cont_imp):
                

                name_list = data_cont_imp.find('span', attrs={'class': 'B_NuCI'})
                price_list = data_cont_imp.find('div', attrs={'class': '_30jeq3 _16Jk6d'})
                rating_list = data_cont_imp.find('div', attrs={'class': '_3LWZlK'})
                img_list = data_cont_imp.find('img', {'class': '_396cs4 _2amPTt _3qGmMb'})
                if img_list is not None and 'src' in img_list.attrs:
                    href_img = img_list['src']
                    if href_img is not None:
                        imglink.append(href_img)
                # print(name_list)
                # print(price_list)
                # print(rating_list)
                if(price_list==None  or name_list==None ):
                    del_li.append(item)
                    continue
                names.append(name_list.text.strip() )
                ratings.append(rating_list.text.strip() if rating_list is not None else "")
                price_temp=price_list.text.strip()
                price_temp=price_temp.replace('₹','')
                price_temp=price_temp.replace(',','')
                prices.append(float(price_temp) )
                

                # print(names)
                # print(ratings)
                # print(prices)
            else:
                # print("HTML PARSING ERROR")
                continue
        else:
            # print("URL ERROR")
            continue

    combined_array = []
    for index, (element1, element2, element3,element4,element5) in enumerate(zip(names,ratings,prices,links,imglink)):
        combined_array.append((index, element1, element2, element3,element4,element5))


    sorted_price_list=sorted(combined_array, key=lambda x: x[3])
    for i in sorted_price_list:
        print(i)

def main(name):
    list_generator(name)

# if __name__ == "__main__":
#     name=input('enter')
    
#     list_generator(name)