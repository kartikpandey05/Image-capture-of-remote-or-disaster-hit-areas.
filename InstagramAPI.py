import requests
import urllib.request

from pip._vendor.distlib.compat import raw_input

url = 'https://api.instagram.com/v1/users/1545666056/media/recent/?access_token=1472346217.29bc906.10a334db51f24e9aa9a02862db535419'
user_details = requests.get(url)
user_details = (user_details.json())

# print (user_details)'
print('user details >>>>>>>')

if user_details['meta']['code'] == 200:
    user_name = user_details['data'][0]['user']['full_name']
    print('other user name : ' + user_name)
    user_id = user_details['data'][0]['user']['id']
    print('other user id : ' + user_id)
else:
    print("user not found")

# print (my details)
print('my details >>>>>>>')

url = 'https://api.instagram.com/v1/users/self/?access_token=1472346217.29bc906.10a334db51f24e9aa9a02862db535419'
my_details = requests.get(url)
my_details = (my_details.json())

if my_details['meta']['code'] == 200:
    my_id = my_details['data']['id']
    print('my id: ' + my_id)
    my_name = my_details['data']['full_name']
    print('my username: ' + my_name)
    my_bio = my_details['data']['bio']
    print('my bio:' + my_bio)
    my_website = my_details['data']['website']
    print('my website: ' + my_website)
    my_profilepicutre = my_details['data']['profile_picture']
    print('profile picute: ' + my_profilepicutre)
    my_counts = my_details['data']['counts']
    print('my counts: ' + str(my_counts))

    # my media section

    my_url = 'https://api.instagram.com/v1/users/' + my_id + '/media/recent/?access_token=1472346217.29bc906.10a334db51f24e9aa9a02862db535419'
    my_details = requests.get(my_url)
    my_details = (my_details.json())
    # print my_details
    if my_details['meta']['code'] == 200:
        my_recent_post_id = my_details['data'][0]['id']
        print('My recent post\'s id is: ' + str(my_recent_post_id))
        my_recent_post_url = my_details['data'][0]['images']['standard_resolution']['url']
        print('Url of my recent post is: ' + my_recent_post_url)
        urllib.request.urlretrieve(my_recent_post_url, 'recent_post_pic.jpg')
        print('The image has been downloaded with name recent_post_pic.jpg')
    else:
        print('Something went terribly wrong, contact administrator for support')

# user input raw



other_user_name = raw_input('\nEnter the username which you want to search: \n')
user_url = 'https://api.instagram.com/v1/users/search?q=' + other_user_name + '&access_token=1545666056.98346f2.38c9a48c189d43dd88ffe4b45bbd9d38'
other_user_details = requests.get(user_url)
other_user_details = (other_user_details.json())
# print other_user_details

if other_user_details['meta']['code'] == 200:
    other_user_user_id = other_user_details['data'][0]['id']
    print('User\'s user id is: ' + str(other_user_user_id))
else:
    print('User does not exist')

other_user_post_url = 'https://api.instagram.com/v1/users/' + other_user_user_id + '/media/recent/?access_token=1545666056.98346f2.38c9a48c189d43dd88ffe4b45bbd9d38'
other_user_posts = requests.get(other_user_post_url)
other_user_posts = (other_user_posts.json())






