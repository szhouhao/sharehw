import random, re, uuid, xlwt
from django.shortcuts import render, HttpResponse, redirect


class CalAPI(object):
    def __init__(self, request, username):
        self.request = request
        self.username = username
        self.cal_object = CalManage

    def get_cal(self):
        num = int(self.request.GET.get('num'))
        count = int(self.request.GET.get('count'))
        rg = int(self.request.GET.get('rg'))
        res = self.cal_object(num, count, rg).get_questions()
        return res

    def get_excel_cal(self):
        num = int(self.request.GET.get('num'))
        count = int(self.request.GET.get('count'))
        rg = int(self.request.GET.get('rg'))
        res = self.cal_object(num, count, rg).get_excel_cal()
        # return redirect('http://192.168.4.81:5000/static/%s'%res)
        return res

    def doc_upload(self):
        doc_name = self.request.FILES.get('docname')
        print(doc_name)
        assert doc_name, '请选择文件'
        upload_path = f'/data/uploads/{doc_name}'
        with open(upload_path, 'wb') as f:
            for i in doc_name.chunks():
                f.write(i)
        return HttpResponse('感谢您的分享！')


class CalManage(object):
    def __init__(self, n_count, n_num, n_range):
        self.n_count = n_count
        self.n_num = n_num
        self.n_range = n_range

    def base_cal(self, a, b, c, res):
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

    def super_cal(self, xx, n_range):
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

    def get_base_ques(self, n_count, n_num, n_range):  # 题目数量，个数，大小范围
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
        data = []
        maths = self.get_base_ques(self.n_count, self.n_num, self.n_range)
        for i in maths:
            dic = {}
            q = str(i[0]) + '=' + str(i[1])
            cc = random.choice(re.findall(r'\d+', q))
            dd = re.sub(cc, '(    )', q, 1)
            # print(dd, '-------正确答案：', cc)
            dic['q'] = dd
            dic['a'] = cc
            data.append(dic)
        return data

    def get_excel_cal(self):
        data = []
        maths = self.get_base_ques(self.n_count, self.n_num, self.n_range)
        cal_excel = xlwt.Workbook()
        qsheet = cal_excel.add_sheet('题目')
        asheet = cal_excel.add_sheet('答案')
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.height = 20 * 13
        style.font = font
        pat = xlwt.Pattern()
        style.pattern = pat
        nid = 1
        col_num = 0
        row_num = 1
        for i in maths:
            q = str(i[0]) + '=' + str(i[1])
            cc = random.choice(re.findall(r'\d+', q))
            dd = re.sub(cc, '(    )', q, 1)
            qsheet.write(row_num, col_num, str(nid) + '、')
            qsheet.write(row_num, col_num + 1, dd, style)
            qsheet.row(0).height_mismatch = True
            qsheet.col(col_num).width = 256 * 5
            qsheet.col(col_num + 1).width = 256 * 25
            qsheet.row(row_num).height = 40 * 80
            asheet.write(row_num, col_num, str(nid) + '、')
            asheet.write(row_num, col_num + 1, cc, style)
            qsheet.row(0).height_mismatch = True
            asheet.col(col_num).width = 256 * 5
            asheet.col(col_num + 1).width = 256 * 25
            asheet.row(row_num).height = 40 * 80
            nid += 1
            col_num += 2
            if col_num >= 6:
                col_num = 0
                row_num += 1
        excel_name = str(uuid.uuid1()) + '.xlsx'
        cal_excel.save("/data/AEApps/sharehw/sharehw/static/file/%s" % excel_name)
        return excel_name
