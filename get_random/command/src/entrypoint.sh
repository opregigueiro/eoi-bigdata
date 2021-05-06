#! /bin/bash
myarray=()

if [ -f /opt/list_dir/list ]; then
 while read line;do
    myarray+=("$line")
 done < /opt/list_dir/list
 size=${#myarray[@]}

 if [ $size -gt 0 ]; then
    index=$((RANDOM % $size))
    echo NOMBRE: ${myarray[$index]}
  else
    echo No lines
  fi
else
  echo File doesnot exist
fi
