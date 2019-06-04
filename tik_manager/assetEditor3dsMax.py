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

# Asset save functions for 3ds Max to be used with assetLibrary
import os

from MaxPlus import FileManager as fManager
from MaxPlus import PathManager as pManager
from pymxs import runtime as rt
from shutil import copyfile
# import json
# import logging


class AssetEditor3dsMax(object):
    def __init__(self):
        super(AssetEditor3dsMax, self).__init__()
        self.directory=""


    def saveAsset(self, assetName, exportUV=True, exportOBJ=True, exportFBX=True, exportABC=True, selectionOnly=True, mbFormat=False, notes="N/A", **info):
        """
        Saves the selected object(s) as an asset into the predefined library
        """
        # self.ssResolution = 1000
        if assetName == "":
            msg = "Asset Name cannot be empty"
            state = rt.messageBox(msg, title='Info')
            return

        if assetName in self.assetsList:
            msg = "This Asset already exists.\nDo you want to overwrite?"
            state = rt.queryBox( msg, title='Manager Question')
            if state:
                pass
            else:
                return

        s_path = fManager.GetFileNameAndPath()
        originalPath = os.path.normpath(s_path)

        dump, origExt = os.path.splitext(originalPath)

        assetDirectory = os.path.join(self.directory, assetName)

        assetAbsPath = os.path.join(assetDirectory, "%s%s" %(assetName, u'.max'))


        originalSelection = rt.execute("selection as array")


        if not os.path.exists(assetDirectory):
            os.mkdir(assetDirectory)

        # ################
        # ## RESEARCH ####
        # ################
        #
        # def getBitmapTextures(objectList):
        #     bDict = {}
        #     for i in objectList:
        #         bDict[i] = rt.getClassInstances(rt.bitmapTexture, target=i, asTrackViewPick=False)
        #     # print rt.getClassInstances(rt.bitmapTexture, target=i, asTrackViewPick=False)
        #     return bDict
        #
        # def getBitmapTexturesZ(objectList):
        #     """Returns the list of objects with bitmap textures as [[Object1, BitmapTexture1], [Object2, BitmapTexture2]]"""
        #     bDict = [(str(i), rt.getClassInstances(rt.bitmapTexture, target=i, asTrackViewPick=False)) for i in
        #              objectList if len(rt.usedMaps(i)) > 0]
        #     return bDict
        #
        # from MaxPlus import FileManager as fManager
        # from MaxPlus import PathManager as pManager
        # from pymxs import runtime as rt
        #
        # selection = rt.execute("selection as array")
        # texArr = []
        #
        # # for x in selection:
        # #	for i in (rt.usedMaps(x)):
        # #		texArr.append(i)
        #
        # # print "old", texArr
        #
        # # for x in selection:
        # #	map(lambda i: (texArr.append(i)), rt.usedMaps(x))
        #
        # texArr = [map(lambda i: i, rt.usedMaps(x)) for x in selection]
        #
        # print texArr
        #
        # ######################################



        # GET TEXTURES
        # ------------
        if selectionOnly:
            possibleFileHolders = rt.execute("selection as Array")
            filteredBitmaps = self._getFileNodes(possibleFileHolders)

        else:
            allTexture = rt.usedMaps()
            allBitmap = rt.getClassInstances(rt.bitmapTexture)
            # this makes sure only the USED bitmaps will stored
            filteredBitmaps = [x for x in allBitmap if x.filename in allTexture]


        textureDatabase = [x for x in self._buildPathDatabase(filteredBitmaps, assetDirectory)]

        self._copyTextures(textureDatabase)

        # CREATE PREVIEWS
        # ---------------
        thumbPath, ssPath, swPath = self._createThumbnail(assetName, selectionOnly=selectionOnly, viewFit=True)

        # CREATE UV SNAPSHOTS
        # ----------------
        if exportUV:
            self._uvSnaps(assetName)

        # SAVE SOURCE
        # -----------
        if selectionOnly:
            fManager.SaveSelected(assetAbsPath)
        else:
            fManager.SaveSceneAsVersion(assetAbsPath)


        # EXPORT OBJ
        # ----------
        exportSettings = self.getExportSettings()

        if exportOBJ:
            objSettings = exportSettings["objExport"]
            objFilePath = os.path.join(assetDirectory, "%s.obj" %assetName)
            if self.exportObj(objFilePath, objSettings):
                objName = "{0}.obj".format(assetName)
            else:
                objName = "N/A"

            # if rt.pluginManager.loadclass(rt.ObjExp):
            #     # Set OBJ Options
            #     ObjSettings = exportSettings["objExport"]
            #
            #     iniPath_exportSettings = rt.objExp.getIniName()
            #     rt.setINISetting(iniPath_exportSettings, "Geometry", "FlipZyAxis", ObjSettings["FlipZyAxis"])
            #     rt.setINISetting(iniPath_exportSettings, "Geometry", "Shapes", ObjSettings["Shapes"])
            #     rt.setINISetting(iniPath_exportSettings, "Geometry", "ExportHiddenObjects", ObjSettings["ExportHiddenObjects"])
            #     rt.setINISetting(iniPath_exportSettings, "Geometry", "FaceType", ObjSettings["FaceType"])
            #     rt.setINISetting(iniPath_exportSettings, "Geometry", "TextureCoords", ObjSettings["TextureCoords"])
            #     rt.setINISetting(iniPath_exportSettings, "Geometry", "Normals", ObjSettings["Normals"])
            #     rt.setINISetting(iniPath_exportSettings, "Geometry", "SmoothingGroups", ObjSettings["SmoothingGroups"])
            #     rt.setINISetting(iniPath_exportSettings, "Geometry", "ObjScale", ObjSettings["ObjScale"])
            #
            #     rt.setINISetting(iniPath_exportSettings, "Output", "RelativeIndex", ObjSettings["RelativeIndex"])
            #     rt.setINISetting(iniPath_exportSettings, "Output", "Target", ObjSettings["Target"])
            #     rt.setINISetting(iniPath_exportSettings, "Output", "Precision", ObjSettings["Precision"])
            #
            #     rt.setINISetting(iniPath_exportSettings, "Optimize", "optVertex", ObjSettings["optVertex"])
            #     rt.setINISetting(iniPath_exportSettings, "Optimize", "optNormals", ObjSettings["optNormals"])
            #     rt.setINISetting(iniPath_exportSettings, "Optimize", "optTextureCoords", ObjSettings["optTextureCoords"])
            #
            #
            #     rt.exportFile(os.path.join(assetDirectory, assetName), rt.Name("NoPrompt"), selectedOnly=selectionOnly, using=rt.ObjExp)
            #     objName = "{0}.obj".format(assetName)
            # else:
            #     msg = "Wavefront(Obj) Export Plugin cannot be initialized. Skipping Obj export"
            #     rt.messageBox(msg, title='Info')
            #     objName = "N/A"
        else:
            objName = "N/A"

        # EXPORT FBX
        # ----------
        if exportFBX:
            fbxSettings = exportSettings["fbxExport"]
            fbxFilePath = os.path.join(assetDirectory, "%s.fbx" %assetName)

            if self.exportFbx(fbxFilePath, fbxSettings):
                fbxName = "{0}.fbx".format(assetName)
            else:
                fbxName = "N/A"

        #     # FBXSettings = exportSettings["fbxExport"]
        #     if rt.pluginManager.loadclass(rt.FBXEXP):
        #         # Set FBX Options
        #         for item in FBXSettings.items():
        #             print item[0], " => ", item[1]
        #             rt.FBXExporterSetParam(rt.Name(item[0]), item[1])
        #
        #         # rt.FBXExporterSetParam(rt.Name("Animation"), True)
        #         # rt.FBXExporterSetParam(rt.Name("ASCII"), False)
        #         # rt.FBXExporterSetParam(rt.Name("AxisConversionMethod"), "Fbx_Root")
        #         # rt.FBXExporterSetParam(rt.Name("BakeAnimation"), True)
        #         # rt.FBXExporterSetParam(rt.Name("BakeFrameStart"), 0)
        #         # rt.FBXExporterSetParam(rt.Name("BakeFrameEnd"), 100)
        #         # rt.FBXExporterSetParam(rt.Name("BakeFrameStep"), 1)
        #         # rt.FBXExporterSetParam(rt.Name("BakeResampleAnimation"), False)
        #         # rt.FBXExporterSetParam(rt.Name("CAT2HIK"), False)
        #         # rt.FBXExporterSetParam(rt.Name("ColladaTriangulate"), False)
        #         # rt.FBXExporterSetParam(rt.Name("ColladaSingleMatrix"), True)
        #         # rt.FBXExporterSetParam(rt.Name("ColladaFrameRate"), float(rt.framerate))
        #         # rt.FBXExporterSetParam(rt.Name("Convert2Tiff"), False)
        #         # rt.FBXExporterSetParam(rt.Name("ConvertUnit"), "in")
        #         # rt.FBXExporterSetParam(rt.Name("EmbedTextures"), True)
        #         # rt.FBXExporterSetParam(rt.Name("FileVersion"), "FBX201400")
        #         # rt.FBXExporterSetParam(rt.Name("FilterKeyReducer"), False)
        #         # rt.FBXExporterSetParam(rt.Name("GeomAsBone"), True)
        #         # rt.FBXExporterSetParam(rt.Name("GenerateLog"), False)
        #         # rt.FBXExporterSetParam(rt.Name("Lights"), True)
        #         # rt.FBXExporterSetParam(rt.Name("NormalsPerPoly"), True)
        #         # rt.FBXExporterSetParam(rt.Name("PointCache"), False)
        #         # rt.FBXExporterSetParam(rt.Name("Preserveinstances"), False)
        #         # rt.FBXExporterSetParam(rt.Name("Removesinglekeys"), False)
        #         # rt.FBXExporterSetParam(rt.Name("Resampling"), float(rt.framerate))
        #         # rt.FBXExporterSetParam(rt.Name("ScaleFactor"), 1.0)
        #         # rt.FBXExporterSetParam(rt.Name("SelectionSetExport"), False)
        #         # rt.FBXExporterSetParam(rt.Name("Shape"), True)
        #         # rt.FBXExporterSetParam(rt.Name("Skin"), True)
        #         # rt.FBXExporterSetParam(rt.Name("ShowWarnings"), False)
        #         # rt.FBXExporterSetParam(rt.Name("SmoothingGroups"), True)
        #         # rt.FBXExporterSetParam(rt.Name("SmoothMeshExport"), True)
        #         # rt.FBXExporterSetParam(rt.Name("SplitAnimationIntoTakes"), True)
        #         # rt.FBXExporterSetParam(rt.Name("TangentSpaceExport"), False)
        #         # rt.FBXExporterSetParam(rt.Name("Triangulate"), False)
        #         # rt.FBXExporterSetParam(rt.Name("UpAxis"), "Y")
        #         # rt.FBXExporterSetParam(rt.Name("UseSceneName"), False)
        #
        #         fileName = "{0}.fbx".format(os.path.join(assetDirectory, assetName))
        #         try:
        #             rt.exportFile(fileName, rt.Name("NoPrompt"), selectedOnly=selectionOnly,
        #                           using=rt.FBXEXP)
        #             fbxName = "{0}.fbx".format(assetName)
        #         except:
        #             msg = "Cannot export FBX for unknown reason. Skipping FBX export"
        #             rt.messageBox(msg, title='Info')
        #             fbxName = "N/A"
        #     else:
        #         msg = "FBX Plugin cannot be initialized. Skipping FBX export"
        #         rt.messageBox(msg, title='Info')
        #         fbxName = "N/A"
        #
        # else:
        #     fbxName = "N/A"

        # EXPORT ALEMBIC
        # --------------

        if exportABC:

            abcSettings = exportSettings["alembicExport"]
            abcFilePath = os.path.join(assetDirectory, "%s.abc" % assetName)
            frame = int(rt.sliderTime)
            abcSettings["StartFrame"] = frame
            abcSettings["EndFrame"] = frame

            if self.exportAlembic(abcFilePath, abcSettings):
                abcName = "{0}.abc".format(assetName)
            else:
                abcName = "N/A"
            # ABCSettings = exportSettings["alembicExport"]
            # fileName = "{0}.abc".format(os.path.join(assetDirectory, assetName))
            # abcName = "{0}.abc".format(assetName)
            # # Set Alembic Options according to the Max Version:
            # v = rt.maxVersion()[0]
            # if v > 17000: # Alembic export is not supported before 3ds Max 2016
            #     if rt.pluginManager.loadclass(rt.Alembic_Export):
            #         if 18000 <= v < 21000: # between versions 2016 - 2018
            #             rt.AlembicExport.CoordinateSystem = rt.Name(ABCSettings["CoordinateSystem"])
            #             rt.AlembicExport.ArchiveType = rt.Name(ABCSettings["ArchiveType"])
            #             rt.AlembicExport.ParticleAsMesh = ABCSettings["ParticleAsMesh"]
            #             rt.AlembicExport.CacheTimeRange = rt.Name(ABCSettings["CacheTimeRange"])
            #             rt.AlembicExport.ShapeName = ABCSettings["ShapeName"]
            #             rt.AlembicExport.StepFrameTime = ABCSettings["StepFrameTime"]
            #
            #         elif v >=21000: # version 2019 and up
            #             rt.AlembicExport.CoordinateSystem = rt.Name(ABCSettings["CoordinateSystem"])
            #             rt.AlembicExport.ArchiveType = rt.Name(ABCSettings["ArchiveType"])
            #             rt.AlembicExport.ParticleAsMesh = ABCSettings["ParticleAsMesh"]
            #             rt.AlembicExport.AnimTimeRange = rt.Name(ABCSettings["AnimTimeRange"])
            #             rt.AlembicExport.ShapeSuffix = ABCSettings["ShapeSuffix"]
            #             rt.AlembicExport.SamplesPerFrame = ABCSettings["SamplesPerFrame"]
            #             rt.AlembicExport.Hidden = ABCSettings["Hidden"]
            #             rt.AlembicExport.UVs = ABCSettings["UVs"]
            #             rt.AlembicExport.Normals = ABCSettings["Normals"]
            #             rt.AlembicExport.VertexColors = ABCSettings["VertexColors"]
            #             rt.AlembicExport.ExtraChannels = ABCSettings["ExtraChannels"]
            #             rt.AlembicExport.Velocity = ABCSettings["Velocity"]
            #             rt.AlembicExport.MaterialIDs = ABCSettings["MaterialIDs"]
            #             rt.AlembicExport.Visibility = ABCSettings["Visibility"]
            #             rt.AlembicExport.LayerName = ABCSettings["LayerName"]
            #             rt.AlembicExport.MaterialName = ABCSettings["MaterialName"]
            #             rt.AlembicExport.ObjectID = ABCSettings["ObjectID"]
            #             rt.AlembicExport.CustomAttributes = ABCSettings["CustomAttributes"]
            #
            #         # Export
            #         rt.exportFile(fileName, rt.Name("NoPrompt"), selectedOnly=selectionOnly,
            #                       using=rt.Alembic_Export)
            #     else:
            #         rt.messageBox("Alembic Plugin cannot be initialized. Skipping", title="Alembic not supported")
            #         abcName = "N/A"
            # else:
            #     rt.messageBox("There is no alembic support for this version. Skipping", title="Alembic not supported")
            #     abcName = "N/A"

        else:
            abcName = "N/A"

        # NUMERIC DATA
        # ------------

        if selectionOnly:
            countLoop = originalSelection

        else:
            countLoop = rt.execute("geometry as array")

        polyCount = sum(rt.getPolygonCount(x)[0] for x in countLoop)
        tiangleCount = sum(rt.getPolygonCount(x)[1] for x in countLoop)

        versionInfo = rt.maxversion()
        vInfo = [versionInfo[0], versionInfo[1], versionInfo[2]]

        # DATABASE
        # --------

        dataDict = {}
        dataDict['sourceProject'] = "3dsMax"
        dataDict['version'] = vInfo
        dataDict['assetName'] = assetName
        dataDict['objPath'] = objName
        dataDict['fbxPath'] = fbxName
        dataDict['abcPath'] = abcName
        dataDict['sourcePath'] = os.path.basename(assetAbsPath)
        dataDict['thumbPath'] = os.path.basename(thumbPath)
        dataDict['ssPath'] = os.path.basename(ssPath)
        dataDict['swPath'] = os.path.basename(swPath)
        dataDict['textureFiles'] = [x["Texture"] for x in textureDatabase]
        dataDict['Faces/Triangles'] = ("%s/%s" % (str(polyCount), str(tiangleCount)))
        dataDict['origin'] = originalPath
        dataDict['notes'] = notes

        print dataDict
        self._setData(assetName, dataDict)

        rt.clearSelection()
        self._returnOriginal(textureDatabase)
        # self.scanAssets() # scanning issued at populate function on ui class
        rt.messageBox("Asset Created Successfully", title='Info')

    def _createThumbnail(self, assetName, selectionOnly=True, viewFit=True):
        # ssResolution = 1000

        thumbPath = os.path.join(self.directory, assetName, "%s_thumb.jpg" % assetName)
        SSpath = os.path.join(self.directory, assetName, "%s_s.jpg" % assetName)
        WFpath = os.path.join(self.directory, assetName, "%s_w.jpg" % assetName)

        selection = rt.execute("selection as array")
        rt.clearSelection()

        if selectionOnly:
            rt.IsolateSelection.EnterIsolateSelectionMode()

        originalState = rt.viewport.GetRenderLevel()
        oWidth = 1600
        oHeight = 1600

        rt.viewport.SetRenderLevel(rt.Name("smoothhighlights"))
        grabShaded = rt.gw.getViewportDib()
        rt.viewport.SetRenderLevel(rt.Name("smoothhighlights"))
        grabWire = rt.gw.getViewportDib()


        ratio = float(grabShaded.width) / float(grabShaded.height)

        if ratio < 1.0:
            new_width = oHeight * ratio
            new_height = oHeight
        elif ratio > 1.0:
            new_width = oWidth
            new_height = oWidth / ratio
        else:
            new_width = oWidth
            new_height = oWidth

        resizeFrameShaded = rt.bitmap(new_width, new_height, color=rt.color(0, 0, 0))
        rt.copy(grabShaded, resizeFrameShaded)

        resizeFrameWire = rt.bitmap(new_width, new_height, color=rt.color(0, 0, 0))
        rt.copy(grabWire, resizeFrameWire)

        ssFrame = rt.bitmap(oWidth, oHeight, color=rt.color(0, 0, 0))
        wfFrame = rt.bitmap(oWidth, oHeight, color=rt.color(0, 0, 0))

        xOffset = (oWidth - resizeFrameShaded.width) / 2
        yOffset = (oHeight - resizeFrameShaded.height) / 2

        rt.pasteBitmap(resizeFrameShaded, ssFrame, rt.point2(0, 0), rt.point2(xOffset, yOffset))
        rt.pasteBitmap(resizeFrameWire, wfFrame, rt.point2(0, 0), rt.point2(xOffset, yOffset))

        # rt.display(ssFrame)
        # rt.display(wfFrame)

        thumbFrame = rt.bitmap(200, 200, color=rt.color(0, 0, 0))
        rt.copy(ssFrame, thumbFrame)

        rt.display(thumbFrame)

        thumbFrame.filename = thumbPath
        rt.save(thumbFrame)
        rt.close(thumbFrame)

        ssFrame.filename = SSpath
        rt.save(ssFrame)
        rt.close(ssFrame)

        wfFrame.filename = WFpath
        rt.save(wfFrame)
        rt.close(wfFrame)

        # switch to original view
        rt.viewport.SetRenderLevel(originalState)

        rt.IsolateSelection.ExitIsolateSelectionMode()

        return thumbPath, SSpath, WFpath

    def replaceWithCurrentView(self, assetName):

        thumbPath = os.path.join(self.directory, assetName, "%s_thumb.jpg" % assetName)
        SSpath = os.path.join(self.directory, assetName, "%s_s.jpg" % assetName)
        WFpath = os.path.join(self.directory, assetName, "%s_w.jpg" % assetName)

        self._createThumbnail(assetName, selectionOnly=False)

    def replaceWithExternalFile(self, assetName, FilePath):
        # TODO
        pass

    def _uvSnaps(self, assetName):
        selection = cmds.ls(sl=True)
        validShapes = cmds.listRelatives(selection, ad=True, type=["mesh", "nurbsSurface"])
        if len(validShapes) > 10:
            msg = "There are %s objects for UV snapshots.\nAre you sure you want to include snapshots to the Asset?" %(len(validShapes))
            state = cmds.confirmDialog(title='Too many objects for UV Snapshot', message=msg, button=['Ok', 'Cancel'])
            # cmds.warning("There are unknown nodes in the scene. Cannot proceed with %s extension. Do you want to proceed with %s?" %(ext, origExt))
            if state == "Ok":
                pass
            else:
                cmds.warning("Uv snapshots skipped")
                return

        assetDirectory = os.path.join(self.directory, assetName)
        UVdir = os.path.join(assetDirectory, "UV_snaps")
        if not os.path.isdir(os.path.normpath(UVdir)):
            os.makedirs(os.path.normpath(UVdir))

        for i in range(0, len(validShapes)):
            objName = validShapes[i].replace(":", "_")
            UVpath = os.path.join(UVdir, '%s_uv.jpg' % objName)
            cmds.select(validShapes[i])
            try:
                cmds.uvSnapshot(o=True, ff="jpg", n=UVpath, xr=1600, yr=1600)
            except:
                cmds.warning("Cannot create UV snapshot for %s" % validShapes[i])
        cmds.select(selection)


    def _getFileNodes(self, objList):
        returnList = []
        for x in objList:
            map(lambda x:(returnList.append(x)), rt.getClassInstances(rt.bitmapTexture, target=x, asTrackViewPick=False))
        return returnList

    def _buildPathDatabase(self, fileNodeList, newRoot):
        for file in fileNodeList:
            oldAbsPath = os.path.normpath(file.filename)
            filePath, fileBase = os.path.split(oldAbsPath)
            newAbsPath = os.path.normpath(os.path.join(newRoot, fileBase))

            yield {"FileNode": file,
                   "Texture": os.path.basename(oldAbsPath),
                   "OldPath": oldAbsPath,
                   "NewPath": newAbsPath
                   }

    def _copyTextures(self, pathDatabase):
        for data in pathDatabase:
            if data["OldPath"] != data["NewPath"]:
                copyfile(data["OldPath"], data["NewPath"])
                data["FileNode"].filename = data["NewPath"]

    def _returnOriginal(self, pathDatabase):
        for data in pathDatabase:
            # print data
            data["FileNode"].filename = data["OldPath"]

    def _checkVersionMatch(self, databaseVersion):
        currentVersion = rt.maxversion()

        if currentVersion != databaseVersion:
            msg = "Database version ({0}) and Current version ({1}) are not matching. Do you want to try anyway?".format(databaseVersion, currentVersion)
            state = rt.queryBox(msg, title='Version Mismatch')
            if state:
                return True
            else:
                return False
        else:
            return True

    def mergeAsset(self, assetName):
        assetData = self._getData(assetName)
        if not self._checkVersionMatch(assetData["version"]):
            print "versionMatching"
            return
        absSourcePath = os.path.join(self.directory, assetName, assetData["sourcePath"])

        textureList = assetData['textureFiles']
        cmds.file(absSourcePath, i=True)

        ## if there are not textures files to handle, do not waste time
        if len(textureList) == 0:
            return

        currentProjectPath = os.path.normpath(cmds.workspace(q=1, rd=1))
        sourceImagesPath = os.path.join(currentProjectPath, "sourceimages")
        if not os.path.isdir(os.path.normpath(sourceImagesPath)):
            os.makedirs(os.path.normpath(sourceImagesPath))

        fileNodes = cmds.ls(type="file")
        for texture in textureList:
            path = os.path.join(self.directory, assetData['assetName'], texture)
            ## find the textures file Node
            for file in fileNodes:
                if os.path.normpath(cmds.getAttr("%s.fileTextureName" %file)) == path:
                    filePath, fileBase = os.path.split(path)
                    newLocation = os.path.join(sourceImagesPath, assetName)
                    if not os.path.exists(newLocation):
                        os.mkdir(newLocation)
                    newPath = os.path.normpath(os.path.join(newLocation, fileBase))

                    copyfile(path, newPath)
                    cmds.setAttr("%s.fileTextureName" %file, newPath, type="string")

    def importAsset(self, assetName):
        assetData = self._getData(assetName)
        if not self._checkVersionMatch(assetData["version"]):
            return
        absSourcePath = os.path.join(self.directory, assetName, assetData["sourcePath"])

        cmds.file(absSourcePath, i=True)

    def importObj(self, assetName):

        # import Settings
        #     iniPath_importSettings = objImp.getIniName()
        #     setINISetting iniPath_importSettings "General" "ResetScene" "0"
        #
        #     setINISetting iniPath_importSettings "Objects" "SingleMesh" "1"
        #     setINISetting iniPath_importSettings "Objects" "Retriangulate" "0"
        #     setINISetting iniPath_importSettings "Objects" "AsEditablePoly" "1"--get it back as a poly
        #     setINISetting iniPath_importSettings "Geometry" "SmoothingGroups" "0"
        #     setINISetting iniPath_importSettings "Geometry" "TextureCoords" "1"

        assetData = self._getData(assetName)
        absObjPath = os.path.join(self.directory, assetName, assetData["objPath"])
        if os.path.isfile(absObjPath):
            cmds.file(absObjPath, i=True)

    def importAbc(self, assetName):
        assetData = self._getData(assetName)
        absAbcPath = os.path.join(self.directory, assetName, assetData["abcPath"])
        if os.path.isfile(absAbcPath):
            cmds.AbcImport(absAbcPath)

    def importFbx(self, assetName):
        assetData = self._getData(assetName)
        absFbxPath = os.path.join(self.directory, assetName, assetData["fbxPath"])
        if os.path.isfile(absFbxPath):
            cmds.file(absFbxPath, i=True)

    def exportObj(self, exportPath, exportSettings, exportSelected=True):
        if rt.pluginManager.loadclass(rt.ObjExp):
            # Set OBJ Options
            iniPath_exportSettings = rt.objExp.getIniName()
            rt.setINISetting(iniPath_exportSettings, "Geometry", "FlipZyAxis", exportSettings["FlipZyAxis"])
            rt.setINISetting(iniPath_exportSettings, "Geometry", "Shapes", exportSettings["Shapes"])
            rt.setINISetting(iniPath_exportSettings, "Geometry", "ExportHiddenObjects",
                             exportSettings["ExportHiddenObjects"])
            rt.setINISetting(iniPath_exportSettings, "Geometry", "FaceType", exportSettings["FaceType"])
            rt.setINISetting(iniPath_exportSettings, "Geometry", "TextureCoords", exportSettings["TextureCoords"])
            rt.setINISetting(iniPath_exportSettings, "Geometry", "Normals", exportSettings["Normals"])
            rt.setINISetting(iniPath_exportSettings, "Geometry", "SmoothingGroups", exportSettings["SmoothingGroups"])
            rt.setINISetting(iniPath_exportSettings, "Geometry", "ObjScale", exportSettings["ObjScale"])

            rt.setINISetting(iniPath_exportSettings, "Output", "RelativeIndex", exportSettings["RelativeIndex"])
            rt.setINISetting(iniPath_exportSettings, "Output", "Target", exportSettings["Target"])
            rt.setINISetting(iniPath_exportSettings, "Output", "Precision", exportSettings["Precision"])

            rt.setINISetting(iniPath_exportSettings, "Optimize", "optVertex", exportSettings["optVertex"])
            rt.setINISetting(iniPath_exportSettings, "Optimize", "optNormals", exportSettings["optNormals"])
            rt.setINISetting(iniPath_exportSettings, "Optimize", "optTextureCoords", exportSettings["optTextureCoords"])

            try:
                rt.exportFile(exportPath, rt.Name("NoPrompt"), selectedOnly=exportSelected, using=rt.ObjExp)
                return True
            except:
                msg = "Cannot export OBJ for unknown reason. Skipping OBJ export"
                rt.messageBox(msg, title='Info')
                return False

            # objName = "{0}.obj".format(assetName)
        else:
            msg = "Wavefront(Obj) Export Plugin cannot be initialized. Skipping Obj export"
            rt.messageBox(msg, title='Info')
            return False
            # objName = "N/A"

    def exportAlembic(self, exportPath, exportSettings, exportSelected=True):
        # Set Alembic Options according to the Max Version:
        v = rt.maxVersion()[0]
        if v > 17000:  # Alembic export is not supported before 3ds Max 2016
            if rt.pluginManager.loadclass(rt.Alembic_Export):
                if 18000 <= v < 21000:  # between versions 2016 - 2018
                    rt.AlembicExport.CoordinateSystem = rt.Name(exportSettings["CoordinateSystem"])
                    rt.AlembicExport.ArchiveType = rt.Name(exportSettings["ArchiveType"])
                    rt.AlembicExport.ParticleAsMesh = exportSettings["ParticleAsMesh"]
                    rt.AlembicExport.CacheTimeRange = rt.Name(exportSettings["AnimTimeRange"])
                    rt.AlembicExport.ShapeName = exportSettings["ShapeSuffix"]
                    # rt.AlembicExport.StepFrameTime = exportSettings["StepFrameTime"]

                elif v >= 21000:  # version 2019 and up
                    rt.AlembicExport.CoordinateSystem = rt.Name(exportSettings["CoordinateSystem"])
                    rt.AlembicExport.ArchiveType = rt.Name(exportSettings["ArchiveType"])
                    rt.AlembicExport.ParticleAsMesh = exportSettings["ParticleAsMesh"]
                    rt.AlembicExport.AnimTimeRange = rt.Name(exportSettings["AnimTimeRange"])
                    rt.AlembicExport.ShapeSuffix = exportSettings["ShapeSuffix"]
                    rt.AlembicExport.SamplesPerFrame = exportSettings["SamplesPerFrame"]
                    rt.AlembicExport.Hidden = exportSettings["Hidden"]
                    rt.AlembicExport.UVs = exportSettings["UVs"]
                    rt.AlembicExport.Normals = exportSettings["Normals"]
                    rt.AlembicExport.VertexColors = exportSettings["VertexColors"]
                    rt.AlembicExport.ExtraChannels = exportSettings["ExtraChannels"]
                    rt.AlembicExport.Velocity = exportSettings["Velocity"]
                    rt.AlembicExport.MaterialIDs = exportSettings["MaterialIDs"]
                    rt.AlembicExport.Visibility = exportSettings["Visibility"]
                    rt.AlembicExport.LayerName = exportSettings["LayerName"]
                    rt.AlembicExport.MaterialName = exportSettings["MaterialName"]
                    rt.AlembicExport.ObjectID = exportSettings["ObjectID"]
                    rt.AlembicExport.CustomAttributes = exportSettings["CustomAttributes"]

                # Export
                rt.exportFile(exportPath, rt.Name("NoPrompt"), selectedOnly=exportSelected,
                              using=rt.Alembic_Export)
                return True

            else:
                rt.messageBox("Alembic Plugin cannot be initialized. Skipping", title="Alembic not supported")
                return False
        else:
            rt.messageBox("There is no alembic support for this version. Skipping", title="Alembic not supported")
            return False


    def exportFbx(self, exportPath, exportSettings, exportSelected=True):
        if rt.pluginManager.loadclass(rt.FBXEXP):
            # Set FBX Options
            for item in exportSettings.items():
                rt.FBXExporterSetParam(rt.Name(item[0]), item[1])

            try:
                rt.exportFile(exportPath, rt.Name("NoPrompt"), selectedOnly=exportSelected,
                              using=rt.FBXEXP)
                return True
            except:
                msg = "Cannot export FBX for unknown reason. Skipping FBX export"
                rt.messageBox(msg, title='Info')
                return False
        else:
            msg = "FBX Plugin cannot be initialized. Skipping FBX export"
            rt.messageBox(msg, title='Info')
            return False





    def loadAsset(self, assetName):
        assetData = self._getData(assetName)
        absSourcePath = os.path.join(self.directory, assetName, assetData["sourcePath"])
        isSceneModified = cmds.file(q=True, modified=True)

        state = cmds.confirmDialog(title='Scene Modified', message="Save Changes to", button=['Yes', 'No'])
        if state == "Yes":
            cmds.file(save=True)
        elif state == "No":
            pass

        if os.path.isfile(absSourcePath):
            cmds.file(absSourcePath, o=True, force=True)

    def uniqueList(self, fList):
        keys = {}
        for e in fList:
            keys[e] = 1
        return keys.keys()





