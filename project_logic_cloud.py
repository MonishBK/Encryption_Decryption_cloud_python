import random as r
import time as t
import numpy as np
import math
import qrcode 
import cv2
import os
from datetime import datetime 
from google.cloud import storage
from pyzbar.pyzbar import decode
from PIL import Image 


# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'advigroup-cd4012038029.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'advigroup-371807-4e323780e417.json'

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "advi_bucket"

# Creates the new bucket
# bucket = storage_client.create_bucket(bucket_name)

# print(f"Bucket {bucket.name} created.")

# accessing the bucket
# my_bucket = storage_client.get_bucket(bucket_name)

# Upload bucket
def Upload_to_bucket(blob_name, file_path):
    try:
        # print(blob_name,file_path)
        bucket = storage_client.get_bucket("advi_bucket")
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False
    
def download_blob(source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket("advi_bucket")
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    
def delete_blob( blob_name):

    storage_client = storage.Client()

    bucket = storage_client.bucket("advi_bucket")
    blob = bucket.blob(blob_name)
    blob.delete()
    return True
    
# delete_blob("Encrypted/sxcsc")

# source_blob_name = "Decrypted/api_decrypt.txt"
# destination_file_name = "E:/VS Code Programs/ADVI Group/hello.txt"
# download_blob(source_blob_name, destination_file_name)
    
# list of Objects 
def File_List( pre_fix, ch):
    try:
        bucket = storage_client.get_bucket("advi_bucket")
        blobs = list(bucket.list_blobs(prefix=pre_fix))

        dir_list = []

        # Encrypted files
        if ch == 1:
            for blog in blobs:
                dir_list.append(blog.name[10 : blog.name.rindex("/")])
            return list(set(dir_list))

        # specific folder files
        elif ch == 2:
            for blog in blobs:
                if blog.name[blog.name.rindex("/")+1: ] != "":
                    dir_list.append(blog.name[blog.name.rindex("/")+1: ])
            return list(set(dir_list))

    except Exception as e:
        print(e)
        # return  
        
def Display_Objects(ch , name=""):
    if ch == 1:
        if name == "":
            return File_List('Encrypted/',1)   
        else:
            return File_List(f'Encrypted/{name}',2)  
    elif ch == 2:
        return File_List('Decrypted/',2)
    elif ch == 3:
        return File_List("input_files/", 2)

    
def Write_to_bucket(blob_name, item, item_val, mode="w", bucket_name="advi_bucket"):

    if mode == "w":
        try:
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            # blob.upload_from_filename(file_path)
            print("item val => ",item_val)
            
            with blob.open(mode,encoding="utf-8") as f:
                f.write(f"{item} {item_val} ")
            # return True
        except Exception as e:
            print(e)
            # return False
    elif mode == "a":
        # print("mode is append => ",item,item_val)
        try:
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            # blob.upload_from_filename(file_path)
            with blob.open('w',encoding="utf-8") as f:
                f.write(f"{item} \n\n{item_val}\n")
            # return True
        except Exception as e:
            print(e)
            # return False
    elif mode == "u":
        # print("mode is append => ",item,item_val)
        try:
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            # blob.upload_from_filename(file_path)
            with blob.open('w',encoding="utf-8") as f:
                f.write(f"Date : {item} \n")
                f.write(f"Plane Text : {item_val}")
            # return True
        except Exception as e:
            print(e)
            # return False
        
    

file_path = "E:\VS Code Programs\ADVI Group\objective_05"
# name = "moni"
# blob_name = "input_files/input"
# Upload_to_bucket(blob_name,os.path.join(file_path, "input.txt") , bucket_name)
# Upload_to_bucket(name, os.path.join(file_path, name), bucket_name)

def read_bucket(blob_name, bucket_name,ch):

    if ch == 1:
        try:
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            
            with blob.open("r",encoding="utf-8") as f:
            # print(f.read())
                f_data = f.readlines()

            # print(f_data)
            return f_data
        except Exception as e:
            print(e)
            return 

    elif ch == 2:
        try:
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            
            with blob.open("r",encoding="utf-8") as f:
            # print(f.read())
                f_data = f.read()

            return f_data
        except Exception as e:
            print(e)
            return 

# read_bucket("input", bucket_name)
# print(read_bucket("codeBook.txt", bucket_name,1)[0])
# data = read_bucket("input_files/input", "advi_bucket",2)
# print(data)


# reading file data
def fileDataRead(file_name,ch,item=""):
    if ch == 1:
        with open(file_name,encoding="utf-8") as f:
            return f.readlines()  

    elif ch == 2:
        with open(file_name,encoding="utf-8") as f:
            return f.read() 
    
    elif ch == 3:
        with open(file_name,encoding="utf-8") as f:
                i=0
                pat_line = -1
                content = True
                while content:
                    content = f.readline()
                    if item in content:
                        return i
                    i+=1 

# LCG random number 
def LCG():
    min_val= 2
    max_val= 150
    a= 17
    c=43
    xn = 15315

    # m = r.randint(min_val,max_val)
    m = 100
    xn = ((a * xn) + c) % m
    rand = xn + m
    sec_num = r.randint(min_val,max_val)
    return rand ^ sec_num

# fragment generation
def Fragment_Gen(input_file,count = 0):

    if count == 0:
        # print("input_file =>",input_file)
        # data = fileDataRead(input_file,2).strip().replace(" ", "︻")
        # data = read_bucket("input", bucket_name,2)
        data = read_bucket(input_file, bucket_name, 2)
        # print("input data => ",data)
        data = data.replace(" ", "︻")
        size = len(data)
        start = 0
        frag = []
        while size != 0:
            N = LCG()
            frag_size = int(size/N)
            end = start+frag_size
            s_val = slice(start,end)
            if (size <= frag_size) or frag_size == 0:
                frag.append(data[start:])
                size = 0
            else:
                frag.append(data[s_val])
                size-=frag_size
            start+=frag_size   
    else:
        # data = fileDataRead(input_file,2).strip().replace(" ", "︻")
        data = read_bucket(input_file, bucket_name,2).strip().replace(" ", "︻")
        size = len(data)
        start = 0
        frag = []
        while count != 0:
            N = LCG()
            frag_size = int(size/N)
            end = start+frag_size
            s_val = slice(start,end)
            if (size <= frag_size) or frag_size == 0:
                frag.append(data[start:])
                size = 0
                count = 0
            else:
                frag.append(data[s_val])
                size-=frag_size
                count-=1
            start+=frag_size  

    return frag

# shuffling the codeBook.txt data 
def interchange(list_val,key):
    c=-1
    while True:
        if int(key[c]) <= 0:
            c-=1
        else:
            k = int(key[c])
            break
    i = 0
    new_list = []
    l_len = len(list_val)
    while i != l_len:
        if k >= l_len:
            k-=l_len 
        rand = list_val[k]
        if rand not in new_list:
            new_list.append(rand)
            i+=1
            k+=1
    return new_list

# converting list to string
def List_to_String(data):
    str_val=""
    for i in data:
        str_val+=i+" "
    return str_val

# fragment encryption
def fragment_Encrypt(input_txt):
    
    ts = t.time()
    # letters = fileDataRead("codeBook.txt.txt",1)[0].strip().split(" ")
    # symbol = fileDataRead("codeBook.txt.txt",1)[1].strip().split(" ")
    letters = read_bucket("codeBook.txt", bucket_name,1)[0].strip().split(" ")
    symbol = read_bucket("codeBook.txt", bucket_name,1)[1].strip().split(" ")
    frag_text = input_txt
    letters = interchange(letters,str(ts)[-3:])
    symbol  = interchange(symbol,str(ts)[-3:])

    i=0
    n=0
    frag_data = {}
    new_sy = ""
    for i in frag_text:
        cypher_Text=""
        # new_sy = 
        for j in i:   
            li = letters.index(j)
            sy = symbol[li]
            cypher_Text+=sy 
        # frag_data.update({symbol[n]: cypher_Text})
        frag_data.update({f"{new_sy}{symbol[n]}": cypher_Text})
        if n == len(symbol)-1:
            n=0
            new_sy+=symbol[n]
        else:
            n+=1
       
    return [frag_data,ts]

# converting the  data fragments into pattern
def lineCypher(size,frag):   
    k = 0
    # symbol = fileDataRead("codeBook.txt.txt",1)[1].strip().split(" ") 
    symbol = read_bucket("codeBook.txt", bucket_name,1)[1].strip().split(" ")  
    # h_range = int(len(frag)/2)
    h_range = size - len(frag)-1
    start = r.randint(0, h_range)
    end = len(frag)-1
    st_ed = "∴"
    flag = False
    cypher = ""
    for i in range(size):
        sym = r.choice(symbol)
        # print("symbol => ",sym)

        if start == i:
            cypher+=f"{st_ed} "
            flag = True
        elif flag:
            cypher+=f"{frag[k]} "
            if k != end:
                k+=1
            else:
                cypher+=f"{st_ed} "
                flag=False
        else:
            cypher+=f"{sym} "
    
    return cypher 

def BoxCypher(size,frag,start_size):
    cypher = lineCypher(size-1,frag)
    # mat = np.empty(size,dtype = str )
    lt = cypher.strip().split(" ")
    
    c = start_size
    pat =""
    items = 0
    for i in range(0,start_size-1):
        pat+=i*" "
        for j in range(0,c-1):
            pat+=f"{lt[items]} " 
            items+=1
        pat+="\n"
        c-=1

    return [pat.strip(),lt]
 
def QR_Generator(data,name,blob_name):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.clear()
    qr.add_data(data)
    qr.make(fit=True)
    try:
        img = qr.make_image(fill_color="black", back_color="white")
        
        cr = os.getcwd()
        # os.chdir(dir)
        qr_name = f"{name}.png"
        img.save(qr_name)
        print("QR Code Generated!!..")
        Upload_to_bucket(f"{blob_name}/{qr_name}",os.path.join(cr, qr_name))
        os.remove(os.path.join(cr, qr_name))
        # os.chdir(cr)
        return qr_name   
    except Exception as e:
        print(e)
    

def read_qr_code(file_name):
    try:
        
        img=cv2.imread(file_name)
        det=cv2.QRCodeDetector()
        val, pts, st_code=det.detectAndDecode(img)
        os.remove(file_name)
        return val
        
    except:
        return

# pattern customization
def customizedPat(ch, frag, level, ts, name):
    frag_keys = ""
    
    for item in frag:
        frag_keys+=item+" "

    frag_keys = frag_keys.strip().split(" ")
    
    # dest_direct = os.getcwd()
    # d_path = os.path.join(dest_direct, name)
    # d_path = d_path.replace('\\', '/')
    # os.mkdir(d_path) 
    # f_path = os.path.join(d_path, "data.txt")
    # f_path = f_path.replace('/', '\\')
    
    
    print("frag_keys = >",frag_keys,"\n",len(frag_keys))
    # exit()
    
    size = len(frag_keys)*level
    if ch == 1: 
        cypher = lineCypher(size,frag_keys)     
             
    elif ch == 2:
        print("size => ", size)
        # exit()
        
        for i in range(1,size):
            if sum(range(1,i)) >= size:
                st_val = i-1
                break
        else:
            st_val = sum(range(1,size))
        print("st_val => ",st_val)
        
        # st_val = r.randint(1, size-len(frag_keys))
        
        size = sum(range(1,st_val))
        print("new size => ",size)
        cypher_data = BoxCypher(size,frag_keys,st_val) 
        cypher = cypher_data[0]  
        l_cypher = cypher_data[1]
        print("Cypher Text => \n",cypher)  
        # exit()               

    elif ch == 3:
        cypher = lineCypher(size,frag_keys)
        l_cypher = cypher.strip().split()
        file_name = QR_Generator(cypher,name,f"Encrypted/{name}")  
        cypher = file_name 
        print("Cypher Text => \n",cypher)  
        
    data = Fragment_Gen("dammy.txt",int(size-len(frag_keys)+2))
    d_frag = fragment_Encrypt(data)
    d_frag_val = list(d_frag[0].values())

    i = 0 
    j = 0
    flag = False
    print(len(l_cypher))
    for item in l_cypher:
        fr = f"frag{j}.txt"
        
        print(f"frag{j}.txt")
        
        fr_path = os.path.join(f"Encrypted/{name}", fr)
        fr_path = fr_path.replace('\\', '/')
        
        if item == "∴":
            if flag == False:
                flag = True
            else:
                flag = False

            # with open(fr_path, "w" , encoding="utf-8") as f:
            #     f.write(f"{item} {d_frag_val[i]} ")
            Write_to_bucket(fr_path, item, d_frag_val[i])
            i+=1
        elif flag:
            # with open(fr_path, "w" , encoding="utf-8") as f:
            #     f.write(f"{item} {frag.get(item)} ")
            Write_to_bucket(fr_path, item, frag.get(item))
        else:
            # with open(fr_path, "w" , encoding="utf-8") as f:
            #     f.write(f"{item} {d_frag_val[i]} ")
            Write_to_bucket(fr_path, item, d_frag_val[i])
            i+=1
        j+=1             
        
    # with open(f_path, "a" , encoding="utf-8") as f:
    #     f.write(f"{ts} \n")
    #     f.write(f"\n{cypher} \n") 
    fr_path = os.path.join(f"Encrypted/{name}", "data.txt")
    fr_path = fr_path.replace('\\', '/')
    Write_to_bucket(fr_path, ts, cypher,"a") 
              
    
    return cypher

# pattern selection
def patternSelection(frag,ts,name,pat_sel,level):
    data = customizedPat(pat_sel, frag,level,ts,name) 
    return data
  
# Decryption 
def decrypt_Fragments(letters,symbols,plain_text):
    
    txt =""
    for i in range(len(plain_text)):
        ch = plain_text[i]
        sym = symbols.index(ch)
        txt+= letters[sym]     
    
    return txt.replace("︻", " ")
    

def Load_Data(src):
    # print("src data => ",src)
    # cr_dir = os.getcwd()
    # os.chdir(src)
    # src_path = os.getcwd()
    # print(src_path)
    # name = src_path[src_path.rindex("\\")+1:]
    name = src
                 
    # log_data = fileDataRead("data.txt",1)
    log_data = read_bucket(f"Encrypted/{name}/data.txt", bucket_name,1)
    
    print(log_data)
    ts = log_data[0].strip()
    
    # print(ts)
    
    pat_line = 2
    p = pat_line
    p1=0
        
    if ".png" in log_data[pat_line].strip():
        file_name = log_data[pat_line].strip()
        cr = os.getcwd()
        download_blob(f"Encrypted/{name}/{file_name}", os.path.join(cr, file_name))
        # print("file name => ",file_name)
        qr_data = read_qr_code(file_name)
        arr = qr_data.split(" ")
    else:
        arr = []
        for i in range(2,len(log_data)):
            val = log_data[i].strip().split(" ")
            for j in val:
                arr.append(j)
    
    # print(arr)
    
    cypher_list = "".join(arr)
    start = cypher_list.index("∴") 
    end = cypher_list.rindex("∴") 
    # print(cypher_list)

    # print(start,end)

    # ls = os.listdir()[1:]
    # ls = Display_Objects(1,name)
    # print("display files => ", ls)
    frag_data = {}
    for i in range(start+1,end):
        # f_name = f"frag{i}.txt"
        f_name = f"Encrypted/{name}/frag{i}.txt"
        check = read_bucket(f_name, bucket_name,1)
        # print("check data => ",check)
        # c_data = fileDataRead(f_name,1)[0].strip().split(" ")
        c_data = read_bucket(f_name, bucket_name,1)[0].strip().split(" ")
        # print("c_data => ",c_data)
        frag_data.update({c_data[0] : c_data[1]})
        
    # print("frag_data => ",frag_data)
    

    org = []
    for key in frag_data:
        org.append(frag_data.get(key))
        
        
    # print(frag_data)
    # print(org)  
    # os.chdir(cr_dir)
    # letters = fileDataRead("codeBook.txt.txt",1)[0].strip().split(" ")
    # symbol = fileDataRead("codeBook.txt.txt",1) [1].strip().split(" ")
    letters = read_bucket("codeBook.txt", bucket_name,1)[0].strip().split(" ")
    symbol = read_bucket("codeBook.txt", bucket_name,1)[1].strip().split(" ")
    letters = interchange(letters,ts[-3:])
    symbol  = interchange(symbol,ts[-3:])
    
    # print("letters =>",letters)
    # print("symbol =>",symbol)
    # print("user name => ",name)
    # os.chdir(dest)
    date_time = datetime.fromtimestamp(float(ts))
    org_data =  decrypt_Fragments(letters,symbol,"".join(org)) 
    # path = f"{name}_decrypt.txt" 
    # with open(path, 'w') as f:
    #     f.write(f"Date : {date_time} \n")
    #     f.write(f"Plane Text : {org_data}")
        
    fr_path = os.path.join(f"Decrypted/", f"{name}_decrypt.txt")
    fr_path = fr_path.replace('\\', '/')
    Write_to_bucket(fr_path, date_time, org_data,"u") 
        
        

# main method
def main(name,file_name,pattern,level):

    # print(f" {name}\n {ch}\n {input_file}\n {pattern}\n {level}\n {dest_direct} ")
    # if ch == 1 : 
        # log_data = fileDataRead("log.txt",2)
            
        d = Fragment_Gen(f"input_files/{file_name}") 
        # print(d)
        frag_data = fragment_Encrypt(d)
        
        # return patternSelection(frag_keys,frag_data[1],name,pattern,level)
        return customizedPat(pattern, frag_data[0], level, frag_data[1], name) 

    # elif ch == 2:
    #     Load_Data(src,dest)
