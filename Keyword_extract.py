# coding utf-8
import re
                 
### TOP LEVEL###
# file_path=input("Welcome to C keyword statistic!\n Please input file Path:")

if __name__ == "__main__":
    level=int(input("Please input level:"))
    f=open('testC.txt', 'r')
    keyword_cnt=[0]*32
    sw_cnt=[0]
    sw_icnt=-1
    if_stack=0
    elseif_stack=0
    elseif_flag=False
    if_flag=False
    if_elseif_cnt=0
    if_else_cnt=0
    shiled_word=['//','/\*','\*/','\"','\\\\n\\\\']
    annota_muti=False    
    key_word=['auto','break','case','char','const', 'continue', 'default','do',
    'double','else','enum','extern','float','for','goto','if',
    'int','long','register','return','short' ,'signed' ,'sizeof','static',
    'struct','switch', 'typedef','union','unsigned','void','volatile','while']
    cnt=1
    total_num=0
    ###Search Layer###
    
    #print(key_word.index('case'))
    quote_pre=False
    for i in f:
        print("line"+str(cnt))
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
                elif shloop_cnt==3:
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
                        else_end=match.end()
                keyword_cnt[kwloop_cnt]+=1
                total_num+=1
            kwloop_cnt+=1
        if if_stack>0:
            for matchb in re.finditer('}',i):
                if_stack-=1
                if_flag=True
                break  
        if  if_flag:
            if if_start - else_end==1:##find elseif in one line
                ##go on to match more elseif
                if elseif_flag==False:
                    elseif_stack+=1
                    elseif_flag=True 
                if_stack-=1
            elif else_end>0:##find else but not if
                if elseif_flag:
                    if_elseif_cnt+=1
                    elseif_flag=False
                    elseif_stack-=1
                else:
                    if_stack+=1
                    if_else_cnt+=1
                if_flag=False

        cnt+=1
    f.close()
    ### Output Layer###
    print("total num:"+str(total_num))
    kwloop_cnt=0
    for kw in key_word:
        if kwloop_cnt == 2:
            print("case num:",end="")
            for idx in range (len(sw_cnt)-1):
                print(sw_cnt[idx],end=" ")
            print()
        else:
            print(kw+" num:"+str(keyword_cnt[kwloop_cnt]))
        kwloop_cnt+=1
    if level>2:
        print("if-else num:"+str(if_else_cnt))
    if level>3:
        print("if-elseif-else num:"+str(if_elseif_cnt))