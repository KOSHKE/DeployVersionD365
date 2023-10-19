# DeployVersionD365
Application, which helps you to delete unecessarry extensions from D365 deployable package
# What programm does
1. It removes unselected extensions from deployable package folders 'AOSService/Packages' and 'AOSService/Packages/files' <br>
2. Removes unselected extensions from HotfixInstallationInfo.xml file
# How to configure
1. In layouts.py configure extensions setup for menu as it shown in the examples <br>
2. In setup.py configure extensions setup as it shown in the examples
# How to use
1. In 'Folder' select deployable package folder <br>
2. Select extensions you want to left in deployable package (unselected will be deleted) <br>
3. Run
