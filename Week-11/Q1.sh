echo "Enter the filename (with path if not in current directory):"
read filename

if [ -e "$filename" ]; then
    echo "The file '$filename' exists."
else
    echo "The file '$filename' does not exist."
fi