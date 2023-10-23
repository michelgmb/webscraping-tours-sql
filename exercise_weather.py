# import datetime
#
# import requests
# import selectorlib
# from datetime import datetime
#
#
# URL = "https://programmer100.pythonanywhere.com/"
#
# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#
#
# def scrape(url):
#     response = requests.get(url, headers=HEADERS)
#     source = response.text
#     return source
#
#
# def extract(source):
#     value_date = {}
#     extractor = selectorlib.Extractor.from_yaml_file("extractexer.yaml")
#     value = extractor.extract(source)['title']
#     date = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
#     value_date[date] = value
#     return value_date
#
#
# def store(extracted):
#     with open('date_temp.txt', 'a') as file:
#         for date in extracted:
#             file = file.writelines(f"{date} , {extracted[date]}\n")
#
#
#
# if __name__ == '__main__':
#     source = scrape(URL)
#     # print (source)
#     extracted = extract(source)
#     print(extracted)
#     store(extracted)



