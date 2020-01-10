import time, hashlib, os, uuid


class DocManageAPI(object):
    def __init__(self, request, username):
        self.request = request
        self.username = username
        self.file_object = DocManage()

    def doc_upload(self):
        print('''11111''')
        doc_name = self.request.FILES.get('docname')
        doc_chk = self.file_object.doc_upload(doc_name)
        print(doc_chk)


class DocManage(object):
    def __init__(self):
        self.upload_path = '/data/docs/'
        # self.upload_path = 'D:\\test\\'
    def doc_upload(self, doc_name) -> str:
        file_new_name = uuid.uuid1()
        houzhui=str(doc_name).split('.')[1]
        self.upload_path = f'/data/docs/{file_new_name}.{houzhui}'

        with open(self.upload_path, 'wb') as f:
            for i in doc_name.chunks():
                f.write(i)
        return self.upload_path
