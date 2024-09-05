This uses a selenium browser to scrape your facebook profile to generate a
graph of your friends-of-friends. It was last tested in October of 2020, and is
non-functional at this point. However, it may be used as inspiration. I have
included the dotfile png output from my analysis as a show of what one can do,
if one were to update the method here.

# Quickstart
1. Make an 'in' folder and specify its location with IN_DIRECTORY and 'out'
folder and specify its location with OUT_DIRECTORY in the secretenv.py file.
2. Navigate to https://www.facebook.com/friends/list in your browser. Save the
source in the 'in' folder, and whatever you name the file put it in the
secretenv.py file as FRIENDS_LIST_HTML. Now run flist.py. Note that when I did
this as of 2024-09-04, I only got the first 60 friends I had, even when I
scrolled. This should generate at OUT_DIRECTORY/FRIENDS_LIST_TXT the facebook
usernames (not displaynames) for your friends.
3. Execute friends-of-friends.py. As I tried this 2024-09-04, this failed to
even login, and the WebDriver object no longer has the method
'find_element_by_id'. This requires significant revision. However, it's point
is just to go to friends list of friends (hence friends of friends) to obtain
your mutual friends and friends of friends.
4. Execute nx-graph.py. Note that nx is not a visualization library and should
only be used for calculations. If you export to a .dot file and visualize this,
it can take place over a reasonable time. In my case, it showed clusters from
high school, undergraduate, and graduate school with a small number of links
between them.


## Sample secretenv.py

USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'
LAST_FOUND_FRIEND_NAME = 'tom.hardy'
# this should be the first friend in your friends list text file when you have never ran before
# this only exists in case you have to run the script multiple times, as friends-of-friends.py is by far the most time consuming
IN_DIRECTORY = 'in'
OUT_DIRECTORY = 'out'
FRIENDS_LIST_HTML = 'https___www.facebook.com_friends_list.html'
FRIENDS_LIST_TXT = 'friends_list.txt'
