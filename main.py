import requests
import selectorlib
import time
from  send_email import sendemail

# get url
URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# get the source
def scrape(url):
    """Scrape the source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


# extra value from website
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yml")
    value = extractor.extract(source)["tours"]
    return value


# send email if value extracted not in db



def store(extracted):
    with open('data.txt', "a") as file:
        file.write(extracted + "\n")


def read():
    with open('data.txt', 'r') as data_list:
        data_list = data_list.read()
        return data_list


# store in database

while True:
    if __name__ == '__main__':

            source = scrape(URL)
            extrated = extract(source)
            print(extrated)
            if extrated != "No upcoming tours":
                content_data = read()
                print(content_data)
                if extrated not in content_data:
                    store(extrated)
                    x = f"{content_data} '\n'{extrated} "
                    print("email send")
                    sendemail(x )
    time.sleep(5)


