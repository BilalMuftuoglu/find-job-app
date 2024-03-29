import psycopg2

class Account:
    def __init__(self,accountId,username,password,userType):
        self.accountId = accountId
        self.userName = username
        self.password = password
        self.userType = userType

        if(self.userName == ""):
            self.userName = None
        if(self.password == ""):
            self.password = None
        if(self.userType == ""): 
            self.userType = None
        

class Employee:
    def __init__(self,employeeId,employeeName,employeeSurname,employeePhone,employeeAddress):
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.employeeSurname = employeeSurname
        self.employeePhone = employeePhone
        self.employeeAddress = employeeAddress
        
        if(employeeName == ""): 
            self.employeeName = None
        if(employeeSurname == ""):
            self.employeeSurname = None
        if(employeePhone == ""):
            self.employeePhone = None
        if(employeeAddress == ""):
            self.employeeAddress = None


class Employer:
    def __init__ (self,employerId,employerName,employerPhone,employerAdress):
        self.employerId = employerId
        self.employerName = employerName
        self.employerPhone = employerPhone
        self.employerAdress = employerAdress
        
        if(employerId == ""):
            self.employerId = None
        if(employerName == ""):
            self.employerName = None
        if(employerPhone == ""):
            self.employerPhone = None
        if(employerAdress == ""):
            self.employerAdress = None


class Education:
    def __init__(self,employeeId,schoolName,startDate,endDate,schoolType):
        self.employeeId = employeeId
        self.schoolName = schoolName
        self.startDate = startDate
        self.endDate = endDate
        self.schoolType = schoolType
        
        if(self.startDate == ""):
            self.startDate = None
        if(self.endDate == ""):
            self.endDate = None
        if(self.schoolName == ""):
            self.schoolName = None
        if(self.schoolType == ""):
            self.schoolType = None
    
class Experience:
    def __init__(self,employeeId,startDate,endDate,positionName,companyName):
        self.employeeId = employeeId
        self.startDate = startDate
        self.endDate = endDate
        self.positionName = positionName
        self.companyName = companyName
        
        if(self.startDate == ""):
            self.startDate = None
        if(self.endDate == ""):
            self.endDate = None
        if(self.positionName == ""):
            self.positionName = None
        if(self.companyName == ""):
            self.companyName = None
        
    def getExperience(self,employeeId):
        return self.employeeId
    
class Application:
    def __init__(self,employerId,applicationId,counter,applicationName,applicationDate,contractType,positionName,description,isActive):
        self.employerId = employerId
        self.applicationId = applicationId
        self.counter = counter
        self.applicationName = applicationName
        self.applicationDate = applicationDate
        self.contractType = contractType
        self.positionName = positionName
        self.description = description
        self.isActive = isActive
        if(self.counter == ""):
            self.counter = None
        if(self.applicationName == ""):
            self.applicationName = None
        if(self.applicationDate == ""):
            self.applicationDate = None
        if(self.contractType == ""):
            self.contractType = None
        if(self.positionName == ""):
            self.positionName = None
        if(self.description == ""):
            self.description = None
        if(self.isActive == ""):
            self.isActive = None
            
class AppliedApplications :
    def __init__(self,employeeId,applicationId,status,applicationDate,coverLetter) :
        self.employeeId = employeeId
        self.applicationId = applicationId
        self.status = status
        self.applicationDate = applicationDate
        self.coverLetter = coverLetter
        
        if(self.status == ""):
            self.status = None
        if(self.applicationDate == ""):
            self.applicationDate = None
        if(self.coverLetter == ""):
            self.coverLetter = None

class Filter:
    def __init__(self,dateFilter,applicationNameFilter,companyNameFilter,positionNameFilter,contractTypeFilter):
        self.applicationDate = dateFilter # 1 No Filter, Ascending, Descending
        self.applicationName = applicationNameFilter # None, name
        self.companyName = companyNameFilter # None, name
        self.positionName = positionNameFilter # None, name
        self.contractType = contractTypeFilter # No Filter, Full Time , Part Time, Intern
        
        if(self.applicationDate == "No Filter"):
            self.applicationDate = None
        if(self.applicationName == ""):
            self.applicationName = None
        if(self.companyName == ""):
            self.companyName = None
        if(self.positionName == ""):
            self.positionName = None
        if(self.contractType == "No Filter"):
            self.contractType = None


    


class ApplicationView :
    def __init__(self,employeeId,applicationId,companyName,counter,applicationName,applicationDate,contractType,positionName,description,status,coverLetter,appliedApplicationDate):
        self.employeeId = employeeId
        self.applicationId = applicationId
        self.companyName = companyName
        self.counter = counter
        self.applicationName = applicationName
        self.applicationDate = applicationDate
        self.contractType = contractType
        self.positionName = positionName
        self.description = description
        self.status = status
        self.coverLetter = coverLetter
        self.appliedApplicationDate = appliedApplicationDate

        if(self.description == ""):
            self.description = None
        
        if(self.coverLetter == ""):
            self.coverLetter = None

        
 
class ApplicantsView:
    def __init__(self,employeeId,applicationId,status,coverLetter,applicationDate,employeeName,employeeSurname,employeePhone,employeeAddress):
        self.employeeId = employeeId
        self.applicationId = applicationId
        self.status = status
        self.coverLetter = coverLetter
        self.applicationDate = applicationDate
        self.employeeName = employeeName
        self.employeeSurname = employeeSurname
        self.employeePhone = employeePhone
        self.employeeAddress = employeeAddress

        if(self.coverLetter == ""):
            self.coverLetter = None
        if(self.employeeName == ""):
            self.employeeName = None
        if(self.employeeSurname == ""):
            self.employeeSurname = None
        if(self.employeePhone == ""):
            self.employeePhone = None
        if(self.employeeAddress == ""):
            self.employeeAddress = None