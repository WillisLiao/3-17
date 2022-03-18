txt = '朋友 王大頭 他的手機號碼 0981-231-432 用了20年了都沒有換，有好也有壞，某天多年前的朋友 S姐的手機 0988000090 號碼出現在他的來電顯示裡，接起電話說要和他結婚，興奮的滿口答應，於是S姐就請他先跟某電視台記者 K先生聯絡 (0999-999-999)，說要辦說明會，王大頭覺得怪，於是打電話給警察朋友 P先生聯絡 (0911-956-956) 請他幫忙分析有沒有可能是詐騙'
def check(txt2):
    flag = 1
    for i in range(12):
        if i==4 or i==8 and txt2[i] != '-':
            flag = 0
        elif txt2[i].isdecimal()==False:
            flag = 0
    if flag ==0:
        return False
    else:
        return True
for i in range(len(txt)-12):
    if txt[i].isdecimal():
        if check(txt[i:i+12]):
            print(txt[i:i+12])
