greet() {
    echo "Hello, $1! Welcome to the shell script tutorial."
}

echo "Enter your name:"
read name
greet "$name"