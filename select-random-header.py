import os
import random
import mastodonAccessToken as seceret


#CONST
#Used to hold value of screen shot path.
file = ''

#Choose a random photo in album
def randomPicture():
    global file
    directory = 'photolib'
    counter = 0
    randomChoice = random.randint(1, len(os.listdir(directory)))
    for filename in os.listdir(directory):
        if counter == randomChoice:
            f = os.path.join(directory, filename)
            file = f
            break
        elif counter != randomChoice:
            counter += 1
        else:
            print("randomPicture() if/elif has an issue, recalling randomPicture()")
            randomPicture()


def main():
    global file
    # get token specified in mastodonAccessToken.py file
    auth = seceret.api_key
    randomPicture()
    # Specify mastodon instance | Access Token | profile content to update
    url = "https://mastodon.social/api/v1/accounts/update_credentials"
    header = "'Authorization: Bearer %s'" % auth 
    payload =  "header='@%s'" % file
    
    command = "curl -v -X PATCH %s -H %s -F %s "  %(url, header, payload)
    send_request = os.system(command)
    print(send_request)

# make a PATCH request to masto API
# https://www.geeksforgeeks.org/patch-method-python-requests/
# requests.patch($URL,$PARAMS={$KEY: $VALUE, args)
# cURL request
# curl -v -X PATCH https://infosec.exchange/api/v1/accounts/update_credentials -H "Authorization: Bearer $secerets" -F header='@header.png'
# ToDo: remove os.system() and use requests lib instead. had issues making the -F (form) and -X (??) work



if __name__ == "__main__":
    #HELP_MENU/Fail
    main()






