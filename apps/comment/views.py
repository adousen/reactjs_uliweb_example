#coding=utf-8
from uliweb import expose, functions, request, json
from bpmappers import Mapper, RawField, ListDelegateField
import shelve


DATA_FILE = "guest_book.dat"


@expose('/')
def index():
    return {}


@expose('/comment.json')
def comment():
    def ret_json_response():
        commentlist = load_data()
        result_dict = CommentListMapper({"data": commentlist}).as_dict()

        print result_dict

        json_response = json(result_dict, content_type='text/json; charset=utf-8')

        return json_response

    if request.method == 'GET':
        return ret_json_response()

    elif request.method == 'POST':
        print dict(request.POST)

        save_data(request.POST)

        return ret_json_response()


class CommentMapper(Mapper):
    author = RawField()
    text = RawField()


class CommentListMapper(Mapper):
    data = ListDelegateField(CommentMapper)


# database
def save_data(comment):
    """Save the comment data."""

    #Open the shelve module database File

    database = shelve.open(DATA_FILE)
    #if there is no greeting_list in database, create it
    if 'comment_list' not in database:
        comment_list = []
    else:
        #get the greeting_list from the database
        comment_list = database['comment_list']

    #appending the data into the list top
    comment_list.append({
        'author': comment["author"],
        'text': comment["text"],
    })

    #update the database
    database['comment_list'] = comment_list

    #close the database file
    database.close()


def load_data():
    """Return the comment data saved before."""

    #open the shelve module database file
    database = shelve.open(DATA_FILE)

    #get the greeting_list . if ont, just return empty list.
    comment_list = database.get('comment_list', [])

    #print(comment_list)

    database.close()

    return comment_list