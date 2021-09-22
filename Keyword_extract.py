# coding utf-8
import re
def pop(str1,nest_num):
    global if_elseif_cnt
    global  if_else_cnt
    #while str1!='': 
    for em in range(nest_num):
        if len(re.findall('10(30)+20', str1))>0:
            if_elseif_cnt+=len(re.findall('10(30)+20', str1))
            str1=re.sub('10(30)+20', '', str1)
        if len(re.findall('1020', str1)):
            if_else_cnt+=len(re.findall('1020', str1))
            str1=re.sub('1020', '', str1)
        te=re.findall('([123])100', str1)
        if len(te)>0:
            for it in te:
                st=it+'100'
                print(type(st))
                rep=it+'0'
                print(type(rep))
                re.sub(st,rep,str)
### TOP LEVEL###

if __name__ == "__main__":
    file_path=input("Welcome to C keyword statistic!\n Please input file Path:")
    level=int(input("Please input level:"))
    f=open(file_path, 'r')
    keyword_cnt=[0]*32
    sw_cnt=[0]
    sw_icnt=-1
    if_stack=0
    stack1=''
    elseif_stack=0
    elseif_flag=False
    if_flag=False
    if_elseif_cnt=0
    if_else_cnt=0
    shiled_word=['//','/\*','\*/','\"','\\\\n\\\\','#']
    annota_muti=False    
    key_word=['auto','break','case','char','const', 'continue', 'default','do',
    'double','else','enum','extern','float','for','goto','if',
    'int','long','register','return','short' ,'signed' ,'sizeof','static',
    'struct','switch', 'typedef','union','unsigned','void','volatile','while']
    cnt=1
    for u in range(len(key_word)):
        key_word[u]+='[(\ ;{]'
    total_num=0
    ###Search Layer###
    quote_pre=False
    for i in f:
#         print("line"+str(cnt))
        shloop_cnt=0
        kwloop_cnt=0
        annota_line=-1
        quote_line=False
        else_end=-1
        if_start=-1
        for sd in shiled_word:
            for match1 in re.finditer(sd,i):
                if shloop_cnt==0:
                    annota_line=match1.start()
                    break
                elif shloop_cnt==1:
                    annota_muti=True
                elif shloop_cnt==2:
                    annota_muti=False
                elif shloop_cnt==3 or shloop_cnt==5:
                    quote_line=True
                    break
                elif shloop_cnt==4 and quote_pre:
                    quote_line=True
            quote_pre=quote_line
            shloop_cnt+=1
        for kw in key_word:
            for match in re.finditer(kw,i):
                if quote_line or annota_muti or match.start()<annota_line:
                    break
                if level>1:
                    if kwloop_cnt==25: #find switch
                        sw_icnt+=1
                        sw_cnt.append(0)
                    if kwloop_cnt==2:   #find case
                        sw_cnt[sw_icnt]+=1
                if level>2:
                    if kwloop_cnt==15:#find if
                        if_stack+=1
                        if_start=match.start()
                    if kwloop_cnt==9:
                        if_stack+=1
                        else_end=match.end()
                keyword_cnt[kwloop_cnt]+=1
                total_num+=1
            kwloop_cnt+=1
        if if_start - else_end==1:##find elseif in one line
            stack1+='3'
            #if_stack-=1
        elif else_end>0:##find else but not if
            stack1+='2'
        elif if_start>0:
            stack1+='1'
        if if_stack>0:
            for matchb in re.finditer('}',i):
                stack1+='0'
                if_stack-=1
       # print(stack1)
        cnt+=1
    ### Output Layer###
    pop(stack1,4)
    kwloop_cnt=0
    # for kw in key_word:
    #     if kwloop_cnt == 2:
    #         print("case num:",end="")
    #         for idx in range (len(sw_cnt)-1):
    #             print(sw_cnt[idx],end=" ")
    #         print()
    #     else:
    #         print(kw[:-7]+" num:"+str(keyword_cnt[kwloop_cnt]))
    #     kwloop_cnt+=1
    if level>0:
        print("total num:"+str(total_num))
    if level>1:
        print("case num:",end="")
        for idx in range (len(sw_cnt)-1):
            print(sw_cnt[idx],end=" ")
        print()
    if level>2:
        print("if-else num:"+str(if_else_cnt))
    if level>3:
        print("if-elseif-else num:"+str(if_elseif_cnt))