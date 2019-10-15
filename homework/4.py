#   file_name:读入或写入的文件名称
#   data_list:读入或写入的数据链表
#   data_tpye:数据类型
#       1:int;2:float;3:string
#   n:矩阵维度

def f_write(file_name,data_list,n=2,data_type=1):
    f = open(file_name,'w')
    if n != 2:
        for datas in data_list:
            datas = str(datas)
            f.write(datas.replace('[', '').replace('],', '|').replace(']', '|').replace("'", '').replace('"', ''))
    elif n == 2:
        for line in data_list:
            if data_type == 3:
                line = str(line).replace('[', '').replace(']', '').replace("'",'').replace('"','')
                line = line + '\n'
            else :
                line = str(line).replace('[','').replace(']','')
                line = line+'\n'
            f.write(line)
    f.close()

def f_read(file_name,output_list=[],n=2,data_type=1):
    f = open(file_name,'r')
    if n != 2:
        for line in f:
            line = line.replace(' ','')
            line = line.split('|')
            print(line)
            t1 = []
            t2 = []
            for nums in line:
                temp=''
                for num in nums:
                    if num == ',' or num == ' ':
                        if data_type == 1:
                            t1.append(int(temp))
                        elif data_type == 2:
                            t1.append(float(temp))
                        elif data_type == 3:
                            t1.append(str(temp))
                        temp=''
                        continue
                    temp+=num
                if temp != '':
                    if data_type == 1:
                        t1.append(int(temp))
                    elif data_type == 2:
                        t1.append(float(temp))
                    elif data_type == 3:
                        t1.append(str(temp))
                if len(t1) != 0:
                    t2.append(t1)
                    t1=[]
                else:
                    if len(t2) != 0:
                        output_list.append(t2)
                        t2 = []
    elif n == 2:
        for line in f:
            line = line.replace('\n','').split(',')
            print(line)
            if data_type == 1:
                datas = [int(num) for num in line ]
            elif data_type == 2:
                datas = [float(num) for num in line]
            else:
                datas = [str(num) for num in line]
            output_list.append(datas)
    f.close()
    print(output_list)

# =========== test on n=3 int =============
int_3_list=[[[1,2,2,3],[2,3,3,4]],[[1,2,2,3],[2,3,3,4]],[[1,2,2,3],[2,3,3,4]]]
f_write('int_3_test.txt',int_3_list,n=3)
int_o_3_list=[]
f_read('int_3_test.txt',int_o_3_list,n=3)
print('------------------------')

# --- test on n=3 string ---
str_3_list = [[['a','b','c'],['d','ef','g']],[['a','b','c'],['d','ef','g']]]
str_o_3_list=[]
f_write('str_3_test.txt',str_3_list,n=3,data_type=3)
f_read('str_3_test.txt',str_o_3_list,n=3,data_type=3)
# print(str_3_list)
print('------------------------')

# --- test on n=3 float ---
float_3_list = [[[1.11,2.22,3.33],[1.34,2.45,3.56]],[[1.11,2.22,3.33],[1.34,2.45,3.56]]]
float_o_3_list=[]
f_write('float_3_test.txt',float_3_list,n=4,data_type=2)
f_read('float_3_test.txt',float_o_3_list,n=4,data_type=2)
# print(float_3_list)

# # =========== test on int data_type =============
# int_list = [[1,2,2,3],[2,3,3,4]]
# int_o_list=[]
# f_write('int_test.txt',int_list)
# f_read('int_test.txt',int_o_list)
#
# # ========= test on float data_type =============
# float_list = [[1.11,2.22,3.33],[1.34,2.45,3.56]]
# float_o_list=[]
# f_write('float_test.txt',float_list,data_type=2)
# f_read('float_test.txt',float_o_list,data_type=2)
#
# # ========= test on string data_type ============
# str_list = [['a','b','c'],['d','ef','g']]
# str_o_list=[]
# f_write('str_test.txt',str_list,data_type=3)
# f_read('str_test.txt',str_o_list,data_type=3)
