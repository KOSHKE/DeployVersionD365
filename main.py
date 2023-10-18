import PySimpleGUI
import layouts
import controller

window = PySimpleGUI.Window('Deploy Version D365', layouts.getLayout('MainWindow'))

while True:                           
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event in ('Cancel'):
        window.close()
    if event in ('Submit'):
        result = controller.runOperation(values['-FOLDER-'], values)
        if (result == True):
            window = PySimpleGUI.Window('Done', layouts.getLayout('ErrorWindow', 'Done'))
            window.read()