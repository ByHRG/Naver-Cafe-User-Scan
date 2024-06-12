import sys
import requests


class Naver:

    def naver_check(self, url):
        try:
            ClubId = requests.get('https://cafe.naver.com/'+url.split('.com/')[-1].split('/')[0]).text.split('g_sClubId = "')[-1].split('";')[0].split("?")[-1]
            req = requests.get(f"https://apis.naver.com/cafe-web/cafe-articleapi/v3/cafes/{ClubId}/articles/{url.split('/')[-1]}/siblings?limit=100&fromAllArticleList=false&page=1")
            for i in req.json()["result"]["articles"]["items"]:
                if str(i["id"]) == url.split('/')[-1]:
                    sys.stdout.write(f'\r{i["writerNick"]}\n{i["writerId"]}\n{i["writerMemberKey"]}\n')
                    sys.stdout.flush()
                    break
        except:
            sys.stdout.write(f'\r문제가 발생했습니다. 잠시후 재시도 하시거나 문의 바랍니다.\n')
            sys.stdout.flush()


    def naver_comment_check(self, url):
        page = 1
        check_list = []
        flop = False
        try:
            ClubId = requests.get('https://cafe.naver.com/' + url.split('.com/')[-1].split('/')[0]).text.split('g_sClubId = "')[-1].split('";')[0].split("?")[-1]
            choice = str(input("댓글 조회 기능을 선택해주세요\n1 - 특정 댓글 작성자 조회\n2 - 모든 댓글 작성자 리스트 조회:"))

            if choice == "1":
                while True:
                    comment_url = f"https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/{ClubId}/articles/{url.split('/')[-1]}/comments/pages/{page}?requestFrom=A&orderBy=asc&fromPopular=true"
                    req = requests.get(comment_url)
                    for i in range(len(req.json()["result"]["comments"]["items"])):
                        if req.json()["result"]["comments"]["items"][i]["id"] in check_list:
                            flop = True
                            break
                        check_list.append(req.json()["result"]["comments"]["items"][i]["id"])
                        content = req.json()["result"]["comments"]["items"][i]["content"].replace("\r\n", " ")
                        sys.stdout.write(f'\r{i+1}:{req.json()["result"]["comments"]["items"][i]["writer"]["nick"]} - {content}\n')
                        sys.stdout.flush()
                    if flop:
                        break
                    take = str(input("아이디 확인을 원하는 댓글 번호를 입력해주세요\n빈칸 입력시 다음 페이지로 이동하거나 종료됩니다:"))
                    if take != "":
                        sys.stdout.write(f'\r{req.json()["result"]["comments"]["items"][int(take)-1]["writer"]["nick"]} - {req.json()["result"]["comments"]["items"][int(take)-1]["writer"]["id"]}\n')
                        sys.stdout.flush()
                    else:
                        page = page + 1
            elif choice == "2":
                id_list = []
                while True:
                    comment_url = f"https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/{ClubId}/articles/{url.split('/')[-1]}/comments/pages/{page}?requestFrom=A&orderBy=asc&fromPopular=true"
                    req = requests.get(comment_url)
                    if len(req.json()["result"]["comments"]["items"]) == 0:
                        break
                    for i in range(len(req.json()["result"]["comments"]["items"])):
                        if req.json()["result"]["comments"]["items"][i]["id"] in check_list:
                            flop = True
                            break
                        check_list.append(req.json()["result"]["comments"]["items"][i]["id"])
                        content = req.json()["result"]["comments"]["items"][i]["content"].replace("\r\n", " ")
                        if req.json()["result"]["comments"]["items"][i]["writer"]["id"] not in check_list:
                            sys.stdout.write(f'\r{req.json()["result"]["comments"]["items"][i]["writer"]["nick"]} - {content}\n')
                            sys.stdout.flush()

                        if f'{req.json()["result"]["comments"]["items"][i]["writer"]["nick"]} - {req.json()["result"]["comments"]["items"][i]["writer"]["id"]}' not in id_list:
                            id_list.append(f'{req.json()["result"]["comments"]["items"][i]["writer"]["nick"]} - {req.json()["result"]["comments"]["items"][i]["writer"]["id"]}')
                    if flop:
                        break
                    page = page + 1
                for i in id_list:
                    print(i)

        except Exception as E:
            sys.stdout.write(f'\r{E}\n문제가 발생했습니다.\n조회가 불가능한 게시글이거나\n잠시후 재시도 하시거나 문의 바랍니다.\n')
            sys.stdout.flush()



    def naver_profile_check(self, url):
        try:
            ClubId = requests.get('https://cafe.naver.com/'+url.split('.com/')[-1].split('/')[0]).text.split('g_sClubId = "')[-1].split('";')[0].split("?")[-1]
            req = requests.get(f"https://apis.naver.com/cafe-web/cafe-articleapi/v3/cafes/{ClubId}/articles/{url.split('/')[-1]}/siblings?limit=100&fromAllArticleList=false&page=1")

            for i in req.json()["result"]["articles"]["items"]:
                if str(i["id"]) == url.split('/')[-1]:
                    sys.stdout.write(f'\r{i["writerNick"]}\n{i["writerId"]}\n')
                    sys.stdout.flush()
                    break
        except:
            sys.stdout.write(f'\r문제가 발생했습니다. 잠시후 재시도 하시거나 문의 바랍니다.\n')
            sys.stdout.flush()
    def run(self):
        print("by Pv\nVer 0.1.1")
        while True:
            choice = str(input("1 - 게시글 작성자 조회\n2 - 댓글 작성자 조회:"))
            if choice == "1":
                url = input("url(ex:):")
                self.naver_check(url)
            elif choice == "2":
                url = input("url(ex:):")
                self.naver_comment_check(url)


Naver().run()
