import json
import define
k="cong nghe thong tin"
data_file=open('data.json').read()
intents=json.loads(data_file)
# a=[]
# tt=0
# question="thực tập của ngành cntt ở đâu v ạ".lower().strip()
k=[]
for intent in intents["intents"]:
     if intent["tag"]=="tohopxettuyen":
        for pattern in intent["patterns"]:
            if "cong nghe thong tin" in define.no_accent_vietnamese(pattern):
                pattern=pattern.lower()
                pattern=define.alias(pattern)
                a=pattern
                pattern=a.replace("công nghệ thông tin","khoa học máy tính")
                print('"'+pattern+'"'+",")
                pattern=a.replace("công nghệ thông tin","hệ thống thông tin")
                print('"'+pattern+'"'+",")
                pattern=a.replace("công nghệ thông tin","kĩ thuật phần mềm")
                print('"'+pattern+'"'+",")
# with open('userdata.txt', 'w') as f:
#     f.writelines('\n'.join(k))
            # if pattern.lower().strip() == question :
            #         print("YES")
# print(tt)
