Intro
---
Have you ever encountered a Tweet that smells like stink? In my case, I usually dream about blocking all those hundreds of people who liked that Tweet. These Tweets are usually posted by special accounts, and are promoted by other special accounts, such as the accounts served as the governments' propaganda.

Silencing the opposite voice isn't something to encourage, but sometimes our mental heath is more important.

Usage
---
In order to run this script on behalf of your account, you need to set up a few things first. If you already have a Twitter Developer account, continue from step 3:
1. Visit [Twitter Developer Platform](https://developer.twitter.com/en/portal/dashboard) and submit your information to access the Developer Portal.
2. Then, go ahead and create an App inside a Project, and save _API Key_ and _API Secret_ values. 
3. Go to _User authentication settings_ section at the _Settings_ page of your App.
4. Enable _OAuth 1.0a_, check Read and Write permissions, and put something random (like `localhost`) for callback urls.
5. Go to _Keys and tokens_ section of your App and generate _Access Token and Secret_.

Now, it's sufficient to pass these information as environment variables and run the code:
* `API_KEY`: The API Key obtained in the previous section
* `API_SECRET`: The API Secret obtained in the previous section
* `ACCESS_TOKEN`: The Access Token obtained in the previous section
* `ACCESS_TOKEN_SECRET`: The Access Token Secret obtained in the previous section
* `TWEET_ID`: The ID of the Tweet you want all accounts who liked it to be blocked. This can be obtained from a Tweet's URL, i.e. twitter.com/username/status/**\<ID\>**

You can create a `.env` file containing `NAME=VALUE` lines for your environment variables.

Finally, install the dependencies and run the code:
```bash
git clone https://github.com/alitoufighi/arzeshi-block.git
cd arzeshi-block
pip install -r requirements.txt
python main.py
```

Note
---
Note that Twitter allows you to perform a limited number of API calls with this free account
