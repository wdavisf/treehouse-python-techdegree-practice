# Jen's explanation:

test_dict = {
    'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
    'Chris Howell': ['new Python course 1', 'random Python trivia', 'crazy Python tricks'],
    'Kenneth Love': ['Python Basics', 'Python Collections']}


def courses(dict):
    all_courses = []
    print(30 * "=")
    print("Jen's version")
    for teacher in dict:
        print(dict[teacher])
        all_courses.extend(dict[teacher])
    print(30 * "=")
    print()
    return all_courses
  

def courses_will(dict):
    course_names = []
    print(30 * "*")
    print("Will's version")
    for course in dict.values():
        print(course)
        course_names.extend(course)
    print(30 * "*")
    print()
    return course_names

print(courses(test_dict))
print()
print(courses_will(test_dict))

# All tasks:

# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

def num_teachers(dict):
    return len(dict)

def num_courses(dict):
    course_list = []
    for course in dict.values():
        course_list += course
    return len(course_list)

def courses(dict):
    course_names = []
    for course in dict.values():
        course_names = course_names + course
    return course_names

def most_courses(dict):
    max_count = 0
    teacher_name = ""
    for teacher,course in dict.items():
        if len(course) > max_count:
            teacher_name = teacher
            max_count = len(course)
    return teacher_name

def stats(dict):
    course_list = []
    for key, value in dict.items():
        course_list.append([key, len(value)])
    return course_list