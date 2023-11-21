import requests

url = "https://example.com/example.pdf" # change this to your url

# make a get request to the server => a get request will GET data from a server
webpage = requests.get(url)

# split the url at every point where there is a forward slash "/" => ["https:", "example.com", "example.pdf"]
#                                               the code will take the last element                 ||
futureName = url.split('/')[-1]

# write the content of the response gotten from the server to a file
# if we didn't do that, the file would just stay as a temporary file, and wouldn't be usable when we closed this window
with open(futureName, 'wb') as file:
    file.write(webpage.content)

