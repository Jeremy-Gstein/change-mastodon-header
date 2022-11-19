# change-mastodon-header
#### change your mastodon header picture using the official Mastodon API (tested on federated instance) 

# Usage
  
  > - 1. First add your Mastodon Acess Token (see screenshot below for location:)
  > - 2. Get your Mastodon Aceess Token (assuming you already have an appliacation with r/w access to account.)
  > - ![image](https://user-images.githubusercontent.com/66806528/202611800-2e952ade-2eb3-4704-8c17-c56c0431434d.png)
  > - 3. Put Access token in mastondonAccessToken.py file (this is in .gitignore so may have to create)
  > - `$ echo "api_key = '$YOUR_ACCESS_TOKEN' " >> mastodonAccessToken.py` 
  
#### On CLI:
 > - ***note: add your own photos to /photolib!***
 > -  `$ python3 $PWD/change-mastodon-header`   - on CLI use exec python3 on "change-mastodon-header.py"

  

### ToDo:
  > - Remove os.system() and replace with python's requests lib. currently making a curl request relying on the host OS having this.
  > - specify a custom/federated mastodon instance in the accessToken.py file.
