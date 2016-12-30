from element_waits import Waits
from element_codexes import ElementCodex


class QuestionBuilder():
    def __init__(self, driver, codexFile):
        self.driver = driver
        self.WO = Waits(self.driver, codexFile+"_codexes.txt")
        self.ECO = ElementCodex(codexFile+"_codexes.txt")

    def createSurvey(self, question_title="Default_survey"):
        '''
        It will create survey with given title
        :param question_title:  survey title
        :return: returns True if survey created successfully
        '''
        rv = self.waitForElement("createSurvey")
        if not rv:
            return rv
        ele = self.getWebElement("createSurvey")
        if not self.click_element(ele):
            return False
        rv = self.waitForElement("createNewSurvey")
        if not rv:
            return rv
        ele = self.getWebElement("createNewSurvey")
        if not self.click_element(ele):
            return False
        ele = self.getWebElement("createSurveyTitle")
        if ele is not False:
            ele.clear()
            ele.send_keys(question_title)
        else:
            return ele
        ele = self.getWebElement("createSurveyAfterTitleEntered")
        if ele:
            self.click_element(ele)
            return True
        else:
            return False

    def click_element(self, ele):
        if ele:
            ele.click()
            return True
        else:
            return False

    def tearDown(self):
        '''
        Shutdown webdriver session
        :return: None
        '''
        self.driver.quit()

    def waitForElement(self, codex):
        '''
        Wait for element appearance
        :param codex: codex for eleement
        :return: return True if element found O.W. False
        '''
        rv = self.WO.waitUntilElementLocated(self.driver, codex)
        return rv

    def waitForCreateSurvey(self):
        '''
        Waiting for create survey button
        :return: returns true if element located O.W False
        '''
        rv = self.waitForElement("createSurvey")
        return rv

    def waitForQuestionContainer(self):
        '''
        Waiting for question container (i.e. for + button)
        :return: returns true if element located O.W False
        '''
        rv = self.waitForElement("questionTypesContainer(+)")
        return rv

    def getWebElement(self, codex):
        '''
        Used to return web element object
        :param codex: codex for web element
        :return: returns element O.W  False
        '''
        codex_details = self.ECO.get_codex(codex)
        ele = self.ECO.getElement(self.driver, codex_details)
        return ele

    def signOutUserLogin(self):
        '''
        signout for user
        :return: True if successfully signout O.W False
        '''
        ele = self.getWebElement("navigateUpTripleLineButton")
        if not self.click_element(ele):
            return False
        rv = self.waitForElement("wheelButtonForSignOut")
        if not rv:
            return rv
        ele = self.getWebElement("wheelButtonForSignOut")
        if not self.click_element(ele):
            return False
        rv = self.waitForElement("signOutButton")
        if not rv:
            return rv
        ele = self.getWebElement("signOutButton")
        if not self.click_element(ele):
            return False
        return True

    def userSignIn(self):
        '''
        user sign in
        :return: returns true if successfully sign in O.W False
        '''
        rv = self.waitForElement("signInButton")
        if not rv:
            return rv
        ele = self.getWebElement("signInButton")
        ele.click()
        ele = self.getWebElement("userNameEntry")
        ele.clear()
        ele.send_keys("InfoBeansP")
        ele = self.getWebElement("passwordEntry")
        ele.clear()
        ele.send_keys("InfoBeans!@#")
        ele = self.getWebElement("signInWithCredentials")
        if ele:
            return self.click_element(ele)
        else:
            return False

    def verifyQuestionContainerIsOpen(self):
        rv = self.waitForElement("selectTextQuestionType")
        return rv

    def openQuestionContainer(self,):
        rv = self.waitForQuestionContainer()
        if not rv:
            return rv
        ele = self.getWebElement("questionTypesContainer(+)")
        ele.click()
        rv = self.verifyQuestionContainerIsOpen()
        return rv

    def addTextTypeOfQuestion(self, question_title):
        rv = self.openQuestionContainer()
        if not rv:
            return rv
        ele = self.getWebElement("selectTextQuestionType")
        ele.click()
        ele = self.getWebElement("textQuestionTypeTitle")
        ele.send_keys(question_title)
        rv = self.saveAnyTypeOfQuestion()
        return True if rv else False

    def addCommentBoxTypeOfQuestion(self, question_title):
        rv = self.openQuestionContainer()
        if not rv:
            return rv
        ele = self.getWebElement("selectCommentBoxQuestionType")
        ele.click()
        ele = self.getWebElement("commentBoxQuestionTypeTitle")
        ele.send_keys(question_title)
        rv = self.saveAnyTypeOfQuestion()
        return True if rv else False

    def addDropDownQuestionTypeOfQuestion(self, question_title):
        rv = self.openQuestionContainer()
        if not rv:
            return rv
        ele = self.getWebElement("selectDropDownQuestionType")
        ele.click()
        rv = self.waitForElement("dropDownQuestionTypeTitle")
        if not rv:
            return rv
        ele = self.getWebElement("dropDownQuestionTypeTitle")
        ele.send_keys(question_title)
        self.hideKeyboard()
        ele = self.getWebElement("dropDownAnswerChoices1")
        ele.send_keys("Yes")
        self.hideKeyboard()
        rv = self.waitForElement("dropDownAnswerChoices2")
        if not rv:
            return rv
        ele = self.getWebElement("dropDownAnswerChoices2")
        ele.send_keys("No")
        self.hideKeyboard()
        rv = self.saveAnyTypeOfQuestion()
        return True if rv else False

    def addMatrixRatingTypeOfQuestion(self, question_title):
        rv = self.openQuestionContainer()
        if not rv:
            return rv
        ele = self.getWebElement("selectMatrixRatingQuestionType")
        ele.click()
        rv = self.waitForElement("matrixRatingQuestionTypeTitle")
        if not rv:
            return rv
        ele = self.getWebElement("matrixRatingQuestionTypeTitle")
        ele.send_keys(question_title)
        ele = self.getWebElement("matrixRatingQuestionTypeRows")
        ele.click()
        rv = self.waitForElement("enterMatrixRatingRowLable1")
        if not rv:
            return rv
        ele = self.getWebElement("enterMatrixRatingRowLable1")
        ele.clear()
        ele.send_keys("Interface")
        rv = self.waitForElement("enterMatrixRatingRowLabel2")
        if not rv:
            return rv
        ele = self.getWebElement("enterMatrixRatingRowLabel2")
        ele.clear()
        ele.send_keys("Survey design")
        rv = self.saveAnyTypeOfQuestion()
        if not rv:
            return rv
        rv = self.saveAnyTypeOfQuestion()
        return True if rv else False

    def hideKeyboard(self):
        self.driver.hide_keyboard()

    def saveAnyTypeOfQuestion(self):
        ele = self.getWebElement("saveQuestion")
        if not ele:
            return False
        else:
            ele.click()
            return True

    def previewAndTestSurvey(self):
        rv = self.waitForElement("tripleDotButtonForPreviewAndTest")
        if not rv:
            return rv
        ele = self.getWebElement("tripleDotButtonForPreviewAndTest")
        ele.click()
        ele = self.getWebElement("selectPreviewAndTestButton")
        ele.click()
        return True
