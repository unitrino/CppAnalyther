import re,copy

global list_func_start_end
list_func_start_end = []

global imena_funckii
imena_funckii = []

global list_tipy_dannih
list_tipy_dannih = ["unsigned char", "unsigned short int", "unsigned int", "unsigned long int","signed char", "short int", "long int",
                        "long double","float", "double","wchar_t", "char","bool","void","elem","int"]

global vvod_per 
vvod_per = []

global ourcode

global ourcode_without_ifs
ourcode_without_ifs = ""

global ourcode_comb
ourcode_comb = ""

global if_else_hierarchi
if_else_hierarchi = []

global loop_var_for
loop_var_for = []

global loop_var_while
loop_var_while = []

global flag_for
flag_for = 0

global flag_while
flag_while = 0

global hierar
hierar = 5

our_errors = []

def if_else_adding(list_hierarchi):
    otvet = []
    spis = []
    spis_na_operejenie = []
    spis_souzov_i = []
    itie = -1
    flagg = 0
    spis_strok = []
    spis_strok2 = []
    tekush = 0
    indexx = -1
    stroka_else = ""
    stroka_if = ""
    indd = 0
    flg = 0
    itie = -1
    for jj in list_hierarchi:
        itie+=1
        if len(jj) == 4:
            if jj[0].find("if(") == -1 and jj[1].find("if(") == -1:
                flg = 0
                if stroka_if !="":
                    spis_strok[indexx] = [stroka_if,stroka_else,tekush]
                    stroka_if = ""
                    stroka_else = ""
                spis_strok.append([])
                indexx+=1
                tekush = jj[3]
                stroka_if = jj[0]
                stroka_else = jj[1]
                spis_strok[indexx] = [stroka_if,stroka_else,tekush]
            elif jj[0].find("if(") != -1 or jj[1].find("if(") != -1:
                if jj[0].find("if(") == -1 and jj[1].find("if(") != -1:
                    flg = 1
                    if stroka_if !="":
                        spis_strok[indexx] = [stroka_if,stroka_else,tekush]
                        stroka_if = ""
                        stroka_else = ""
                    spis_strok.append([])
                    indexx+=1
                    tekush = jj[3]
                    stroka_if = jj[0]
                    stroka_else = " "
                    spis_strok[indexx] = [stroka_if,stroka_else,tekush]
                elif jj[0].find("if(") != -1 and jj[1].find("if(") == -1:
                    flg = 1
                    if stroka_if !="":
                        spis_strok[indexx] = [stroka_if,stroka_else,tekush]
                        stroka_if = ""
                        stroka_else = ""
                    spis_strok.append([])
                    indexx+=1
                    tekush = jj[3]
                    stroka_if = " "
                    stroka_else = jj[1]
                    spis_strok[indexx] = [stroka_if,stroka_else,tekush]                    
                        
        elif len(jj) == 3: 
            if jj[1] == 566:
                spis_souzov_i.append(jj)
            elif jj[2] == tekush:
                if flg == 1:
                    if jj[0].strip('\n') != "":
                        if jj[1] == 2:
                            spis_strok.append([])
                            indexx+=1
                            spis_strok[indexx] = [jj[0],jj[0],tek]
                            stroka_if = ""
                            stroka_else = ""
                            continue                   
                        else:
                            spis_na_operejenie.append(jj)
                            stroka_if = ""
                            stroka_else = ""                            
                            print jj
                            continue

                if jj[1] == 2:
                    stroka_if,stroka_else,tek = spis_strok[indexx]
                    stroka_if= stroka_if + jj[0]
                    stroka_else= stroka_else + jj[0]
                    spis_strok[indexx] = [stroka_if,stroka_else,tek]
                elif jj[1] == 3:
                    stroka_if,stroka_else,tek = spis_strok[indexx]
                    stroka_if= jj[0] + stroka_if
                    stroka_else= jj[0] + stroka_else
                    spis_strok[indexx] = [stroka_if,stroka_else,tek]
            elif jj[2] == tekush+1:
                spis_na_operejenie.append(jj)
            
    
    massiv_ifa = [[0]*len(spis_strok) for _ in range(len(spis_strok))]
    index1 = 0
    index2 = 0
    predd = 100
    flag_povt = 0
    spis_dubl = []
    nov_spis = []
    true_break = 0
    flag_perenosa = 0
    for kk in spis_strok:
        flag_perenosa  = 0
        for ii in spis_strok:
            if kk == ii:
                index2+=1
                flag_povt = 1
                continue
            else:
                for jj in list_hierarchi:
                    if jj[0] == "\n":
                        continue
                    flag_zahoda = 0
                    if len(jj) == 4:
                        if jj[0].find("if(") != -1 or jj[1].find("if(") != -1:
                            flag_zahoda = 1
                            flag = ""
                            dop_znach = ""
                            for k in kk[:2]:
                                if k == "" or k == " ":
                                    continue
                                for i in ii[:2]:
                                    if i == "" or i == " ":
                                        continue                                    
                                    stroka1 = k.split("\n");
                                    stroka2 = i.split("\n");
                                    for elemi in stroka1:
                                        for elemi2 in stroka2:
                                            if jj[0].find(elemi)!= -1 and jj[0].find(elemi2)!= -1:
                                                flag = "I"
                                                continue
                                            elif jj[1].find(elemi)!= -1 and jj[1].find(elemi2)!= -1:
                                                flag = "I"
                                                continue
                                            elif jj[0].find(elemi)!= -1 and jj[1].find(elemi2)!= -1:
                                                flag = "ILI"
                                                flag_nov = ""
                                                if nov_spis != []:
                                                    for ili1,ili2 in nov_spis:
                                                        for k in ili1[:2]:
                                                            for i in ili2[:2]:
                                                                stroka1 = k.split("\n");
                                                                stroka2 = i.split("\n");
                                                                for elem in stroka1:
                                                                    for elem2 in stroka2:
                                                                        if jj[0].find(elem)!=-1 and jj[0].find(elem2)!=-1:
                                                                            flag_nov = "IIII"
                                                                            continue
                                                                        elif jj[1].find(elem)!=-1 and jj[1].find(elem2)!=-1:
                                                                            flag_nov = "IIII"
                                                                            continue                                                                        
                                                                        else:
                                                                            flag_nov = "NNEE"
                                                                            break
                                                                    if flag_nov == "NNEE":
                                                                        break
                                                                if flag_nov == "NNEE":
                                                                    break
                                                            if flag_nov == "NNEE":
                                                                break
                                                    if flag_nov == "IIII":
                                                        flag = "ILI1"
                                                    else:
                                                        flag = "ILI2"
                                                        nov_spis = []
                                                break
                                            elif jj[0].find(elemi2)!= -1 and jj[1].find(elemi)!= -1:
                                                flag = "ILI"
                                                flag_nov = ""
                                                if nov_spis != []:
                                                    for ili1,ili2 in nov_spis:
                                                        for k in ili1[:2]:
                                                            for i in ili2[:2]:
                                                                stroka1 = k.split("\n");
                                                                stroka2 = i.split("\n");
                                                                for elem in stroka1:
                                                                    for elem2 in stroka2:
                                                                        if jj[0].find(elem)!=-1 and jj[0].find(elem2)!=-1:
                                                                            flag_nov = "IIII"
                                                                            continue
                                                                        elif jj[1].find(elem)!=-1 and jj[1].find(elem2)!=-1:
                                                                            flag_nov = "IIII"
                                                                            continue                                                                        
                                                                        else:
                                                                            flag_nov = "NNEE"
                                                                            break
                                                                    if flag_nov == "NNEE":
                                                                        break
                                                                if flag_nov == "NNEE":
                                                                    break
                                                            if flag_nov == "NNEE":
                                                                break
                                                    if flag_nov == "IIII":
                                                        flag = "ILI1"
                                                    else:
                                                        flag = "ILI2"
                                                        nov_spis = []
                                                break
                                            
                                            elif jj[0] == jj[1]:
                                                break
                                            elif jj[0].find(elemi) == -1 and jj[1].find(elemi) == -1:
                                                if elemi != '':
                                                    dop_znach = "ACTIVE"
                                                    continue
                                            elif jj[0].find(elemi2) == -1 and jj[1].find(elemi2) == -1:
                                                if elemi2 != '':                                                
                                                    dop_znach = "ACTIVE"
                                                    continue 
                                            
                                        if flag == "I":
                                            continue
                                        else:
                                            break
                                    if flag == "I":
                                        continue
                                    else:
                                        break
                            if flag == "":
                                flag_zahoda = 0
                                continue
    
                            if flag != "":
                                if dop_znach == "ACTIVE":
                                    dop_znach = ""
                                    continue
                                
                                nov_spis.append([kk,ii])
                                nov_spis.append([ii,kk])
                                if index1 >= index2:
                                    continue
                                if flag_povt != 1:
                                    if predd >= index2:
                                        index2+=1                                    
                                massiv_ifa[index1][index2] = flag                              
                                flag_povt = 0
                                predd = index2
                                true_break = 1
                                if flag_perenosa == 0:
                                    index1+=1
                                    flag_perenosa = 1
                                break
                                                
                        if flag_zahoda == 0:
                            continue
                        else:
                            break 
            if true_break == 1:
                true_break = 0
                break
        if flag_perenosa == 0:
            flag_perenosa = 0
            index1+=1

    spis_povtorov = []
    i = 0
    j = 0
    while 1 == 1:
        if i <= (len(spis_strok)-1):
            if j <= (len(spis_strok)-1):
                if i == j:
                    j +=1
                else:
                    if str(massiv_ifa[i][j]) != "0":
                        #print str(spis_strok[i][:2])+"  " + str(massiv_ifa[i][j]) + "  " +str(spis_strok[j][:2])
                        i+=1
                        j+=1
                    else:
                        #print str(spis_strok[i][:2])+"  " + " PSEVDO II" + "  " +str(spis_strok[j][:2])
                        massiv_ifa[i][j] = "I"
                        i+=1
                        j+=1
            else:
                break
    
    indexi_dlia_I = []#
    flag_dlia_I = 0########1111111111111
    for i in range(1,len(spis_strok)):########1111111111111
        for j in range(len(spis_strok)):########1111111111111
            if str(massiv_ifa[j][i]) == "0":########1111111111111
                flag_dlia_I = 1########1111111111111
                continue########1111111111111
            else:########1111111111111
                flag_dlia_I = 0########1111111111111
                break########1111111111111
        if flag_dlia_I == 1:########1111111111111
            indexi_dlia_I.append(i)########1111111111111
            
    spisok_perebora = []
    index_spiska = -1
    i = 0
    j = 0    
    while 1 == 1:
        if i <= (len(spis_strok)-1):
            if j <= (len(spis_strok)-1):
                if i == j:
                    j +=1
                    continue
                else:              
                    if str(massiv_ifa[i][j]) != "0":
                        if spisok_perebora == []:
                            flag_promejut = 0
                            if str(massiv_ifa[i][j]) == "I":
                                for hh in spis_souzov_i:
                                    if spis_strok[j][2] == hh[2] or spis_strok[j][2] == hh[2]-1:
                                        spisok_perebora.append([spis_strok[i][:2],str(massiv_ifa[i][j]) + "   " + str(hh[0]),spis_strok[j][:2]])
                                        index_spiska +=1                                        
                                        flag_promejut = 1
                                        spis_souzov_i.pop(0)
                            if flag_promejut == 0:
                                spisok_perebora.append([spis_strok[i][:2],str(massiv_ifa[i][j]),spis_strok[j][:2]])
                                index_spiska +=1
                            flag_promejut = 0                            
                        else:
                            flag_promejut = 0
                            if str(massiv_ifa[i][j]) == "I":
                                for hh in spis_souzov_i:
                                    if spis_strok[j][2] == hh[2]:
                                        spisok_perebora[index_spiska].append(str(massiv_ifa[i][j]) + "   " + str(hh[0]))
                                        spisok_perebora[index_spiska].append(spis_strok[j][:2])
                                        flag_promejut = 1
                                        spis_souzov_i.pop(0)                                           
                            if flag_promejut == 0:
                                spisok_perebora[index_spiska].append(str(massiv_ifa[i][j]))
                                spisok_perebora[index_spiska].append(spis_strok[j][:2])
                            flag_promejut = 0
                        if spis_na_operejenie != []:
                            for znach,pozic,ierar in spis_na_operejenie:
                                if spis_strok[j][2] - 1 == ierar or spis_strok[j][2] == ierar or spis_strok[j][2] == ierar-1:
                                    if pozic == 3:
                                        spisok_perebora[index_spiska].insert(0,"I"+"   "+znach)
                                        spis_na_operejenie.pop(0)
                                    elif pozic == 2:
                                        spisok_perebora[index_spiska].append(znach)
                                        spis_na_operejenie.pop(0)
                i+=1
                j+=1
            else:
                break
        
    if spisok_perebora == []:
        return spis_strok
        
    for hh in range(len(spisok_perebora[0])):
        if type(spisok_perebora[0][hh]) == list:
            if len(spisok_perebora[0][hh][0]) > 1:   
                if spisok_perebora[0][hh][0].strip() == "":
                    spisok_perebora[0][hh][0] = " "
            if len(spisok_perebora[0][hh][1]) > 1:   
                if spisok_perebora[0][hh][1].strip() == "":
                    print spisok_perebora[0][hh]
                    spisok_perebora[0][hh][1] = " "                
    kolvo_elem = 0
    for hh in spisok_perebora[0]:
        print hh
        if type(hh) == list:
            kolvo_elem+=1
        elif hh == "ILI" or hh == "ILI1" or hh == "ILI2":
            kolvo_elem+=1
            
    massiv_vibora = [0 for _ in range(kolvo_elem)]
    out_massive = []
    for k in range(1,len(massiv_vibora)):
        for i in range(1,len(massiv_vibora),k):
            for j in range(0,len(massiv_vibora),i):
                if massiv_vibora[j] == 0:
                    massiv_vibora[j]+=1
                    if massiv_vibora not in out_massive:
                        mass = copy.deepcopy(massiv_vibora)
                        out_massive.append(mass)
                    continue
                if massiv_vibora[j] == 1:
                    massiv_vibora[j]-=1
                    if massiv_vibora not in out_massive:
                        mass = copy.deepcopy(massiv_vibora)
                        out_massive.append(mass)                    
                    continue            
    
    for k in range(1,len(massiv_vibora)):        
        for i in range(1,len(massiv_vibora),k):
            for j in range(0,len(massiv_vibora),i):
                if massiv_vibora[-j] == 0:
                    massiv_vibora[-j]+=1
                    if massiv_vibora not in out_massive:
                        mass = copy.deepcopy(massiv_vibora)
                        out_massive.append(mass)                    
                    continue
                if massiv_vibora[-j] == 1:
                    massiv_vibora[-j]-=1
                    if massiv_vibora not in out_massive:
                        mass = copy.deepcopy(massiv_vibora)
                        out_massive.append(mass)                    
                    continue                
             
    mas_vihodnih_strok = []
    for elem_comb in out_massive:
        stroka = []
        ii = 0
        flagg = 0
        nexxt = 0
        for hh in spisok_perebora[0]:
            if flagg == 1:
                flagg = 0
                continue
            if type(hh) == list:               
                if hh[elem_comb[ii]] == " ":
                    nexxt = 1
                    break                    
                elif hh[elem_comb[ii]] == "":
                    ii+=1
                    continue                
                else:
                    stroka.append(hh[elem_comb[ii]])
                    ii+=1                   
                    continue
            elif hh == "ILI" or hh == "ILI2":
                if elem_comb[ii] == 0:
                    ii+=2
                    flagg = 1                 
                    continue
                else:
                    stroka.pop()
                    ii+=1                  
                    continue
            elif hh == "ILI1":
                if elem_comb[ii] == 1:
                    stroka = []
                    ii += 1                  
                    continue
                else:
                    ii+=2
                    flagg = 1 
                    continue
            elif hh.startswith("I"):
                    if len(hh) > 4:
                        stroka.append(hh.split("I   ")[1])
                        continue
        if nexxt == 1:
            nexxt = 0
            continue
        if stroka != []:
            stroka_gotovaia = "" 
            for chasti in stroka:
                stroka_gotovaia+=chasti
            mas_vihodnih_strok.append(stroka_gotovaia) 
                    
    mas_vihodnih_strok = list(set(mas_vihodnih_strok))
    return mas_vihodnih_strok
    
    
def if_else_analyzing(ourcode_with_ifs,povtrr):
    global hierar
    global ourcode_without_ifs
    povtor = 0
    stroki_ifa = ""
    stroki_elsa = ""
    skobki_if = 0
    skobki_else = 0
    flag_if = 0
    flag_else = 0
    index_stroki = 0
    index_stroki2 = 0
    starting_if = 0
    starting_else = 0
    ending_if = 0
    konec = 0
    for sss in ourcode_with_ifs.split('\n'):
        index_stroki+=1
        sss = sss.lstrip().strip()
        
        if skobki_if == 0 and flag_if == 1 and sss.find("{") == -1:
                    break        

        if flag_if == 1:
            stroki_ifa += sss + "\n"
        if sss.startswith("if(") and flag_if == 0:
            starting_if = index_stroki-1############################
            flag_if = 1
        if sss.find("{") != -1 and flag_if == 1:
            skobki_if += 1
        elif sss.find("}") != -1 and flag_if == 1:
            skobki_if -= 1


    if ourcode_without_ifs == "":
        ourcode_without_ifs = ourcode_with_ifs.split('\n')[:starting_if]
            
    if ourcode_with_ifs.split('\n')[index_stroki-1].lstrip() == "else":
        ending_if = index_stroki
        index_stroki -=1
        for sss in ourcode_with_ifs.split('\n')[index_stroki:]:
            index_stroki2+=1
            sss = sss.lstrip().strip()
            
            if skobki_else == 0 and flag_else == 1 and sss.find("{") == -1:
                break        

            if flag_else == 1:
                stroki_elsa += sss + "\n"
            if sss.startswith("else") and flag_else == 0:
                starting_else = index_stroki + index_stroki2-1##############################
                flag_else = 1
            if sss.find("{") != -1 and flag_else == 1:
                skobki_else += 1
            elif sss.find("}") != -1 and flag_else == 1:
                skobki_else -= 1
    else:
        stroki_elsa = ""
        index_stroki2 = 0

    flag_if = 0
    flag_else = 0

    if stroki_ifa.find("if(") != -1:      
        stroki_ifa = stroki_ifa.lstrip('{')
        stroki_ifa = stroki_ifa.rstrip('\n')
        stroki_ifa = stroki_ifa.rstrip('}')
        otvet = if_else_analyzing(stroki_ifa,-1)
    if stroki_elsa.find("if(") != -1:
        stroki_elsa = stroki_elsa.lstrip('{')
        stroki_elsa = stroki_elsa.rstrip('\n')
        stroki_elsa = stroki_elsa.rstrip('}')
        otvet = if_else_analyzing(stroki_elsa,-1)

    #else:
    if_else_hierarchi.append([stroki_ifa,stroki_elsa,1,hierar])
    skobki_if = 0
    skobki_else = 0
    flag_if = 0
    flag_else = 0                      
    stroki_ifa = ""
    stroki_elsa = ""

    stroka_dalee_do = ""
    stroka_dalee_posle = ""
    for cusok in ourcode_with_ifs.split("\n")[:starting_if]:
        stroka_dalee_do += cusok + "\n"

    for cusok in ourcode_with_ifs.split("\n")[index_stroki+index_stroki2-1:]:#index_stroki2
        stroka_dalee_posle += cusok + "\n"
    if index_stroki2 == 0:
        pass
        #print "SUMMARNII KONEC"

    bonus_str = ""
    if stroka_dalee_posle.find("if(") !=-1:
        for kk in stroka_dalee_posle.split("\n"):
            if kk.find("if(") != -1:
                break
            else:
                bonus_str += kk + "\n"
    if bonus_str != "":
        if_else_hierarchi.append([bonus_str,566,hierar])#########
    if stroka_dalee_posle.find("if(") != -1: #or stroka_dalee_posle.find("else") != -1:      
        if_else_analyzing(stroka_dalee_posle,povtrr+1)
    else:
        if_else_hierarchi.append([stroka_dalee_posle,2,hierar])     
    if povtrr == -1:
            #print "ARGUMENTI IIIFFAA"
            #print stroka_dalee_do
            if stroka_dalee_do != "}\n\n" or stroka_dalee_do != "\n\n" or stroka_dalee_do != "\n":                
                if_else_hierarchi.append([stroka_dalee_do,3,hierar])#2
                
    global ourcode_comb
    #ourcode_with_ifs = stroka_dalee
    if ourcode_comb == "":############111111111111111
        ourcode_comb = copy.deepcopy(ourcode_with_ifs)##################11111111111111111
    stroki_ifa = ""
    stroki_elsa = ""
    skobki_if = 0
    skobki_else = 0
    flag_if = 0
    flag_else = 0
    
    hierar+=1 

    
def Analyzing_input_heap_allocation(tipp,var,starting):
    global our_errors
    
    list_of_opernd_for_loop_depend =["\->","\<<","\-","\%","\.","\++",
    "\+","\-=","\*=",
    "\/=","\=","\%","\&","\|","\^","\,","\;","\*"]

    list_of_opernd_for_loop =["\+=","\-=","\*=",
    "\/=","\%=","\&=","\|=","\^=","\=","\=","\%","\&","\|","\^","\,","\;","\*"]

    str_of_operand_for_loop = "[("
    for jj2 in list_of_opernd_for_loop:
        str_of_operand_for_loop += jj2+ '|'

    str_of_operand_for_loop +=")]"
    reg_exprr = ""
    reg_exprr +="^"
    reg_exprr += var
    reg_exprr +="(| |)*"
    reg_exprr +=str_of_operand_for_loop

    stroka_pred = ""
    poz = -1
    for sss in ourcode.split('\n')[starting::-1]:
        poz+=1
        sss = sss.lstrip()
        if re.search(reg_exprr,str(sss)):
            for jj in list_operand_var:
                
                reg_exprr2 = ""

                str_of_operand_for_loop_depend = "[("
                for jj2 in list_of_opernd_for_loop_depend:
                    str_of_operand_for_loop_depend += jj2 + '|'

                str_of_operand_for_loop_depend +=")]*"

                reg_exprr2 += str_of_operand_for_loop_depend
                reg_exprr2 +="[^A-Za-z][(| |)]*"
                reg_exprr2 += jj[1]
                reg_exprr2 +="[(| |)]*"
                reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"

                if re.search(reg_exprr2,str(sss)):
                    if re.search("(| |)[^+|^-|^*|^/][\=](| |)",str(sss)):
                        if var != jj[1]:
                            if jj[1] not in vvod_per:
                                Analyzing_input_heap_allocation(jj[0],jj[1],starting-poz-1)
                                print "ZZZZZZZZZZZZZ"
                            elif jj[1] in vvod_per:
                                oshibka = ""
                                oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                oshibka += "Warning"+"\n"
                                oshibka += "Heap is depend upon variable " + str(jj[1])+"\n"
                                oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                                oshibka += sss+"\n"
                                oshibka += stroka_pred+"\n"
                                oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                if our_errors == []:
                                    our_errors.append(oshibka)
                                else:
                                    if oshibka not in our_errors:
                                        our_errors.append(oshibka)                    
    
                                break
			else:
			    continue
                    else:
                        if jj[1] not in vvod_per:
                            Analyzing_input_heap_allocation(jj[0],jj[1],starting-poz-1)
                        elif jj[1] in vvod_per:
                            oshibka = ""
                            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                            oshibka += "Warning"+"\n"
                            oshibka += "Heap is depend upon variable " + str(jj[1])+"\n"
                            oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                            oshibka += sss+"\n"
                            oshibka += stroka_pred+"\n"
                            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                            if our_errors == []:
                                our_errors.append(oshibka)
                            else:
                                if oshibka not in our_errors:
                                    our_errors.append(oshibka)                    
    
                            break
                        #else:
                            #continue                        
            break
        elif tipp.find("*")!= -1:
            imia_tipa = tipp.split("*")[0]
            ostalnie_stroki = ""
            for perr in tipp.split("*")[1:]:
                ostalnie_stroki += perr + "\*"
            ostalnie_stroki += "(| |)*"
        elif tipp.find("*") == -1:
            imia_tipa = tipp
            ostalnie_stroki = ""
        if re.search("^" + imia_tipa + "(| |)*" + ostalnie_stroki +reg_exprr[1:],str(sss)):
            for jj in list_operand_var:
                reg_exprr2 = ""

                str_of_operand_for_loop_depend = "[("
                for jj2 in list_of_opernd_for_loop_depend:
                    str_of_operand_for_loop_depend += jj2 + '|'

                str_of_operand_for_loop_depend +=")]*"
                
                reg_exprr2 += str_of_operand_for_loop_depend
                reg_exprr2 +="[^A-Za-z][(| |)]*"
                reg_exprr2 += jj[1]
                reg_exprr2 +="[(| |)]*"
                reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                if re.search(reg_exprr2,str(sss)):
                    if var != jj[1]:
                        if jj[1] not in vvod_per:
                            Analyzing_input_heap_allocation(jj[0],jj[1],starting-poz-1)
                        elif jj[1] in vvod_per:
                            oshibka = ""
                            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                            oshibka += "Warning"+"\n"
                            oshibka += "Heap is depend upon variable " + str(jj[1])+"\n"
                            oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                            oshibka += sss+"\n"
                            oshibka += stroka_pred+"\n"
                            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                            if our_errors == []:
                                our_errors.append(oshibka)
                            else:
                                if oshibka not in our_errors:
                                    our_errors.append(oshibka)                    
                            break
		    else:
			continue                                                         

            break
        stroka_pred = sss  

    
def Analyzing_heap_alloc():
    global our_errors
    global heap_alloc_var    
    heap_alloc_var = []    
    for jj in list_operand_var:
        poz = -1
        for sss in ourcode.split('\n'):
            poz+=1  
            if re.search("new .*\[.*"+jj[1]+".*\]",str(sss)):
               if jj[1] in vvod_per:
                   stroka_analiza = "\n Analyzing heap:" +str(sss)+"\n"
                   if our_errors == []:
                       our_errors.append(stroka_analiza)
                   else:
                        if stroka_analiza not in our_errors:
                            our_errors.append(stroka_analiza)                   
                   oshibka = ""
                   oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                   oshibka += "Warning"+"\n"
                   oshibka += "Heap is depend upon variable " + str(jj[1])+"\n"
                   oshibka += stroka_pred+"\n"
                   oshibka += sss+"\n"
                   oshibka += ourcode.split('\n')[poz+1]+"\n"
                   oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                   if our_errors == []:
                       our_errors.append(oshibka)
                   else:
                       if oshibka not in our_errors:
                           our_errors.append(oshibka)
               else:
                   Analyzing_input_heap_allocation(jj[0],jj[1],poz+1)
            stroka_pred = sss
            
            
def Analyzing_input_massive(tipp,var,starting):
    global our_errors
    
    list_of_opernd_for_loop_depend =["\->","\<<","\-","\%","\.","\++",
    "\+","\-=","\*=",
    "\/=","\=","\%","\&","\|","\^","\,","\;","\*"]

    list_of_opernd_for_loop =["\+=","\-=","\*=",
    "\/=","\%=","\&=","\|=","\^=","\=","\=","\%","\&","\|","\^","\,","\;","\*"]

    str_of_operand_for_loop = "[("
    for jj2 in list_of_opernd_for_loop:
        str_of_operand_for_loop += jj2+ '|'

    str_of_operand_for_loop +=")]"
    reg_exprr = ""
    #reg_exprr = ""
    #reg_exprr +=str_of_operand_for_loop
    reg_exprr +="^"
    reg_exprr += var
    reg_exprr +="(| |)*"
    reg_exprr +=str_of_operand_for_loop

    stroka_pred = ""
    poz = -1
    for sss in ourcode.split('\n')[starting::-1]:
        poz+=1
        sss = sss.lstrip()
        if re.search(reg_exprr,str(sss)):
            for jj in list_operand_var:
                
                reg_exprr2 = ""

                str_of_operand_for_loop_depend = "[("
                for jj2 in list_of_opernd_for_loop_depend:
                    str_of_operand_for_loop_depend += jj2 + '|'

                str_of_operand_for_loop_depend +=")]*"

                reg_exprr2 += str_of_operand_for_loop_depend
                reg_exprr2 +="(| |)*"
                reg_exprr2 += jj[1]
                reg_exprr2 +="(| |)*"
                reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"

                if re.search(reg_exprr2,str(sss)):
                    if re.search("(| |)[^+|^-|^*|^/][\=](| |)",str(sss)):
                        if var != jj[1]:
                            if jj[1] not in vvod_per:
                                Analyzing_input_massive(jj[0],jj[1],starting-poz-1)
                            elif jj[1] in vvod_per:
                                oshibka = ""
                                oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                oshibka += "Warning"+"\n"
                                oshibka += "Massive is depend upon variable " + str(jj[1])+"\n"
                                oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                                oshibka += sss+"\n"
                                oshibka += stroka_pred+"\n"
                                oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                if our_errors == []:
                                    our_errors.append(oshibka)
                                else:
                                    if oshibka not in our_errors:
                                        our_errors.append(oshibka)                    
                                break
			else:
			    continue
                    else:
                        if jj[1] not in vvod_per:
                            Analyzing_input_massive(jj[0],jj[1],starting-poz-1)
                        elif jj[1] in vvod_per:
                            oshibka = ""
                            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                            oshibka += "Warning"+"\n"
                            oshibka += "Massive is depend upon variable " + str(jj[1])+"\n"
                            oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                            oshibka += sss+"\n"
                            oshibka += stroka_pred+"\n"
                            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                            if our_errors == []:
                                our_errors.append(oshibka)
                            else:
                                if oshibka not in our_errors:
                                    our_errors.append(oshibka)                    
    
                            break
                        #else:
                            #continue                        
            break
        elif tipp.find("*")!= -1:
            imia_tipa = tipp.split("*")[0]
            ostalnie_stroki = ""
            for perr in tipp.split("*")[1:]:
                ostalnie_stroki += perr + "\*"
            ostalnie_stroki += "(| |)*"
        elif tipp.find("*") == -1:
            imia_tipa = tipp
            ostalnie_stroki = ""
        if re.search("^" + imia_tipa + "(| |)*" + ostalnie_stroki +reg_exprr[1:],str(sss)):        
            for jj in list_operand_var:
                reg_exprr2 = ""

                str_of_operand_for_loop_depend = "[("
                for jj2 in list_of_opernd_for_loop_depend:
                    str_of_operand_for_loop_depend += jj2 + '|'

                str_of_operand_for_loop_depend +=")]*"
                
                reg_exprr2 += str_of_operand_for_loop_depend
                reg_exprr2 +="(| |)*"
                reg_exprr2 += jj[1]
                reg_exprr2 +="(| |)*"
                reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                if re.search(reg_exprr2,str(sss)):
                    if var != jj[1]:
                        if jj[1] not in vvod_per:
                            Analyzing_input_massive(jj[0],jj[1],starting-poz-1)
                            print "ZZZZZZZZZZZZZ"
                        elif jj[1] in vvod_per:
                            oshibka = ""
                            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                            oshibka += "Warning"+"\n"
                            oshibka += "Massive is depend upon variable " + str(jj[1])+"\n"
                            oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                            oshibka += sss+"\n"
                            oshibka += stroka_pred+"\n"
                            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                            if our_errors == []:
                                our_errors.append(oshibka)
                            else:
                                if oshibka not in our_errors:
                                    our_errors.append(oshibka)                    
                            break
		    else:
			continue                                                         

            break
        stroka_pred = sss
      
def Analyzing_input_loop(tipp,var,starting):
    global our_errors
    #obshaia = tipp + var
    
    list_of_opernd_for_loop_depend =["\->","\<<","\-","\%","\.","\++",
    "\+","\-=","\*=",
    "\/=","\=","\%","\&","\|","\^","\,","\;","\*"]

    list_of_opernd_for_loop =["\+=","\-=","\*=",
    "\/=","\%=","\&=","\|=","\^=","\=","\=","\%","\&","\|","\^","\,","\;","\*"]

    str_of_operand_for_loop = "[("
    for jj2 in list_of_opernd_for_loop:
        str_of_operand_for_loop += jj2+ '|'

    str_of_operand_for_loop +=")]"
    reg_exprr = ""
    print "IN FUNC 2"
    #reg_exprr = ""
    #reg_exprr +=str_of_operand_for_loop
    reg_exprr +="^"
    reg_exprr += var
    reg_exprr +="(| |)*"
    reg_exprr +=str_of_operand_for_loop

    stroka_pred = ""
    poz = -1
    for sss in ourcode.split('\n')[starting::-1]:
        poz+=1
        sss = sss.lstrip()
        if re.search(reg_exprr,str(sss)):
            for jj in list_operand_var:
                
                reg_exprr2 = ""

                str_of_operand_for_loop_depend = "[("
                for jj2 in list_of_opernd_for_loop_depend:
                    str_of_operand_for_loop_depend += jj2 + '|'

                str_of_operand_for_loop_depend +=")]*"

                reg_exprr2 += str_of_operand_for_loop_depend
                reg_exprr2 +="(| |)*"
                reg_exprr2 += jj[1]
                reg_exprr2 +="(| |)*"
                reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"

                if re.search(reg_exprr2,str(sss)):
                    if re.search("(| |)[^+|^-|^*|^/][\=](| |)",str(sss)):
                        if var != jj[1]:
                            if jj[1] not in vvod_per:
                                Analyzing_input_loop(jj[0],jj[1],starting-poz-1)
                                print "ZZZZZZZZZZZZZ"
                            elif jj[1] in vvod_per:
                                oshibka = ""
                                oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                oshibka += "Warning"+"\n"
                                oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                                oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                                oshibka += sss+"\n"
                                oshibka += stroka_pred+"\n"
                                oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                if our_errors == []:
                                    our_errors.append(oshibka)
                                else:
                                    if oshibka not in our_errors:
                                        our_errors.append(oshibka)                    
    
                                break
			else:
			    print "ZZZZZZZZZZZZZ"
			    continue
                    else:
                        if jj[1] not in vvod_per:
                            Analyzing_input_loop(jj[0],jj[1],starting-poz-1)
                            print "ZZZZZZZZZZZZZ"
                        elif jj[1] in vvod_per:
                            oshibka = ""
                            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                            oshibka += "Warning"+"\n"
                            oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                            oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                            oshibka += sss+"\n"
                            oshibka += stroka_pred+"\n"
                            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                            if our_errors == []:
                                our_errors.append(oshibka)
                            else:
                                if oshibka not in our_errors:
                                    our_errors.append(oshibka)                    

                            break
		    #else:
			#continue
                        
            break
        elif tipp.find("*")!= -1:
            imia_tipa = tipp.split("*")[0]
            ostalnie_stroki = ""
            for perr in tipp.split("*")[1:]:
                ostalnie_stroki += perr + "\*"
            ostalnie_stroki += "(| |)*"
        elif tipp.find("*") == -1:
            imia_tipa = tipp
            ostalnie_stroki = ""
        if re.search("^" + imia_tipa + "(| |)*" + ostalnie_stroki +reg_exprr[1:],str(sss)):        
            for jj in list_operand_var:
                reg_exprr2 = ""

                str_of_operand_for_loop_depend = "[("
                for jj2 in list_of_opernd_for_loop_depend:
                    str_of_operand_for_loop_depend += jj2 + '|'

                str_of_operand_for_loop_depend +=")]*"
                
                reg_exprr2 += str_of_operand_for_loop_depend
                reg_exprr2 +="(| |)*"
                reg_exprr2 += jj[1]
                reg_exprr2 +="(| |)*"
                reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                if re.search(reg_exprr2,str(sss)):
                    if var != jj[1]:
                        if jj[1] not in vvod_per:
                            Analyzing_input_loop(jj[0],jj[1],starting-poz-1)
                            print "ZZZZZZZZZZZZZ"
                        elif jj[1] in vvod_per:
                            oshibka = ""
                            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                            oshibka += "Warning"+"\n"
                            oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                            oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                            oshibka += sss+"\n"
                            oshibka += stroka_pred+"\n"
                            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                            if our_errors == []:
                                our_errors.append(oshibka)
                            else:
                                if oshibka not in our_errors:
                                    our_errors.append(oshibka)                    
                            break
		    else:
			print "ZZZZZZZZZZZZZ"
			continue                                                         

            break
        stroka_pred = sss  


'''
def Analyzing_input_loop(tipp,var,starting):
    global our_errors
    
    list_of_opernd_for_loop_depend =["\->","\<<","\-","\%","\.","\++",
    "\+","\-=","\*=",
    "\/=","\=","\%","\&","\|","\^","\,","\;","\*"]

    list_of_opernd_for_loop =["\+=","\-=","\*=",
    "\/=","\%=","\&=","\|=","\^=","\=","\=","\%","\&","\|","\^","\,","\;","\*"]

    str_of_operand_for_loop = "[("
    for jj2 in list_of_opernd_for_loop:
        str_of_operand_for_loop += jj2+ '|'

    str_of_operand_for_loop +=")]"
    reg_exprr = ""
    #reg_exprr = ""
    #reg_exprr +=str_of_operand_for_loop
    reg_exprr +="^"
    reg_exprr += var
    reg_exprr +="(| |)*"
    reg_exprr +=str_of_operand_for_loop

    stroka_pred = ""
    poz = -1
    for sss in ourcode.split('\n')[starting::-1]:
        poz+=1
        sss = sss.lstrip()
        if re.search(reg_exprr,str(sss)):
            for jj in list_operand_var:
                
                reg_exprr2 = ""

                str_of_operand_for_loop_depend = "[("
                for jj2 in list_of_opernd_for_loop_depend:
                    str_of_operand_for_loop_depend += jj2 + '|'

                str_of_operand_for_loop_depend +=")]*"

                reg_exprr2 += str_of_operand_for_loop_depend
                reg_exprr2 +="(| |)*"
                reg_exprr2 += jj[1]
                reg_exprr2 +="(| |)*"
                reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"

                if re.search(reg_exprr2,str(sss)):
                    if re.search("(| |)[^+|^-|^*|^/][\=](| |)",str(sss)):
                        if var != jj[1]:
                            if jj[1] not in vvod_per:
                                Analyzing_input_loop(jj[0],jj[1],starting-poz-1)
                            elif jj[1] in vvod_per:
                                oshibka = ""
                                oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                oshibka += "Warning"+"\n"
                                oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                                oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                                oshibka += sss+"\n"
                                oshibka += stroka_pred+"\n"
                                oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                if our_errors == []:
                                    our_errors.append(oshibka)
                                else:
                                    if oshibka not in our_errors:
                                        our_errors.append(oshibka)                    
    
                                break
                            else:
                                continue
                    else:
                        if jj[1] not in vvod_per:
                            Analyzing_input_loop(jj[0],jj[1],starting-poz-1)
                        elif jj[1] in vvod_per:
                            oshibka = ""
                            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                            oshibka += "Warning"+"\n"
                            oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                            oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                            oshibka += sss+"\n"
                            oshibka += stroka_pred+"\n"
                            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                            if our_errors == []:
                                our_errors.append(oshibka)
                            else:
                                if oshibka not in our_errors:
                                    our_errors.append(oshibka)                    

                            break
                        else:
                            continue
                        
            break   
        elif re.search("^" + tipp+"(| |)*" + reg_exprr[1:],str(sss)):
            for jj in list_operand_var:
                reg_exprr2 = ""

                str_of_operand_for_loop_depend = "[("
                for jj2 in list_of_opernd_for_loop_depend:
                    str_of_operand_for_loop_depend += jj2 + '|'

                str_of_operand_for_loop_depend +=")]*"
                
                reg_exprr2 += str_of_operand_for_loop_depend
                reg_exprr2 +="(| |)*"
                reg_exprr2 += jj[1]
                reg_exprr2 +="(| |)*"
                reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                if re.search(reg_exprr2,str(sss)):
                    if var != jj[1]:
                        if jj[1] not in vvod_per:
                            Analyzing_input_loop(jj[0],jj[1],starting-poz-1)
                        elif jj[1] in vvod_per:
                            oshibka = ""
                            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                            oshibka += "Warning"+"\n"
                            oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                            oshibka += ourcode.split('\n')[starting-poz-1]+"\n"
                            oshibka += sss+"\n"
                            oshibka += stroka_pred+"\n"
                            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                            if our_errors == []:
                                our_errors.append(oshibka)
                            else:
                                if oshibka not in our_errors:
                                    our_errors.append(oshibka)                    
                            break
                        else:
                            continue                                                         

            break
        stroka_pred = sss
'''
'''
def Analyzing_loops():
    
    global our_errors
    global flag_for
    global loop_var_for    
    flag_for = 0
    loop_var_for = []   
    
    global flag_while
    global loop_var_while      
    flag_while = 0
    loop_var_while = []
    
    list_of_opernd_for_loop_depend =["\->","\<<","\-","\%","\.","\++",
    "\+","\-=","\*=",
    "\/=","\=","\%","\&","\|","\^","\,","\;","\*","\<=","\<","\>=","\>","\!="]
    
    list_of_opernd_for_loop =["\+=","\-=","\*=",
    "\/=","\%=","\&=","\|=","\^=","\=","\=","\%","\&","\|","\^","\,","\;","\*","\<=","\<","\>=","\>","\!="]
    
    str_of_operand_for_loop = "[("
    for jj2 in list_of_opernd_for_loop:
        str_of_operand_for_loop += jj2+ '|'
    
    str_of_operand_for_loop +=")]"
    reg_exprr = "" 
    
    #print "IN FUNC  Analyzing_loops FOR_WHILE"
    poz = -1
    stroka_pred = ""
    for sss in ourcode.split('\n'):
        poz+=1
        if re.search("for\(.*\)",str(sss)):
            pole1,pole2,pole3 = re.search("for\((.*);(.*);(.*)\)",str(sss)).groups()
            pole1 = pole1+";"
            pole2 = pole2+";"
            pole3 = pole3+";"
            for jj in list_operand_var:
                reg_exprr = ""
                reg_exprr +="^"
                reg_exprr += jj[1]
                reg_exprr +="(| |)*"
                reg_exprr +=str_of_operand_for_loop  
                for pole in [pole1,pole2,pole3]:
                    if re.search(reg_exprr,str(pole)):
                        for jj in list_operand_var:
                            reg_exprr2 = ""
                            str_of_operand_for_loop_depend = "[("
                            for jj2 in list_of_opernd_for_loop_depend:
                                str_of_operand_for_loop_depend += jj2 + '|'
                            str_of_operand_for_loop_depend +=")]*"

                            reg_exprr2 += str_of_operand_for_loop_depend
                            reg_exprr2 +="(| |)*"
                            reg_exprr2 += jj[1]
                            reg_exprr2 +="(| |)*"
                            reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                       
                            if re.search(reg_exprr2,str(pole)):
                                global loop_var_for
                                #print "Loop is depend upon variable " + str(jj[1])
                                loop_var_for.append([jj[0],jj[1]])
                                stroka_analiza = "\n Analyzing loop:" +str(sss)+"\n"
                                if our_errors == []:
                                     our_errors.append(stroka_analiza)
                                else:
                                    if stroka_analiza not in our_errors:
                                        our_errors.append(stroka_analiza)                                 
                                if jj[1] not in vvod_per:
                                    Analyzing_input_loop(jj[0],jj[1],poz)
                                    continue
                                else:
                                    oshibka = ""
                                    oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                    oshibka += "Warning"+"\n"
                                    oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                                    oshibka += stroka_pred+"\n"
                                    oshibka += sss+"\n"
                                    oshibka += ourcode.split('\n')[poz+1]+"\n"
                                    oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                    if our_errors == []:
                                        our_errors.append(oshibka)
                                    else:
                                        if oshibka not in our_errors:
                                            our_errors.append(oshibka)
                                    global flag_for
                                    flag_for = 1                                       
                    elif re.search("^" + "[" +jj[0]+"]"+"(| |)*" + reg_exprr[1:],str(pole)):
                        for jj in list_operand_var:
                            reg_exprr2 = ""
            
                            str_of_operand_for_loop_depend = "[("
                            for jj2 in list_of_opernd_for_loop_depend:
                                str_of_operand_for_loop_depend += jj2 + '|'
            
                            str_of_operand_for_loop_depend +=")]*"
                            
                            reg_exprr2 += str_of_operand_for_loop_depend
                            reg_exprr2 +="(| |)*"
                            reg_exprr2 += jj[1]
                            reg_exprr2 +="(| |)*"
                            reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                            if re.search(reg_exprr2,str(pole)):
                                global loop_var_for
                                #print "Loop is depend upon variable " + str(jj[1])
                                loop_var_for.append([jj[0],jj[1]])
                                stroka_analiza = "\n Analyzing loop:" +str(sss)+"\n"
                                if our_errors == []:
                                     our_errors.append(stroka_analiza)
                                else:
                                    if stroka_analiza not in our_errors:
                                        our_errors.append(stroka_analiza)                                
                                if jj[1] not in vvod_per:
                                    Analyzing_input_loop(jj[0],jj[1],poz)
                                    continue
                                else:
                                    oshibka = ""
                                    oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                    oshibka += "Warning"+"\n"
                                    oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                                    oshibka += stroka_pred+"\n"
                                    oshibka += sss+"\n"
                                    oshibka += ourcode.split('\n')[poz+1]+"\n"
                                    oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                    if our_errors == []:
                                        our_errors.append(oshibka)
                                    else:
                                        if oshibka not in our_errors:
                                            our_errors.append(oshibka)
                                    global flag_for
                                    flag_for = 1                                        
                               
    
        elif re.search("while\((.*)\)",str(sss)):
            pole1 = re.search("while\((.*)\)",str(sss)).group(1)
            pole1 = pole1 + ";"
            print re.search("while\((.*)\)",str(sss)).groups()
            for jj in list_operand_var:
                reg_exprr = ""
                reg_exprr +="^"
                reg_exprr += jj[1]
                reg_exprr +="(| |)*"
                reg_exprr +=str_of_operand_for_loop  
                if re.search(reg_exprr,str(pole1)):
                    for jj in list_operand_var:
                        reg_exprr2 = ""
                        str_of_operand_for_loop_depend = "[("
                        for jj2 in list_of_opernd_for_loop_depend:
                            str_of_operand_for_loop_depend += jj2 + '|'
                   
                        str_of_operand_for_loop_depend +=")]*"

                        reg_exprr2 += str_of_operand_for_loop_depend
                        reg_exprr2 +="(| |)*"
                        reg_exprr2 += jj[1]
                        reg_exprr2 +="(| |)*"
                        reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                   
                        if re.search(reg_exprr2,str(pole1)):
                            global loop_var_while
                            #print "Loop is depend upon variable " + str(jj[1])
                            loop_var_while.append([jj[0],jj[1]])
                            stroka_analiza = "\n Analyzing loop:" +str(sss)+"\n"
                            if our_errors == []:
                                 our_errors.append(stroka_analiza)
                            else:
                                if stroka_analiza not in our_errors:
                                    our_errors.append(stroka_analiza)                            
                            if jj[1] not in vvod_per:
                                Analyzing_input_loop(jj[0],jj[1],poz)
                                stroka_pred = sss
                                continue
                            else:
                                oshibka = ""
                                oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                oshibka += "Warning"+"\n"
                                oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                                oshibka += stroka_pred+"\n"
                                oshibka += sss+"\n"
                                oshibka += ourcode.split('\n')[poz+1]+"\n"
                                oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                if our_errors == []:
                                    our_errors.append(oshibka)
                                else:
                                    if oshibka not in our_errors:
                                        our_errors.append(oshibka)
                                global flag_while
                                flag_while = 1                                       
               
                elif re.search("^" + jj[0]+"(| |)*" + reg_exprr[1:],str(sss)):
                    for jj in list_operand_var:
                        reg_exprr2 = ""
               
                        str_of_operand_for_loop_depend = "[("
                        for jj2 in list_of_opernd_for_loop_depend:
                            str_of_operand_for_loop_depend += jj2 + '|'
               
                        str_of_operand_for_loop_depend +=")]*"
                        
                        reg_exprr2 += str_of_operand_for_loop_depend
                        reg_exprr2 +="(| |)*"
                        reg_exprr2 += jj[1]
                        reg_exprr2 +="(| |)*"
                        reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                        if re.search(reg_exprr2,str(pole1)):
                            global loop_var_while
                            #print "Loop is depend upon variable " + str(jj[1])
                            loop_var_while.append([jj[0],jj[1]])
                            stroka_analiza = "\n Analyzing loop:" +str(sss)+"\n"
                            if our_errors == []:
                                 our_errors.append(stroka_analiza)
                            else:
                                if stroka_analiza not in our_errors:
                                    our_errors.append(stroka_analiza)                            
                            if jj[1] not in vvod_per:
                                Analyzing_input_loop(jj[0],jj[1],poz)
                                continue
                            else:
                                oshibka = ""
                                oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                oshibka += "Warning"+"\n"
                                oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                                oshibka += stroka_pred+"\n"
                                oshibka += sss+"\n"
                                oshibka += ourcode.split('\n')[poz+1]+"\n"
                                oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                if our_errors == []:
                                    our_errors.append(oshibka)
                                else:
                                    if oshibka not in our_errors:
                                        our_errors.append(oshibka)
                                global flag_while
                                flag_while = 1           
                          
        stroka_pred = sss
'''


def Analyzing_loops():
    
    global our_errors
    global flag_for
    global loop_var_for    
    flag_for = 0
    loop_var_for = []   
    
    global flag_while
    global loop_var_while      
    flag_while = 0
    loop_var_while = []
    
    list_of_opernd_for_loop_depend =["\->","\<<","\-","\%","\.","\++",
    "\+","\-=","\*=",
    "\/=","\=","\%","\&","\|","\^","\,","\;","\*","\<=","\<","\>=","\>","\!="]
    
    list_of_opernd_for_loop =["\+=","\-=","\*=",
    "\/=","\%=","\&=","\|=","\^=","\=","\%","\&","\|","\^","\,","\;","\*","\<=","\<","\>=","\>","\!="]
    
    str_of_operand_for_loop = "[("
    for jj2 in list_of_opernd_for_loop:
        str_of_operand_for_loop += jj2+ '|'
    
    str_of_operand_for_loop +=")]"
    reg_exprr = ""
    print "IN FUNC 2"  
    
    
    print "IN FUNC  Analyzing_loops FOR_WHILE"
    poz = -1
    stroka_pred = ""
    for sss in ourcode.split('\n'):
        poz+=1
        if re.search("for\(.*\)",str(sss)):
            pole1,pole2,pole3 = re.search("for\((.*);(.*);(.*)\)",str(sss)).groups()
            print re.search("for\((.*);(.*);(.*)\)",str(sss)).groups()
            pole1 = pole1+";"
            pole2 = pole2+";"
            pole3 = pole3+";"
            for jj in list_operand_var:
                reg_exprr = ""
                reg_exprr +="^"
                reg_exprr += jj[1]
                reg_exprr +="(| |)*"
                reg_exprr +=str_of_operand_for_loop  
                for pole in [pole1,pole2,pole3]:
                    if re.search(reg_exprr,str(pole)):
                        for jj in list_operand_var:
                            reg_exprr2 = ""
                            str_of_operand_for_loop_depend = "[("
                            for jj2 in list_of_opernd_for_loop_depend:
                                str_of_operand_for_loop_depend += jj2 + '|'
                            str_of_operand_for_loop_depend +=")]*"

                            reg_exprr2 += str_of_operand_for_loop_depend
                            reg_exprr2 +="(| |)*"
                            reg_exprr2 += jj[1]
                            reg_exprr2 +="(| |)*"
                            reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                       
                            if re.search(reg_exprr2,str(pole)):
                                global loop_var_for
                                print "LOOOPPPPPPP is depend upon variable " + str(jj[1])
                                loop_var_for.append([jj[0],jj[1]])
                                stroka_analiza = "\n Analyzing loop:" +str(sss)+"\n"
                                if our_errors == []:
                                     our_errors.append(stroka_analiza)
                                else:
                                    if stroka_analiza not in our_errors:
                                        our_errors.append(stroka_analiza)                                 
                                if jj[1] not in vvod_per:
                                    Analyzing_input_loop(jj[0],jj[1],poz)
                                    #stroka_pred = sss
                                    print "ZZZZZZZZZZZZZ"
                                    print sss
                                    continue
                                else:
                                    oshibka = ""
                                    oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                    oshibka += "Warning"+"\n"
                                    oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                                    oshibka += stroka_pred+"\n"
                                    oshibka += sss+"\n"
                                    oshibka += ourcode.split('\n')[poz+1]+"\n"
                                    oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                    if our_errors == []:
                                        our_errors.append(oshibka)
                                    else:
                                        if oshibka not in our_errors:
                                            our_errors.append(oshibka)
                                    global flag_for
                                    flag_for = 1
                    elif jj[0].find("*")!= -1:
                        imia_tipa = jj[0].split("*")[0]
                        ostalnie_stroki = ""
                        for perr in jj[0].split("*")[1:]:
                            ostalnie_stroki += perr + "\*"
                        ostalnie_stroki += "(| |)*"
                    elif jj[0].find("*") == -1:
                        imia_tipa = jj[0]
                        ostalnie_stroki = ""
                    if re.search("^" + imia_tipa + "(| |)*" + ostalnie_stroki +reg_exprr[1:],str(pole)):
                        for jj in list_operand_var:
                            reg_exprr2 = ""
            
                            str_of_operand_for_loop_depend = "[("
                            for jj2 in list_of_opernd_for_loop_depend:
                                str_of_operand_for_loop_depend += jj2 + '|'
            
                            str_of_operand_for_loop_depend +=")]*"
                            
                            reg_exprr2 += str_of_operand_for_loop_depend
                            reg_exprr2 +="(| |)*"
                            reg_exprr2 += jj[1]
                            reg_exprr2 +="(| |)*"
                            reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                            if re.search(reg_exprr2,str(pole)):
                                global loop_var_for
                                print "LOOOPPPPPPP is depend upon variable " + str(jj[1])
                                loop_var_for.append([jj[0],jj[1]])
                                stroka_analiza = "\n Analyzing loop:" +str(sss)+"\n"
                                if our_errors == []:
                                     our_errors.append(stroka_analiza)
                                else:
                                    if stroka_analiza not in our_errors:
                                        our_errors.append(stroka_analiza)                                
                                if jj[1] not in vvod_per:
                                    Analyzing_input_loop(jj[0],jj[1],poz)
                                    #stroka_pred = sss
                                    print "ZZZZZZZZZZZZZ"
                                    continue
                                else:
                                    oshibka = ""
                                    oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                    oshibka += "Warning"+"\n"
                                    oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                                    oshibka += stroka_pred+"\n"
                                    oshibka += sss+"\n"
                                    oshibka += ourcode.split('\n')[poz+1]+"\n"
                                    oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                    if our_errors == []:
                                        our_errors.append(oshibka)
                                    else:
                                        if oshibka not in our_errors:
                                            our_errors.append(oshibka)
                                    global flag_for
                                    flag_for = 1                                        
                               
    
        elif re.search("while\((.*)\)",str(sss)):
            pole1 = re.search("while\((.*)\)",str(sss)).group(1)
            pole1 = pole1 + ";"
            print re.search("while\((.*)\)",str(sss)).groups()
            for jj in list_operand_var:
                reg_exprr = ""
                reg_exprr +="^"
                reg_exprr += jj[1]
                reg_exprr +="(| |)*"
                reg_exprr +=str_of_operand_for_loop  
                if re.search(reg_exprr,str(pole1)):
                    for jj in list_operand_var:
                        reg_exprr2 = ""
                        str_of_operand_for_loop_depend = "[("
                        for jj2 in list_of_opernd_for_loop_depend:
                            str_of_operand_for_loop_depend += jj2 + '|'
                   
                        str_of_operand_for_loop_depend +=")]*"

                        reg_exprr2 += str_of_operand_for_loop_depend
                        reg_exprr2 +="(| |)*"
                        reg_exprr2 += jj[1]
                        reg_exprr2 +="(| |)*"
                        reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                   
                        if re.search(reg_exprr2,str(pole1)):
                            global loop_var_while
                            print "LOOOPPPPPPP is depend upon variable " + str(jj[1])
                            loop_var_while.append([jj[0],jj[1]])
                            stroka_analiza = "\n Analyzing loop:" +str(sss)+"\n"
                            if our_errors == []:
                                 our_errors.append(stroka_analiza)
                            else:
                                if stroka_analiza not in our_errors:
                                    our_errors.append(stroka_analiza)                            
                            if jj[1] not in vvod_per:
                                Analyzing_input_loop(jj[0],jj[1],poz)
                                stroka_pred = sss
                                print "ZZZZZZZZZZZZZ"
                                continue
                            else:
                                oshibka = ""
                                oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                oshibka += "Warning"+"\n"
                                oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                                oshibka += stroka_pred+"\n"
                                oshibka += sss+"\n"
                                oshibka += ourcode.split('\n')[poz+1]+"\n"
                                oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                if our_errors == []:
                                    our_errors.append(oshibka)
                                else:
                                    if oshibka not in our_errors:
                                        our_errors.append(oshibka)
                                global flag_while
                                flag_while = 1                               
               
                elif jj[0].find("*")!= -1:
                        imia_tipa = jj[0].split("*")[0]
                        ostalnie_stroki = ""
                        for perr in jj[0].split("*")[1:]:
                            ostalnie_stroki += perr + "\*"
                        ostalnie_stroki += "(| |)*"
                elif jj[0].find("*") == -1:
                    imia_tipa = jj[0]
                    ostalnie_stroki = ""
                if re.search("^" + imia_tipa + "(| |)*" + ostalnie_stroki +reg_exprr[1:],str(sss)):
                    for jj in list_operand_var:
                        reg_exprr2 = ""
               
                        str_of_operand_for_loop_depend = "[("
                        for jj2 in list_of_opernd_for_loop_depend:
                            str_of_operand_for_loop_depend += jj2 + '|'
               
                        str_of_operand_for_loop_depend +=")]*"
                        
                        reg_exprr2 += str_of_operand_for_loop_depend
                        reg_exprr2 +="(| |)*"
                        reg_exprr2 += jj[1]
                        reg_exprr2 +="(| |)*"
                        reg_exprr2 += str_of_operand_for_loop_depend[:-1]+"+"
                        if re.search(reg_exprr2,str(pole1)):
                            global loop_var_while
                            print "LOOOPPPPPPP is depend upon variable " + str(jj[1])
                            loop_var_while.append([jj[0],jj[1]])
                            stroka_analiza = "\n Analyzing loop:" +str(sss)+"\n"
                            if our_errors == []:
                                 our_errors.append(stroka_analiza)
                            else:
                                if stroka_analiza not in our_errors:
                                    our_errors.append(stroka_analiza)                            
                            if jj[1] not in vvod_per:
                                Analyzing_input_loop(jj[0],jj[1],poz)
                                print "ZZZZZZZZZZZZZ"
                                #stroka_pred = sss
                                continue
                            else:
                                oshibka = ""
                                oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                                oshibka += "Warning"+"\n"
                                oshibka += "Loop is depend upon variable " + str(jj[1])+"\n"
                                oshibka += stroka_pred+"\n"
                                oshibka += sss+"\n"
                                oshibka += ourcode.split('\n')[poz+1]+"\n"
                                oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                                if our_errors == []:
                                    our_errors.append(oshibka)
                                else:
                                    if oshibka not in our_errors:
                                        our_errors.append(oshibka)
                                global flag_while
                                flag_while = 1           
                          
        stroka_pred = sss



def Function_start_end():
    global our_errors
    start_func  = 0
    for line_of in imena_funckii:
        Ln = line_of[1]
        for sss in ourcode2.split('\n')[line_of[1]-1:]:
            if sss.find("{") != -1:
                start_func = Ln
                break
            else:
                Ln+=1
        Ln = start_func
        skob = 1
        for sss in ourcode2.split('\n')[start_func:]:
            if sss.find("{") != -1:
                 skob+=1
            elif sss.find("}") != -1:
                skob-=1
            if skob == 0:
                end_func = Ln
                list_func_start_end.append([line_of[0],start_func,end_func])
                break
            else:
                Ln+=1

def Function_detect():
    global our_errors  
    
    stroka_tipov = ""
    stroka_tipov += "("
    for tip in list_tipy_dannih:
        stroka_tipov+=(str(tip))
        stroka_tipov += '|'

    stroka_tipov = stroka_tipov.rstrip('|')
    stroka_tipov += ")"
    Ln = 0
    Kolvo_func = 0
    for sss in ourcode2.split('\n'):
        Ln +=1
        sss = sss.strip().strip()
        if re.search(stroka_tipov+"(| |)(|\*|)(| |)([A-Za-z])*\(",str(sss)):
            Kolvo_func+=1
            imena_funckii.append([re.search(stroka_tipov+"(| |)(|\*|)(| |)([A-Za-z]*)\(",str(sss)).groups()[-1],Ln])
            for peremen in re.search("\(.*\)",str(sss)).group(0).split(","):
                argument =  peremen.strip(")").strip("(")
                if len(argument.split("*"))  != 1:
                    if argument.split("*")[1] != "":
                        vvod_per.append(argument.split("*")[1])
                elif len(argument.split(" "))  != 1:
                    if argument.split(" ")[1] != "":
                        vvod_per.append(argument.split(" ")[1])
                
        elif re.search(stroka_tipov+" [A-Za-z]*\(",str(sss)):
            Kolvo_func+=1
            imena_funckii.append([re.search(stroka_tipov+" [a-z]*\(",str(sss)).group(0).partition(" ")[2].rstrip('('),Ln])
            for peremen in re.search("\(.*\)",str(sss)).group(0).split(","):
                argument =  peremen.strip(")").strip("(")
                if len(argument.split("*"))  != 1:
                    if argument.split("*")[1] != "":
                        vvod_per.append(argument.split("*")[1])
                elif len(argument.split(" "))  != 1:
                    if argument.split(" ")[1] != "":
                        vvod_per.append(argument.split(" ")[1])
    

def Analyzing_unsave_function():
    global our_errors
    
    list_of_func = ["strcmp(","strcpy(","memcpy(","strlen(","printf("]
    str_of_func = ""
    str_of_func += "[("
    for jj in list_of_func:
        str_of_func += jj + '|'
    str_of_func += ")]"
    poz = -1
    stroka_pred = ""
    for sss in ourcode.split('\n'):
        poz +=1
        if re.search(str_of_func,str(sss)):
            oshibka = ""
            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
            oshibka += "Warning"+"\n"
            oshibka += "Unsafed function"+"\n"
            oshibka += stroka_pred+"\n"
            oshibka += sss+"\n"
            oshibka += ourcode.split('\n')[poz+1]+"\n"
            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
            if our_errors == []:
                our_errors.append(oshibka)
            else:
                for oshibki in our_errors:
                    if oshibki != oshibka:
                        our_errors.append(oshibka)              
        stroka_pred = sss
                               
def Analyzing_inject_command():
    global our_errors
    poz = -1
    stroka_pred = ""
    for sss in ourcode.split('\n'):
        poz+=1
        if re.search("system(| |)\(",str(sss)):
            argumenti = re.search("system(| |)\(.*",str(sss)).group(0).partition("(")[2].rstrip(";").rstrip(")")
            for k in list_operand_var:
                if argumenti.find(k[1]) != -1:
                    oshibka = ""
                    oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                    oshibka += "Warning"+"\n"
                    oshibka += "Unsafed function system()"+"\n"
                    oshibka += stroka_pred+"\n"
                    oshibka += sss+"\n"
                    oshibka += ourcode.split('\n')[poz+1]+"\n"
                    oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                    if our_errors == []:
                        our_errors.append(oshibka)
                    else:
                        if oshibka not in our_errors:
                            our_errors.append(oshibka)                      
                    #Analyzing_inject_command_input(k[0],k[1])  
            for k in list_operand_mass:
                if argumenti.find(k[1]) != -1:
                    oshibka = ""
                    oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                    oshibka += "Warning"+"\n"
                    oshibka += "Unsafed function system()"+"\n"
                    oshibka += stroka_pred+"\n"
                    oshibka += sss+"\n"
                    oshibka += ourcode.split('\n')[poz+1]+"\n"
                    oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                    if our_errors == []:
                        our_errors.append(oshibka)
                    else:
                        if oshibka not in our_errors:
                            our_errors.append(oshibka)                    
                    #Analyzing_inject_command_input(k[0],k[1])                    
            for k in vvod_per:
                if argumenti.find(k) != -1:
                    oshibka = ""
                    oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                    oshibka += "Warning"+"\n"
                    oshibka += "Unsafed function system()"+"\n"                    
                    oshibka += stroka_pred+"\n"
                    oshibka += sss+"\n"
                    oshibka += ourcode.split('\n')[poz+1]+"\n"
                    oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                    if our_errors == []:
                        our_errors.append(oshibka)
                    else:
                        if oshibka not in our_errors:
                            our_errors.append(oshibka)                    
        stroka_pred = sss

def Analyzing_exception():
    global our_errors
    poz = -1
    stroka_pred = ""
    for sss in ourcode.split('\n'):
        poz+=1
        if re.search("catch(| |)(...)(\{)?",str(sss)):
            oshibka = ""
            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
            oshibka += "Unsafed catch (catch (...))"+"\n"
            oshibka += stroka_pred+"\n"
            oshibka += sss+"\n"
            oshibka += ourcode.split('\n')[poz+1]+"\n"
            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
            if our_errors == []:
                our_errors.append(oshibka)
            else:
                for oshibki in our_errors:
                    if oshibki != oshibka:
                        our_errors.append(oshibka)                          
        elif re.search("catch(| |)(Exception)(\{)?",str(sss)):
            oshibka = ""
            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
            oshibka += "Unsafed catch (catch (Exception))" +"\n"
            oshibka += stroka_pred+"\n"
            oshibka += sss+"\n"
            oshibka += ourcode.split('\n')[poz+1]+"\n"
            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
            if our_errors == []:
                our_errors.append(oshibka)
            else:
                for oshibki in our_errors:
                    if oshibki != oshibka:
                        our_errors.append(oshibka)                          
        elif re.search("__except\(EXCEPTION_EXECUTE_HANDLER\)(\{)?",str(sss)):
            oshibka = ""
            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
            oshibka += "Unsafed SEH catch ( __except(EXCEPTION_EXECUTE_HANDLER) )" +"\n"
            oshibka += stroka_pred+"\n"
            oshibka += sss+"\n"
            oshibka += ourcode.split('\n')[poz+1]+"\n"
            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
            if our_errors == []:
                our_errors.append(oshibka)
            else:
                for oshibki in our_errors:
                    if oshibki != oshibka:
                        our_errors.append(oshibka)                         
        stroka_pred = sss
        
def Analyzing_pointers_init(k):
    global our_errors
    list_of_opernd_for_pointer =["->","<<",">>","<",">","-","%",".","\++","\+=","\-=","\*=","\/=","\%=","\&=","\|=","\^=","\>=","\<=","\(","\["]
    str_of_operand_for_poitner = "[("
    for jj in list_of_opernd_for_pointer:
        str_of_operand_for_poitner += jj + '|'

    str_of_operand_for_poitner +=")]*"



    list_of_opernd_for_pointer2 =["->","<<",">>","<",">",
    "-","%",".","\++","\]","\)",";","\="]

    str_of_operand_for_poitner2 = "[("
    for jj in list_of_opernd_for_pointer2:
        str_of_operand_for_poitner2 += jj + '|'

    str_of_operand_for_poitner2 +=")]"
    
    print "IN FUNC 2"
    reg_exprr = ""
    reg_exprr +="^"#str_of_operand_for_poitner
    reg_exprr += k[1]
    reg_exprr +="[(| |)]*[=]"
    #reg_exprr +=#str_of_operand_for_poitner2
    for sss in ourcode.split('\n'):
        sss = sss.lstrip("\t").strip()
        if re.search(reg_exprr,str(sss)):
            print str(sss)
            #if sss.find("=") != -1:
            if sss.split("=")[1].find("malloc") != -1:
                #k[3] = "allocated"
                k[2] = "initialize pointer"
                k[3] = "malloc"
                k[4] = "malloc"
                break
            elif sss.split("=")[1].find("[") != -1 and sss.split("=")[1].find("new") != -1:
                #k[3] = "allocated"
                k[2] = "initialize pointer"
                k[3] = "new[]"
                k[4] = "new[]"
                break
            elif sss.split("=")[1].find("[") == -1 and sss.split("=")[1].find("new") != -1:
                #k[3] = "allocated"
                k[2] = "initialize pointer"
                k[3] = "new"
                k[4] = "new"
                break
            else:
                k[2] = "initialize pointer"
                #k[2] = "initialize pointer"
                #k[3] = ""
                #k[4] = ""                    
                #k[4] = ""
                #k[5] = ""
                break


def Analyzing_pointers_free(k):
    global our_errors
    list_of_opernd_for_pointer =["\->","\<<","\>>","\<","\>","\-","\%","\.","\++",
    "\+=","\-=","\*=",
    "\/=","\%=","\&=","\|=","\^=","\>=","\<=","\(","\[","\*","\="]
    str_of_operand_for_poitner = "[("
    for jj in list_of_opernd_for_pointer:
        str_of_operand_for_poitner += jj + '|'

    str_of_operand_for_poitner +=")]*"
    global our_errors


    list_of_opernd_for_pointer2 =["\->","\<<","\>>","\<","\>",
    "\-","\%","\.","\++","\]","\)","\;","\=","\["]

    str_of_operand_for_poitner2 = "[("
    for jj in list_of_opernd_for_pointer2:
        str_of_operand_for_poitner2 += jj + '|'

    str_of_operand_for_poitner2 +=")]+"
    
    reg_exprr = ""
    reg_exprr +=str_of_operand_for_poitner
    reg_exprr +="[^A-Za-z][(| |)]*"
    reg_exprr += k[1]
    reg_exprr +="[(| |)]*"
    reg_exprr +=str_of_operand_for_poitner2
    flag_free = 0
    stroka_pred = ""
    poz = -1
    init_not_heap = 0
    if k[3] == "":
        flag_free = 1
        init_not_heap  = 1
    for sss in ourcode.split('\n'):
        poz+=1
        if re.search(reg_exprr,str(sss)):
            sss = sss.lstrip()
            if flag_free == 1:
                print  k[3]
                if sss.find("new") != -1 and sss.find("[") != -1:
                    k[3] = "new[]"
                    k[4] = "new[]"
                    flag_free = 0
                    stroka_pred = sss
                    continue
                elif sss.find("new") != -1:
                    k[3] = "new"
                    k[4] = "new"
                    flag_free = 0
                    stroka_pred = sss
                    continue
                elif sss.find("malloc(") != -1:
                    k[3] = "malloc"
                    k[4] = "malloc"
                    flag_free = 0
                    stroka_pred = sss
                    continue
                elif sss.startswith("delete[]") or sss.startswith("delete") or sss.startswith("free("):
                    if init_not_heap == 1:
                        oshibka = ""
                        oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                        oshibka += "Incorrect free  " + k[0] + "  " + k[1]+"\n"
                        oshibka += stroka_pred+"\n"
                        oshibka += sss+"\n"
                        oshibka += ourcode.split('\n')[poz+1]+"\n"
                        oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                        if our_errors == []:
                            our_errors.append(oshibka)
                        else:
                            if oshibka not in our_errors:
                                our_errors.append(oshibka)
                    else:
                        oshibka = ""
                        oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                        oshibka += "DOUBLE  FREE  " + k[0] + "  " + k[1]+"\n"
                        oshibka += stroka_pred+"\n"
                        oshibka += sss+"\n"
                        oshibka += ourcode.split('\n')[poz+1]+"\n"
                        oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                        if our_errors == []:
                            our_errors.append(oshibka)
                        else:
                            if oshibka not in our_errors:
                                our_errors.append(oshibka)                         
                    stroka_pred = sss
                    continue
                else:
                    if init_not_heap == 0:
                        oshibka = ""
                        oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                        oshibka += "USE AFTER FREE  " + k[0] + "  " + k[1]+"\n"
                        oshibka += stroka_pred+"\n"
                        oshibka += sss+"\n"
                        oshibka += ourcode.split('\n')[poz+1]+"\n"
                        oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                        if our_errors == []:
                            our_errors.append(oshibka)
                        else:
                            if oshibka not in our_errors:
                                our_errors.append(oshibka)                  
                        stroka_pred = sss
                        continue
                    
            if sss.startswith("delete[]"):
                flag_free = 1
                init_not_heap = 0
                if k[3] == "new[]":
                    k[3] = "correct free"
                else:
                    k[3] = "incorrect free"
                    oshibka = ""
                    oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                    oshibka += "Incorrect free  " + k[0] + "  " + k[1]+"\n"
                    oshibka += stroka_pred+"\n"
                    oshibka += sss+"\n"
                    oshibka += ourcode.split('\n')[poz+1]+"\n"
                    oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                    if our_errors == []:
                        our_errors.append(oshibka)
                    else:
                        if oshibka not in our_errors:
                            our_errors.append(oshibka)                                       
            elif sss.startswith("delete"):
                flag_free = 1
                init_not_heap = 0
                if k[3] == "new":
                    k[3] = "correct free"
                else:
                    k[3] = "incorrect free"
                    oshibka = ""
                    oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                    oshibka += "Incorrect free  " + k[0] + "  " + k[1]+"\n"
                    oshibka += stroka_pred+"\n"
                    oshibka += sss+"\n"
                    oshibka += ourcode.split('\n')[poz+1]+"\n"
                    oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                    if our_errors == []:
                        our_errors.append(oshibka)
                    else:
                        if oshibka not in our_errors:
                            our_errors.append(oshibka)                    
            elif sss.startswith("free("):
                flag_free = 1
                init_not_heap = 0
                if k[3] == "new" or  k[3] == "malloc":
                    k[3] = "correct free"
                else:
                    k[3] = "incorrect free"
                    oshibka = ""
                    oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                    oshibka += "Incorrect free  " + k[0] + "  " + k[1]+"\n"
                    oshibka += stroka_pred+"\n"
                    oshibka += sss+"\n"
                    oshibka += ourcode.split('\n')[poz+1]+"\n"
                    oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                    if our_errors == []:
                        our_errors.append(oshibka)
                    else:
                        if oshibka not in our_errors:
                            our_errors.append(oshibka) 
        stroka_pred = sss

print "++++++++++++++++++++++++++++++++++++++"

 
def Main_func():
    global our_errors

    global list_operand_var
    list_operand_var = []
    global list_operand_mass
    list_operand_mass = []

    global ourcode

            
    for sss in ourcode.split('\n'):
        if str(sss).startswith("typedef"):
            list_tipy_dannih.append(str(sss).partition(" ")[2].partititon(" "))

        stroka_tipov = ""
        stroka_tipov += "("
        for tip in list_tipy_dannih:
            stroka_tipov+=(str(tip))
            stroka_tipov += '|'

        stroka_tipov = stroka_tipov.rstrip('|')
        stroka_tipov += ")"
            
    for sss in ourcode.split('\n'):
        sss = sss.strip().strip()
        if re.search(stroka_tipov+" [A-Za-z]*\;",str(sss)):
            tip = re.search(stroka_tipov+" [A-Za-z]*\;",str(sss)).group(1)
            nazv = re.search(stroka_tipov+" [A-Za-z]*\;",str(sss)).group(0).partition(tip)[2].strip().strip(';')
            list_operand_var.append([tip,nazv,"uninitialize variable"])
        elif re.search(stroka_tipov+"(| |)*([*]+)(| |)*[A-Za-z]*\;",str(sss)):
            sss = sss.replace(' ','')
            sss = sss.replace(' ','')
            tip = re.search(stroka_tipov+"(| |)*([*]+)(| |)*[A-Za-z]*\;",str(sss)).group(1)
            tip += re.search(stroka_tipov+"(| |)*([*]+)(| |)*[A-Za-z]*\;",str(sss)).group(3)
            nazv = re.search(stroka_tipov+"(| |)*[*]+(| |)*[A-Za-z]*\;",str(sss)).group(0).partition(tip)[2].strip().strip(';')
            list_operand_var.append([tip,nazv,"uninitialize pointer","",""])
        elif re.search(stroka_tipov+"(| |)*([*]+)(| |)*[A-Za-z]*(\[\d*\])+;",str(sss)):
            sss = sss.replace(' ','')
            #print "Massiv ukazatelei"
            tip =  re.search(stroka_tipov+"(| |)*([*]+)(| |)*[A-Za-z]*(\[\d*\])+;",str(sss)).group(1) +"*"
            nazv = re.search(stroka_tipov+"(| |)*([*]+)(| |)*[A-Za-z]*(\[\d*\])+;",str(sss)).group(0).partition(tip)[2].partition("[")[0]

            list_operand_mass.append([tip,nazv,"uninitialize","massive-pointer"])
        elif re.search(stroka_tipov+" [A-Za-z]*(\[\d*\])+;",str(sss)):
            tip =  re.search(stroka_tipov+" [A-Za-z]*(\[\d*\])+;",str(sss)).group(1)
            nazv = re.search(stroka_tipov+" [A-Za-z]*(\[\d*\])+;",str(sss)).group(0).partition(tip)[2].partition("[")[0].strip()
            #print "Massiv obch"
            list_operand_mass.append([tip,nazv,"uninitialize","massive"])

            #Proinicializirovannie peremennii


    #print "================================="
    for sss in ourcode.split('\n'):
        if re.search(stroka_tipov+" [A-Za-z]*(| |)*\=(| |)*",str(sss)):
            #print "obichnaia peremennaia"
            tip = re.search(stroka_tipov+" [A-Za-z]*(| |)*\=(| |)*",str(sss)).group(1)
            nazv = re.search(stroka_tipov+" [A-Za-z]*(| |)*\=(| |)",str(sss)).group(0).partition(tip)[2].strip().partition(' ')[0]
            list_operand_var.append([tip,nazv,"initialize variable"])
            if [tip,nazv,"initialize variable"] not in list_operand_var:
                list_operand_var.append([tip,nazv,"initialize variable"])
        elif re.search(stroka_tipov+"(| |)*([\*]+)(| |)[A-Za-z]*(| |)*\=(| |)*",str(sss)):
            #print "ukazatel"
            tip = re.search(stroka_tipov+"(| |)*([*]+)(| |)*[A-Za-z]*(| |)*\=(| |)*",str(sss)).group(1)
            tip += re.search(stroka_tipov+"(| |)*([*]+)(| |)*[A-Za-z]*(| |)*\=(| |)*",str(sss)).group(3)
            nazv = re.search(stroka_tipov+"(| |)*([*]+)(| |)*[A-Za-z]*(| |)*\=(| |)*",str(sss)).group(0).replace(' ','').partition(tip)[2].strip().partition("=")[0].strip()
	    #print re.search(stroka_tipov+"(| |)*([*]+)(| |)*[A-Za-z]*(| |)*\=(| |)*",str(sss)).group(0)
            #print tip
            #print nazv
            vid = ""
            if sss.split('=')[1].strip().strip(';').startswith("new"):
                if sss.find("[") != -1:
                    vid = "new[]"
                elif sss.find("[") == -1:
                    vid = "new"
            elif sss.split('=')[1].strip().strip(';').startswith("(" + tip + ")" + "malloc"):
                vid = "malloc"
            #elif sss.split('=')[1].strip().strip(';').startswith("NULL") or sss.split('=')[1].strip().strip(';').startswith("0"):
                #vid = "NULL pointer"
            else:
                vid = ""            
            if [tip,nazv,"initialize pointer",vid,vid] not in list_operand_var:
                list_operand_var.append([tip,nazv,"initialize pointer",vid,vid])
        elif re.search(stroka_tipov+" [A-Za-z]*(\[\d*\])+(| |)=",str(sss)):
            tip =  re.search(stroka_tipov+" [A-Za-z]*(\[\d*\])+(| |)=",str(sss)).group(1)
            nazv = re.search(stroka_tipov+" [A-Za-z]*(\[\d*\])+(| |)=",str(sss)).group(0).partition(tip)[2].partition("[")[0].strip()
            #print "Massiv obch"
            list_operand_mass.append([tip,nazv,"initialize","massive"])

    #print "-=-=-=-==-===================-------------"
    for peremenn in list_operand_var:
        if peremenn[2] == "uninitialize variable":
            for sss in ourcode.split('\n'):
                sss = sss.strip().strip()
                if sss.startswith(peremenn[1]) and sss.find("=") != -1 and sss.find("+=") == -1 and sss.find("-=") == -1 and sss.find("*=") == -1 and sss.find("/=") == -1:
                    peremenn[2] = "initialize variable"
    

    #print "============================
    list_of_opernd =["+","*","-","/"
    "++","--","%"]
    #print "================================="
    global vvod_per 
    vvod_per = []
    for sss in ourcode.split('\n'):
        if re.search("cin[(| |>>| |)(|*|)[A-Za-z]*]*",str(sss)):
            stroka = sss.split(">>")
            for per in stroka[1:]:
                vvod_per.append(per.strip().strip(';'))
                for our_per in list_operand_var:
                    if our_per[2] == "uninitialize variable" and our_per[1] == per.strip().strip(';'):
                        our_per[2] = "initialize variable"
                for elem_mas in list_operand_mass:
                    if elem_mas[2] == "uninitialize" and elem_mas[1] == per.strip().strip(';'):
                        elem_mas[2] = "initialize"

    for peremenn in list_operand_var:
        if peremenn[2] == "uninitialize variable":
            oshibka = ""
            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
            oshibka += "Uninitialize variable:  " + peremenn[1]+"\n"
            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
            if our_errors == []:
                our_errors.append(oshibka)
            else:
                if oshibka not in our_errors:
                    our_errors.append(oshibka)            
    for mass in list_operand_mass:
        if mass[2] == "uninitialize":
            oshibka = ""
            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
            oshibka += "Uninitialize massive:  " + mass[1]+"\n"
            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
            if our_errors == []:
                our_errors.append(oshibka)
            else:
                if oshibka not in our_errors:
                    our_errors.append(oshibka)            
  
    list_of_opernd22 =["->","<<",">>","<",">","-","%",".","\++",
    "\+=","\-=","\*=",
    "\/=","\%=","\&=","\|=","\^=","\>=","\<=","\(","\["]
    global str_of_operand
    str_of_operand = "[("
    for jj in list_of_opernd22:
        str_of_operand += jj + '|'

    str_of_operand +=")]"

    global str_of_operand2


    list_of_opernd33 =["->","<<",">>","<",">",
    "\-","%",".","\++","\]","\)",";","\=","\*","\+","\[","\("]

    str_of_operand2 = "[("
    for jj in list_of_opernd33:
        str_of_operand2 += jj + '|'

    str_of_operand2 +=")]"


    #print "RABOTA S UKAZATELIAMI"
    for k in list_operand_var:
        if k[2] == "uninitialize pointer": #or (k[2] == "initialize pointer" and k[3] == "NULL pointer"):
            Analyzing_pointers_init(k)


    list_udalenie  = []
    #NEINICIALIZIROVANI
    for j in list_operand_var:
        if j[2] == "uninitialize pointer":
            oshibka = ""
            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
            oshibka += "Pointer was not allocated or wasn PRIRAVNEN:  " + j[0] + "  " + j[1]+"\n"
            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
            if our_errors == []:
                our_errors.append(oshibka)
            else:
                if oshibka not in our_errors:
                    our_errors.append(oshibka)            
            #print "Dlia ukazatelia " + j[0] + " " + j[1] + " ne videleno mesto"
	    list_udalenie.append(j)
            #list_operand_var.remove(j)
	    
    for jj in list_udalenie:
        list_operand_var.remove(jj)

    for j in list_operand_var:
        if j[2] == "initialize pointer":
            Analyzing_pointers_free(j)

    for j in list_operand_var:
        if j[2] == "initialize pointer":
            if j[3] == "malloc" or j[3] == "new" or j[3] == "new[]":
                oshibka = ""
                oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                oshibka += "Pointer was not freed:  " + j[0] + "  " + j[1]+"\n"
                oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                if our_errors == []:
                    our_errors.append(oshibka)
                else:
                    if oshibka not in our_errors:
                        our_errors.append(oshibka)                



    #Exception ERROR
    Analyzing_exception()
    #Exception SYSTEM
    Analyzing_inject_command()
    Analyzing_heap_alloc()
    Analyzing_loops()
    
    for kk in list_operand_var:
        if kk[2] == "initialize pointer" or kk[2] == "uninitialize pointer": 
            if kk[4] == "new[]":
                list_operand_mass.append([kk[0],kk[1],"",""])

    #print " POISK MASSIVOV "
    for (_,name_of,_,_) in list_operand_mass:
        reg_exprr = ""
        reg_exprr +=str_of_operand+"+"
        reg_exprr +="(| |)*"
        reg_exprr += name_of
        reg_exprr +="\["
        poz = -1
        stroka_pred = ""
        for sss in ourcode.split('\n'):
            poz+=1
            if re.search(reg_exprr,str(sss)):
                for jj in list_operand_var:
                    reg_exprr2 = ""
                    reg_exprr2 +=str_of_operand+"+"
                    reg_exprr2 +="(| |)*"
                    reg_exprr2 += jj[1]
                    reg_exprr2 +="(| |)*"
                    reg_exprr2 +=str_of_operand2+"+"
                    if re.search(reg_exprr2,str(sss)):
                        stroka_analiza = "\n Analyzing massive:" +str(name_of) + "\n"
                        if our_errors == []:
                             our_errors.append(stroka_analiza)
                        else:
                            if stroka_analiza not in our_errors:
                                our_errors.append(stroka_analiza)                        
                        if jj[1] not in vvod_per:
                            Analyzing_input_massive(jj[0],jj[1],poz+1)
                        else:
                            oshibka = ""
                            oshibka += "+++++++++++++++++++++++++++++++++++"+"\n"
                            oshibka += "Warning"+"\n"
                            oshibka += "Massive is depend upon variable " + str(jj[1])+"\n"
                            oshibka += stroka_pred+"\n"
                            oshibka += sss+"\n"
                            oshibka += ourcode.split('\n')[poz+1]+"\n"
                            oshibka += "++++++++++++++++++++++++++++++++++++"+"\n"
                            if our_errors == []:
                                our_errors.append(oshibka)
                            else:
                                if oshibka not in our_errors:
                                    our_errors.append(oshibka)
            stroka_pred = sss                       
def Main_function(stroki_koda):
    global list_func_start_end
    list_func_start_end = []
    global imena_funckii
    imena_funckii = []
    global vvod_per
    vvod_per = []
    global ourcode_without_ifs
    ourcode_without_ifs = ""
    global ourcode_comb
    ourcode_comb = ""
    global if_else_hierarchi
    if_else_hierarchi = []
    global loop_var_for
    loop_var_for = []
    global loop_var_while
    loop_var_while = []
    global flag_for
    flag_for = 0
    global flag_while
    flag_while = 0
    global hierar
    hierar = 5
    global our_errors
    our_errors = []    
    ourcode2 = ""
    global ourcode2
    ourcode2 = stroki_koda

    Function_detect()
    Function_start_end()

    for funkcii in imena_funckii:############################
        stroka_analiza = "\n Analyzing function:" +str(funkcii[0])+"\n"
        if our_errors == []:
             our_errors.append(stroka_analiza)
        else:
            if stroka_analiza not in our_errors:
                our_errors.append(stroka_analiza)     
        global ourcode
        global if_else_hierarchi
        global ourcode_without_ifs
        ourcode = ""
        if_else_hierarchi = []
        for i in list_func_start_end:
            if i[0] == funkcii[0]:
                for ssttrr in ourcode2.split('\n')[i[1]:i[2]]:
                    ourcode += ssttrr+ "\n"
        if_else_analyzing(ourcode,0)
        
        if ourcode_without_ifs ==[]:
            vvod_per = []
            Main_func()
        else:
            razdelenii_if = if_else_adding(if_else_hierarchi)
            stroka_do_ifov = ""
            for stroki in ourcode_without_ifs:
                stroka_do_ifov += "\n"+stroki
            if len(razdelenii_if) > 1:
                for chasti_ifa in razdelenii_if:
                    ourcode = stroka_do_ifov + chasti_ifa
                    global our_errors
                    vvod_per = []
                    Main_func()
            else:
                ourcode = stroka_do_ifov + razdelenii_if[0][0]
                global our_errors
                vvod_per = []
                Main_func()
                
                ourcode = stroka_do_ifov + razdelenii_if[0][1]
                global our_errors
                vvod_per = []
                Main_func()           
    return our_errors    
                
        



