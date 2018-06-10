if (( $# -ne 1 )); then
    echo "Usage: copy.sh FILEPATH"
    exit 1
fi


copy ./* $1
