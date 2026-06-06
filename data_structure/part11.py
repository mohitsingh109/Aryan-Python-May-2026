# Assignment: YouTube Creator Analytics Dashboard
#
# A YouTube content creator wants to analyze the performance of their channel.
#
# 1. LIST
#    - Store all video titles.
#
# 2. TUPLE
#    - Store video category information in the format:
#      (Video ID, Category Name)
#
# 3. DICTIONARY
#    - Store video statistics:
#      {
#          "video_id": {
#              "title": "...",
#              "views": ...,
#              "likes": ...,
#              "comments": ...
#          }
#      }
#
# 4. SET
#    - Store all unique tags used across videos.
#
# Your program should provide the following menu options:
#
# 1. Add a new video.
#    - Enter Video ID, Title, Category, Views, Likes, Comments.
#    - Enter multiple tags separated by commas.
#
# 2. Display all videos.
#
# 3. Search a video by Video ID.
#
# 4. Show the most viewed video.
#
# 5. Show the video with the highest engagement score.
#    Engagement Score = Likes + Comments
#
# 6. Display all unique tags used in the channel.
#
# 7. Show category-wise statistics:
#    Example:
#    Education -> Total Videos, Total Views
#    Gaming -> Total Videos, Total Views
#    Technology -> Total Videos, Total Views
#
# 8. Find creators' "Trending Candidates".
#    A video is considered trending if:
#    - Views > 100000
#    - Likes > 5000
#    - Comments > 500
#
# 9. Display the Top 3 Videos by Views.
#
# 10. Show channel summary:
#     - Total Videos
#     - Total Views
#     - Total Likes
#     - Total Comments
#     - Average Views per Video
#
# 11. Remove a video.
#
# 12. Exit.

def add_video():
    







while True:
    print('1. Add a new video')
    print('2. View all videos')
    print('3. View a video by video id')
    print('4. Show the most viewed video')
    print('5. Show the video with highest engagement score')
    print('6. display all unique tags used in the channel')
    print('7. Find creators-Trending candidates')
    print('8. Display the top 3 videos by views')
    print('9. Show channel summary')
    print('10. Remove a video')
    print('12. Exit')
    choice = int(input("Enter your choice:"))
    if choice == 1:
