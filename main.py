# import NetworkScanner
import crawler


def menu():
    print('''1: Network Scanner
2: Web Crawler
3: Exit''')


option = 0
isApplicationRunning = True
target_url = 'https://www.geeksforgeeks.org'

menu()
while isApplicationRunning:
    try:
        option = int(input("Please Enter an option from the above menu: "))
        if option == 1:
            # NetworkScanner.Execute()
            print('NetWork Scanner')
            print('Network Scanning has been executed.')
            menu()
        elif option == 2:
            print('Web Crawler')
            crawl = crawler.Crawler(target_url)
            crawl.isCrawling = True
            crawl.crawl()
            print('Web Crawling has been executed.')
            menu()
        elif option == 3:
            isApplicationRunning = False
            exit(0)
        else:
            print('Print Valid Input')
    except:
        if isApplicationRunning:
            print('Invalid Entry')
