#encoding=utf-8

import os,sys

star_file = "D:/web/source/_posts/zhengshuang.md"
url = 'https://raw.githubusercontent.com/liweixiong0621/star/master/zhengshuang/'
old_list = []
path = "zhengshuang/"
image_list = os.listdir(path)

for filename in image_list:
    name, fileformat = filename.split(".")
    if fileformat.lower() == "jpg" or fileformat.lower() == "png" or fileformat.lower() == "gif":
        #name_list.append(filename)
    	content = "<img src=" + "'"+ url + filename + "'" + ''+"width='200' height='300'>"
        with open(star_file,'a+') as f:
            lines = f.readlines()
            for line in lines:
                old_list.append(line)
            if content not in lines:
                f.write(content)
                f.write("\n")
                print("add sucess")
            else:
                print("exits")
                break

        f.close()
os.system('git add --all')
os.system('git commit -m "add photos"')
os.system('git push origin master')
#<img src = 'https://raw.githubusercontent.com/liweixiong0621/star/master/郑爽/2020-01-12_006B0JhPgy1gakhbcg0y5j34kn39l4qs.jpg' width="200" height="300">