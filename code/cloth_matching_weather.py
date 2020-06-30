import urllib.request
import json
#import test_predict_function as predict # 연동 시 필요, 여기서 테스트만 할거라면 주석처리 ㄱㄱ

def searchWord(input): # 인자값에 따라 read1, 2값이 달라짐
    if input == " ": print("옷을 인식한게 맞는지 확인하십시오") # 애초에 옷 자체를 안식 못해버린거
    else: # 50개 중 무언가로 인식한 경우
        if "Tee" == input or "Button-Down" == input or "Henley" == input or "Jersey" == input:
            read1 = "상의"; read2 = "가변성";
        elif "Top" == input or "Tank" == input or "halter" == input or "Blazer" == input\
                or "Blouse" == input or "Hoodie" == input or "Cardigan" == input or "Jacket" == input\
                or "Poncho" == input or "Flannel" == input or "Sweater" == input or "Parka" == input\
                or "Turtleneck" == input or "Bomber" == input or "Peacoat" == input or "Anorak" == input:
            read1 = "상의"; read2 = "고정성";
        elif "Jeans" == input or "Joggers" == input or "Sweatpants" == input or "Shorts" == input or "Skirt" == input:
            read1 = "하의"; read2 = "가변성";
        elif "Cutoffs" == input or "Sweatshorts" == input or "Trunks" == input or "Culottes" == input\
                or "Gauchos" == input or "Sarong" == input or "capri" == input or "Chinos" == input\
                or "Jeggings" == input or "Jodhpurs" == input or "Leggings" == input:
            read1 = "하의"; read2 = "고정성";
        elif "Dress" == input or "Coat" == input or "Nightdress" == input\
                or "Robe" == input or "Romper" == input or "Shirtdress" == input:
            read1 = "한 벌 옷"; read2 = "가변성";
        elif "Sundress" == input or "Onesie" == input or "Coverup" == input or "Caftan" == input\
                or "Kaftan" == input or "Jumpsuit" == input or "Kimono" == input or "Cape" == input:
            read1 = "한 벌 옷"; read2 = "고정성";
        matching(read1, read2, input) # 어떤 옷인지 구분해주는 read1, 2값과 인식한 옷을 인자로 해서 날씨적합성 판단함수로 넘김


def matching(want_element1, want_element2, input):
    # want_element1 = 상하의, want_element2=종류, want_element3=기온(=temp), want_element4=날씨(=weather)
    apiurl = 'http://api.openweathermap.org/data/2.5/weather?'
    """city = ['Seoul', 'Busan', 'Daegu', 'Incheon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Suwon', 'Yongin',
    'Changwon', 'Goyang', 'Seongnam', 'Bucheon', 'Cheongju', 'Hwaseong', 'Namyangju', 'Jeonju', 'Ansan', 'Cheonan']"""
    apikey = '&APPID=556ce4146768bd277ba1bfb88f8c7bcb'
    # api 받아오기 위한 좌표 등 기본정보
    """ 원래 ex-'이 옷은 [파란색] [상의] [Tee] 입니다' 지금 날씨(기온)이 ~ 이므로 지금 입기에 (ex-적합/부적합)합니다.
    이런식으로 하는게 우리가 생각한 시나리오인데 도중에 장소선택 이 나와있네..! 오직 정왕동만 한다면 상관없지만
    시흥시를 범위로 뒤고 동 단위를 선택한다고 한다면 조금 생각해 볼 문제임 -> 우선은 장소고정!
    print("1: Seoul / 2: Busan / 3: Daegu / 4: Incheon / 5: Daejeon \n" +
      "6: Gwangju / 7: Ulsan / 8: Jeju / 9: Suwon-si / 10: Yongin \n\n" +
      "11: Changwon / 12: Goyang-si / 13: Seongnam-si / 14: Bucheon-si / 15: Cheongju-si \n" +
      "16: Hwaseong-si / 17: Namyangju / 18: Jeonju / 19: Ansan-si / 20: Cheonan \n" + "(0: Exit)")
    num = int(input("Choose city number: ")) # 왜 잘되던게 값자기 str객체드립치면서 오류뜨냐...? 주석만 수정했는데 왜..? """

    #url = urllib.request.urlopen(apiurl + "q=" + city[num - 1] + apikey) 장소 고정이 아닐 경우
    url = urllib.request.urlopen(apiurl + "q=" + 'Ansan-si' + apikey)
    apid = url.read()
    data = json.loads(apid)
    cityname = data['name']
    weather = data['weather'][0]['main'] # == want_element4
    temp = int(data['main']['temp'] - 273.15) # == want_element3
    """ 여기까지 해서 날씨와 관련된 변수들도 get했고 이제 본격적으로 날씨적합성을 판단한다. 아니면 날씨 관련 변수들 구하는 걸
    별도 함수로 구현하고 총 4개의 인자를 받아 날씨적합성 판단하는 코드를 만드는 식으로 분리구현해도 된다! -> 일단은 그냥 전자대로 ㅎ"""

    # 날씨적합성 판단 시작! want_element 값에 따라 실행되는 함수가 달라짐
    result1 = "현재 날씨는 " + weather + ', ' + str(temp) + '˚C' + " 입니다. "
    result2 = "지금 고른 옷은 " + input + "이므로 "
    if want_element2 == "가변성": # 우선은 가변성 의류부터!
        """ 지금은 기온 먼저 분류하고 상/하/한 했지만 상/하/한 먼저 분류한 다음 기온분류 하는걸로 바꿀수도 있음!
        일단 이해는 해야 하니까 각각 다 써줬지만 공통인 부분만큼 코드 합칠거임!!!!! 그냥 코드는 전자대로... ㅎ """
        if temp > 28:
            if want_element1 == "상의":
                print(result1+result2+"두께가 얇고 길이가 짧다면 지금 입기에 가장 적합합니다.")
            elif want_element1 == "하의":
                print(result1+result2+"두께가 얇고 길이가 짧다면 지금 입기에 가장 적합합니다.")
            else: # want_element1 == "한벌옷"
                print(result1+result2+"두께가 얇고 길이가 짧다면 지금 입기에 가장 적합합니다.")
        elif temp > 23:
            if want_element1 == "상의":
                print(result1+result2+"두께가 얇고 길이가 짧다면 지금 입기에 가장 적합합니다.")
            elif want_element1 == "하의":
                print(result1+result2+"두께가 얇다면 지금 입기에 가장 적합합니다.")
            else: # want_element1 == "한벌옷"
                print(result1+result2+"두께가 얇고 길이가 짧거나 보통일 때 지금 입기에 가장 적합합니다.")
        elif temp > 20:
            if want_element1 == "상의":
                print(result1+result2+"두께는 얇고 길이가 짧거나 보통일 때 지금 입기에 가장 적합합니다.")
            elif want_element1 == "하의":
                print(result1+result2+"두께는 얇거나 보통일 때 지금 입기에 가장 적합합니다.")
            else: # want_element1 == "한벌옷"
                print(result1+result2+"두께는 얇거나 보통일 때 지금 입기에 가장 적합합니다.")
        elif temp > 17:
            if want_element1 == "상의":
                print(result1+result2+"두께는 얇거나 보통일 때 지금 입기에 가장 적합합니다.")
            elif want_element1 == "하의":
                print(result1+result2+"두께는 얇거나 보통이고 길이가 보통이거나 길 경우 지금 입기에 가장 적합합니다.")
            else: # want_element1 == "한벌옷"
                print(result1+result2+"두께는 보통일 때 지금 입기에 가장 적합합니다.")
        elif temp > 11:
            if want_element1 == "상의":
                print(result1+result2+"두께는 보통이고 길이가 보통이거나 길 경우 지금 입기에 가장 적합합니다.")
            elif want_element1 == "하의":
                print(result1+result2+"두께는 보통이고 길이가 길 경우 지금 입기에 가장 적합합니다.")
            else: # want_element1 == "한벌옷"
                print(result1+result2+"두께가 보통이거나 두껍고 길이는 보통이거나 긴 경우 지금 입기에 가장 적합합니다.")
        elif temp > 9:
            if want_element1 == "상의":
                print(result1+result2+"두께는 보통이고 길이가 두껍거나 긴 경우 지금 입기에 가장 적합합니다.")
            elif want_element1 == "하의":
                print(result1+result2+"두께는 보통이고 길이가 두껍거나 긴 경우 지금 입기에 가장 적합합니다.")
            else: # want_element1 == "한벌옷"
                print(result1+result2+"두께는 두껍고 길이가 긴 경우 지금 입기에 가장 적합합니다.")
        elif temp > 5:
            if want_element1 == "상의":
                print(result1+result2+"두께는 두껍고 길이가 긴 경우 지금 입기에 가장 적합합니다.")
            elif want_element1 == "하의":
                print(result1+result2+"두께는 두껍고 길이가 긴 경우 지금 입기에 가장 적합합니다.")
            else: # want_element1 == "한벌옷"
                print(result1+result2+"두께는 두껍고 길이가 긴 경우 지금 입기에 가장 적합합니다.")
        else:
            if want_element1 == "상의":
                print(result1+result2+"두께는 두껍고 길이가 긴 경우 지금 입기에 가장 적합합니다.")
            elif want_element1 == "하의":
                print(result1+result2+"두께는 두껍고 길이가 긴 경우 지금 입기에 가장 적합합니다.")
            else: # want_element1 == "한벌옷"
                print(result1+result2+"두께는 두껍고 길이가 긴 경우 지금 입기에 가장 적합합니다.")

    else: # want_element2 == "고정성"
        # 기온 별 적합성 옷 모음(상하의, 한벌옷 구분X, 오직 같은기온대로만 구분!)
        upper28 = ['Top', 'Tank', 'Cutoffs', 'Sweatshorts', 'Trunks', 'Sundress']
        from23to28 = ['halter', 'Onesie', 'Sundress', 'Coverup']
        from20to23 = ['Blazer', 'Blouse', 'Caftan', 'Kaftan', 'Jumpsuit', 'Kimono', 'Coverup']
        from17to20 = ['Blazer', 'Blouse', 'Hoodie', 'Cardigan', 'Jacket', 'Poncho', 'Culottes',
                      'Gauchos', 'Sarong', 'Caftan', 'Kaftan', 'Jumpsuit', 'Kimono', 'Coverup']
        from11to17 = ['Hoodie', 'Flannel',  'Cardigan', 'Jacket', 'Poncho',
                      'Caftan(Kaftan)', 'Jumpsuit', 'Kimono', 'Cape', 'Coverup']
        from9to11 = ['Hoodie', 'Cardigan', 'Jacket', 'Sweater', 'Turtleneck',
                     'Bomber', 'Parka', 'Peacoat', 'Cape', 'Coverup']
        from5to9 = ['Sweater', 'Parka', 'Bomber', 'Anorak', 'Turtleneck', 'Peacoat', 'capri',
                    'Chinos', 'Gauchos', 'Jeggings', 'Jodhpurs', 'Leggings', 'Sarong', 'Cape', 'Coverup']
        under5 = ['Sweater', 'Bomber', 'Parka', 'Peacoat', 'Cape', 'Coverup']

        # 멘트모음
        result3 = "입으면 조금 더울 것으로 예상됩니다. 다시한번 생각해 보십시오."
        result4 = "입으면 많이 더울 것으로 예상됩니다. 입지 않는 것을 추천합니다."
        result5 = "입으면 적당할 것으로 예상됩니다. 다른 얇은 옷을 먼저 입은 다음에 입는것도 가능합니다."
        result6 = "(이것만)입으면 조금 추울 것으로 예상됩니다. 만약 입는다면, 더 두꺼운 옷을 조금 껴입는 것을 추천합니다."
        result7 = "(이것만)입으면 많이 추울 것으로 예상됩니다. 만약 입는다면, 더 두꺼운 옷을 많이 껴입는 것을 추천합니다."

        if temp > 28: # 현재 기온이 28'C 이상인데
            if input in upper28: # 지금 고른 옷이 28'C 이상일 때 가장 적합한 경우
                print(result1+result2+"입으면 적당할 것으로 예상됩니다.") # 적당
            elif input in from23to28: # 지금 고른 옷이 23~28'C일 때 가장 적합한 경우
                print(result1+result2+result3) # 조금 더움
            else: # 지금 고른 옷이 23'C 이하일 때 가장 적합한 경우
                print(result1+result2+result4) # 많이 더움
        elif temp > 23: # 현재 기온이 23~28'C 인데
            if input in from23to28: # 지금 고른 옷이 23~28'C일 때 가장 적합한 경우
                print(result1+result2+result5) # 적당
            elif input in upper28: # 지금 고른 옷이 28'C 이상일 때 가장 적합한 경우
                print(result1+result2+result6) # 조금 추움
            elif input in from20to23: # 지금 고른 옷이 20~23'C일 때 가장 적합한 경우
                print(result1+result2+result3) # 조금 더움
            else: # 지금 고른 옷이 20'C 이하일 때 가장 적합한 경우
                print(result1+result2+result4) # 많이 더움
        elif temp > 20: # 현재 기온이 20~23'C 인데
            if input in from20to23: # 지금 고른 옷이 20~23'C일 때 가장 적합한 경우
                print(result1+result2+result5) # 적당
            elif input in from23to28: # 지금 고른 옷이 23~28'C일 때 가장 적합한 경우
                print(result1+result2+result6) # 조금 추움
            elif input in upper28: # 지금 고른 옷이 28'C 이상일 때 가장 적합한 경우
                print(result1+result2+result7) # 많이 추움
            elif input in from17to20:  # 지금 고른 옷이 17~20'C일 때 가장 적합한 경우
                print(result1+result2+result3)  # 조금 더움
            else: # 지금 고른 옷이 17'C 이하일 때 가장 적합한 경우
                print(result1+result2+result4) # 많이 더움
        elif temp > 17: # 현재 기온이 17~20'C 인데
            if input in from17to20: # 지금 고른 옷이 17~20'C일 때 가장 적합한 경우
                print(result1+result2+result5) # 적당
            elif input in from20to23: # 지금 고른 옷이 20~23'C일 때 가장 적합한 경우
                print(result1+result2+result6) # 조금 추움
            elif input in from23to28 or input in upper28: # 지금 고른 옷이 23'C 이상일 때 가장 적합한 경우
                print(result1+result2+result7) # 많이 추움
            elif input in from11to17: # 지금 고른 옷이 11~17'C일 때 가장 적합한 경우
                print(result1+result2+result3)  # 조금 더움
            else: # 지금 고른 옷이 11'C 이하일 때 가장 적합한 경우
                print(result1+result2+result4) # 많이 더움
        elif temp > 11: # 현재 기온이 11~17'C 인데
            if input in from11to17: # 지금 고른 옷이 11~17'C일 때 가장 적합한 경우
                print(result1+result2+result5) # 적당
            elif input in from17to20: # 지금 고른 옷이 17~20'C일 때 가장 적합한 경우
                print(result1+result2+result6) # 조금 추움
            elif input in from20to23 or input in from23to28 or input in upper28: # 지금 고른 옷이 20'C 이상일 때 가장 적합한 경우
                print(result1+result2+result7) # 많이 추움
            elif input in from9to11: # 지금 고른 옷이 9~11'C일 때 가장 적합한 경우
                print(result1+result2+result3) # 조금 더움
            else: # 지금 고른 옷이 9'C 이하일 때 가장 적합한 경우
                print(result1+result2+result4) # 많이 더움
        elif temp > 9: # 현재 기온이 9~11'C 인데
            if input in from9to11: # 지금 고른 옷이 9~11'C일 때 가장 적합한 경우
                print(result1+result2+result5) # 적당
            elif input in from11to17:  # 지금 고른 옷이 11~17'C일 때 가장 적합한 경우
                print(result1+result2+result6) # 조금 추움
            elif input in from17to20 or input in from20to23 or input in from23to28 or input in upper28 : # 지금 고른 옷이 17'C 이상일 때 가장 적합한 경우
                print(result1+result2+result7) # 많이 추움
            elif input in from5to9: # 지금 고른 옷이 5~9'C일 때 가장 적합한 경우
                print(result1+result2+result3) # 조금 더움
            else: # 지금 고른 옷이 5'C 이하일 때 가장 적합한 경우
                print(result1+result2+result4) # 많이 더움
        elif temp > 5: # 현재 기온이 5~9'C 인데
            if input in from5to9: # 지금 고른 옷이 5~9'C일 때 가장 적합한 경우
                print(result1+result2+result5)  # 적당
            elif input in from9to11: # 지금 고른 옷이 9~11'C일 때 가장 적합한 경우
                print(result1+result2+result6)  # 조금 추움
            elif input in from11to17 or input in from17to20 or input in from20to23 or input in from23to28 or input in upper28: # 지금 고른 옷이 11'C 이상일 때 가장 적합한 경우
                print(result1+result2+result7) # 많이 추움
            else: # 지금 고른 옷이 5'C 이하일 때 가장 적합한 경우
                print(result1+result2+result3)  # 조금 더움
        else: # 지금 고른 옷이 5'C 이하인데
            if input in under5: # 지금 고른 옷이 5'C 이하일 때 가장 적합한 경우
                print(result1+result2+result5) # 적당
            elif input in from5to9: # 지금 고른 옷이 5~9'C일 때 가장 적합한 경우
                print(result1+result2+result6) # 조금 추움
            else: # 지금 고른 옷이 11'C 이상일 때 가장 적합한 경우
                print(result1+result2+result7) # 많이 추움


if __name__ == "__main__":
    """ '이 옷은 파란색 상의 Tee 입니다.' > 이건 조합임. 타 코드와의 연동 고려해서
    ex) print("이 옷은 ", %s, "색 ", %s, %s, "입니다.", 색상, 상/하/한벌, 옷세부종류);
    처럼 리턴값을 문자열 통째로보단 각각 분리해서 받아야 함. 그러나!
    '파란', '상의' 이것들만으론 옷 속성판별이 조금 힘듬. 그래서 그냥 카테고리만 따져서 ㄱㄱ """
    # 연동할 때
    #inputTxt = predict.category_total()
    # 여기서 테스트
    inputTxt ="Top" # test_predict_function.py 에서 return 되는 'text' 변수!!!!!!!
    searchWord(inputTxt) # inputTxt는 옷 인식 결괏값을 string 문자열로 받아온거임
