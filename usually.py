def URLEncode(region_or_title):
    encoded=str(region_or_title.encode('utf-8'))
    splited=encoded.replace("\\"," ").replace("x","%").replace("\'"," ").split()
    splited=splited[1:]
    output="".join(splited)
    return output



if len(s_title) >0 :
    store_information += '🐥 가게 이름 : ' + s_title + '\n'
    if len(s_address) > 0 :
        store_information += '🐥 주소 : ' + s_address + '\n'
        if len(s_telephone) > 0 :
            store_information += '🐥 전화번호 : ' + s_telephone + '\n'
            if len(s_description) > 0 :
                store_information += '🐥 요약 : ' + s_description + '\n'
                if len(s_link) > 0 :
                    store_information += '🐥 사이트 : ' + s_link + '\n'


  # store_information = '🐥 가게 이름 : ' + s_title + '\n🐥 주소 : ' + s_address + '\n' + s_telephone + '\n' + s_description + '\n' + s_link
