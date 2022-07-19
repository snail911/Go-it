from datetime import datetime



def get_birthdays_per_week(users):
    current_datetime = datetime.now()

    month = current_datetime.month
    day = current_datetime.day
    max = day + 7
    new_lst = []
    lst = []
    for i in users:
        s = i.get('birthday')
        lst.append(s)
    for i in lst:
        if i.month == month and day <= i.day <= max:
            new_lst.append(i)

    items = []
    names = []
    dic = {}
    for el in users:
        for item in new_lst:
            a = el.get('birthday')

            if a == item:
                item = item.strftime('%A %d %B %Y')
                item = item.split(" ")[0]
                s = el.get('name')
                items.append(item)
                names.append(s)
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    index = 0
    for i in items:
        if i == 'Friday':
            friday.append(names[index])
        if i == 'Tuesday':
            tuesday.append(names[index])
        if i == 'Wednesday':
            wednesday.append(names[index])
        if i == 'Thursday':
            thursday.append(names[index])
        if i == 'Monday' or i == 'Sunday' or i == 'Saturday':
            monday.append(names[index])
        index += 1
    all = [monday] + [tuesday] + [wednesday] + [thursday] + [friday]

    for days in all:
        if not days:
            pass
        else:
            if days == monday:
                print('Monday: ' + ', '.join(days))
            if days == tuesday:
                print('Tuesday: ' + ', '.join(days))
            if days == wednesday:
                print('Wednesday: ' + ', '.join(days))
            if days == thursday:
                print('Thursday: ' + ', '.join(days))
            if days == friday:
                print('Friday: ' + ', '.join(days))




