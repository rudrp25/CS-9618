class Lesson:
    def __init__(self,t,d,r):
        self.__LessonTitle = t
        self.__DurationMins = d
        self.__RequiresLab = r

    def SetLessonTitle(self,newt):
        self.__LessonTitle = newt

    def SetLabStatus(self,newl):
        self.__RequiresLab = newl

    def SetDuration(self, time):
        self.__DurationMins = time

    def GetLessonTitle(self):
        return(self.__LessonTitle)

    def GetLabStatus(self):
        return(self.__RequiresLab)

    def GetDuration(self):
        return(self.__DurationMins)

    def OutputLessonsDetails(self):
        print("Lesson title: ", self.__LessonTitle)
        print("Lesson duration: ", self.__DurationMins)
        print("Requires lab? ", self.__RequiresLab)


class Assessment:
    def __init__(self,t,m):
        self.__AssessmentTitle = t
        self.__MaxMarks = m

    def SetTitle(self,t):
        self.__AssessmentTitle = t

    def SetMarks(self,m):
        self.__MaxMarks = m

    def GetTitle(self):
        return(self.__AssessmentTitle)

    def GetMaxMarks(self):
        return(self.__MaxMarks)

    def OutputAssessmentDetails(self):
        print("Assessment title is: ", self.__AssessmentTitle)
        print("Max marks obtained: ", self.__MaxMarks)


class Course:
    def __init__(self,t,m):
        self.__CourseTitle = t
        self.__MaxStudents = m
        self.__NumberOfLessons = 0
        self.__CourseLesson = []
        self.__CourseAssessment = Assessment(t,m)

    def AddLesson(self,t,d,r):
        self.__NumberOfLessons += 1
        self.__CourseLesson.append(Lesson(t,d,r))

    def AddAssessment(self,t,m):
        self.__CourseAssessment = Assessment(t,m)

    def OutputCourseDetails(self):
        print("Course title: ", self.__CourseTitle)
        print("Max students: ", self.__MaxStudents)
        for i in range(self.__NumberOfLessons):
            print(self.__CourseLesson[i].OutputLessonDetails)

# actual task

course  = []

t = input("Enter course title: ")
m = input("Enter max students: ")
course.append(Course(t,m))

for i in range(0,3):
    print("-----------------------")
    t = input("Enter lesson title: ")
    d = input("Duration of lesson: ")
    r = input("Does it require lab (Yes/No)? ")
    course.append(Lesson(t,d,r))

t = input("Add assessment title: ")
m = input("Max marks for test: ")
course.append(Assessment(t,m))

for i in course:
    course[i].OutputCourseDetails()
    course[i].OutputLessonsDetails()
    course[i].OutputAssessmentDetails()