#!/bin/bash
function cgrep()
{
	find . -type f \( -name '*.c' -o -name '*.cc' -o -name '*.cpp'  -o -name '*.h' -o -name '*.m' -o -name '*.mm'  \) -print0 | xargs -0 grep --color -n "$@"
}



function ergodic(){
for file in `ls $1`
do
	if [ -d $1"/"$file ]
	then
		ergodic $1"/"$file
	else
		#echo $1"/"$file >> b
		if  [[ $file == *.m ]];then
			filename=${file%%.m}
			lines=`cgrep -l $filename|wc -l` 
			if [[ $lines -lt 4 ]];then
				echo $lines
			    echo "classname:$filename" >>~/files.txt
				cgrep -l $filename >>~/files.txt
				echo "" >>~/files.txt
			fi
	    fi
	fi
done
}

echo "">~/files.txt
ergodic .
