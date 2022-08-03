class Note(object):
    def __init__(self, content = str):
        self.content = content

    def __add__(self, other):
        return self.content + other.content

    def __str__(self):
        return self.content

    def write(self, content = str):
        return self.content

    def clear(self):
        self.content = ""
        return self.content

class NoteBook(object):
    def __init__(self):
        self.note_list = {}

    def add_note(self, note):
        self.note_list.append(note)

    def remove_note(self, note, page_nuumber):
        self.note_list.pop(page_nuumber)

    def get_note_by_page(self, index):
        return self.note_list[index] if len(self.note_list) > index and index >= 0 else None

    def size(self):
        return len(self.note_list)

def print_banner():
    print("""
    *************************
    *  노트북                 *
    *************************
    메뉴 :
    1. 새 메모 생성
    2. 메모 조회
    3. 메모 수정
    4. 메모 삭제
    5. 메모 페이지 조회
    """)


def run_notebook():
    notebook = NoteBook()
    while True:
        ipt = input("메뉴를 선택하세요 (종료 : 'exit'): ")
        if ipt == "exit": break
        if ipt == "1":
            note = Note()
            notebook.add_note(note)
            print(f"새로운 메모를 생성했습니다. (메모 수 : {notebook.size()})")
        elif ipt == "2":
            page_number = int(input("메모의 페이지 번호를 입력하세요: "))
            note = notebook.get_note_by_page(page_number)
            if note:
                print(f"메모의 내용: {note}")
            else:
                print("존재하지 않는 메모입니다.")
        elif ipt == "3":
            page_number = int(input("메모의 페이지 번호를 입력하세요: "))
            note = notebook.get_note_by_page(page_number)
            if note:
                note.clear()
                print(f"메모를 지웠습니다. (메모 수 : {notebook.size()})")
            else:
                print("존재하지 않는 메모입니다.")
        elif ipt == "4":
            page_number = int(input("메모의 페이지 번호를 입력하세요: "))
            note = notebook.get_note_by_page(page_number)
            if note:
                note.write()
                print(f"메모를 수정했습니다. (메모 수 : {notebook.size()})")
            else:
                print("존재하지 않는 메모입니다.")
        elif ipt == "5":
            size_notes = notebook.size()
            if size_notes == 0:
                print("메모가 없습니다.")
            else:
                print(f"메모 수: {size_notes}")
                for i in range(size_notes):
                    note = notebook.get_note_by_page(i)
                    print(f"{i+1}. {note}")