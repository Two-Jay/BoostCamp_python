from urllib.request import urlopen

def request_lyrics() -> str:
    url = "https://raw.githubusercontent.com/TeamLab/introduction_to_python_TEAMLAB_MOOC/master/code/6/yesterday.txt"
    return urlopen(url).read().decode("utf-8")

def find_word_in_lyrics(word: str, lyrics: str) -> None:
    print(f"{word} count: {lyrics.lower().count(word)}")

def print_lyrics() -> None:
    print("Yesterday ___ by Beatles ____")
    print(request_lyrics())

def run_finder() -> None:
    print_lyrics()
    find_word_in_lyrics(input("Yesterday 가사에서 찾을 단어를 입력하세요 (소문자로) : "), request_lyrics())

run_finder()