from time import sleep
from selenium_funcs import scroll_down, login
import pickle
from secretenv import OUT_DIRECTORY, FRIENDS_LIST_TXT,\
        LAST_FOUND_FRIEND_NAME # this is the last name obtained the last time the script was ran

# friend list saved locally
with open(f'{OUT_DIRECTORY}/{FRIENDS_LIST_TXT}', 'r') as _:
    friends = _.readlines()

start = False
browser = login()

for name in friends:
    name = name.rstrip('\n')

    if start:
        browser.get(f'https://facebook.com/{name}/friends')
        scroll_down(browser)

        l = []
        elems = browser.find_elements_by_xpath('//a[@href]')
        #looking at all hyperlinks in the page will return many spurious results
        #but the containers are not simple and it is easier to post filter
        for elem in elems:
            elem = elem.get_attribute('href').split('/')[-1]
            l.append(elem)

        with open(f'{OUT_DIRECTORY}/{name}.pickle', 'wb') as _:
            pickle.dump(l, _)

    if name == LAST_FOUND_FRIEND_NAME:
        start = True
