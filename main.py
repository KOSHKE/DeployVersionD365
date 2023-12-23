import PySimpleGUI
import layouts
import controller

window = PySimpleGUI.Window('Deploy Version D365',
                            layouts.get_layout('MainWindow'))

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event in ('Cancel'):
        window.close()
    if event in ('Submit'):
        result = controller.run_operation(values['-FOLDER-'], values)
        if result is True:
            window = PySimpleGUI.Window('Done',
                                        layouts.get_layout('ErrorWindow',
                                                          'Done'))
            window.read()
