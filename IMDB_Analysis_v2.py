from urllib.request import  urlopen as uReq
#import requests
from bs4 import BeautifulSoup


def fetchhtml(url):
    uClient = uReq(url)
    content = uClient.read()
    uClient.close()
    soup = BeautifulSoup(content, "html.parser")
    return soup
    

def write_to_csv(data): 
    print("writing data to file...")
    with open('data-with-year-remaining.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data) 


def scrapedata_main():
    # Base url of the website
    url = "http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8"

    main_soup = fetchhtml(url)
    table = main_soup.findAll("tbody",{"class":"lister-list"})

    for table_loop in table:
        tr_tag = table_loop.find_all("tr")

        for tr_loop in tr_tag:
            details = tr_loop.findAll("td",{"class":"titleColumn"})
            title_name = details[0].a.text.replace(",",".")
            
            page_link = details[0].a.get("href")
            scrapedata_page(page_link)
                        
            year = details[0].span.text.replace("(","").replace(")","").strip()
            rank = details[0].div.text.split('(')[0].strip()

            details_2 = tr_loop.findAll("td",{"class":"ratingColumn imdbRating"})
            rating = details_2[0].text.strip()
                        
            #print(details)
            #print(title_name)
            #print(year)
            #print(rank)
            #print(rating)

def scrapedata_page(page_link):
    link = "http://www.imdb.com" + page_link
    page_soup = fetchhtml(link.strip())
    table = main_soup.findAll("tbody",{"class":"lister-list"})
    
    

if __name__== "__main__":
    scrapedata_main()
