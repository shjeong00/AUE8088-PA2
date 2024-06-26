ang = 0
ang1 = 0
ang2 = 0 

#validation.txt로 부터 validation 리스트 받아오기
with open('validation.txt', 'r') as f:
    datas = f.readlines()

#작성할 json파일 만들기
with open('KAIST_annotation.json', 'w') as fk:
    fk.write("{\n    \"info\": {\n        \"dataset\": \"KAIST Multispectral Pedestrian Benchmark\",\n        \"url\": \"https://soonminhwang.github.io/rgbt-ped-detection/\",\n        \"related_project_url\": \"http://multispectral.kaist.ac.kr\",\n        \"publish\": \"CVPR 2015\"\n    },\n    \"info_improved\": {\n        \"sanitized_annotation\": {\n            \"publish\": \"BMVC 2018\",\n            \"url\": \"https://li-chengyang.github.io/home/MSDS-RCNN/\",\n            \"target\": \"files in train-all-02.txt (set00-set05)\"\n        },\n        \"improved_annotation\": {\n            \"url\": \"https://github.com/denny1108/multispectral-pedestrian-py-faster-rcnn\",\n            \"publish\": \"BMVC 2016\",\n            \"target\": \"files in test-all-20.txt (set06-set11)\"\n        }\n    },\n")
    fk.write("    \"images\": [\n")
    for data in datas:
        data = data.strip()
        data = data[36:53]
        eng1 = data[:5]
        eng2 = data[6:10]
        eng3 = data[11:]
        #print("{\n\"id\": "+str(ang)+",\n\"im_name\": \""+data+"\",\n\"height\": 512,\n"+"\"width\": 640\n},")
        
        if data == data[-1]:
            fk.write("        {\n            \"id\": "+str(ang)+",\n            \"im_name\": \""+eng1+"/"+eng2+"/"+eng3+"\",\n            \"height\": 512,\n"+"            \"width\": 640\n}\n")
        else:
            fk.write("        {\n            \"id\": "+str(ang)+",\n            \"im_name\": \""+eng1+"/"+eng2+"/"+eng3+"\",\n            \"height\": 512,\n"+"            \"width\": 640\n        },\n")
        ang = ang + 1
    fk.write("    ],\n    \"annotations\": [\n")
    for data in datas:
        data = data.strip()
        data = data[36:53]
        with open('./datasets/kaist-rgbt/train/labels/'+data+'.txt', 'r') as f:
            ongs = f.readlines()
            for ong in ongs:
                if ong == "[]":
                    pass
                else:
                    ong = ong.strip()
                    #print(ong)
                    list_ong = ong.split(" ")
                    #print(list_ong[0])
                    print("        {\n            \"id\": "+str(ang2)+",\n    \"image_id\": "+str(ang1)+",\n    \"category_id\": "+list_ong[0]+",\n"+"    \"bbox\": [\n        "+str(float(list_ong[1])*640)[:-2]+",\n        "+str(float(list_ong[2])*512)[:-2]+",\n        "+str(float(list_ong[3])*640)[:-2]+",\n        "+str(float(list_ong[4])*512)[:-2]+"\n    ],\n    \"height\": "+str(float(list_ong[4])*512)[:-2]+",\n    \"occlusion\": "+list_ong[5]+",\n    \"ignore\": 0\n},")
                    #fk.write("{\n    \"id\": "+str(ang2)+",\n    \"image_id\": "+str(ang1)+",\n    \"category_id\": "+list_ong[0]+",\n"+"    \"bbox\": [\n        "+str(int(float(list_ong[1])*640))+",\n        "+str(int(float(list_ong[2])*512))+",\n        "+str(int(float(list_ong[3])*640))+",\n        "+str(int(float(list_ong[4])*512))+"\n    ],\n    \"height\": "+str(int(float(list_ong[4])*512))+",\n    \"occlusion\": "+list_ong[5]+",\n    \"ignore\": 0\n},\n")
                    fk.write("        {\n            \"id\": "+str(ang2)+",\n            \"image_id\": "+str(ang1)+",\n            \"category_id\": "+list_ong[0]+",\n"+"            \"bbox\": [\n                "+str(int(float(list_ong[1])*640))+",\n                "+str(int(float(list_ong[2])*512))+",\n                "+str(int(float(list_ong[3])*640))+",\n                "+str(int(float(list_ong[4])*512))+"\n            ],\n            \"height\": "+str(int(float(list_ong[4])*512))+",\n            \"occlusion\": "+list_ong[5]+",\n            \"ignore\": 0\n        },\n")
                    ang2 = ang2 + 1
        ang1 = ang1 + 1

    fk.write("    ],\n    \"categories\": [\n        {\n            \"id\": 0,\n            \"name\": \"person\"\n        },\n        {\n            \"id\": 1,\n            \"name\": \"cyclist\"\n        },\n        {\n            \"id\": 2,\n            \"name\": \"people\"\n        },\n        {\n            \"id\": 3,\n            \"name\": \"person?\"\n        }\n    ]\n}")

'''
with open('kaist_ano1.txt', 'r') as f:
    for item in datas:
        data1 = data1.strip()
        f.write("{\n" % item)

with open('kaist_ano2.txt', 'r') as f:
    for item in datas:
        f.write("%s" % item)
#data
'''