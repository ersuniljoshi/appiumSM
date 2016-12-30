# Import question builder class
from library.question_types import QuestionBuilder
# Importing setlog file for logging purpose
from library.setlog import Logger

loggerObj = Logger()
logger = loggerObj.setLogger("logs")


# Testcase 1 : This testcase will sign-in and create survey with 4 questions
def test_createSurveyWithFiveQuestions(setUp, codexFile):
    driver = setUp
    QB = QuestionBuilder(driver, codexFile)
    logger.info("Executing Testcase 1...........")
    logger.info("Signing in..........")
    # User sign in
    assert QB.userSignIn()
    # create survey
    rv = QB.createSurvey("survey 1")
    if not rv:
        logger.info("survey creation failed")
        QB.tearDown()
        assert rv
    else:
        logger.info("Survey created")
    # Question 1 : Text type
    rv = QB.addTextTypeOfQuestion("A survey about Infobeans")
    if not rv:
        logger.info("Failed to add text type of question")
        QB.tearDown()
        assert rv
    else:
        logger.info("Added text type of question")
    # Question 2 : Comment box
    rv = QB.addCommentBoxTypeOfQuestion("Tell us about infobeans")
    if not rv:
        logger.info("Failed to add comment box type of question")
        QB.tearDown()
        assert rv
    else:
        logger.info("Added comment box type of question")
    # Question 3 : drop down
    rv = QB.addDropDownQuestionTypeOfQuestion("Are you a tester?")
    if not rv:
        logger.info("Failed to add drop down type of question")
        QB.tearDown()
        assert rv
    else:
        logger.info("Added drop down type of question")
    # Question 4 : Matrix / Rating
    rv = QB.addMatrixRatingTypeOfQuestion("Best feature of SM")
    if not rv:
        logger.info("Failed to add matrix rating type of question")
        QB.tearDown()
        assert rv
    else:
        logger.info("Added matrix rating type of question")
    # Verify survey in preview
    logger.info("Verifying survey is created......")
    rv = QB.previewAndTestSurvey()
    if not rv:
        logger.info("Unable preview and test survey")
    else:
        logger.info("Survey created with 4 questions")
        logger.info("Testcase 1 passed")
    QB.tearDown()
    assert rv


# Testcase 2 : This test will be failed forcefully
def test_defaultSurveynameTestcase(setUp, codexFile):
    driver = setUp
    QB = QuestionBuilder(driver, codexFile)
    logger.info("Executing Testcase 2.............")
    rv = QB.createSurvey()
    if not rv:
        logger.info("Testcase 2 failed")
        QB.tearDown()
        assert rv
    else:
        logger.info("Survey created")
        screen_shot(driver)
        QB.tearDown()


# Testcase 3 : This test will create a empty survey
def test_createBlankSurvey(setUp, codexFile):
    driver = setUp
    QB = QuestionBuilder(driver, codexFile)
    logger.info("Executing Testcase 3.............")
    rv = QB.createSurvey("survey 3")
    if not rv:
        logger.info("Testcase 3 failed")
        QB.tearDown()
        assert rv
    else:
        logger.info("Survey created")
        logger.info("Testcase 3 passed")
        QB.tearDown()


# Testcase 4 : This test will sign-out user login
def test_userSignOut(setUp, codexFile):
    driver = setUp
    QB = QuestionBuilder(driver, codexFile)
    logger.info("Executing Testcase 4.............")
    # waiting for create survey button
    assert QB.waitForCreateSurvey()
    # sign out
    logger.info("Signing out..........")
    rv = QB.signOutUserLogin()
    if not rv:
        logger.info("Testcase 4 failed")
    else:
        logger.info("successfully signout")
        logger.info("Testcase 4 passed")
    QB.tearDown()
    assert rv


# Method used to take screenshot
def screen_shot(driver):
    screenshot = driver.get_screenshot_as_base64()
    f = open('myfile1', 'w')
    f.write(screenshot)  # python will convert \n to os.linesep
    f.close()
