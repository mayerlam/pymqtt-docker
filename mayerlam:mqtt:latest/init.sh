DIR=/mqtt_main/data
FILE=$DIR/connector.py

# echo "alias 'run'='sh /run.sh'" >> /etc/bash.bashrc 
# source /etc/bash.bashrc 

if [ -d "$DIR" ]; then
    echo "$DIR exists."
else 
    mkdir -p $DIR
fi

if [ -f "$FILE" ]; then
    echo "$FILE exists."
    python $FILE
else 
    cp /etc/tmp/template.py $DIR/$FILE
    /bin/bash
fi





