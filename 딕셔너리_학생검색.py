import json
student_map = {} # 학생정보 저장할 빈 딕셔너리 생성

# 학생정보 등록
def reg_student():
    student_id = input("학번 입력 : ")
    name = input("이름 입력 : ")
    addr = input("주소 입력 : ")
    student_map[student_id] = {"이름" : name, "주소" : addr} # 값에 딕셔너리 추가, 아래에서 계속 사용
    print(f"{name}님의 정보가 등록되었습니다.")

# 학생정보 검색
def search_student():
    student_id = input("검색 학번 입력 : ")
    student_info = student_map.get(student_id)
    if student_info:
        print(f"학번 : {student_id}")
        print(f"이름 : {student_info['이름']}")
        print(f"주소 : {student_info['주소']}")
    else:
        print("해당 학생 정보를 찾을 수 없음")

# 학생정보 변경
def modify_student():
    student_id = input("수정할 학번 입력 : ")
    student_info = student_map.get(student_id)
    if student_info:
        name = input("새로운 이름 입력 : ") #여기서 학생에 관한 정보 넣고
        addr = input("새로운 주소 입력 : ")
        student_info['이름'] = name      #이 정보를 딕셔너리에서 업데이트하고 수정 사항을 확인합니다.
        student_info['주소'] = addr
        print(f"{name}님의 정보 수정완료!")
    else: print("해당 학생 정보가 없음")

# 학생정보 삭제
def delete_student():
    student_id = input("삭제할 학번 입력 : ")
    if student_map.get(student_id):
        del student_map[student_id]
        print("삭제 완료!")
    else: print("해당 학생 정보 찾을 수 없음")

# 학생정보 보기
def view_all_student():
    for student_id in student_map: # 이제 입력했던 값 불러오는 것
        student_info = student_map[student_id] # student_map.get(student_id)
        print(f"학번: {student_id}")
        print(f"이름: {student_info['이름']}")
        print(f"주소: {student_info['주소']}")

# 학생정보 저장
def save_student():
    with open("student.json", 'w', encoding='utf-8')as file:
        json.dump(student_map,file,ensure_ascii=False) #ensure_ascii=False 매개변수는 JSON 파일에 비 ASCII 문자가 올바르게 인코딩되도록 합니다.
# json파일 불러옴
def load_student():
    try:
        with open('student.json','r',encoding='utf-8')as file:
            student_map.clear()
            student_map.update(json.load(file))
        print("학생정보 불러옴")
    except FileExistsError:
        print("학생정보가 저장된 파일을 찾을 수 없음")


while True :
    print("="*5, "학생 정보 관리 프로그램", "="*5)
    choice = input("[1]등록 [2]검색 [3]수정 [4]삭제 [5]전체보기 [6]저장 [7]불러오기 [8]종료")
    if choice   == "1":reg_student()
    elif choice == "2":search_student()
    elif choice == "3":modify_student()
    elif choice == "4":delete_student()
    elif choice == "5":view_all_student()
    elif choice == "6":save_student()
    elif choice == "7":load_student()
    elif choice == "8":break
    else: print("선택한 메뉴가 없습니다.")