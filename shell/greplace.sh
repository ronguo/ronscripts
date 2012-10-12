
#replace content in source files
function cgrep()
{
	find . -type f \( -name '*.c' -o -name '*.cc' -o -name '*.cpp'  -o -name '*.h' -o -name '*.m' -o -name '*.mm'  \) -print0 | xargs -0 grep --color -n "$@"
}

strfrom=$1
strto=$2
cgrep -l $1 |xargs perl -pi -e "s/$1/$2/g"
