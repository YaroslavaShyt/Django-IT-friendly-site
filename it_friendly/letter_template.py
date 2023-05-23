def get_letter_template(course_data):
    subject = f'IT-friendly {course_data["type"]}: {course_data["title"]}'
    message = f'Вітаємо!\n\n' \
              f'Вам надано доступ до {course_data["type"]}у {course_data["title"]}.\n\n' \
              f'Постійне посилання на курс: https://teams.microsoft.com/l/meetup-join/19%3ameeting_NzIxNGJmYzktYWVjYy00NzAwLWJmYWYtMjc0ZWQ5OWQwZWRh%40thread.v2/0?context=%7b%22Tid%22%3a%22cf94ad9d-2983-43f5-9909-722602ea2165%22%2c%22Oid%22%3a%22122c3cf2-8129-47f8-a762-010691385d4d%22%7d'
    return {'subject': subject, 'message': message}


def get_ask_question_letter_template(question_data):
    print(question_data)
    subject = f'IT-friendly: питання'
    message = f'Ім\'я: {question_data["name"]}\n\n' \
              f'Тип зв\'язку: {question_data["contact_method"]}\n\n' \
              f'Ідентифікатор: {question_data["contact_info"]}\n\n' \
              f'Запитання: {question_data["question"]}'
    return {'subject': subject, 'message': message}