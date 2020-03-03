from flask import Flask,request,render_template,flash,session
import database
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# 用户个人信息管理类
class userInfoManage(object):
    def __init__(self, id):
    def updateInfo(self):
    def viewInfo(self):


# 用户功能类
class userDo(object):
    userStatus = 0
    def __init__(self):

    # 阅览话题(直接显示主页面中的内容)
    def Browse(self):

    # 关键词搜索话题
    def keyQuary(self):

    # 显示注册页面
    def showRegister(self):
        return render_template("register.html")

    # 显示登陆页面
    def showLogin(self):

    # 注册为注册用户(参数待调整)
    def doUserRegister(self, name, pwd, methods=['GET']):
        self.name = request.args.get("uname")
        self.pwd = request.args.get("upwd")
        if database.optSuccess == 1:
            # 注册成功
            flash("注册成功")
            return render_template("index.html")
        else:
            # 注册失败
            flash("注册失败")
            return render_template("register.html")

    # 注册为注册用户(参数待调整)
    def doUserRegister(self, name, pwd, methods=['GET']):


class memberDo(userDo, userInfoManage):
    # 是否注册用户(公有)
    userStatus = 1
    # 是否禁言状态（私有）
    __isMute = 0

    def __init__(self):

    def userCollectAdd(): # 增加收藏

    def userCollectDel(): # 删除收藏

    def userCollectShow(): # 展示收藏

    def userAttentionAdd(): # 增加关注

    def userAttentionDel(): # 删除关注

    def userAttentionShow(): # 展示关注用户名单（获得 查看该用户提问，回答 权限）

    def raiseQuestion(self):
        def questionPublish(): # 提问
        def questionEdit(): # 编辑问题
        def questionDelete(): # 删除问题

    def AnswerQuestion(self):
        def answerPublish():
        def answerEdit():
        def answerDelete():

    def ManageQuestion(self): # 新增：查看自己的提问记录（有必要吗）

    def ManageAnswer(self): # 新增：查看自己的回答记录

class Admin(memberDo):
    userStatus = 2
    # 禁言注册用户
    def muteMember(self):

    # 解除注册用户禁言
    def unmuteMember(self):

    # 删除注册用户
    def deleteMember(self):

    # 获得指定注册用户所有或部分权限
    def manageMember(self): #获得指定member的所有权限，我觉得这样简单些（或者查看及删除指定member的提问与回答记录）

    def DeleteQuestion(self): #删除指定提问

    def DeleteAnswer(self):  # 删除指定回答

class dbHelper(): # 单独一个py文件放database

if __name__ == '__main__':
    app.run()

