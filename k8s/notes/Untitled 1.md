docker ps -a  | awk -F ' ' '{print $1}' | grep -v CON | xargs docker rm



批量停容器



docker ps   | awk -F ' ' '{print $1}' | grep -v CON | xargs docker stop