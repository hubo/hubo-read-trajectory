case "$1" in
	'forward' )
		./hubo-read-trajectory -s -f 200 -n walking_traj/walk1sZp05m.traj
		exit 0
	;;

	'forward5' )
		./hubo-read-trajectory -s -f 200 -n walking_traj/walk5sZp05m.traj
		exit 0
	;;

	'turn' )
		./hubo-read-trajectory -s -f 200 -w $2 -n walking_traj/walk1sTurnBase0m.traj
		exit 0
	;;
	
	'walkready' )
		./hubo-read-trajectory -s -f 200 -n walking_traj/walkReady.traj
	;;

	'home' )
		./hubo-read-trajectory -s -f 200 -n walking_traj/home.traj
	;;

	*)
		echo 'No command given'
		exit 1
	;;
esac
