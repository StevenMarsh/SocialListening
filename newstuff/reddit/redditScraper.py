import praw
import pickle

reddit = praw.Reddit(client_id='Er4Vv0BqmH-nOQ',
                     client_secret='o_u7JD1fNJgwVbB3WALvrbDUdbIizQ',
                     username='TMGTest',
                     password='TMGtest2020',
                     user_agent='TMGToneAnalyzer')


class RedditSubmission:
    def __init__(self, up_votes, upvote_ratio, down_votes, title, submission_id):
        self.up_votes = up_votes
        self.upvote_ratio = upvote_ratio
        self.down_votes = down_votes
        self.title = title
        self.submission_id = submission_id
        self.comment_list = []


class RedditComment(RedditSubmission):
    def __init__(self, comment_id, comment_text, parent_id):
        self.comment_id = comment_id
        self.comment_text = comment_text
        self.parent_id = parent_id


class SubmissionBox:
    def __init__(self):
        self.submission_list = []
        self.sentimentDictionary = {}
        # intialize and empty dictionary that maps a parent ID to a list of sentiments(when we get it back from IBM tone analyzer)


# class for 'redditSubmission' contain, upvotes, upvote ratio, down votes, text of the submission title,
    # redditSubmission will have a parent ID
# child class for redditSubmission is redditComments
    # redditComment will have the comment id and Parent ID
# submissionBox object everytime creating a new reddit submission add the submission to the submission box
# every reddit submission have a list of the redditComments objects in it

def redditStream(user_subreddit, user_post_count):

    # make 'python' into a variable so the user can decide what they want to put in

    subreddit = reddit.subreddit(user_subreddit)


    # make 'limit = 10' a parameter so the user can decide what they want to put in

    hot_python = subreddit.hot(limit=user_post_count)

    submissionData = SubmissionBox()
    for submission in hot_python:
        downVote = round((submission.ups / submission.upvote_ratio) - submission.ups)
        userSubmission = RedditSubmission(submission.ups, submission.upvote_ratio, downVote, submission.title, submission.id)
        submission.comments.replace_more(limit=0)  # https://praw.readthedocs.io/en/latest/tutorials/comments.html
        for comment in submission.comments.list():
            new_comment = RedditComment(comment.id, comment.body, comment.parent())
            userSubmission.comment_list.append(RedditComment(comment.id, comment.body, comment.parent()))
        submissionData.submission_list.append(userSubmission)
    print(len(submissionData.submission_list))
    redditFile = open("redditBox.p", "wb")
    pickle.dump(submissionData, redditFile)





    # for every comment create a submission COmment and append it to the Comment list in the submission object (reddit.submission.commentlist.apppend[]_


def pickle_reddit():
    redditBox = pickle.load(open("redditBox.p", "rb"))
    print(redditBox.submission_list[0].title)



def main():
    user_subreddit = input("What subreddit would you like to scrape? ")
    user_post_count = int(input("How many posts would you like to scrape? "))
    redditStream(user_subreddit, user_post_count)
    pickle_reddit()
main()