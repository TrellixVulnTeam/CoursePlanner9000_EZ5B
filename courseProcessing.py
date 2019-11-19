import pandas as pd
from pathlib import Path
import re
# Read the data as a dataframe


# TODO: 
def checkRequiredCourses(requiredCourses, currentCourses):
    '''
    This method will take in a list of required courses and current courses and return the courses you still need
    '''
    li_dif = [i for i in requiredCourses + currentCourses if i not in requiredCourses or i not in currentCourses] 
    return li_dif 

#%%
def getCourseTimes(text):
    '''
    Looks for the start and end times of a course
    '''
    # Import the table
    cwd = Path.cwd()
    filePath = Path(cwd / 'courseData/2019_S1_offering.csv')
    courseTable = pd.read_csv(filePath)

    # Parse the text to get usefull information
    # timeRegexPat = "([a-zA-Z]+)\s(\d{2}):(\d{2})-(\d{2}):(\d{2})([A-Z]{2})"
    # instructorRegexPat = "(.*?)(?=\/)"
    # instructors = re.findall(instructorRegexPat, text)
    # times = re.findall(timeRegexPat, text)

    # while("" in instructors): 
    #     instructors.remove("")
    spaceDelimWords = text.split()
    filteredList = list(filter(lambda a: a != '/', spaceDelimWords))
    

    # not the prettiest way, but its fast
    
    # print(times)
    # print(instructors)

    # TODO: add 
    # start time column, 
    # end time column, 
    # instructors column, 
    # location column
    return filteredList

 
# TODO:
# Make a SQL database with these columns
# ID (auto id), 
# STUDENT_REVIEW_ID (LATER),
# COURSE_CODE (string), 
# SUBJECT_CODE (string), 
# START_TIME (datetime),
# END_TIME (datetime),
# DAY_SUN, 
# DAY_MON, 
# DAY_TUES, 
# DAY_WED, 
# DAY_THURS, 
# DAY_FRI, 
# DAY_SAT,
# LOCATION,
# COURSE_NAME, 
# COURSE_DESCRIPTION, 
# PREREQUISITES, 
# CREDITS, 
# INSTRUCTORS, 
# SECTION,
# RECOMMENDED_PRERQUISITES,
# EST_HOURS,
# LAB (BOOLEAN),
# DATE_ADDED
# %%
