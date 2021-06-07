import platform, os

if platform.system() != "Linux":
	print('Sorry! Installer is only available for linux system.')
	exit(0)
if os.getuid() != 0:
	print('Error! Pls Run It As Root!.')
	exit(0)

try:
	os.system('chmod 777 ip.py;mv ip.py trace; mv trace /usr/bin/;rm -rf ../xt')
	os.chdir('../')
	print('Installed Successfully!!')
	print('You can now run "trace" command anywhere in your terminal!.')
except:
	print('Err')
