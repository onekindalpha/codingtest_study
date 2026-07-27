#C, C#, D, D#, E, F, F#, G, G#, A, A#, B
#각 음은 1분에 1개씩 재생
# 처음부터 재생. 음악길이보다 재생된 시간이 길 때는 처음부터 반복해서 재생
# 음악길이 보다 재생된 시간이 짧을 때는 처음부터 재생시간만큼만 재생
# 00:00을 넘기지 않음
# 조건이 일치하는 음악이 여러개일때는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환함.
# 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환함.
# 조건이 일치하는 음악이 없을 대 "(None)"을 반환함.

#음악은 1분에 1개씩 제공됨.

harmony = ["C, C#, D, D#, E, F, F#, G, G#, A, A#, B"]
def replace_sharp(melody):
    return (melody
            .replace("C#", "c")
            .replace("D#", "d")
            .replace("F#", "f")
            .replace("G#", "g")
            .replace("A#", "a"))

def to_minute(start_music, end_music):
    #map(int, ...)은 문자열 목록의 각 값을 int로 바꾸는 기능
    start_hour, start_minute = map(int, start_music.split(":"))
    end_hour, end_minute = map(int, end_music.split(":"))
    # 각 음은 1분에 1개씩 재생되니까, 분단위로 맞춘다.
    start_total = start_hour * 60 + start_minute
    end_total = end_hour * 60 + end_minute
    # 총 분을 반환한다.
    return end_total - start_total

#m은 이중에 내가 기억한 멜로디 일부분?
def solution(m, musicinfos):
    answer = "(None)"
    ## 실제 재생 시간은 0 이상이므로 첫 후보가 나오면 무조건 갱신된다.
    max_play_time = -1
    #조건에 일치하는 음악제목을 찾기.
    for musicinfo in musicinfos:
        # 정보들을 분리한다.
        start_music, end_music, music_title, music_sheet = musicinfo.split(",")
        # 악보 길이는 #이 있는 경우를 고려해서 변환해야 함.
        music_sheet = replace_sharp(music_sheet)
        # 멜로디의 길이는 #이 있는 경우를 고려해서 변환해야 함.
        melody = replace_sharp(m)
        #원본 악보의 음개수.
        music_sheet_len = len(music_sheet)
        #재생시간 계산
        play_time = to_minute(start_music, end_music)
        # 재생시간만큼 악보(악보의 음의 개수)를 반복한 뒤 필요한 길이만 자른다.
        # ex. [:1]이건 앞에서 한개.
        played = music_sheet * (play_time // music_sheet_len) + music_sheet[:play_time%music_sheet_len]
        # 기억한 멜로디가 재생한 멜로디에 포함되는지 본다.
        if melody in played:
            ## 재생 시간이 더 긴 곡만 정답으로 갱신한다.
            # 재생 시간이 같으면 갱신하지 않는다.
            # 그래야 musicinfos에서 먼저 나온 곡 제목이 유지된다.
            ## >= 를 쓰면 재생 시간이 같은 경우 뒤에 나온 곡으로 바뀌므로 조건에 맞지 않는다.
            if play_time > max_play_time:
                #최대재생시간곡을 갱신한다.
                max_play_time = play_time
                #정답은 음악 제목이다.
                answer = music_title
    return answer