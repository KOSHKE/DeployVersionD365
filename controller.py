import os
import PySimpleGUI
import layouts
import setup
from xml.etree import ElementTree as ET


def runOperation(path: str, parameters):
    # Check path is defined
    if (path == ''):
        window = PySimpleGUI.Window('Path is not defined',
                                    layouts.getLayout('ErrorWindow', 'Path is not defined'),
                                    background_color='red')
        window.read()
        return False

    # Delete files (base path + AOSService/Packages/files)
    deleteFiles(path + '//AOSService//Packages//files', parameters)
    # Delete packages (base path + AOSService/Packages)
    deleteFiles(path + '//AOSService//Packages', parameters)
    # Update HotfixInstallationInfo.xml (base path)
    processHotfixInstallationInfo(path + '/HotfixInstallationInfo.xml',
                                  parameters)
    return True


def checkAndRemoveNodeWithValue(elem, value, node, parametersValue):
    if value.text.startswith(parametersValue):
        elem.remove(node)


def checkAndRemoveNode(elem, node, parametersValue):
    if node.text.startswith(parametersValue):
        elem.remove(node)


def checkAndRemoveFile(os, file, parametersValue):
    if file.startswith(parametersValue):
        os.remove(file)


def processHotfixInstallationInfo(path: str, parameters):
    file = ET.parse(path)
    root = file.getroot()
    # Process first MetadataModuleList
    for elem in root.findall('MetadataModuleList'):
        for node in elem.findall('string'):
            for key in parameters.keys():
                if (if parameters[key] is False):
                    checkAndRemoveNode(elem, node, setup.xmlDict[key])

    # Process AllComponentList
    for elem in root.findall('AllComponentList'):
        for node in elem.findall('ArrayOfString'):
            for value in node.findall('string'):
                for key in parameters.keys():
                    if (if parameters[key] is False):
                        checkAndRemoveNodeWithValue(elem, value, node, setup.xmlDict[key])

    file.write(path)


def deleteFiles(path: str, parameters):
    os.chdir(path)
    for root, dirs, files in os.walk(path):
        for file in files:
            for key in parameters.keys():
                if (if parameters[key] is False):
                    checkAndRemoveFile(os, file, setup.filesDict[key])
