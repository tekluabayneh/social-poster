from src.services.facebook_service import Post_FaceBook
from src.services.reddit_service import Post_Reddit
from src.services.linkedin_service import Post_Linkedin
from src.services.x_service import Post_x

def post_everywhere(message):
    print(Post_FaceBook(message))
    print(Post_Linkedin(message))
    print(Post_Reddit(message))
    print(Post_x(message))
