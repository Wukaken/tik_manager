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

from SmUIRoot import MainUI as baseUI
import os
from SmRoot import RootManager

import shutil

# import MaxPlus
from MaxPlus import FileManager as fManager
from MaxPlus import PathManager as pManager
from pymxs import runtime as rt

import datetime
import socket
import logging
# from glob import glob

from Qt import QtWidgets, QtCore, QtGui

import _version

import pprint



__author__ = "Arda Kutlu"
__copyright__ = "Copyright 2018, Pd Manager for 3dsMax Projects"
__credits__ = []
__version__ = "2.0.0"
__license__ = "GPL"
__maintainer__ = "Arda Kutlu"
__email__ = "ardakutlu@gmail.com"
__status__ = "Development"

SM_Version = "Pd Manager 3ds Max v%s" %_version.__version__

logging.basicConfig()
logger = logging.getLogger('sm3dsMax')
logger.setLevel(logging.WARNING)

class MaxManager(RootManager):
    def __init__(self):
        super(MaxManager, self).__init__()

        self.init_paths()
        # self.backwardcompatibility()  # DO NOT RUN UNTIL RELEASE
        self.init_database()


    def getSoftwarePaths(self):
        """Overriden function"""
        softwareDatabaseFile = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "softwareDatabase.json"))
        softwareDB = self._loadJson(softwareDatabaseFile)
        return softwareDB["3dsMax"]
        # To tell the base class maya specific path names
        # return {"niceName": "3dsMax",
        #         "databaseDir": "maxDB",
        #         "scenesDir": "scenes_3dsMax",
        #         "pbSettingsFile": "pbSettings_3dsMax.json",
        #         "categoriesFile": "categories3dsMax.json",
        #         "userSettingsDir": "PdManager/3dsMax"} # this is just for 3ds max. expanduser"~" returns different in max

    def getProjectDir(self):
        """Overriden function"""
        # p_path = pManager.GetProjectFolderDir()
        # norm_p_path = os.path.normpath(p_path)
        projectsDict = self._loadProjects()


        if not projectsDict:
            norm_p_path = os.path.normpath(pManager.GetProjectFolderDir())
            projectsDict = {"3dsMaxProject": norm_p_path}
            self._saveProjects(projectsDict)
            return norm_p_path

        # get the project defined in the database file
        try:
            norm_p_path = projectsDict["3dsMaxProject"]
            return norm_p_path
        except KeyError:
            norm_p_path = os.path.normpath(pManager.GetProjectFolderDir())
            projectsDict = {"3dsMaxProject": norm_p_path}
            self._saveProjects(projectsDict)
            return norm_p_path

    def getSceneFile(self):
        """Overriden function"""
        # Gets the current scene path ("" if untitled)
        logger.debug("GETSCENEFILE")
        s_path = fManager.GetFileNameAndPath()
        norm_s_path = os.path.normpath(s_path)
        return norm_s_path

    def setProject(self, path):
        """Sets the project"""
        logger.debug("Func: setProject")

        wsMxp = os.path.join(path, '%s.mxp' % os.path.basename(path))
        if not os.path.isfile(wsMxp):
            msg = 'This is not a standard max project,\ndo nothing!'
            rt.messageBox(msg, title='Error In Setting Project')
            return

        projSettingFile = os.path.join(path, 'smDatabase', 'projectSettings.json')
        status, verMsg = self.compareProjectSoftWareVersion(projSettingFile)
        if status:
            rt.messageBox(verMsg, title='Error In Max Version')
            return

        projectsDict = self._loadProjects()
        if not projectsDict:
            projectsDict = {"3dsMaxProject": path}
        else:
            projectsDict["3dsMaxProject"] = path
        self._saveProjects(projectsDict)
        self.projectDir = path

    def saveBaseScene(self, categoryName, nickname, baseName, subProjectIndex=0, makeReference=True, versionNotes="", sceneFormat="max", *args, **kwargs):
        """
        Saves the scene with formatted name and creates a json file for the scene
        Args:
            category: (String) Category if the scene. Valid categories are 'Model', 'Animation', 'Rig', 'Shading', 'Other'
            userName: (String) Predefined user who initiates the process
            baseName: (String) Base name of the scene. Eg. 'Shot01', 'CharacterA', 'BookRig' etc...
            subProject: (Integer) The scene will be saved under the sub-project according to the given integer value. The 'self.subProjectList' will be
                searched with that integer.
            makeReference: (Boolean) If set True, a copy of the scene will be saved as forReference
            versionNotes: (String) This string will be stored in the json file as version notes.
            *args:
            **kwargs:

        Returns: Scene DB Dictionary

        """
        logger.debug("Func: saveBaseScene")

        projectPath = self.projectDir
        now = datetime.datetime.now().strftime("%H:%M - %Y/%m/%d")
        completeNote = "[%s] on %s\n%s\n" % (self.currentUser, now, versionNotes)

        info = self.getOutputFileInfo(
            categoryName, nickname, baseName, 1, 1, sceneFormat,
            checkUniqueBaseName=1, subProjectIndex=subProjectIndex,
            makeReference=makeReference)
        if not info:
            return [-1, '']

        sceneDir = info['sceneDir']
        sceneFile = info['sceneFile']
        jsonFile = info['jsonFile']
        thumbFile = info['thumbFile']
        referenceFile = info['referenceFile']
        referenceVersion = info['referenceVersion']
        referenceSubVersion = info['referenceSubVersion']

        fManager.Save(sceneFile)
        self.doCreateThumbnail(thumbFile)

        versionInfo = rt.maxversion()
        vInfo = [versionInfo[0], versionInfo[1], versionInfo[2]]
        
        jsonInfo = {}
        jsonInfo["ID"] = "Sm3dsMaxV02_sceneFile"
        jsonInfo["3dsMaxVersion"] = vInfo
        jsonInfo["Name"] = baseName
        jsonInfo["Nickname"] = nickname
        jsonInfo["Path"] = os.path.relpath(sceneDir, start=projectPath)
        jsonInfo["Category"] = categoryName
        jsonInfo["Creator"] = self.currentUser
        jsonInfo["CreatorHost"] = (socket.gethostname())
        if referenceFile:
            jsonInfo["ReferenceFiles"] = [os.path.relpath(referenceFile, start=projectPath)]
            jsonInfo["ReferencedVersions"] = [referenceVersion]
            jsonInfo["ReferencedSubVersions"] = [referenceSubVersion]
        else:
            jsonInfo["ReferenceFiles"] = []
            jsonInfo["ReferencedVersions"] = []
            jsonInfo["ReferencedSubVersions"] = []

        jsonInfo["Versions"] = [  # PATH => Notes => User Initials => Machine ID => Playblast => Thumbnail
            {"RelativePath": os.path.relpath(sceneFile, start=projectPath),
             "Nickname": nickname,
             "Note": completeNote,
             "User": self._usersDict[self.currentUser],
             "Workstation": socket.gethostname(),
             "Preview": {},
             "Thumb": os.path.relpath(thumbFile, start=projectPath),
             "Ranges": self._getTimelineRanges()
             }
        ]

        jsonInfo["SubProject"] = self._subProjectsList[subProjectIndex]
        self._dumpJson(jsonInfo, jsonFile)
        return [0, ""]

    def saveVersion(self, makeReference=True, versionNotes="", sceneFormat="max", *args, **kwargs):
        """
        Saves a version for the predefined scene. The scene json file must be present at the /data/[Category] folder.
        Args:
            userName: (String) Predefined user who initiates the process
            makeReference: (Boolean) If set True, make a copy of the forReference file. There can be only one 'forReference' file for each scene
            versionNotes: (String) This string will be hold in the json file as well. Notes about the changes in the version.
            *args:
            **kwargs:

        Returns: Scene DB Dictionary

        """
        logger.debug("Func: saveVersion")

        sceneInfo = self.getOpenSceneInfo()
        if sceneInfo:
            if sceneFormat is None:
                sceneFormat = sceneInfo['sceneFormat']

            projectPath = self.projectDir
            
            now = datetime.datetime.now().strftime("%H:%M - %Y/%m/%d")
            completeNote = "[%s] on %s\n%s\n" % (self.currentUser, now, versionNotes)

            jsonFile = sceneInfo["jsonFile"]
            versionUp = kwargs.get('versionUp', 1)
            info = self.getOutputVersionUpFileInfo(jsonFile, versionUp, sceneFormat,
                                                   makeReference=makeReference)
            sceneFile = info['sceneFile']
            thumbFile = info['thumbFile']
            nickname = info['nickname']
            referenceFile = info['referenceFile']
            referenceVersion = info['referenceVersion']
            referenceSubVersion = info['referenceSubVersion']

            fManager.Save(sceneFile)
            self.doCreateThumbnail(thumbFile)
                
            jsonInfo = self._loadJson(jsonFile)
            jsonInfo["Versions"].append(
                {"RelativePath": os.path.relpath(sceneFile, start=projectPath),
                 "Nickname": nickname,
                 "Note": completeNote,
                 "User": self._usersDict[self.currentUser],
                 "Workstation": socket.gethostname(),
                 "Preview": {},
                 "Thumb": os.path.relpath(thumbFile, start=projectPath),
                 "Ranges": self._getTimelineRanges()})

            if referenceFile is not None:
                shutil.copyfile(sceneFile, referenceFile)
                refVers = jsonInfo["ReferencedVersion"]
                if referenceVersion in refVers:
                    refIdx = refVers.index(referenceVersion)
                    jsonInfo["ReferenceFiles"][refIdx] = os.path.relpath(
                        referenceFile, start=projectPath)
                    jsonInfo["ReferencedVersions"][refIdx] = referenceVersion
                    jsonInfo["ReferencedSubVersions"][refIdx] = referenceSubVersion
                else:
                    refVers.append(referenceVersion)
                    refVers.sort()
                    refIdx = refVers.index(referenceVersion)
                    jsonInfo["ReferencedVersions"] = refVers
                    jsonInfo["ReferenceFiles"].insert(refIdx, os.path.relpath(
                        referenceFile, start=projectPath))
                    jsonInfo["ReferencedSubVersions"].insert(refIdx, referenceSubVersion)

            self._dumpJson(jsonInfo, jsonFile)
        else:
            msg = "This is not a base scene (Json file cannot be found)"
            logger.warning(msg)
            return -1, msg
        return jsonInfo

    def createPreview(self, *args, **kwargs):
        """Creates a Playblast preview from currently open scene"""
        # rt = pymxs.runtime

        openSceneInfo = self.getOpenSceneInfo()
        if not openSceneInfo:
            msg = "This is not a base scene. Scene must be saved as a base scene before playblasting."
            # raise Exception([360, msg])
            self._exception(360, msg)
            return
            # logger.warning(msg)
            # return -1, msg

        # get view info
        viewportType = rt.viewport.getType()
        print "CVP", viewportType
        if str(viewportType) == "view_camera":
            currentCam = str(rt.getActiveCamera().name)
        else:
            currentCam = str(viewportType)

        validName = currentCam.replace("|", "__").replace(" ", "_")
        extension = "avi"

        # versionName = rt.getFilenameFile(rt.maxFileName) #
        versionName = rt.maxFilePath + rt.maxFileName # abs path of the filename with extension
        print "versionName", versionName
        relVersionName = os.path.relpath(versionName, start=openSceneInfo["projectPath"]) # relative path of filename with ext

        if not os.path.isdir(os.path.normpath(openSceneInfo["previewPath"])):
            os.makedirs(os.path.normpath(openSceneInfo["previewPath"]))
        playBlastFile = os.path.join(openSceneInfo["previewPath"], "{0}_{1}_PB.{2}".format(self.niceName(versionName), validName, extension))
        relPlayBlastFile = os.path.relpath(playBlastFile, start=openSceneInfo["projectPath"])

        if os.path.isfile(playBlastFile):
            try:
                os.remove(playBlastFile)
            except WindowsError:
                msg = "The file is open somewhere else"
                logger.warning(msg)
                return -1, msg

        jsonInfo = self._loadJson(openSceneInfo["jsonFile"])
        if jsonInfo == -1:
            msg = "Database file is corrupted"
            return -1, msg
        # returns 0,"" if everything is ok, -1,msg if error

        pbSettings = self.loadPBSettings()
        originalValues = {"width": rt.renderWidth,
                        "height": rt.renderHeight
                        }

        originalSelection = rt.execute("selection as array")



        # change the render settings temporarily
        rt.renderWidth = pbSettings["Resolution"][0]
        rt.renderHeight = pbSettings["Resolution"][1]

        if pbSettings["PolygonOnly"]:
            dspGeometry = True
            dspShapes = False
            dspLights = False
            dspCameras = False
            dspHelpers = False
            dspParticles = False
            dspBones = False
        else:
            dspGeometry = True
            dspShapes = True
            dspLights = True
            dspCameras = True
            dspHelpers = True
            dspParticles = True
            dspBones = True

        dspGrid = pbSettings["ShowGrid"]
        dspFrameNums = pbSettings["ShowFrameNumber"]
        percentSize = pbSettings["Percent"]

        if pbSettings["WireOnShaded"]:
            rndLevel = rt.execute("#litwireframe")
        else:
            rndLevel = rt.execute("#smoothhighlights")

        if pbSettings["ClearSelection"]:
            rt.clearSelection()


        # find the path of where the avi file be created
        # if rt.maxFilePath:
        #     previewname = rt.getFilenameFile(rt.maxFileName)
        # else:
        #     previewname = "Untitled"

        sourceClip = rt.GetDir(rt.execute("#preview")) + "\_scene.avi "

        # destination = os.path.join(rt.maxFilePath, previewname)

        print "sourceClip is: %s" % sourceClip

        print "test: %s" %os.path.isfile(sourceClip)

        if os.path.isfile(sourceClip):
            try:
                os.remove(sourceClip)
            except WindowsError:
                msg = "Cannot continue creating preview.\n Close '%s' and try again" %sourceClip
                logger.error(msg)
                return -1, msg

        rt.createPreview(percentSize=percentSize, dspGeometry=dspGeometry,
                         dspShapes=dspShapes, dspLights=dspLights,
                         dspCameras=dspCameras, dspHelpers=dspHelpers,
                         dspParticles=dspParticles, dspBones=dspBones,
                         dspGrid=dspGrid, dspFrameNums=dspFrameNums,
                         rndLevel=rndLevel)


        # return the render width and height to original:
        rt.renderWidth = originalValues["width"]
        rt.renderHeight = originalValues["height"]

        rt.select(originalSelection)

        shutil.copy(sourceClip, playBlastFile)

        ## find this version in the json data
        print "relVersionName", relVersionName
        print "jInfo", jsonInfo

        for version in jsonInfo["Versions"]:
            if relVersionName == version["RelativePath"]:
                version["Preview"][currentCam] = relPlayBlastFile

        self._dumpJson(jsonInfo, openSceneInfo["jsonFile"])
        return 0, ""

    def loadBaseScene(self, force=False):
        """Loads the scene at cursor position"""
        # TODO // TEST IT
        logger.debug("Func: loadBaseScene")
        idx = self.getRealVersionIndex()
        relSceneFile = self._currentSceneInfo["Versions"][idx]["RelativePath"]
        absSceneFile = os.path.join(self.projectDir, relSceneFile)
        if os.path.isfile(absSceneFile):
            fManager.Open(absSceneFile)
            return 0
        else:
            msg = "File in Pd Manager database doesnt exist"
            logger.error(msg)
            return -1, msg

    def importBaseScene(self):
        """Imports the scene at cursor position"""
        logger.debug("Func: importBaseScene")
        idx = self.getRealVersionIndex()
        relSceneFile = self._currentSceneInfo["Versions"][idx]["RelativePath"]
        absSceneFile = os.path.join(self.projectDir, relSceneFile)
        if os.path.isfile(absSceneFile):
            # fManager.Merge(absSceneFile, mergeAll=True, selectMerged=True)
            fManager.Merge(absSceneFile)
            return 0
        else:
            msg = "File in Pd Manager database doesnt exist"
            logger.error(msg)
            return -1, msg

    def referenceBaseScene(self):
        """Creates reference from the scene at cursor position"""
        logger.debug("Func: referenceBaseScene")
        projectPath = self.projectDir
        relReferenceFiles = self._currentSceneInfo["ReferenceFiles"]
        relReferenceVersions = self._currentSceneInfo["ReferencedVersions"]
        relReferenceFile = ''
        idx = 0
        if self._currentVersionIndex in relReferenceVersions:
            idx = relReferenceVersions.index(self._currentVersionIndex)
            relReferenceFile = relReferenceFiles[idx]
        
        if relReferenceFile:
            referenceFile = os.path.join(projectPath, relReferenceFile)

            # software specific
            Xrefobjs = rt.getMAXFileObjectNames(referenceFile)
            rt.xrefs.addNewXRefObject(referenceFile, Xrefobjs)
            try:
                ranges = self._currentSceneInfo["Versions"][idx]["Ranges"]
                q = self._question("Do You want to set the Time ranges same with the reference?")
                if q:
                    self._setTimelineRanges(ranges)
            except KeyError:
                pass

        else:
            logger.warning("There is no reference set for this scene. Nothing changed")

    def doCreateThumbnail(self, thumbFile):
        oWidth = 221
        oHeight = 124

        grab = rt.gw.getViewportDib()
        ratio = float(grab.width) / float(grab.height)

        if ratio <= 1.782:
            new_width = oHeight * ratio
            new_height = oHeight
        else:
            new_width = oWidth
            new_height = oWidth / ratio

        resizeFrame = rt.bitmap(new_width, new_height, color=rt.color(0, 0, 0))
        rt.copy(grab, resizeFrame)
        thumbFrame = rt.bitmap(oWidth, oHeight, color=rt.color(0, 0, 0))
        xOffset = (oWidth - resizeFrame.width) / 2
        yOffset = (oHeight - resizeFrame.height) / 2

        rt.pasteBitmap(resizeFrame, thumbFrame, rt.point2(0, 0), rt.point2(xOffset, yOffset))
        thumbFrame.filename = thumbFile
        rt.save(thumbFrame)
        rt.close(thumbFrame)

    def createThumbnail(self, useCursorPosition=False, dbPath = None, versionInt = None):
        """
        Creates the thumbnail file.
        :param databaseDir: (String) If defined, this folder will be used to store the created database.
        :param version: (integer) if defined this version number will be used instead currently open scene version.
        :return: (String) Relative path of the thumbnail file
        """
        projectPath = self.projectDir
        if useCursorPosition:
            versionInt = self.currentVersionIndex
            dbPath = self.currentDatabasePath
        else:
            if not dbPath or not versionInt:
                logger.warning (("Both dbPath and version must be defined if useCursorPosition=False"))

        versionStr = "v%s" % (str(versionInt).zfill(3))
        dbDir, shotNameWithExt = os.path.split(dbPath)
        shotName = os.path.splitext(shotNameWithExt)[0]

        thumbPath = "{0}_{1}_thumb.jpg".format(os.path.join(dbDir, shotName), versionStr)
        relThumbPath = os.path.relpath(thumbPath, projectPath)

        ## Software specific section
        # rt = pymxs.runtime
        oWidth = 221
        oHeight = 124

        grab = rt.gw.getViewportDib()

        ratio = float(grab.width)/float(grab.height)

        if ratio <= 1.782:
            new_width = oHeight * ratio
            new_height = oHeight
        else:
            new_width = oWidth
            new_height = oWidth / ratio

        resizeFrame = rt.bitmap(new_width, new_height, color = rt.color(0,0,0))
        rt.copy(grab, resizeFrame)
        thumbFrame = rt.bitmap(oWidth, oHeight, color = rt.color(0,0,0))
        xOffset = (oWidth - resizeFrame.width) /2
        yOffset = (oHeight - resizeFrame.height) /2

        rt.pasteBitmap(resizeFrame, thumbFrame, rt.point2(0, 0), rt.point2(xOffset, yOffset))

        # rt.display(thumbFrame)

        thumbFrame.filename = thumbPath
        rt.save(thumbFrame)
        rt.close(thumbFrame)



        # img = rt.gw.getViewportDib()
        # img.fileName = thumbPath
        # rt.save(img)
        # rt.close(img)

        return relThumbPath

    def replaceThumbnail(self, filePath=None):
        """
        Replaces the thumbnail with given file or current view
        :param filePath: (String)  if a filePath is defined, this image (.jpg or .gif) will be used as thumbnail
        :return: None
        """
        logger.debug("Func: replaceThumbnail")
        thumbName = self.getThumbnailName(
            self._currentSceneInfo['Name'], self._currentVersionIndex,
            self._currentSubVersionIndex)
        jsonDir = os.path.dirname(self.currentDatabasePath)
        thumbFile = os.path.normpath(os.path.join(jsonDir, thumbName))
        if not filePath:
            self.doCreateThumbnail(thumbFile)
        else:
            shutil.copy(filePath, thumbFile)

        idx = self.getRealVersionIndex()
        projectPath = self.projectDir
        self._currentSceneInfo["Versions"][idx]["Thumb"] = os.path.relpath(
            thumbFile, start=projectPath)

        self._dumpJson(self._currentSceneInfo, self.currentDatabasePath)

    def getSoftwareVersion(self):
        versionInfo = rt.maxversion()
        return [versionInfo[0], versionInfo[1], versionInfo[2]]

    def getSoftwareMainVersion(self):
        apiVer = self.getSoftwareVersion()
        mainVer = str((apiVer[0] - 11000) / 1000 + 2009)
        return mainVer

    def compareProjectSoftWareVersion(self, projSettingFile):
        swVer = self.getSoftwareVersion()
        projSetting = self._loadJson(projSettingFile)
        projVerKey = '3dsMaxVersion'
        projVer = projSetting.get(projVerKey)
        status = 0
        msg = ''
        if projVer is None:
            status = 1
            msg = 'Project not defined max version'
        elif not swVer[0] == projVer[0]:
            status = 2
            msg = 'Project version: %s.%s.%s, current max version: %s.%s.%s, not match' % (
                projVer[0], projVer[1], projVer[2],
                swVer[0], swVer[1], swVer[2])

        return status, msg

    def compareVersions(self):
        """Compares the versions of current session and database version at cursor position"""
        # TODO : Write compare function for 3ds max
        # return 0, ""
        if not self._currentSceneInfo["3dsMaxVersion"]:
            logger.warning("Cursor is not on a base scene")
            return
        versionDict = {11000: "v2009",
                       12000: "v2010",
                       13000: "v2011",
                       14000: "v2012",
                       15000: "v2013",
                       16000: "v2014",
                       17000: "v2015",
                       18000: "v2016",
                       19000: "v2017",
                       20000: "v2018",
                       21000: "v2019",
                       22000: "v2020",
                       }

        #version serialization:
        # version, api, sdk = rt.maxversion()
        versionInfo = rt.maxversion()
        # currentVersion = [version, api, sdk]
        currentVersion = [versionInfo[0], versionInfo[1], versionInfo[2]]
        logger.debug("currentversion %s" %currentVersion)
        baseSceneVersion = self._currentSceneInfo["3dsMaxVersion"]
        logger.debug("baseVersion %s" % baseSceneVersion)

        try:
            niceVName = versionDict[currentVersion[0]]
        except KeyError:
            niceVName = str(currentVersion[0])

        if currentVersion == baseSceneVersion:
            msg = ""
            return 0, msg

        if currentVersion[0] > baseSceneVersion[0]: # max version compare
            message = "Base Scene is created with a LOWER 3ds Max version ({0}). Are you sure you want to continue?".format(niceVName)
            return -1, message

        if currentVersion[0] < baseSceneVersion[0]:
            message = "Base Scene is created with a HIGHER 3ds Max version ({0}). Are you sure you want to continue?".format(niceVName)
            return -1, message

        if currentVersion[1] > baseSceneVersion[1]: # max Api
            message = "Base Scene is created with a LOWER Build ({0}). Are you sure you want to continue?".format(niceVName)
            return -1, message

        if currentVersion[1] < baseSceneVersion[1]:
            message = "Base Scene is created with a HIGHER Build ({0}). Are you sure you want to continue?".format(niceVName)
            return -1, message

        # old or corrupted database
        return 0, ""  # skip


    def isSceneModified(self):
        """Checks the currently open scene saved or not"""
        return fManager.IsSaveRequired()

    def saveSimple(self):
        """Save the currently open file"""
        fManager.Save()

    def getFormatsAndCodecs(self):
        """Returns the codecs which can be used in current workstation"""
        # TODO : Write Get Formats and Codecs for 3ds max (if applicable)
        logger.warning ("getFormatsAndCodecs Function not yet implemented")


    def preSaveChecklist(self):
        """Checks the scene for inconsistencies"""
        checklist = []

        # TODO : Create a fps comparison with the settings file
        fpsValue_setting = self.getFPS()
        fpsValue_current = rt.framerate
        if fpsValue_setting is not fpsValue_current:
            msg = "FPS values are not matching with the project settings.\n Project FPS => {0}\n scene FPS => {1}\nDo you want to continue?".format(fpsValue_setting, fpsValue_current)
            checklist.append(msg)

        return checklist

    def _exception(self, code, msg):
        """Overriden Function"""

        rt.messageBox(msg, title=self.errorCodeDict[code])
        if (200 >= code < 210):
            raise Exception(code, msg)

    def _question(self, msg):
        state = rt.queryBox( msg, title='Manager Question')
        return state

    def _getTimelineRanges(self):
        R_ast = int(rt.animationRange.start)
        R_min = int(rt.animationRange.start)
        R_max = int(rt.animationRange.end)
        R_aet = int(rt.animationRange.end)
        return [R_ast, R_min, R_max, R_aet]

    def _setTimelineRanges(self, rangeList):
        """Sets the timeline ranges [AnimationStart, Min, Max, AnimationEnd]"""
        rt.animationRange = rt.interval(rangeList[0], rangeList[-1])

    def _createCallbacks(self, handler):
        logger.warning("_createCallbacks Function yet implemented")

    def _killCallbacks(self, callbackIDList):
        logger.warning("_killCallbacks Function not yet implemented")

    def createProjectWorkspaceFile(self, projectName, resolvedPath, projectType):
        wsFile = os.path.join(self._pathsDict["generalSettingsDir"],
                              "%sWorkspace.mxp" % projectType)
        if not os.path.isfile(wsFile):
            wsFile = os.path.join(self._pathsDict["generalSettingsDir"],
                                  "defaultWorkspace.mxp")

        toWsFile = os.path.join(resolvedPath, "%s.mxp" % projectName)
        shutil.copy(wsFile, toWsFile)


class MainUI(baseUI):
    def __init__(self):
        super(MainUI, self).__init__()

        self.manager = MaxManager()
        problem, msg = self.manager._checkRequirements()
        if problem:
            self.close()
            self.deleteLater()

        self.buildUI()
        self.initMainUI(newborn=True)
        self.extraMenus()

    def extraMenus(self):
        self.scenes_rcItem_0.setText('Merge Scene')
