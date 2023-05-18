from datetime import datetime, timedelta, date
from test_users_dict import users  # імпорт тестового списка


def get_birthdays_per_week(users):
    # Визначаємо поточну дату
    today = datetime.now()

    # Знаходимо першу неділю від поточної дати
    sunday = today + timedelta(days=(6 - today.weekday()))

    # Знаходимо дати для кожного дня наступного тижня
    next_week = [sunday + timedelta(days=i) for i in range(7)]

    # Створюємо словник, в якому ключами є дні тижня, а значеннями — порожні списки
    birthdays_per_day = {day.strftime('%A'): [] for day in next_week}

    # Додаємо користувачів до списків для відповідних днів тижня
    for user in users:
        for key, value in user.items():
            name = key
            birthday = value

            # Якщо день народження вже пройшов цього року, то додаємо його наступного року
            if birthday < today:
                birthday = date(
                    today.year + 1, birthday.month, birthday.day)

            # Додаємо користувача до відповідного списку
            day_of_week = birthday.strftime('%A')
            if day_of_week in birthdays_per_day:
                if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                    birthdays_per_day['Monday'].append(name)
                else:
                    birthdays_per_day[day_of_week].append(name)

    # Виводимо список користувачів для кожного дня тижня
    for day, users in birthdays_per_day.items():
        if users:
            print(f'{day}: {", ".join(users)}')


# викликаємо функцію
get_birthdays_per_week(users)
