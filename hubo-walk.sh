
MakeAch()
{
	ach -1 -C hubo-walking -m 10 -n 3000
	sudo chmod 777 /dev/shm/achshm-hubo-*
}

Start()
{

	sudo python walkHuboAchInterface.py
}

case "$1" in 
	'remote')
		MakeAch
		achd -r push $2 hubo-walking &
	;;

	'makeach')
		MakeAch
	;;

	'start')
		MakeAch
		Start
	;;
	*)
		echo 'Hubo-Walking: Daniel M. Lofaro <dan@danLofaro.com>'
		echo '--------------------------------------------------'
		echo ' '
		echo 'Options:'
		echo '  start                  : Walking Interface'
		echo '  makeach                : Make the ach channels'
		echo '  remote xxx.xxx.xxx.xxx : create remote connection'
	;;
esac
