import praw 
import config
import time
import os

def bot_login():
    # Logs into account and returns the logged in object
    print("Logging in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "botmastrz9009's dog comment responder v0.1")
    print("Logged in..!")

    return r

def run_bot(r, c):
    # Looks through 10 reddit comments test subreddit, looking for the word "dog"
    print("Checking 10 comments...")

    for comment in r.subreddit('test').comments(limit=10):
        # Looks for new "dog" comments that aren't from the bot or person already replied to
        if "dog" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print('\nString with "dog" found in comment ' + comment.id)
            comment.reply("\nI also love dogs! [Here](https://i.redd.it/hgzsish8nrs51.jpg) is a nice dog pic.")
            print("\nReplied to comment " + comment.id)

            comments_replied_to.append(comment.id)

            with open("replied_comments.txt", "a") as f:
                f.write(comment.id + "\n")
    

    print("\nSleep for 10 seconds...")
    # Sleep for 10 seconds
    time.sleep(10)

def get_saved_comments():
    # Checks for .txt file of comments replied to and creates one if non-existent
    if not os.path.isfile("replied_comments.txt"):
        comments_replied_to = []
    else:
        with open("replied_comments.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    run_bot(r, comments_replied_to)  