"""

Usage:
	primefeed view_feed
	primefeed post <title> <body>
	primefeed comment <postId> <title> <body>
    

"""

import cmd
import sys
import os
import urllib
import json
from docopt import docopt, DocoptExit
from feed.news_feed import News_feed



def docopt_cmd(func):
    

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
           
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
           
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def display_title_bar():
    os.system('cls')
    print("\t**********************************************")
    print("\t---               NEWS FEED                ---")
    print("\t---        Post, Share, Comment on News    ---")
    print("\t**********************************************")


class primefeed(cmd.Cmd):
	intro = display_title_bar()
	prompt = 'primefeed->>'
	primefeed = News_feed()

@docopt_cmd
def view_feed():
    pass

@docopt_cmd
def add_post():
	pass

def do_quit(self, arg):
    """Quits interactive mode"""
    print('Have a nice day :)')
    exit()

if __name__ == '__main__':
    try:
        print(__doc__)
      	primefeed().cmdloop()
    except KeyboardInterrupt:
        print('Exiting...')
