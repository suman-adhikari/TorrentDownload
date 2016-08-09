import re
import string
import os
import requests

query = raw_input("Enter your query:")
parent_url = "https://kat.cr/usearch/"
url = parent_url+query
html = requests.get(url).text
query_string = string.replace(query," ","-")
urls = re.findall(r'<a href="/'+query_string+'.+</a>',html)
#urls = re.findall(r'<a href="/heroes-reborn-s01e01.+</a>',html)
href = re.findall(r'/.*html',urls[0])
final_url = "https://kat.cr"+href[0]
print final_url
html_child = requests.get(final_url).text
magnet_urls = re.findall(r'<a class="kaGiantButton " data-nop title="Magnet link" href="magnet:.+</a>',html_child)
magnet_url = re.findall(r'magnet.*?"',magnet_urls[0])
magnet = string.replace(magnet_url[0],'"',"")

os.startfile(magnet)











