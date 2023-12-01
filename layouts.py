import PySimpleGUI

NAME_SIZE = 23


def name(name):
    dots = NAME_SIZE - len(name) - 2
    return PySimpleGUI.Text(name + ' ' +
                            '•' * dots,
                            size=(NAME_SIZE, 1), justification='r',
                            pad=(0, 0), font='Courier 10')


def getLayout(form: str, value: str = ''):
    match form:
        case 'MainWindow':
            layout = [
                        [PySimpleGUI.Text('Folder'), PySimpleGUI.InputText(key='-FOLDER-'), PySimpleGUI.FolderBrowse()],
                        [PySimpleGUI.T('Extensions Setup: (Select which is needed, others will be deleted)')],
                        [name('SomeExtension'), PySimpleGUI.Checkbox('', key='-Ext-'),
                         name('SomeExtension1'), PySimpleGUI.Checkbox('', key='-Ext1-'),
                         name('SomeExtension2'), PySimpleGUI.Checkbox('', key='-Ext2-')],
                        [name('SomeExtension3'), PySimpleGUI.Checkbox('', key='-Ext3-'),
                         name('SomeExtension4'), PySimpleGUI.Checkbox('', key='-Ext4-'),
                         name('SomeExtension5'), PySimpleGUI.Checkbox('', key='-Ext5-')],
                        [PySimpleGUI.Submit(), PySimpleGUI.Cancel()]
                     ]
        case 'ErrorWindow':
            layout = [
                        [PySimpleGUI.T(value)]
                     ]

    return layout
