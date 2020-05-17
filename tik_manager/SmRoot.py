#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------
# Copyright (c) 2017-2018, Arda Kutlu (ardakutlu@gmail.com)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  - Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
#  - Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
#  - Neither the name of the software nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# -----------------------------------------------------------------------------

import getpass
import platform
import datetime
import os
import logging
# import pprint
import hashlib

import shutil
from glob import glob
import json
import filecmp
import re
# import ctypes
import socket

import urllib

import _version

__author__ = "Arda Kutlu"
__copyright__ = "Copyright 2018, Tik Manager Root Functions"
__credits__ = []
__license__ = "GPL"
__maintainer__ = "Arda Kutlu"
__email__ = "ardakutlu@gmail.com"
__status__ = "Development"

logging.basicConfig()
logger = logging.getLogger('smRoot')
logger.setLevel(logging.WARNING)


class RootManager(object):
    """Base of all Scene Manager Command Classes"""
    def __init__(self):
        # super(RootManager, self).__init__()

        # self.database = db.SmDatabase()
        # self.validCategories = ["Model", "Shading", "Rig", "Layout", "Animation", "Render", "Other"]

        self.currentPlatform = platform.system()
        self._pathsDict={}
        self.fpsList=["15", "24", "25", "30", "48", "50", "60"]
        # self.padding = 3

        self.errorCodeDict = {200: "Corrupted File",
                         201: "Missing File",
                         202: "Read/Write Error",
                         203: "Delete Error",
                         210: "OS Not Supported",
                         101: "Out of range",
                         102: "Missing Override",
                         340: "Naming Error",
                         341: "Mandatory fields are not filled",
                         360: "Action not permitted"}

    def init_paths(self):
        """Initializes all the necessary paths"""
        logger.debug("Func: init_paths")
        # all paths in here must be absolute paths
        _softwarePathsDict = self.getSoftwarePaths()

        self._pathsDict["userSettingsDir"] = os.path.normpath(os.path.join(self.getUserDirectory(), _softwarePathsDict["userSettingsDir"]))
        self._folderCheck(self._pathsDict["userSettingsDir"])

        self._pathsDict["bookmarksFile"] = os.path.normpath(os.path.join(self._pathsDict["userSettingsDir"], "smBookmarks.json"))
        self._pathsDict["currentsFile"] = os.path.normpath(os.path.join(self._pathsDict["userSettingsDir"], "smCurrents.json"))
        self._pathsDict["projectsFile"] = os.path.normpath(os.path.join(self._pathsDict["userSettingsDir"], "smProjects.json"))

        self._pathsDict["projectDir"] = self.getProjectDir()
        self._pathsDict["sceneFile"] = ""
        # _softwarePathsDict = self.getSoftwarePaths()
        if self._pathsDict["projectDir"] == -1 or self._pathsDict["sceneFile"] == -1 or _softwarePathsDict == -1:
            msg = "The following functions must be overridden in inherited class:\n'getSoftware'\n'getProjectDir'\n'getSceneFile'"
            logger.error(msg)
            raise Exception([102, msg])

        self._pathsDict["masterDir"] = os.path.normpath(os.path.join(self._pathsDict["projectDir"], "smDatabase"))
        self._folderCheck(self._pathsDict["masterDir"])


        self._pathsDict["databaseDir"] = os.path.normpath(os.path.join(self._pathsDict["masterDir"], _softwarePathsDict["databaseDir"]))
        self._folderCheck(self._pathsDict["databaseDir"])

        self._pathsDict["scenesDir"] = os.path.normpath(os.path.join(self._pathsDict["projectDir"], _softwarePathsDict["scenesDir"]))
        self._folderCheck(self._pathsDict["scenesDir"])

        self._pathsDict["projectSettingsFile"] = os.path.normpath(os.path.join(self._pathsDict["masterDir"], "projectSettings.json"))
        # self._pathsDict["subprojectsFile"] = os.path.normpath(os.path.join(self._pathsDict["databaseDir"], "subPdata.json"))
        self._pathsDict["subprojectsFile"] = os.path.normpath(os.path.join(self._pathsDict["masterDir"], "subPdata.json"))
        self._pathsDict["categoriesFile"] = os.path.normpath(os.path.join(self._pathsDict["databaseDir"], _softwarePathsDict["categoriesFile"]))

        parts = os.path.splitext(_softwarePathsDict["categoriesFile"])
        categoriesNickNameFileName = _softwarePathsDict.get(
            "categoriesNickNameFile",
            "%sNickName%s" % (parts[0], parts[1]))
        self._pathsDict["categoriesNickNameFile"] = os.path.normpath(os.path.join(self._pathsDict["databaseDir"], categoriesNickNameFileName))

        self._pathsDict["previewsDir"] = os.path.normpath(os.path.join(self._pathsDict["projectDir"], "Playblasts", _softwarePathsDict["niceName"])) # dont change
        self._folderCheck(self._pathsDict["previewsDir"])

        self._pathsDict["pbSettingsFile"] = os.path.normpath(os.path.join(self._pathsDict["previewsDir"], _softwarePathsDict["pbSettingsFile"]))

        self._pathsDict["generalSettingsDir"] = os.path.dirname(os.path.abspath(__file__))

        self._pathsDict["usersFile"] = os.path.normpath(os.path.join(self._pathsDict["generalSettingsDir"], "sceneManagerUsers.json"))

        self._pathsDict["softwareDatabase"] = os.path.normpath(os.path.join(self._pathsDict["generalSettingsDir"], "softwareDatabase.json"))
        self._pathsDict["sceneManagerDefaults"] = os.path.normpath(os.path.join(self._pathsDict["generalSettingsDir"], "sceneManagerDefaults.json"))
        self._pathsDict["projectDirectoryDatabase"] = os.path.normpath(os.path.join(self._pathsDict["generalSettingsDir"], "projectDirectoryDatabase.json"))

    def getSoftwarePaths(self):
        """This method must be overridden to return the software currently working on"""
        # This function should return a dictionary which includes string values for:
        # databaseDir, scenesDir, pbSettingsFile keys. Software specific paths will be resolved with these strings
        logger.debug("Func: getSoftwarePaths")
        return -1

    def getProjectDir(self):
        """This method must be overridden to return the project directory of running software"""
        logger.debug("Func: getProjectDir")
        return -1

    def getSceneFile(self):
        """This method must be overridden to return the full scene path ('' for unsaved) of current scene"""
        logger.debug("Func: getSceneFile")
        return -1

    def init_database(self):
        """Initializes all databases"""
        logger.debug("Func: init_database")

        # defaults dictionary holding "defaultCategories", "defaultPreviewSettings", "defaultUsers"
        self._sceneManagerDefaults = self._loadJson(self._pathsDict["sceneManagerDefaults"])
        self._projectDirectoryDefaultInfo = {}
        if os.path.isfile(self._pathsDict["projectDirectoryDatabase"]):
            self._projectDirectoryDefaultInfo = self._loadJson(
                self._pathsDict["projectDirectoryDatabase"])

        # self.currentPlatform = platform.system()
        self._categories = self._loadCategories()
        self._usersDict = self._loadUsers()
        self._currentsDict = self._loadUserPrefs()
        self._subProjectsList = self._loadSubprojects()

        # unsaved DB
        self._baseScenesInCategory = []
        self._currentBaseSceneName = ""
        self._currentSceneInfo = {}
        self._currentVersionDetailInfo = {}

        #Scene Specific
        self._currentVersionIndex = -1
        self._currentSubVersionIndex = -1
        self._currentPreviewsDict = {}
        self._currentPreviewCamera = ""
        self._currentNotes = ""
        self._currentThumbFile = ""

        self._openSceneInfo = ""

        self.scanBaseScenes()

    def _setCurrents(self, att, newdata):
        """Sets the database stored cursor positions and saves them to the database file"""
        logger.debug("Func: _setCurrents")

        self._currentsDict[att] = newdata
        self._saveUserPrefs(self._currentsDict)

    @property
    def projectDir(self):
        """Returns Current Project Directory"""
        logger.debug("Func: projectDir/getter")
        return self._pathsDict["projectDir"]

    @projectDir.setter
    def projectDir(self, path):
        """Sets the Scene Manager Project directory to given path"""
        logger.debug("Func: projectDir/setter")
        self._pathsDict["projectDir"] = path
        # self.init_paths()
        # self.init_database()

    @property
    def subProject(self):
        """Returns the name of the active sub-project"""
        logger.debug("Func: subProject/getter")
        return self._subProjectsList[self.currentSubIndex]

    # @property
    # def baseScene(self):
    #     """Returns the name of the Base Scene at cursor position"""
    #     baseSceneDir = os.path.abspath(os.path.join(self._pathsDict["sceneFile"], os.pardir))
    #     return os.path.basename(baseSceneDir)

    @property
    def currentTabIndex(self):
        """Returns the Category index at cursor position"""
        logger.debug("Func: currentTabIndex/getter")
        return self._currentsDict["currentTabIndex"]

    @currentTabIndex.setter
    def currentTabIndex(self, indexData):
        """Moves the cursor to the given category index"""
        logger.debug("Func: currentTabIndex/setter")
        if not 0 <= indexData < len(self._categories):
            msg="Tab index is out of range!"
            # logger.error(msg)
            # raise Exception([101, msg])
            self._exception(101, msg)
            return
        if indexData == self.currentTabIndex:
            self.cursorInfo()
            return
        self._setCurrents("currentTabIndex", indexData)
        self.scanBaseScenes()
        self.currentBaseSceneName = ""
        self._currentVersionIndex = -1
        self._currentSubVersionIndex = -1
        self._currentPreviewCamera = ""
        self.cursorInfo()

    @property
    def currentSubIndex(self):
        """Returns the sub-project index at cursor position"""
        logger.debug("Func: currentSubIndex/getter")
        return self._currentsDict["currentSubIndex"]

    @currentSubIndex.setter
    def currentSubIndex(self, indexData):
        """Moves the cursor to the given sub-project index"""
        logger.debug("Func: currentSubIndex/setter")
        if not 0 <= indexData < len(self._subProjectsList):
            msg="Sub Project index is out of range!"
            # raise Exception([101, msg])
            self._exception(101, msg)
            return


        if indexData == self.currentSubIndex:
            self.cursorInfo()
            return

        self._setCurrents("currentSubIndex", indexData)
        self.scanBaseScenes()
        # de-select previous base scene
        self._currentBaseSceneName = ""
        self._currentVersionIndex = -1
        self._currentSubVersionIndex = -1
        self._currentPreviewCamera = ""
        self.cursorInfo()

    @property
    def currentUser(self):
        """Returns the current user"""
        return getpass.getuser()

    @currentUser.setter
    def currentUser(self, name):
        """Sets the current user"""
        logger.debug("Func: currentUser/setter")
        self._setCurrents("currentUser", name)

    @property
    def currentMode(self):
        """Returns the current access mode (Load or Reference)"""
        logger.debug("Func: currentMode/getter")

        return self._currentsDict["currentMode"]

    @currentMode.setter
    def currentMode(self, state):
        """Sets the current access mode 0 == Load, 1 == Reference"""
        logger.debug("Func: currentMode/setter")

        if not type(state) is bool:
            if bool is 0:
                state = False
            elif bool is 1:
                state = True
            else:
                msg = ("only boolean or 0-1 accepted, entered %s" %state)
                logger.error(msg)
                # raise Exception([101, msg])
                self._exception(101, msg)
                return
        self._setCurrents("currentMode", state)

    @property
    def currentBaseSceneName(self):
        """Returns current Base Scene Name at cursor position"""
        logger.debug("Func: currentBaseSceneName/getter")

        return self._currentBaseSceneName

    @currentBaseSceneName.setter
    def currentBaseSceneName(self, sceneName):
        """Moves the cursor to the given base scene name"""
        logger.debug("Func: currentBaseSceneName/setter")
        if not sceneName:
            self._currentBaseSceneName = ""
            self.currentVersionIndex = -1
            self.currentSubVersionIndex = -1
            return
        if sceneName not in self._baseScenesInCategory.keys():

            self.currentVersionIndex = -1
            self.currentSubVersionIndex = -1
            # msg = "There is no scene called %s in current category" %sceneName

            # self._exception(101, msg)
            return

        self._currentBaseSceneName = sceneName
        self._currentSceneInfo = self._loadSceneInfo()

        # assert (self._currentSceneInfo == -2)
        if self._currentSceneInfo == -2: # corrupted db file
            # self._currentSceneInfo == {}
            self._currentBaseSceneName = ""
            self.currentVersionIndex = -1
            self.currentSubVersionIndex = -1
            self._currentVersionDetailInfo = {}
            msg = "Database file %s is corrupted"
            # raise Exception ([200, "Database file %s is corrupted\nDo you want to fix it manually?" %sceneName, self._baseScenesInCategory[sceneName]] )
            self._exception(200, msg)
            return

        self._currentVersionDetailInfo = self.getVersionDetailInfo()

        if self._currentSceneInfo["ReferencedVersion"]:
            self.currentVersionIndex = self._currentSceneInfo["ReferencedVersion"]
            self.currentSubVersionIndex = self._currentSceneInfo.get("ReferencedSubVersion", 1)
        else:
            self.currentVersionIndex = len(self._currentVersionDetailInfo)
            vIds = self._currentVersionDetailInfo.keys()
            vIds.sort()
            self.currentSubVersionIndex = len(self._currentVersionDetailInfo[vIds[-1]])

        self.cursorInfo()
        # self._currentPreviewIndex = 0

    @property
    def currentBaseScenePath(self):
        """Returns absolute path of Base Scene at cursor position"""
        logger.debug("Func: currentBaseScenePath/getter")

        return os.path.join(self.projectDir, self._currentSceneInfo["Path"])

    @property
    def currentScenePath(self):
        """Returns absolute path of Base Scene Version at cursor position"""
        logger.debug("Func: currentBaseScenePath/getter")

        idx = self.getRealVersionIndex()
        return os.path.join(self.projectDir, self._currentSceneInfo["Versions"][idx]["RelativePath"])

    @property
    def currentPreviewPath(self):
        """Returns absolute path of preview folder of the Base scene at cursor position"""
        logger.debug("Func: currentPreviewPath/getter")
        if self._currentSceneInfo["SubProject"] is not "None":
            path = os.path.join(self._pathsDict["previewsDir"], self._currentSceneInfo["Category"],
                                self._currentSceneInfo["Name"])
        else:
            path = os.path.join(self._pathsDict["previewsDir"], self._currentSceneInfo["Category"],
                                self._currentSceneInfo["SubProject"], self._currentSceneInfo["Name"])
        return path
        # if os.path.isdir(path):
        #     return path
        # else:
        #     return ""

    @property
    def currentVersionIndex(self):
        """Returns the index number of Version at cursor position"""
        logger.debug("Func: currentVersionIndex/getter")

        """Returns current Version index at cursor position"""
        return self._currentVersionIndex

    @currentVersionIndex.setter
    def currentVersionIndex(self, indexData):
        """Moves the cursor to given Version index"""
        logger.debug("Func: currentVersionIndex/setter")

        if indexData <= 0:
            self._currentVersionIndex = -1
            self._currentSubVersionIndex = -1
            self._currentThumbFile = ""
            self._currentNotes = ""
            self._currentPreviewCamera = ""
            return
        if not self._currentSceneInfo:
            # logger.warning(("BaseScene not Selected"))
            return

        versions = self._currentVersionDetailInfo.keys()
        if not 1 <= indexData <= len(versions):
            msg = "out of version range! %s" % indexData
            # logger.error(msg)
            # raise Exception([101, msg])
            self._exception(101, msg)
            return
        # if self._currentVersionIndex == indexData:
        #     logger.warning("Cursor is already at %s" % indexData)
        #     return
        self._currentVersionIndex = indexData
        subVersionInfo = self._currentVersionDetailInfo[self._currentVersionIndex]
        subVerIds = sorted(subVersionInfo, key=lambda x: subVersionInfo[x])
        self.currentSubVersionIndex = subVerIds[-1]
        self.cursorInfo()

    @property
    def currentSubVersionIndex(self):
        return self._currentSubVersionIndex

    @currentSubVersionIndex.setter
    def currentSubVersionIndex(self, indexData):
        """Moves the cursor to given Version index"""
        logger.debug("Func: currentVersionIndex/setter")

        if indexData <= 0:
            self._currentSubVersionIndex = -1
            return
        if not self._currentSceneInfo:
            return
        if self.currentVersionIndex == -1:
            self._currentSubVersionIndex = -1
            return
        
        subVersions = self._currentVersionDetailInfo[self.currentVersionIndex]
        if not 1 <= indexData <= len(subVersions):
            msg = "out of subversion range! %s" % indexData
            # logger.error(msg)
            # raise Exception([101, msg])
            self._exception(101, msg)
            return

        self._currentSubVersionIndex = indexData
        idx = self.getRealVersionIndex()
        self._currentNotes = self._currentSceneInfo["Versions"][idx]["Note"]
        self._currentPreviewsDict = self._currentSceneInfo["Versions"][idx]["Preview"]
        # print self._currentPreviewsDict
        if not self._currentPreviewsDict.keys():
            self._currentPreviewCamera = ""
        else:
            self._currentPreviewCamera = sorted(self._currentPreviewsDict.keys())[0]

        self._currentThumbFile = self._currentSceneInfo["Versions"][idx]["Thumb"]
        self.cursorInfo()

    # @property
    # def currentPreviewCamera(self):
    #     """Returns current Previewed Camera name at cursor position"""
    #     logger.debug("Func: currentPreviewCamera/getter")
    #
    #     return self._currentPreviewCamera
    #
    # @currentPreviewCamera.setter
    # def currentPreviewCamera(self, cameraName):
    #     """Moves the cursor to the given Preview Camera Name"""
    #     logger.debug("Func: currentPreviewCamera/setter")
    #
    #     if not self._currentSceneInfo:
    #         logger.warning(("BaseScene not Selected"))
    #         return
    #     if cameraName not in self._currentPreviewsDict.keys():
    #         logger.error(("There is no preview for that camera"))
    #         return
    #     self._currentPreviewCamera = cameraName
    #     self.cursorInfo()

    # @property
    # def baseScenesInCategory(self):
    #     return sorted(self._baseScenesInCategory.keys())

    @property
    def currentDatabasePath(self):
        """Returns absolute path of database file of the scene at cursor position"""
        logger.debug("Func: currentDatabasePath/getter")

        if not self._currentSceneInfo:
            msg = "no current info"
            # logger.error(msg)
            # raise Exception([101, msg])
            self._exception(101, msg)
            return

        if self._currentSceneInfo["SubProject"] == "None":
            subP = ""
        else:
            subP = self._currentSceneInfo["SubProject"]

        dbFile = os.path.join (self.projectDir,
                      self._pathsDict["databaseDir"],
                      self._currentSceneInfo["Category"],
                      subP, "%s.json" %self._currentSceneInfo["Name"])
        return dbFile

    def cursorInfo(self):
        """function to return cursor position info for debugging purposes"""

        logger.info("""
        Category: {0}
        SubProject: {1}
        BaseScenes Under: {2}
        Current BaseScene: {3}
        Version: {4}
        SubVersion: {5}
        Preview: {6}
        Thumbnail: {7}
        """.format(
            self._categories[self.currentTabIndex],
            self._subProjectsList[self.currentSubIndex],
            sorted(self._baseScenesInCategory.keys()),
            self._currentBaseSceneName,
            self._currentVersionIndex,
            self._currentSubVersionIndex,
            self._currentPreviewCamera,
            self._currentThumbFile))

    def getUserDirectory(self):
        """Returns Documents Directory"""
        dir = os.path.expanduser('~')
        if not "Documents" in dir:
            dir = os.path.join(dir, "Documents")

        return os.path.normpath(dir)

    def getOpenSceneInfo(self):
        """
        Collects the necessary scene info by resolving the scene name and current project
        Returns: Dictionary{jsonFile, projectPath, subProject, category, shotName} or None
        """
        logger.debug("Func: getOpenSceneInfo")

        self._pathsDict["sceneFile"] = self.getSceneFile()
        if not self._pathsDict["sceneFile"]:
            return None

        dbDir = self._pathsDict["databaseDir"]
        if not self._pathsDict['sceneFile'].startswith(self.projectDir):
            return None
        
        resPart = os.path.relpath(self._pathsDict["sceneFile"], start=self.projectDir)
        rResPart = resPart.split(os.path.sep, 1)[1]
        jsonPart = '%s.json' % os.path.dirname(rResPart)
        jsonFile = os.path.normpath(os.path.join(dbDir, jsonPart))

        if os.path.isfile(jsonFile):
            jsonInfo = self._loadJson(jsonFile)

            category = jsonInfo['Category']
            baseName = jsonInfo['Name']
            subProject = jsonInfo['SubProject']
            pbPath = self.getPreviewFolder(category, baseName, subProject)
            sceneFormat = os.path.splitext(self._pathsDict["sceneFile"])[1][1:]
            self._openSceneInfo = {
                "jsonFile": jsonFile,
                "projectPath": self._pathsDict["projectDir"],
                "subProject": jsonInfo['SubProject'],
                "category": jsonInfo['Category'],
                "shotName": jsonInfo['Name'],
                "sceneFormat": sceneFormat,
                "previewPath": pbPath
            }
            return self._openSceneInfo
        else:
            return None

    def getCategories(self):
        """Returns All Valid Categories"""
        logger.debug("Func: getCategories")

        return self._categories

    def getSubProjects(self):
        """Returns list of sub-projects"""
        logger.debug("Func: getSubProjects")

        return self._subProjectsList

    def getUsers(self):
        """Returns nice names of all users"""
        logger.debug("Func: getUsers")

        return sorted(self._usersDict.keys())

    def getBaseScenesInCategory(self):
        """Returns list of nice base scene names under the category at cursor position"""
        logger.debug("Func: getBaseScenesInCategory")

        self.scanBaseScenes()
        # return sorted(self._baseScenesInCategory.keys())
        return self._baseScenesInCategory

    def getVersions(self):
        """Returns Versions List of base scene at cursor position"""
        logger.debug("Func: getVersions")

        try:
            return self._currentSceneInfo["Versions"]
        except:
            return []

    def getNotes(self):
        """returns (String) version notes on cursor position"""
        logger.debug("Func: getNotes")

        return self._currentNotes

    def getPreviews(self):
        """returns (list) nice preview names of version on cursor position"""
        logger.debug("Func: getPreviews")
        
        # return "ASDFASDF"
        return sorted(self._currentPreviewsDict.keys())

    def getThumbnail(self):
        """returns (String) absolute thumbnail path of version on cursor position"""
        logger.debug("Func: getThumbnail")

        return os.path.join(self.projectDir, self._currentThumbFile)

    def getFPS(self):
        """returns the project FPS setting"""
        # load it each time, since this setting is not limited to a single user
        projectSettingsDB = self.loadProjectSettings()
        try:
            fpsValue = projectSettingsDB["FPS"]
            return fpsValue
        except KeyError:
            msg = "Database Error while reading projectSettings.json"
            logger.error(msg)
            return None

    def getResolution(self):
        """returns the project Resolution setting as a list"""
        # load it each time, since this setting is not limited to a single user
        projectSettingsDB = self.loadProjectSettings()
        try:
            resolution = projectSettingsDB["Resolution"]
            return resolution
        except KeyError:
            msg = "Database Error while reading projectSettings.json"
            logger.error(msg)
            return None

    def getSceneInfoAsText(self):
        name = self._currentSceneInfo["Name"]
        pass

    # def getFavorites(self):
    #     """returns List of favorite projects"""
    #     self._bookmarksList = self.loadFavorites(self.bookmarksFile)  # not immediate
    #     return self._bookmarksList

    def createNewProject(self, projectRoot, projectName, settingsData=None):
        """
        Creates New Project Structure
        :param projectRoot: (String) Path to where all projects are
        :param projectName: (String) Name of the project
        :return: None
        """
        logger.debug("Func: createNewProject")

        # resolve the project path
        resolvedPath = self.resolveProjectPath(projectRoot, projectName)

        projectType = settingsData.get('ProjectType', 'default')

        # check if there is a duplicate
        if not os.path.isdir(os.path.normpath(resolvedPath)):
            os.makedirs(os.path.normpath(resolvedPath))
        else:
            msg = "Project already exists"
            # logger.warning(msg)
            # raise Exception ([340, msg])
            self._exception(340, msg)
            return

        self.createProjectDirectory(resolvedPath, projectType)
        # Create project settings file
        if not settingsData:
            settingsData = {"Resolution": [1920, 1080],
                            "FPS": 25}

        self._dumpJson(settingsData, os.path.join(resolvedPath, "smDatabase", "projectSettings.json"))

        self.createProjectWorkspaceFile(resolvedPath, projectType)

        return resolvedPath

    def createSubproject(self, nameOfSubProject):
        """Creates a Scene Manager Sub-project"""
        logger.debug("Func: createSubproject")

        if nameOfSubProject in self._subProjectsList:
            msg = "%s is already in sub-projects list" % nameOfSubProject
            # logger.warning(msg)
            # raise Exception([340, msg])
            self._exception(340, msg)
            return

        self._subProjectsList.append(nameOfSubProject)
        self._saveSubprojects(self._subProjectsList)
        self.currentSubIndex = len(self._subProjectsList)-1
        return self._subProjectsList


    def showInExplorer(self, path):
        """Opens the path in Windows Explorer(Windows) or Nautilus(Linux)"""
        logger.debug("Func: showInExplorer")

        if self.currentPlatform == "Windows":
            os.startfile(path)
        elif self.currentPlatform == "Linux":
            os.system('nautilus %s' % path)
        else:
            os.system('open %s' % path) 

    def scanBaseScenes(self, categoryAs=None, subProjectAs=None):
        """Returns the basescene database files in current category"""
        logger.debug("Func: scanBaseScenes")

        if self.currentSubIndex >= len(self._subProjectsList):
            self.currentSubIndex = 0

        if categoryAs:
            category = categoryAs
        else:
            try:
                category = self._categories[self.currentTabIndex]
            except IndexError:
                self.currentTabIndex = 0
                category = self._categories[self.currentTabIndex]

        if subProjectAs:
            if type(subProjectAs) == int: # it index number of projects list is given, get the name from t
                subProject = self._subProjectsList[subProjectAs]
            else:
                subProject = subProjectAs
        else:
            subProject = self._subProjectsList[self.currentSubIndex]

        categoryDBpath = os.path.normpath(os.path.join(self._pathsDict["databaseDir"], category))
        self._folderCheck(categoryDBpath)
        if not (self.currentSubIndex == 0):
            try:
                categorySubDBpath = os.path.normpath(os.path.join(categoryDBpath, subProject)) # category name
            except IndexError:
                self.currentSubIndex = 0
                categorySubDBpath = os.path.normpath(os.path.join(categoryDBpath, subProject)) # category name
            self._folderCheck(categorySubDBpath)

            searchDir = categorySubDBpath
        else:
            searchDir = categoryDBpath

        self._baseScenesInCategory = {self.niceName(file):file for file in glob(os.path.join(searchDir, '*.json'))}
        # self._baseScenesInCategory = {self.niceName(file): self.filterReferenced(file) for file in glob(os.path.join(searchDir, '*.json'))}
        # self._currentBaseScenes = [os.path.join(searchDir, file) for file in os.listdir(searchDir) if file.endswith('.json')]
        return self._baseScenesInCategory # dictionary of json files

    def getProjectReport(self):

        # TODO // NEEDS to be working on

        # Hard Coded Software List - get path
        hardCodedSwPath = os.path.normpath(os.path.join(self._pathsDict["generalSettingsDir"], "softwareDatabase.json"))
        softwareDictionary = self._loadJson(hardCodedSwPath)
        # softwareDBList=["mayaDB", "maxDB", "houdiniDB", "nukeDB"]

        def getOldestFile(listOfFiles):
            return min(listOfFiles, key=lambda fn: os.stat(fn).st_mtime)

        def getNewestFile(listOfFiles):
            return max(listOfFiles, key=lambda fn: os.stat(fn).st_mtime)

        def uniqueList(seq, idfun=None):
            # order preserving
            if idfun is None:
                def idfun(x): return x
            seen = {}
            result = []
            for item in seq:
                marker = idfun(item)
                # in old Python versions:
                # if seen.has_key(marker)
                # but in new ones:
                if marker in seen: continue
                seen[marker] = 1
                result.append(item)
            return result


        now = datetime.datetime.now()
        formattedDate = now.strftime("%Y.%m.%d.%H.%M")
        filename = "summary_{0}.txt".format(formattedDate)

        # search entire database folder

        allDBfiles = []
        for sw in softwareDictionary.keys():
            dbDirName = softwareDictionary[sw]["databaseDir"]
            dbPath = os.path.join(self._pathsDict["masterDir"], dbDirName)
            if os.path.isdir(dbPath):

                swCategories = os.listdir(dbPath)
                for category in swCategories:
                    # get all json files in it recursively
                    for root, dirs, files in os.walk(os.path.join(dbPath, category)):
                        for file in files:
                            if file.endswith(".json"):
                                allDBfiles.append(os.path.join(root, file))
                                print(os.path.join(root, file))


        usersList = []
        usedSoftwares = []
        for sceneFile in allDBfiles:
            sceneInfo = self._loadJson(sceneFile)
            for v in sceneInfo["Versions"]:
                # print v
                usersList.append(v["User"])

        print uniqueList(usersList)



        oldestFile = getOldestFile(allDBfiles)
        pathOldestFile, nameOldestFile = os.path.split(oldestFile)
        oldestTimeMod = datetime.datetime.fromtimestamp(os.path.getmtime(oldestFile))
        newestFile = getNewestFile(allDBfiles)
        pathNewestFile, nameNewestFile = os.path.split(oldestFile)
        newestTimeMod = datetime.datetime.fromtimestamp(os.path.getmtime(newestFile))

        # print ", ".join(usedSofwares)
        formattedUsedSoftwares = ", ".join(usedSofwares)

        ReportText = """
Scene Manager Report - by {0} on {1}
---------------
Participants:{2}
Softwares Used:{3}
Oldest Scene File:{4}
Most Recent Scene File:{5}
Elapsed Time:{6}
        """.format(self.currentUser, formattedDate, "2", formattedUsedSoftwares, oldestFile, newestFile, "6")
        print ReportText
        pass
    # def getProjectReport(self):
    #     # TODO This function should be re-written considering all possible softwares
    #     # TODO instead of clunking scanBaseScenes with extra arguments, do the scanning inside this function
    #     def getOldestFile(rootfolder, extension=".avi"):
    #         return min(
    #             (os.path.join(dirname, filename)
    #              for dirname, dirnames, filenames in os.walk(rootfolder)
    #              for filename in filenames
    #              if filename.endswith(extension)),
    #             key=lambda fn: os.stat(fn).st_mtime)
    #
    #     def getNewestFile(rootfolder, extension=".avi"):
    #         return max(
    #             (os.path.join(dirname, filename)
    #              for dirname, dirnames, filenames in os.walk(rootfolder)
    #              for filename in filenames
    #              if filename.endswith(extension)),
    #             key=lambda fn: os.stat(fn).st_mtime)
    #
    #     oldestFile = getOldestFile(self.scenesDir, extension=(".mb", ".ma"))
    #     pathOldestFile, nameOldestFile = os.path.split(oldestFile)
    #     oldestTimeMod = datetime.datetime.fromtimestamp(os.path.getmtime(oldestFile))
    #     newestFile = getNewestFile(self.scenesDir, extension=(".mb", ".ma"))
    #     pathNewestFile, nameNewestFile = os.path.split(oldestFile)
    #     newestTimeMod = datetime.datetime.fromtimestamp(os.path.getmtime(newestFile))
    #
    #     L1 = "Oldest Scene file: {0} - {1}".format(nameOldestFile, oldestTimeMod)
    #     L2 = "Newest Scene file: {0} - {1}".format(nameNewestFile, newestTimeMod)
    #     L3 = "Elapsed Time: {0}".format(str(newestTimeMod - oldestTimeMod))
    #     L4 = "Scene Counts:"
    #
    #     report = {}
    #     for subP in range(len(self._subProjectsList)):
    #         subReport = {}
    #         for category in self._categories:
    #             categoryItems = (self.scanBaseScenes(categoryAs=category, subProjectAs=subP))
    #             categoryItems = [x for x in categoryItems if x != []]
    #
    #             L4 = "{0}\n{1}: {2}".format(L4, category, len(categoryItems))
    #             subReport[category] = categoryItems
    #         report[self._subProjectsList[subP]] = subReport
    #
    #     report = pprint.pformat(report)
    #     now = datetime.datetime.now()
    #     filename = "summary_{0}.txt".format(now.strftime("%Y.%m.%d.%H.%M"))
    #     filePath = os.path.join(self.projectDir, filename)
    #     file = open(filePath, "w")
    #     file.write("{0}\n".format(L1))
    #     file.write("{0}\n".format(L2))
    #     file.write("{0}\n".format(L3))
    #     file.write("{0}\n".format(L4))
    #     file.write((report))
    #
    #     file.close()
    #     logger.info("Report has been logged => %s" %filePath)
    #     return report

    def addNote(self, note):
        """Adds a note to the version at current position"""
        logger.debug("Func: addNote")

        if not self._currentBaseSceneName:
            logger.warning("No Base Scene file selected")
            return
        if self._currentVersionIndex == -1 or self._currentSubVersionIndex == -1:
            logger.warning("No Version selected")
            return
        now = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M")
        self._currentNotes = "%s\n[%s] on %s\n%s\n" % (self._currentNotes, self.currentUser, now, note)
        idx = self.getRealVersionIndex()
        self._currentSceneInfo["Versions"][idx]["Note"] = self._currentNotes
        self._dumpJson(self._currentSceneInfo, self._baseScenesInCategory[self._currentBaseSceneName])

    '''
    def addUser(self, fullName, initials):
        """
        Adds a new user to the database
        :param fullName: (String)
        :param initials: (String)
        :return: None
        """
        logger.debug("Func: addUser")

        # old Name
        currentDB = self._loadUsers()
        # currentDB, dbFile = self.initUsers()
        initialsList = currentDB.values()
        if initials in initialsList:
            msg="Initials are in use"
            # raise Exception([340, msg])
            self._exception(340, msg)
            return
            # return -1, msg
        currentDB[fullName] = initials
        self._dumpJson(currentDB, self._pathsDict["usersFile"])
        self._usersDict = currentDB
        return None, None

    def removeUser(self, fullName):
        """Removes the user from database"""
        logger.debug("Func: removeUser")

        # old Name removeUser
        currentDB = self._loadUsers()
        del currentDB[fullName]
        self._dumpJson(currentDB, self._pathsDict["usersFile"])
        self._usersDict = currentDB
        return None, None
    '''
    def addCategory(self, categoryName):
        """Adds a new category to the database"""
        curCategories = self._loadCategories()
        if categoryName in curCategories:
            msg = "Duplicate Category names are not allowed"
            # logger.warning(msg)
            # raise Exception([340, msg])
            self._exception(101, msg)
            return
            # return -1
        curCategories.append(categoryName)
        self._dumpJson(curCategories, self._pathsDict["categoriesFile"])
        self._categories = curCategories
        return

    def moveCategory(self, categoryName, direction):
        """Moves the category index one step towards given direction"""
        # TODO : NOT TESTED
        if direction == "left" or direction == "down":
            dir = -1
        if direction == "right" or direction == "up":
            dir = 1

        curCategories = self._loadCategories()

        index = curCategories.index(categoryName)
        newindex= index+dir
        if not (0 <= newindex <= len(curCategories)):
            return

        itemAtNewIndex = curCategories[newindex]

        curCategories[newindex] = categoryName
        curCategories[index] = itemAtNewIndex

        self._dumpJson(curCategories, self._pathsDict["categoriesFile"])
        self._categories = curCategories
        return


    def removeCategory(self, categoryName):
        """Removes the category from database"""
        curCategories = self._loadCategories()
        if len(curCategories) == 1:
            # Last category cannot be removed
            msg = "Last Category cannot be removed"
            # logger.warning(msg)
            # raise Exception([360, msg])
            self._exception(360, msg)
            return

        if categoryName in curCategories:
            # Check if category about to be removed is empty
            for subP in self._subProjectsList:
                baseScenes = self.scanBaseScenes(categoryAs=categoryName, subProjectAs=subP)
                if baseScenes:
                    # if it in not empty abort
                    msg = "Category is not empty. Aborting..."
                    # logger.warning(msg)
                    # raise Exception([360, msg])
                    self._exception(360, msg)
                    return

            # remove the empty category
            curCategories.remove(categoryName)
            self._dumpJson(curCategories, self._pathsDict["categoriesFile"])
            self._categories = curCategories
            return

        else:
            msg = "Specified Category does not exist"
            # logger.warning(msg)
            # raise Exception([101, msg])
            self._exception(101, msg)
            return

        # try:
        #     curCategories.remove(categoryName)
        #     self._dumpJson(curCategories, self._pathsDict["categoriesFile"])
        #     self._categories = curCategories
        #     return
        # except ValueError:
        #     logger.warning("Specified Category does not exist")



    def playPreview(self, camera):
        """Runs the playblast at cursor position"""
        logger.debug("Func: playPreview")
        print "cam", camera
        # absPath = os.path.join(self.projectDir, self._currentPreviewsDict[self._currentPreviewCamera])
        absPath = os.path.join(self.projectDir, self._currentPreviewsDict[camera])
        if self.currentPlatform == "Windows":
            try:
                os.startfile(absPath)
            except WindowsError:
                return -1, ["Cannot Find Playblast", "Playblast File is missing", "Do you want to remove it from the Database?"]
        # TODO something to play the file in linux
        return

    def removePreview(self):
        """Deletes the preview file and removes it from the database"""
        logger.debug("Func: removePreview")

        if self._currentPreviewCamera:
            previewName = self._currentPreviewCamera
            previewFile = self._currentPreviewsDict[self._currentPreviewCamera]
            os.remove(os.path.join(self.projectDir, self._currentPreviewsDict[self._currentPreviewCamera]))
            del self._currentPreviewsDict[self._currentPreviewCamera]
            idx = self.getRealVersionIndex()
            self._currentSceneInfo["Versions"][idx]["Preview"] = self._currentPreviewsDict
            self._dumpJson(self._currentSceneInfo, self._baseScenesInCategory[self.currentBaseSceneName])
            logger.info("""Preview file deleted and removed from database successfully 
            Preview Name: {0}
            Path: {1}
                        """.format(previewName, previewFile))


    def deleteBasescene(self, databaseFile):
        """
        Deletes the given Base Scene and ALL its versions. Removes it from the database completely
        !!!USE WITH CAUTION!!!
        :param databaseFile: (String) Absolute path of the database file
        :return: None
        """
        logger.debug("Func: deleteBasescene")

        #ADMIN ACCESS
        jsonInfo = self._loadJson(databaseFile)
        if jsonInfo == -2:
            return -2
        # delete all version files
        for version in jsonInfo["Versions"]:
            try:
                os.remove(os.path.join(self.projectDir, version["RelativePath"]))
            except:
                msg = "Cannot delete scene version:%s" % (version["RelativePath"])
                logger.warning(msg)
                raise Exception([203, msg])
                # pass

        # delete reference file
        if jsonInfo["ReferenceFile"]:
            try:
                os.remove(os.path.join(self.projectDir, jsonInfo["ReferenceFile"]))
            except:
                msg = "Cannot delete reference file %s" % (jsonInfo["ReferenceFile"])
                logger.warning(msg)
                raise Exception([203, msg])
                # pass

        # delete base scene directory
        scene_path = os.path.join(self.projectDir, jsonInfo["Path"])
        try:
            os.rmdir(scene_path)
        except:
            msg = "Cannot delete scene path %s" % (scene_path)
            # logger.warning(msg)
            # raise Exception([203, msg])
            self._exception(203, msg)
            # pass
        # delete json database file
        try:
            os.remove(os.path.join(self.projectDir, databaseFile))
        except:
            msg = "Cannot delete scene path %s" % (databaseFile)
            # logger.warning(msg)
            # raise Exception([203, msg])
            self._exception(203, msg)
            # pass
        msg = "all database entries and version files of %s deleted" %databaseFile
        logger.debug(msg)
        self.errorLogger(title="Deleted Base Scene", errorMessage=msg)

    def deleteReference(self, databaseFile):
        """
        Deletes the Reference file of the given Base Scene (If exists).
        Basically this is opposite of what "makeReference"  method does.
        :param databaseFile: (String) Absolute path of the database file
        :return: None
        """
        logger.debug("Func: deleteReference")

        #ADMIN ACCESS
        jsonInfo = self._loadJson(databaseFile)
        if jsonInfo == -2:
            return -2

        if jsonInfo["ReferenceFile"]:
            try:
                referenceFile = jsonInfo["ReferenceFile"]
                os.remove(os.path.join(self.projectDir, jsonInfo["ReferenceFile"]))
                jsonInfo["ReferenceFile"] = None
                jsonInfo["ReferencedVersion"] = None
                self._dumpJson(jsonInfo, databaseFile)
                self.errorLogger(title="Deleted Reference File", errorMessage="%s deleted" %referenceFile)
            except:
                msg = "Cannot delete reference file %s" % (jsonInfo["ReferenceFile"])
                logger.warning(msg)
                raise Exception([203, msg])
                pass

    def makeReference(self):
        """Creates a Reference copy from the base scene version at cursor position"""
        logger.debug("Func: makeReference")

        if self._currentVersionIndex == -1 or self._currentSubVersionIndex == -1:
            msg = "Cursor is not on a Base Scene Version. Cancelling"
            # logger.warning(msg)
            # raise Exception([101, msg])
            self._exception(101, msg)
            return
            # return

        idx = self.getRealVersionIndex()
        absVersionFile = os.path.join(self.projectDir, self._currentSceneInfo["Versions"][idx]["RelativePath"])
        name = os.path.split(absVersionFile)[1]
        filename, extension = os.path.splitext(name)
        referenceName = "{0}_{1}_forReference".format(self._currentSceneInfo["Name"], self._currentSceneInfo["Category"])
        relReferenceFile = os.path.join(self._currentSceneInfo["Path"], "{0}{1}".format(referenceName, extension))
        absReferenceFile = os.path.join(self.projectDir, relReferenceFile)
        shutil.copyfile(absVersionFile, absReferenceFile)
        self._currentSceneInfo["ReferenceFile"] = relReferenceFile
        # SET the referenced version as the 'VISUAL INDEX NUMBER' starting from 1
        self._currentSceneInfo["ReferencedVersion"] = self._currentVersionIndex
        self._currentSceneInfo["ReferencedSubVersion"] = self._currentSubVersionIndex

        self._dumpJson(self._currentSceneInfo, self._baseScenesInCategory[self.currentBaseSceneName])

    def saveCallback(self):
        """Callback function to update reference files when files saved regularly"""

        ## TODO // TEST IT
        self._pathsDict["sceneFile"] = self.getSceneFile()
        try:
            openSceneInfo = self.getOpenSceneInfo()
            if not openSceneInfo:
                return
        except TypeError:
            return
        if openSceneInfo["jsonFile"]:
            jsonInfo = self._loadJson(openSceneInfo["jsonFile"])
            if jsonInfo["ReferenceFile"]:
                absRefFile = os.path.join(self._pathsDict["projectDir"], jsonInfo["ReferenceFile"])
                # TODO : ref => Dict
                absBaseSceneVersion = os.path.join(self._pathsDict["projectDir"], jsonInfo["Versions"][int(jsonInfo["ReferencedVersion"]) - 1]["RelativePath"])
                # if the refererenced scene file is the saved file (saved or saved as)
                if self._pathsDict["sceneFile"] == absBaseSceneVersion:
                    # copy over the forReference file
                    try:
                        shutil.copyfile(self._pathsDict["sceneFile"], absRefFile)
                        print "Scene Manager Update:\nReference File Updated"
                    except:
                        pass

    def checkReference(self, databaseFile, deepCheck=False):
        """
        Checks the Reference integrity of the base scene
        :param databaseFile: (String) Absolute path of the database file of the Base Scene
        :param deepCheck: (Bool) If True, iterates an additional checksum test. May be time
        consuming for large files or on systems with slow network speed.
        :return: Integer Codes: -2 => Error code for corrupted database file
                                -1 => Code Red : Reference File does not exist or checksum mismatch
                                0 => Code Yellow : No reference file found on database file
                                1 => Code Green : Checked without error
        """
        logger.debug("Func: checkReference")

        sceneInfo = self._loadJson(databaseFile)
        # assert (sceneInfo == -2)
        if sceneInfo == -2:
            return -2 # Corrupted database file

        if sceneInfo["ReferenceFile"]:
            relVersionFile = sceneInfo["Versions"][sceneInfo["ReferencedVersion"] - 1]["RelativePath"]
            absVersionFile = os.path.join(self.projectDir, relVersionFile)
            relRefFile = sceneInfo["ReferenceFile"]
            absRefFile = os.path.join(self.projectDir, relRefFile)

            if not os.path.isfile(absRefFile):
                logger.info("CODE RED: Reference File does not exist")
                return -1 # code red
            else:
                if deepCheck:
                    if filecmp.cmp(absVersionFile, absRefFile):
                        logger.info("CODE GREEN: Everything is OK")
                        return 1 # code Green
                    else:
                        logger.info("CODE RED: Checksum mismatch with reference file")
                        return -1 # code red
                else:
                    logger.info("CODE GREEN: Everything is OK")
                    return 1 # code Green
        else:
            logger.info("CODE YELLOW: File does not have a reference copy")
            return 0 # code yellow

    def errorLogger(self, title="", errorMessage=""):
        """
        Logs the error message
        :param title: (String) Title of the message
        :param errorMessage: (String) Body of the error message
        :return:
        """
        #
        logger = logging.getLogger('SceneManager')
        filePath = os.path.join(self._pathsDict["masterDir"], "sm_logs.log")
        file_logger = logging.FileHandler(filePath)
        logger.addHandler(file_logger)
        logger.setLevel(logging.DEBUG)

        now = datetime.datetime.now()
        timeInfo = now.strftime("%d.%m.%Y - %H:%M")
        userInfo = self.currentUser
        machineInfo = socket.gethostname()
        ## stuff
        logMessage = "-----------------------------------------\n" \
                     "{0} - {1}\n" \
                     "-----------------------------------------\n" \
                     "Log Message:\n" \
                     "{2}\n\n" \
                     "User: {3}\n" \
                     "Workstation: {4}\n".format(title, timeInfo, errorMessage, userInfo, machineInfo)

        logger.debug(logMessage)

        logger.removeHandler(file_logger)
        file_logger.flush()
        file_logger.close()

    def checkPassword(self, password):
        """Compares the given password with the hashed password file. Returns True if matches else False"""
        # get the hash
        pswFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "adminPass.psw")
        if os.path.isfile(pswFile):
            f = open(pswFile, "r")
            if f.mode == "r":
                hashedPass = f.read()
            else:
                return None
            f.close()
        ## use the default password hash if there is no password file
        else:
            hashedPass="7110eda4d09e062aa5e4a390b0a572ac0d2c0220"

        passToCheck = (hashlib.sha1(str(password).encode('utf-8')).hexdigest())

        if passToCheck == hashedPass:
            return True
        else:
            return False

    def changePassword(self, oldPassword, newPassword):
        """
        Changes the password and saves the hash
        :param oldPassword: (String)
        :param newPassword: (String)
        :return: (bool) True if successfull
        """
        if self.checkPassword(oldPassword):
            pswFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "adminPass.psw")
            tempFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "adminPassTmp.psw")
            newHash = (hashlib.sha1(str(newPassword).encode('utf-8')).hexdigest())

            f = open(tempFile, "w+")
            f.write(newHash)
            f.close()
            shutil.copyfile(tempFile, pswFile)
            os.remove(tempFile)
            return True
        else:
            return False

    def _exception(self, code, msg):
        """Exception report function. Throws a log error and raises an exception"""

        logger.error("Exception %s" %self.errorCodeDict[code])
        logger.error(msg)
        raise Exception (code, msg)

    def _checkRequirements(self):
        """
        Checks the requirements for platform and administrator rights. Returns [None, None] if passes both
        Returns: (List) [ErrorCode, ErrorMessage]
        """
        logger.debug("Func: _checkRequirements")

        # check platform
        # currentOs = platform.system()
        '''
        if currentOs != "Linux" and currentOs != "Windows":
            self._exception(210, "Operating System is not supported\nCurrently only Windows and Linux supported")
            return -1, ["OS Error", "Operating System is not supported",
                        "Scene Manager only supports Windows and Linux Operating Systems"]
        '''
        ## check admin rights
        # try:
        #     is_admin = os.getuid() == 0
        # except AttributeError:
        #     is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        # if not is_admin:
        #     self._exception(360, "Admin Rights Needed\nSoftware needs to be run as administrator in order to work with Scene Manager")
        #     return -1, ["Admin Rights", "You dont have the administrator rights",
        #                 "You need to run the Software as administrator to work with Scene Manager"]
        return None, None

    def _folderCheck(self, folder):
        """Checks if the folder exists, creates it if doesnt"""
        logger.debug("Func: _folderCheck")

        if not os.path.isdir(os.path.normpath(folder)):
            os.makedirs(os.path.normpath(folder))

    def nameCheck(self, text, allowSpaces=False):
        """Checks the text for illegal characters, Returns:  corrected Text or -1 for Error """
        logger.debug("Func: nameCheck")

        if allowSpaces:
            pattern = "^[ A-Za-z0-9_-]*$"
        else:
            pattern = "^[A-Za-z0-9_-]*$"

        if re.match(pattern, text):
            return True
        else:
            return False


    def niceName(self, path):
        """Gets the base name of the given filename"""
        logger.debug("Func: niceName")

        basename = os.path.split(path)[1]
        return os.path.splitext(basename)[0]

    def resolveProjectPath(self, projectRoot, projectName):
        """Parses the info to the absolute project folder path"""
        logger.debug("Func: resolveProjectPath")

        if projectName == "":
            msg = ("Fill the mandatory fields")
            # logger.warning(msg)
            # raise Exception([341, msg])
            self._exception(341, msg)
            return

        fullPath = os.path.join(os.path.normpath(str(projectRoot)), projectName)
        return fullPath

    ## Database loading / saving functions
    ## -----------------------------

    def _loadJson(self, file):
        """Loads the given json file"""
        # TODO : Is it paranoid checking?
        if os.path.isfile(file):
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    return data
            except ValueError:
                msg = "Corrupted JSON file => %s" % file
                # logger.error(msg)
                self._exception(200, msg)
                # return -2 # code for corrupted json file
        else:
            msg = "File cannot be found => %s" % file
            self._exception(201, msg)

    def _dumpJson(self, data, file):
        """Saves the data to the json file"""
        name, ext = os.path.splitext(file)
        tempFile = "{0}.tmp".format(name)
        with open(tempFile, "w") as f:
            json.dump(data, f, indent=4)
        shutil.copyfile(tempFile, file)
        os.remove(tempFile)

    def loadProjectSettings(self):
        """Loads Project Settings from file"""
        if not os.path.isfile(self._pathsDict["projectSettingsFile"]):
            projectSettingsDB = {"Resolution": [1920, 1080],
                                   "FPS": 25}
            self._dumpJson(projectSettingsDB, self._pathsDict["projectSettingsFile"])
            return projectSettingsDB
        else:
            projectSettingsDB = self._loadJson(self._pathsDict["projectSettingsFile"])
            if projectSettingsDB== -2:
                return -2
            return projectSettingsDB

    def saveProjectSettings(self, data):
        """Dumps the data to the project settings database file"""
        try:
            self._dumpJson(data, self._pathsDict["projectSettingsFile"])
            msg = ""
            return 0, msg
        except:
            msg = "Cannot save current settings"
            return -1, msg

    def _loadUsers(self):
        """Load Users from file"""
        logger.debug("Func: _loadUsers")
        user = getpass.getuser()
        pat = re.compile('\W')
        formatUser = pat.sub('_', user)
        return {user: formatUser}

    def loadFavorites(self):
        """Loads Bookmarked projects"""
        logger.debug("Func: loadFavorites")

        if os.path.isfile(self._pathsDict["bookmarksFile"]):
            bookmarksData = self._loadJson(self._pathsDict["bookmarksFile"])
            if bookmarksData == -2:
                return -2
        else:
            bookmarksData = []
            self._dumpJson(bookmarksData, self._pathsDict["bookmarksFile"])
        return bookmarksData

    def addToFavorites(self, shortName, absPath):
        """
        Adds the given project info to the favorites database
        :param shortName: (String) Name of the project
        :param absPath: (String) Absolute path of the project folder
        :return: (List) [Favorites Data]
        """
        logger.debug("Func: addToFavorites")

        # old Name userFavoritesAdd
        bookmarksData = self.loadFavorites()
        bookmarksData.append([shortName, absPath])
        self._dumpJson(bookmarksData, self._pathsDict["bookmarksFile"])
        return bookmarksData

    def removeFromFavorites(self, index):
        """Removes the data from the Favorites database. Accepts index number of the Favorites list"""
        logger.debug("Func: removeFromFavorites")

        # old Name userFavoritesRemove
        bookmarksData = self.loadFavorites()
        del bookmarksData[index]
        self._dumpJson(bookmarksData, self._pathsDict["bookmarksFile"])
        return bookmarksData

    def _loadCategories(self):
        """Load Categories from file"""
        logger.debug("Func: _loadCategories")

        if os.path.isfile(self._pathsDict["categoriesFile"]):
            categoriesData = self._loadJson(self._pathsDict["categoriesFile"])
            if categoriesData == -2:
                return -2
        else:
            categoriesData = self._sceneManagerDefaults["defaultCategories"]
            # categoriesData = ["Model", "Shading", "Rig", "Layout", "Animation", "Render", "Other"]
            self._dumpJson(categoriesData, self._pathsDict["categoriesFile"])
        return categoriesData

    def _loadSceneInfo(self):
        """Returns scene info of base scene at cursor position"""
        logger.debug("Func: _loadSceneInfo")

        sceneInfo = self._loadJson(self._baseScenesInCategory[self._currentBaseSceneName])
        if sceneInfo == -2:
            return -2
        return sceneInfo

    def _loadUserPrefs(self):
        """Load Last CategoryIndex, SubProject Index, User name and Access mode from file as dictionary"""
        logger.debug("Func: _loadUserPrefs")

        if os.path.isfile(self._pathsDict["currentsFile"]):
            settingsData = self._loadJson(self._pathsDict["currentsFile"])
            if settingsData == -2:
                return -2
        else:
            settingsData = {"currentTabIndex": 0, "currentSubIndex": 0, "currentUser": self._usersDict.keys()[0],
                            "currentMode": True}
            self._dumpJson(settingsData, self._pathsDict["currentsFile"])
        return settingsData

    def _saveUserPrefs(self, settingsData):
        """Save Last CategoryIndex, SubProject Index, User name and Access mode to file as dictionary"""
        logger.debug("Func: _saveUserPrefs")
        try:
            self._dumpJson(settingsData, self._pathsDict["currentsFile"])
            msg = ""
            return 0, msg
        except:
            msg = "Cannot save current settings"
            return -1, msg

    def _loadSubprojects(self):
        """Loads Subprojects of current project"""
        logger.debug("Func: _loadSubprojects")

        if not os.path.isfile(self._pathsDict["subprojectsFile"]):
            data = ["None"]
            self._dumpJson(data, self._pathsDict["subprojectsFile"])
        else:
            data = self._loadJson(self._pathsDict["subprojectsFile"])
            if data == -2:
                return -2
        return data

    def _saveSubprojects(self, subprojectsList):
        """Save Subprojects to the file"""
        logger.debug("Func: _saveSubprojects")

        self._dumpJson(subprojectsList, self._pathsDict["subprojectsFile"])

    def _loadProjects(self):
        """Loads Projects dictionary for each software"""
        logger.debug("Func: _loadProjects")

        if not os.path.isfile(self._pathsDict["projectsFile"]):
            return
        else:
            projectsData = self._loadJson(self._pathsDict["projectsFile"])
            if projectsData == -2:
                return -2
        return projectsData

    def _saveProjects(self, data):
        """Saves the current project data to the file"""
        logger.debug("Func: _saveProjects %s")

        self._dumpJson(data, self._pathsDict["projectsFile"])

    def loadPBSettings(self):
        """Loads the preview settings data"""
        # TODO // NEEDS to be IMPROVED and compatible with all softwares (Nuke and Houdini)
        logger.debug("Func: loadPBSettings")

        # old Name getPBsettings

        # pbSettingsFile = os.path.normpath(os.path.join(self.project_Path, "Playblasts", "PBsettings.json"))

        if not os.path.isfile(self._pathsDict["pbSettingsFile"]):
            # defaultSettings = {"Resolution": (1280, 720),  ## done
            #                    "Format": 'avi',  ## done
            #                    "Codec": 'IYUV codec',  ## done
            #                    "Percent": 100,  ## done
            #                    "Quality": 100,  ## done
            #                    "ShowFrameNumber": True,
            #                    "ShowSceneName": False,
            #                    "ShowCategory": False,
            #                    "ShowFrameRange": True,
            #                    "ShowFPS": True,
            #                    "PolygonOnly": True,  ## done
            #                    "ShowGrid": False,  ## done
            #                    "ClearSelection": True,  ## done
            #                    "DisplayTextures": True,  ## done
            #                    "WireOnShaded": False,
            #                    "UseDefaultMaterial": False,
            #                    }
            defaultSettings = self._sceneManagerDefaults["defaultPreviewSettings"]
            self._dumpJson(defaultSettings, self._pathsDict["pbSettingsFile"])
            return defaultSettings
        else:
            pbSettings = self._loadJson(self._pathsDict["pbSettingsFile"])
            if pbSettings == -2:
                return -2
            return pbSettings

    def savePBSettings(self, pbSettings):
        """Dumps the Preview settings data to the database"""
        logger.debug("Func: savePBSettings")

        # old Name setPBsettings

        self._dumpJson(pbSettings, self._pathsDict["pbSettingsFile"])
        return

    def checkNewVersion(self):

        url = "http://www.ardakutlu.com/Tik_Manager/versionCheck/versionInfo.json"

        response = urllib.urlopen(url)
        data = json.loads(response.read())
        majorV_remote, minorV_remote, patch_remote = map(lambda x: int(x), data["CurrentVersion"].split("."))
        versionStr_remote = data["CurrentVersion"]
        downloadPath = data["DownloadPath"]
        whatsNewPath = data["WhatsNew"]
        # try:
        #     response = urllib.urlopen(url)
        #     data = json.loads(response.read())
        #     majorV_remote, minorV_remote, patch_remote = map(lambda x: int(x) ,data["CurrentVersion"].split("."))
        #     versionStr_remote = data["CurrentVersion"]
        #     downloadPath = data["DownloadPath"]
        #     whatsNewPath = data["WhatsNew"]
        # except:
        #     vMsg = "Cannot reach version information. Check you internet connection"
        #     return vMsg, None, None

        majorV, minorV, patch = map(lambda x: int(x) ,_version.__version__.split("."))

        if majorV_remote > majorV:
            vMsg = "New major version!\nTik Manager v{0} is now available".format(versionStr_remote)
            return vMsg, downloadPath, whatsNewPath

        elif minorV_remote > minorV:
            vMsg = "Tik Manager v{0} is now available".format(versionStr_remote)
            return vMsg, downloadPath, whatsNewPath

        elif patch_remote > patch:
            vMsg = "Tik Manager v{0} with minor bug fixes and improvements is now available".format(versionStr_remote)
            return vMsg, downloadPath, whatsNewPath

        else:
            vMsg = "Tik Manager is up to date"
            return vMsg, None, None

    def checkBaseNameUnique(self, categoryName, baseName, subProjectIndex=0):
        scenesToCheck = self.scanBaseScenes(categoryAs=categoryName, subProjectAs=subProjectIndex)
        for key in scenesToCheck.keys():
            if baseName.lower() == key.lower():
                msg = ("Base Scene Name is not unique!\nABORTING")
                self._exception(360, msg)
                return -1, msg

        return 0

    def getFileVersionInfo(self, filePath):
        pat = re.compile('_v([\d]{3})_([\d]{3})$', re.I)
        cName = os.path.splitext(os.path.basename(filePath))[0]
        m = pat.search(cName)
        curVersion = 0
        curSubVersion = 0
        if m:
            curVersion = int(m.group(1))
            curSubVersion = int(m.group(2))
        else:
            curVersion = int(cName[-3:])
            curSubVersion = 1

        info = {'currentVersion': curVersion,
                'currentSubVersion': curSubVersion}
        return info

    def getSubProject(self, subProjectIndex):
        subProject = self._subProjectsList[subProjectIndex]
        if subProject == 'None':
            subProject = ''

        return subProject

    def getOutputSceneFolder(self, categoryName, baseName, subProjectIndex=0, checkUniqueBaseName=0):
        if checkUniqueBaseName:
            self.checkBaseNameUnique(categoryName, baseName, subProjectIndex=0)

        scenesDir = self._pathsDict["scenesDir"]
        subProject = self.getSubProject(subProjectIndex)
        outFolder = os.path.normpath(os.path.join(
            scenesDir, categoryName, subProject, baseName))
        self._folderCheck(outFolder)
        return outFolder

    def getOutputJsonFolder(self, categoryName, baseName, subProjectIndex=0):
        databaseDir = self._pathsDict["databaseDir"]
        subProject = self.getSubProject(subProjectIndex)
        outFolder = os.path.normpath(os.path.join(
            databaseDir, categoryName, subProject))
        self._folderCheck(outFolder)
        return outFolder

    def getPreviewFolder(self, categoryName, baseName, subProject=None, subProjectIndex=0):
        if subProject is None:
            subProject = self.getSubProject(subProjectIndex)

        pbDir = self._pathsDict["previewsDir"]
        outFolder = os.path.normpath(os.path.join(
            pbDir, categoryName, subProject, baseName))
        self._folderCheck(outFolder)
        return outFolder

    def getOutputFileName(self, baseName, categoryName, version, subVersion, fileFormat):
        sceneName = "{0}_{1}_v{2}_{3}.{4}".format(
            baseName, categoryName, str(version).zfill(3),
            str(subVersion).zfill(3), fileFormat)
        return sceneName

    def getOutputJsonName(self, baseName):
        return '%s.json' % baseName

    def getReferenceFileName(self, baseName, categoryName, fileFormat):
        referenceName = "{0}_{1}_forReference".format(baseName, categoryName)
        return referenceName

    def getThumbnailName(self, baseName, version, subVersion):
        thumbName = "%s_v%03d_%03d_thumb.jpg" % (
            baseName, version, subVersion)
        return thumbName

    def getOutputFileInfo(self, categoryName, baseName, version, subVersion,
                          sceneFormat, checkUniqueBaseName=0, subProjectIndex=0,
                          makeReference=True, *args, **kwargs):
        sceneDir = self.getOutputSceneFolder(
            categoryName, baseName, subProjectIndex=subProjectIndex,
            checkUniqueBaseName=checkUniqueBaseName)
        sceneName = self.getOutputFileName(baseName, categoryName,
                                           version, subVersion, sceneFormat)
        sceneFile = os.path.normpath(os.path.join(sceneDir, sceneName))

        jsonDir = self.getOutputJsonFolder(categoryName, baseName,
                                           subProjectIndex=subProjectIndex)
        jsonName = self.getOutputJsonName(baseName)
        jsonFile = os.path.normpath(os.path.join(jsonDir, jsonName))

        thumbName = self.getThumbnailName(baseName, version, subVersion)
        thumbFile = os.path.normpath(os.path.join(jsonDir, thumbName))

        referenceFile = None
        referenceVersion = None
        referenceSubVersion = None
        if makeReference:
            referenceName = self.getReferenceFileName(
                baseName, categoryName, sceneFormat)
            referenceFile = os.path.normpath(os.path.join(sceneDir, referenceName))
            referenceVersion = version
            referenceSubVersion = subVersion

        info = {'sceneDir': sceneDir,
                'sceneFile': sceneFile,
                'jsonFile': jsonFile,
                'thumbFile': thumbFile,
                'referenceFile': referenceFile,
                'referenceVersion': referenceVersion,
                'referenceSubVersion': referenceSubVersion}
        return info

    def getOutputVersionUpFileInfo(self, jsonFile, versionUp, fileFormat,
                                   makeReference=True, *args, **kwargs):
        jsonInfo = self._loadJson(jsonFile)

        versions = jsonInfo["Versions"]
        lastVersion = versions[-1]
        lastRp = lastVersion['RelativePath']

        verInfo = self.getFileVersionInfo(lastRp)
        curVersion = verInfo['currentVersion']
        curSubVersion = verInfo['currentSubVersion']

        version = 0
        subVersion = 0
        if versionUp:
            version = curVersion + 1
            subVersion = 1
        else:
            version = curVersion
            projSetting = self.loadProjectSettings()
            maxSubVerNum = projSetting.get('MaxSubVerNum', 20)
            subVersion = curSubVersion % maxSubVerNum + 1

        baseName = jsonInfo['Name']
        category = jsonInfo['Category']
        outName = self.getOutputFileName(
            baseName, category, version, subVersion, fileFormat)

        relPath = jsonInfo["Path"]
        relSceneFile = os.path.join(relPath, outName)
        sceneFile = os.path.join(self._pathsDict["projectDir"], relSceneFile)

        jsonDir = os.path.dirname(jsonFile)
        thumbName = self.getThumbnailName(baseName, version, subVersion)
        thumbFile = os.path.normpath(os.path.join(jsonDir, thumbName))

        referenceFile = None
        referenceVersion = None
        referenceSubVersion = None

        sceneDir = os.path.dirname(sceneFile)
        if makeReference:
            referenceName = self.getReferenceFileName(
                baseName, category, fileFormat)
            referenceFile = os.path.normpath(os.path.join(sceneDir, referenceName))
            referenceVersion = version
            referenceSubVersion = subVersion

        info = {'sceneDir': sceneDir,
                'sceneFile': sceneFile,
                'jsonFile': jsonFile,
                'thumbFile': thumbFile,
                'referenceFile': referenceFile,
                'referenceVersion': referenceVersion,
                'referenceSubVersion': referenceSubVersion}
        return info

    def getVersionDetailInfo(self):
        versionData = self.getVersions()

        verIdInfo = {}
        for i, curVersionData in enumerate(versionData):
            relPath = curVersionData['RelativePath']
            verInfo = self.getFileVersionInfo(relPath)
            version = verInfo['currentVersion']
            subVersion = verInfo['currentSubVersion']

            verIdInfo.setdefault(version, {})
            verIdInfo[version][subVersion] = i

        return verIdInfo

    def getRealVersionIndex(self):
        idx = self._currentVersionDetailInfo[self._currentVersionIndex][self._currentSubVersionIndex]
        return idx

    def getDefaultProjectDirectory(self):
        defaultProjectDirs = [
            "_COMP",
            "_REF",
            "_TRANSFER/FBX",
            "_TRANSFER/ALEMBIC",
            "_TRANSFER/OBJ",
            "_TRANSFER/MA",
            "cache",
            "data",
            "images/_CompRenders",
            "particles",
            "Playblasts",
            "renderData/depth",
            "renderData/fur",
            "renderData/iprImages",
            "renderData/mentalray",
            "renderData/shaders",
            "scenes",
            "scripts",
            "sound",
            "sourceimages/_FOOTAGE",
            "sourceimages/_HDR",
            "smDatabase"]
        return defaultProjectDirs

    def createProjectDirectory(self, resolvedPath, projectType):
        defaultProjectDirs = self.getDefaultProjectDirectory()
        projDirs = self._projectDirectoryDefaultInfo.get(projectType, defaultProjectDirs)
        projDirs.append(resolvedPath)
        for projDir in projDirs:
            outDir = os.path.join(resolvedPath, projDir)
            if not os.path.isdir(outDir):
                os.makedirs(outDir)

    def createProjectWorkspaceFile(self, resolvedPath, projectType):
        wsFile = os.path.join(self._pathsDict["generalSettingsDir"],
                              "%sWorkspace.mel" % projectType)
        if not os.path.isfile(wsFile):
            wsFile = os.path.join(self._pathsDict["generalSettingsDir"],
                                  "defaultWorkspace.mel")

        toWsFile = os.path.join(resolvedPath, "workspace.mel")
        shutil.copy(wsFile, toWsFile)

    def checkProjectFolder(self):
        projSetting = self.loadProjectSettings()
        projectType = projSetting['ProjectType']
        self._projectDirectoryDefaultInfo = self._loadJson(
            self._pathsDict["projectDirectoryDatabase"])

        defaultProjectDirs = self.getDefaultProjectDirectory()
        projDirs = self._projectDirectoryDefaultInfo.get(
            projectType, defaultProjectDirs)

        resolvedPath = self.getProjectDir()
        for projDir in projDirs:
            outDir = os.path.join(resolvedPath, projDir)
            if not os.path.isdir(outDir):
                os.makedirs(outDir)
