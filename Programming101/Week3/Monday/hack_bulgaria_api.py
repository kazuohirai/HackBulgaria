import requests
from random import shuffle


class API():

    def __init__(self, url):
        self.url = url

    def list_all_courses(self):
        r = requests.get(self.url, verify=False)
        courses = r.json()
        coursesList = []
        for each in range(0, len(courses)):
            for course in range(0, len(courses[each]['courses'])):
                coursesList.append(courses[each]['courses'][course]['name'])
        coursesList = sorted(set(coursesList))
        for item in range(0, len(coursesList)):
            print ("[%s] %s" % (item+1, coursesList[item]))
        return coursesList

    def match_teams(self, course_id, team_size, group_time):
        course_id -= 1
        peopleToMatch = []
        r = requests.get(self.url, verify=False)
        courses = r.json()
        coursesList = self.list_all_courses()
        courseToMatchFrom = coursesList[course_id]
        for each in range(0, len(courses)):
            for course in range(0, len(courses[each]['courses'])):
                if (courses[each]['courses'][course]['name'] ==
                   courseToMatchFrom and
                   courses[each]['courses'][course]['group'] == group_time):
                    peopleToMatch.append(courses[each]['name'])
        peopleToMatch = sorted(peopleToMatch)

        shuffle(peopleToMatch)
        for i in range(0, len(peopleToMatch)):
            if i % team_size == 0:
                print ('\n')
            print (peopleToMatch[i])


new = API('https://hackbulgaria.com/api/students/')
new.match_teams(8, 3, 2)
