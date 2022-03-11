#!/bin/bash

TARGET_DIR="./target"
CONTENT_DIR="$TARGET_DIR/content"
RUNNER_DIR="./presentation_runner"
LECTURES_DIR="./lecture"
ASSIGNMENTS_DIR="./assignment"
UITWERKINGEN_DIR="./uitwerkingen"

if [ ! -d "$TARGET_DIR" ]; then
    echo "creating target directory: $TARGET_DIR";
    mkdir $TARGET_DIR;
fi

if [ ! -d "$CONTENT_DIR" ]; then
    echo "creating content directory: $CONTENT_DIR";
    mkdir $CONTENT_DIR;
fi

if [ -d "$RUNNER_DIR" ]; then
    echo "Copying reveal presentation runner";
    cp -r $RUNNER_DIR/* $CONTENT_DIR ;
else
    echo $RUNNER_DIR " directory does not exist";
fi

if [ -d "$LECTURES_DIR" ]; then
    echo "Copying lectures";
    cp -r $LECTURES_DIR $CONTENT_DIR ;
else
    echo $LECTURES_DIR " directory does not exist";
fi

for FILENAME in $LECTURES_DIR/*/*.md; do
    BASENAME=$(basename $FILENAME .md)
    CONTENT_FILENAME=${FILENAME#./lectures/}
    echo "Creating HTML file for lecture " $BASENAME "(" $FILENAME "->" $CONTENT_FILENAME ")"
    sed "s:presentatie.md:$CONTENT_FILENAME:g" $CONTENT_DIR/index.html > $CONTENT_DIR/lecture-1-$BASENAME.html
done

if [ -d "$ASSIGNMENTS_DIR" ]; then
    echo "Copying assignments general content";
    FILENAME=$ASSIGNMENTS_DIR/index.md
    cp $FILENAME "$ASSIGNMENTS_CONTENT_DIR" ;
    BASENAME=$(basename $FILENAME .md)
    echo "Creating HTML file for index " $BASENAME "(" $FILENAME  ")"
    pandoc -c ./css/assignment.css $FILENAME -f markdown -t html -s -o $CONTENT_DIR/$BASENAME.html
else
    echo $ASSIGNMENTS_DIR " directory does not exist";
fi


