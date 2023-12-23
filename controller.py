import os
import PySimpleGUI
import layouts
import setup
from xml.etree import ElementTree as ET


def run_operation(path: str, parameters):
    # Check path is defined
    if (path == ''):
        window = PySimpleGUI.Window('Path is not defined',
                                    layouts.get_layout('ErrorWindow', 'Path is not defined'),
                                    background_color='red')
        window.read()
        return False

    # Delete files (base path + AOSService/Packages/files)
    delete_files(path + '//AOSService//Packages//files', parameters)
    # Delete packages (base path + AOSService/Packages)
    delete_files(path + '//AOSService//Packages', parameters)
    # Update HotfixInstallationInfo.xml (base path)
    process_hotfixinstallationinfo(path + '/HotfixInstallationInfo.xml',
                                  parameters)
    return True


def check_and_remove_node_with_value(elem, value, node, parametersValue):
    if value.text.startswith(parametersValue):
        elem.remove(node)


def check_and_remove_node(elem, node, parametersValue):
    if node.text.startswith(parametersValue):
        elem.remove(node)


def check_and_remove_file(os, file, parametersValue):
    if file.startswith(parametersValue):
        os.remove(file)


def process_hotfixinstallationinfo(path: str, parameters):
    file = ET.parse(path)
    root = file.getroot()
    # Process first MetadataModuleList
    for elem in root.findall('MetadataModuleList'):
        for node in elem.findall('string'):
            for key in parameters.keys():
                if parameters[key] is False:
                    check_and_remove_node(elem, node, setup.xmlDict[key])

    # Process AllComponentList
    for elem in root.findall('AllComponentList'):
        for node in elem.findall('ArrayOfString'):
            for value in node.findall('string'):
                for key in parameters.keys():
                    if parameters[key] is False:
                        check_and_remove_node_with_value(elem, value, node, setup.xmlDict[key])

    file.write(path)


def delete_files(path: str, parameters):
    os.chdir(path)
    for root, dirs, files in os.walk(path):
        for file in files:
            for key in parameters.keys():
                if parameters[key] is False:
                    check_and_remove_file(os, file, setup.filesDict[key])
