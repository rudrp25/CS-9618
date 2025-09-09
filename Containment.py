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

    def OutputLessonDetails(self):
        print("Lesson title: ", self.GetLessonTitle())
        print("Lesson duration: ", self.GetDuration())
        print("Requires lab? ", self.GetLabStatus())


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
        print("Assessment title is: ", self.GetTitle())
        print("Max marks obtained: ", self.GetMaxMarks())


class Course:
    def __init__(self,t,m):
        self.__CourseTitle = t
        self.__MaxStudents = m
        self.__NumberOfLessons = 0
        self.__CourseLesson = []
        self.__CourseAssessment = None

    def GetTitle(self):
        return (self.__CourseTitle)

    def GetMaxStudents(self):
        return (self.__MaxStudents)

    def GetNumberOfLessons(self):
        return (self.__NumberOfLessons)

    def IncrementLesson(self):
        self.__NumberOfLessons += 1

    def AddLesson(self,t,d,r):
        self.__CourseLesson.append(Lesson(t,d,r))
        self.IncrementLesson()

    def AddAssessment(self,t,m):
        self.__CourseAssessment = Assessment(t,m)

    def OutputCourseDetails(self):
        print("Course title: ", self.GetTitle())
        print("Max students: ", self.GetMaxStudents())

        print("--- Lessons ---")
        for lesson in self.__CourseLesson:
            lesson.OutputLessonDetails()
            print()
        print('--- Assessments --- ')
        if self.__CourseAssessment:
            self.__CourseAssessment.OutputAssessmentDetails()
            print()

# actual task
course = Course("A Level Computer Science", 30)
course.AddLesson('Python OOP Basics', 60, True)
course.AddLesson('Recursion', 50, False)
course.AddLesson('Abstract Data Types', 70, True)
course.AddAssessment('Unit Test 1', 50 )

course.OutputCourseDetails()