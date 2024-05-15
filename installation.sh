#!/bin/bash

# Make the launcher script executable
chmod +x installation.sh

# Give all permissions to the launcher script
chmod 755 installation.sh

# Check and install Python3 if not already installed
if ! command -v python3 &> /dev/null; then
    echo "Installing Python3..."
    sudo apt-get update
    sudo apt-get install -y python3
    echo "Python3 installed successfully."
else
    echo "Python3 is already installed in the system."
fi

# Check and install SSH if not already installed
if ! command -v sshd &> /dev/null; then
    echo "Installing SSH..."
    sudo apt-get update
    sudo apt-get install -y openssh-server
    sudo systemctl start ssh
    sudo systemctl enable ssh
    echo "SSH installed and activated successfully."
else
    echo "SSH is already installed in the system."
fi

# Check if MongoDB is installed
if ! command -v mongo &> /dev/null; then
    echo "Installing MongoDB..."
    sudo apt-get update
    sudo apt-get install -y mongodb
    echo "MongoDB installed successfully."
else
    echo "MongoDB is already installed in the system."
fi

# Check if MongoDB host and port are configured correctly
expected_host="127.0.0.1"
expected_port="27017"

current_host=$(mongo --quiet --eval "printjson(db.serverStatus().host)" | cut -d':' -f1)
current_port=$(mongo --quiet --eval "printjson(db.serverStatus().host)" | cut -d':' -f2)

if [ "$current_host" != "$expected_host" ] || [ "$current_port" != "$expected_port" ]; then
    echo "Adjusting MongoDB host and port..."
    sudo sed -i "s|127.0.0.1:27017|$expected_host:$expected_port|g" /etc/mongod.conf
    sudo systemctl restart mongod
    echo "MongoDB host and port adjusted successfully."
else
    echo "MongoDB host and port are already configured correctly."
fi

# List of Python libraries to check and install if not already installed
python_libraries=("requests" "beautifulsoup4" "pymongo" "random" "pandas")

for lib in "${python_libraries[@]}"; do
    if ! python3 -c "import $lib" &> /dev/null; then
        echo "Installing $lib..."
        sudo apt-get update
        sudo apt-get install -y python3-pip
        sudo pip3 install $lib
        echo "$lib installed successfully."
    else
        echo "$lib is already installed."
    fi
done

# Python files to scrap all data needed
python_files=("pokemonNames.py" "pokemonSkills.py" "pokeTypes.py" "typeEffect.py" "pokemonImg.py")

# Execute each Python file sequentially
for file in "${python_files[@]}"; do
    if [ -f "$file" ]; then
        echo "Executing $file..."
        python3 "$file"
        echo "$file execution completed."
    else
        echo "$file not found."
    fi
done


