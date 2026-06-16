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

video_info = {}



def add_video():
    global video_info
    v_id = input("Enter video id:")
    title = input("Enter video title:")
    views = int(input("Enter video views:"))
    likes = int(input("Enter video likes:"))
    comments = input ("Enter video comments:")
    chanel_id = input("Enter channel id:")
    tag = input("Enter video tags:")
    tag = tag.split(",")
    category = input("Enter video category:")
    comments = comments.split(",")
    if v_id not in video_info:
        video_info[v_id] =  { "title" : title , "views" : views, "likes" : likes, "comments" : comments ,
                              "tag": tag , "chanel_id": chanel_id , "category" : category }
    else:
        print("Video already exists")

def view_all_video():
    global video_info
    for v_id, record in video_info.items():
        print(f" Video id : {v_id} , views : {record["views"]} , likes : {record["likes"]}")
        print(f"Comments : {record["comments"]}")
        print(f" Tag : {record["tag"]}")

def search_video_by_id():
    global video_info
    v_id = input("Enter video id:")
    if v_id not in video_info:
        print("Video doesn't exist")
        return False
    else:
        record = video_info[v_id]
        print(f" Video id : {v_id} , views : {record["views"]} , likes : {record["likes"]}")
        print(f"Comments : {record["comments"]}")
        print(f" Tag : {record["tag"]}")
        return True

def max_view_video():
    global video_info
    m_views = -1
    m_v_id = None
    m_record = None

    for v_id, record in video_info.items():
        if record["views"] > m_views :
            m_views = record["views"]
            m_v_id = v_id
            m_record = record

    print(f"Video id : {m_v_id} , views:{m_views}, likes: {m_record["likes"]}")
    return m_views


def highest_engagement():
    global video_info
    engagement = 0
    m_v_id = None
    m_record = None

    for v_id ,record in video_info.items():
        if record["likes"] + len(record["comments"]) > engagement:
            engagement = record["likes"] + len(record["comments"])
            m_v_id = v_id
            m_record = record

    print(f"Video id : {m_v_id} ,Engagement : {engagement}, views : {m_record["views"]}, likes: {m_record["likes"]}")

    return engagement,m_v_id, m_record

def unique_tags_used_in_channel():
    global video_info
    channel = {}

    for record in video_info.values():
        channel_id = record["chanel_id"]
        if channel_id not in channel:
            channel[channel_id] = set(record["tag"])
        else :
            channel[channel_id].update(record["tag"])

    for channel_id, tags in channel.items():
        print(f'channel_id : {channel_id}, tags : {tags}')

    return channel

def category_statistics():
    global video_info
    category_statistics = {}
    for record in video_info.values():
        views = record["views"]
        category = record["category"]
        if category not in category_statistics:
            category_statistics[category] = { "total_views" : views , "total_videos": 1}
        else :
            category_statistics[category]["total_views"] += views
            category_statistics[category]["total_videos"] += 1


def trending_candidates():
    global video_info
    trending_candidates = {}

    for record in video_info.values():
        views = record["views"]
        likes = record["likes"]
        comments = record["comments"]
        channel_id = record["chanel_id"]
        if views > 100000 and  likes > 5000 and len(comments) > 500:
            trending_candidates[channel_id] = { "candidate" : channel_id}

    for channel_id, record in trending_candidates.items():
        print(f" trending candidate : {record['candidate']} ")

    return trending_candidates

def top_3_videos_by_views():
    global video_info
    values = sorted(video_info.items(), key=lambda item: item[1]["views"], reverse=True)
    top_3_videos = values[:3]

    for items in top_3_videos:
        v_id = items[0]
        views = items[1]["views"]
        likes = items[1]["likes"]
        print(f"Top video views : {views}, Top video likes : {likes}, Video id : {v_id}")

    return top_3_videos

def channel_summary():
    global video_info
    channel_summary = {}

    for record in video_info.values():
        views = record["views"]
        likes = record["likes"]
        comments = record["comments"]
        channel_id = record["chanel_id"]
        if channel_id not in channel_summary:
            channel_summary[channel_id] = {"total_views" : views, "total_videos": 1,"total_likes" : likes, "total_comments" : len(comments)}
        else :
            channel_summary[channel_id]["total_views"]+= views
            channel_summary[channel_id]["total_videos"] += 1
            channel_summary[channel_id]["total_likes"] += likes
            channel_summary[channel_id]["total_comments"] += len(comments)

    for channel_id,record in channel_summary.items():
        average_views = record["total_views"] / record["total_videos"]
        channel_summary[channel_id]["average_views"] = average_views

    for channel_id,record in channel_summary.items():
        print(f" Channel_id : {channel_id}, total_views : {record["total_views"]} , total_videos : {record["total_videos"]}, "
              f"total_likes: {record["total_likes"]} , total_comments: {record["total_comments"]}")

    return channel_summary

def remove_video():
    global video_info
    v_id = input("Enter your video id:")
    if v_id not in video_info:
        print("Video id does not exist")
        return
    else:
        # del video_info[v_id] # to delete a key from a dictionary
        video_info.pop(v_id)

while True:
    print('1. Add a new video')
    print('2. View all videos')
    print('3. View a video by video id')
    print('4. Show the most viewed video')
    print('5. Show the video with highest engagement score')
    print('6. display all unique tags used in the channel')
    print('7. Category statistics')
    print('8. Find creators-Trending candidates')
    print('9. Display the top 3 videos by views')
    print('10. Show channel summary')
    print('11. Remove a video')
    print('12. Exit')
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_video()
    elif choice == 2:
        view_all_video()
    elif choice == 3:
        search_video_by_id()
    elif choice == 4:
        max_view_video()
    elif choice == 5:
        highest_engagement()
    elif choice == 6:
        unique_tags_used_in_channel()
    elif choice == 7:
        category_statistics()
    elif choice == 8:
        trending_candidates()
    elif choice == 9:
        top_3_videos_by_views()
    elif choice == 10:
        channel_summary()
    elif choice == 11:
        remove_video()
    elif choice == 12:
        print('Exit')
        break
    else:
        print('Invalid choice')






