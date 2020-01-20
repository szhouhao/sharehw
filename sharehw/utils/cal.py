import random, re
class CalAPI(object):
    def __init__(self, request, username):
        self.request = request
        self.username = username
        self.cal_object = CalManage

    def get_cal(self):
        num=int(self.request.GET.get('num'))
        count=int(self.request.GET.get('count'))
        rg=int(self.request.GET.get('rg'))
        res=self.cal_object(num, count, rg).get_questions()
        return res
class CalManage(object):
    def __init__(self,n_count, n_num, n_range):
        self.n_count=n_count
        self.n_num=n_num
        self.n_range=n_range

    def base_cal(self,a, b, c, res):
        if a + b <= c:
            res = res + '+' + str(b)
            c = a + b
            return res, c
        elif a >= b:
            res = res + '-' + str(b)
            c = a - b
            return res, c
        else:
            return False

    def super_cal(self,xx, n_range):
        cc = 1
        if xx == 0:
            while cc:
                a = random.randint(0, n_range)
                b = random.randint(0, n_range)
                a = self.base_cal(a, b, n_range, str(a))
                if a:
                    cc = 0
                    return a
                else:
                    cc = 1
        else:
            while cc:
                a = xx[1]
                b = random.randint(0, n_range)
                a = self.base_cal(a, b, n_range, xx[0])
                if a:
                    cc = 0
                    return a
                else:
                    cc = 1

    def get_base_ques(self,n_count, n_num, n_range):  # 题目数量，个数，大小范围
        num_list = []

        for i in range(n_count):
            first_num = self.super_cal(0, n_range)
            num_list.append(first_num)
        if n_num == 2:
            res_list = num_list
        else:
            while n_num > 2:
                res_list = []
                for x in num_list:
                    s_num = self.super_cal(x, n_range)
                    res_list.append(s_num)
                num_list = res_list
                n_num -= 1
        return res_list
    def get_questions(self):
        data=[]
        maths=self.get_base_ques(self.n_count,self.n_num,self.n_range)
        for i in maths:
            dic={}
            q = str(i[0]) + '=' + str(i[1])
            cc = random.choice(re.findall(r'\d+', q))
            dd = re.sub(cc, '(    )', q, 1)
            # print(dd, '-------正确答案：', cc)
            dic['q']=dd
            dic['a']=cc
            data.append(dic)
        return data


