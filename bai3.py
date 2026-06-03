students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

def find_student_by_id(student_list, student_id):
    for i in student_list:
        if i['student_id'] == student_id:
            return i

    return None

def display_students(student_list):
    if len(student_list) == 0:
        print('Danh sách học viên hiện đang trống.')
        return

    print('--- DANH SÁCH HỌC VIÊN ---')

    for index, i in enumerate(student_list, start=1):
        print(f'{index}. Mã: {i["student_id"]} | Tên: {i["name"]} | Toán: {i["math_score"]} | Anh: {i["english_score"]}')

def add_student(student_list):
    while True:
        student_id = input('Nhập mã học viên: ').strip().upper()

        if find_student_by_id(student_list, student_id) != None:
            print('Mã học viên đã tồn tại, vui lòng nhập mã khác!')
            continue

        break

    while True:
        name = input('Nhập tên học viên: ').strip().title()

        if name == '':
            print('Tên học viên không được để trống!')
            continue

        break

    while True:
        math_score = input('Nhập điểm Toán: ').strip()

        if not math_score.replace('.', '', 1).isdigit():
            print('Điểm không hợp lệ, phải là số từ 0 đến 10!')
            continue

        math_score = float(math_score)

        if math_score < 0 or math_score > 10:
            print('Điểm không hợp lệ, phải là số từ 0 đến 10!')
            continue

        break

    while True:
        english_score = input('Nhập điểm Anh: ').strip()

        if not english_score.replace('.', '', 1).isdigit():
            print('Điểm không hợp lệ, phải là số từ 0 đến 10!')
            continue

        english_score = float(english_score)

        if english_score < 0 or english_score > 10:
            print('Điểm không hợp lệ, phải là số từ 0 đến 10!')
            continue

        break

    student_list.append({
        'student_id': student_id,
        'name': name,
        'math_score': math_score,
        'english_score': english_score
    })

    print('Thêm học viên thành công!')

def update_score(student_list):
    update_id = input('Nhập mã học viên cần cập nhật: ').strip().upper()

    flag = find_student_by_id(student_list, update_id)

    if flag == None:
        print(f'Không tìm thấy học viên mang mã {update_id}!')
        return

    while True:
        new_math = input('Nhập điểm Toán mới: ').strip()

        if not new_math.replace('.', '', 1).isdigit():
            print('Điểm không hợp lệ, phải là số từ 0 đến 10!')
            continue

        new_math = float(new_math)

        if new_math < 0 or new_math > 10:
            print('Điểm không hợp lệ, phải là số từ 0 đến 10!')
            continue

        flag['math_score'] = new_math
        break

    while True:
        new_english = input('Nhập điểm Anh mới: ').strip()

        if not new_english.replace('.', '', 1).isdigit():
            print('Điểm không hợp lệ, phải là số từ 0 đến 10!')
            continue

        new_english = float(new_english)

        if new_english < 0 or new_english > 10:
            print('Điểm không hợp lệ, phải là số từ 0 đến 10!')
            continue

        flag['english_score'] = new_english
        break

    print('Cập nhật điểm thành công!')

def get_rank(avg_score):
    if avg_score >= 8:
        return 'Giỏi'
    elif avg_score >= 6.5:
        return 'Khá'
    elif avg_score >= 5:
        return 'Trung bình'
    else:
        return 'Yếu'

def evaluate_students(student_list):
    if len(student_list) == 0:
        print('Danh sách học viên hiện đang trống.')
        return

    print('--- ĐÁNH GIÁ HỌC LỰC ---')

    for i in student_list:
        avg_score = (i['math_score'] + i['english_score']) / 2
        rank = get_rank(avg_score)

        print(f'Mã: {i["student_id"]} | Tên: {i["name"]} | ĐTB: {avg_score:.2f} | Xếp loại: {rank}')

if __name__ == '__main__':
    while True:
        choice = input('''
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====
1. Hiển thị danh sách học viên
2. Thêm học viên mới
3. Cập nhật điểm thi theo mã học viên
4. Đánh giá học lực của toàn bộ học viên
5. Thoát chương trình
====================================================
Chọn chức năng (1-5): ''')

        if not choice.isdigit():
            print('Lựa chọn không hợp lệ! Nhập lại từ 1 - 5!')
            continue

        choice = int(choice)

        if choice == 1:
            display_students(students)

        elif choice == 2:
            add_student(students)

        elif choice == 3:
            update_score(students)

        elif choice == 4:
            evaluate_students(students)

        elif choice == 5:
            print('Cảm ơn bạn đã sử dụng hệ thống!')
            break

        else:
            print('Lựa chọn không hợp lệ! Nhập lại từ 1 - 5!')