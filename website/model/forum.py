
from google.appengine.ext import db


class Forum(db.Model):
  name = db.StringProperty(required=True)
  slug = db.StringProperty(required=True)
  description = db.TextProperty(required=True)
  alliance = db.StringProperty()


class ForumThread(db.Model):
  forum = db.ReferenceProperty(Forum, required=True)
  posted = db.DateTimeProperty(required=True)
  subject = db.StringProperty(required=True)
  slug = db.StringProperty(required=True)
  user = db.UserProperty(required=True)


class ForumPost(db.Model):
  forum = db.ReferenceProperty(Forum, required=True)
  user = db.UserProperty(required=True)
  posted = db.DateTimeProperty(required=True)
  content = db.TextProperty(required=True)


class ForumShardedCounter(db.Model):
  """This is a simple sharded counter that contains counts of various posts.

  We use it to count the number of posts in the forum, number of threads in
  a forum, number of replies to a post and so on."""
  name = db.StringProperty(required=True)
  count = db.IntegerProperty(required=True, default=0)
