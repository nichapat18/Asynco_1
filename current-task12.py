# check the status of many webpages
import asyncio
import time
from urllib.parse import urlsplit

# get the HTTP/S status of a webpage
async def get_status(url):
    # split the url into components
    url_parsed = urlsplit(url)
    print(f'{time.ctime()} fetch {url}')
    # open the connection
    if url_parsed.scheme == 'http':
        reader, writer = await asyncio.open_connection(url_parsed.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(url_parsed.hostname, 80)
    # send GET request
    query = f'GET {url_parsed.path} HTTP/1.1\r\nHost: {url_parsed.hostname}\r\n\r\n'
    # write query to socket
    writer.write(query.encode())
    # wait for the bytes to be written to the socket
    writer.write(query.encode())
    # read the single line response
    response = await reader.readline()
    # close the connection
    writer. close()
    # decode and strip white space
    status = response.decode().strip()
    print(f'{time.ctime()} done {url}')
    # return the response
    return status

# main coroutine
async def main():
    # list of top 10 websites to check
    sites = ['http://www.google.com/',
             'http://www.youtube.com/',
             'http://www.facebook.com/',
             'http://www.twitter.com/',
             'http://www.instagram.com/'
             'http://www.baidu.com/',
             'http://www.wikipedia.org/',
             'http://yandex.ru',
             'http://yahoo.com/',
             'http://www.whatsapp.com/',
             ]
    # create all coroutine requests
    coros = [get_status(url) for url in sites]
    # execute all coroutines and wait
    results = await asyncio.gather(*coros)
    # process all results
    for url, status in zip(sites, results):
        # report status
        print(f'{time.ctime()} {url:30}:\t{status}')

# run the asyncio program
asyncio.run(main())