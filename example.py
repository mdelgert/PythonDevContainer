# Get a joke from this endpoint and print it - https://official-joke-api.appspot.com/random_joke
# This is sample response {"type":"general","setup":"What did the traffic light say to the car as it passed?","punchline":"Don't look I'm changing!","id":185}
import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke = response.json()
        print(f"{joke['setup']} {joke['punchline']}")
    else:
        print("Failed to retrieve joke")

if __name__ == "__main__":
    #print("Hello, World!")
    get_joke()