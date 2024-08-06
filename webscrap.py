
# pip install bs4
# pip install lxml
# pip install requests

# importing libraries
from bs4 import BeautifulSoup
import requests

def main(URL):
    # opening our output file in append mode
    with open("C:/Users/dinam/Documents/Data-Analytics-Projects-Using-Python/Web_Scripting-Amazon-Price/output1.csv", "a") as File:
        # specifying user agent, You can use other user agents
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'
        }

        # Making the HTTP Request
        webpage = requests.get(URL, headers=HEADERS)

        # Creating the Soup Object containing all data
        soup = BeautifulSoup(webpage.content, "lxml")

        # retrieving product title
        try:
            # Outer Tag Object
            title = soup.find("span", attrs={"id": 'productTitle'})
            # Inner NavigableString Object
            title_value = title.string
            # Title as a string value
            title_string = title_value.strip().replace(',', '')
        except AttributeError:
            title_string = "NA"
        print("Product Title = ", title_string)

        # saving the title in the file
        File.write(f"{title_string},")

        # retrieving price
        try:
            price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')
        except AttributeError:
            price = "NA"
        print("Product Price = ", price)

        # saving the price in the file
        File.write(f"{price},")

        # retrieving product rating
        try:
            rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')
        except AttributeError:
            try:
                rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
            except AttributeError:
                rating = "NA"
        print("Overall Rating = ", rating)

        File.write(f"{rating},")

        # retrieving review count
        try:
            review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')
        except AttributeError:
            review_count = "NA"
        print("Total Reviews = ", review_count)
        File.write(f"{review_count},")

        # retrieving availability status
        try:
            available = soup.find("div", attrs={'id': 'availability'}).find("span").string.strip().replace(',', '')
        except AttributeError:
            available = "NA"
        print("Availability = ", available)

        # saving the availability and closing the line
        File.write(f"{available}\n")


if __name__ == '__main__':
    # opening our url file to access URLs
    with open("C:/Users/dinam/Documents/Data-Analytics-Projects-Using-Python/Web_Scripting-Amazon-Price/url.txt", "r") as file:
        # iterating over the urls
        for links in file.readlines():
            main(links.strip())