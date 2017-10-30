from friend.models import Friend
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.
def index():
  pass

def get_friend_list(request):

#検索用データの取得
    requested_user = request.user.id
    follow_user = request.user.id

    #ログインユーザが友達申請をしている、または申請されているユーザ一覧
    friendList = Friend.objects.filter(Q(requested_user=requested_user) | Q(follow_user=follow_user),
                                       Q(request_state=1))

    print(friendList.values())

    #レスポンス用の友達リスト
    friendNameList = []

    #友達の名前取得
    if friendList:
        #IN句で使用する友達IDリスト
        friendIdList = []

        for x in friendList:
            friendIdList.append(x.requested_user)
            friendIdList.append(x.follow_user)

        #自分の名称は除外
        friendNameList = User.objects.filter(Q(id__in=friendIdList), ~Q(id = requested_user))

        print(friendNameList.values())

    return friendNameList
