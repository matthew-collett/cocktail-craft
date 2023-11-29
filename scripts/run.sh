#!/bin/bash
# scripts/run.sh
command_exists () {
  type "$1" &> /dev/null ;
}

python_command="python"
pip_command="pip"

if command_exists python3 ; then
  echo "Python 3 is installed."
  python_command="python3"
  if command_exists pip3 ; then
    echo "pip3 is installed."
    pip_command="pip3"
  else
    echo "pip3 not found, trying pip..."
    if command_exists pip ; then
      echo "pip is installed."
    else
      echo "Neither pip nor pip3 is installed."
      echo "To install pip, visit https://pip.pypa.io/en/stable/installing/ or use your operating system's package manager."
      exit 1
    fi
  fi
elif command_exists python ; then
  echo "Python is installed."
  if command_exists pip ; then
    echo "pip is installed."
  else
      echo "pip not found, trying pip3..."
      if command_exists pip3 ; then
        echo "pip3 is installed."
        pip_command="pip3"
      else
        echo "Neither pip nor pip3 is installed."
        echo "To install pip, visit https://pip.pypa.io/en/stable/installing/ or use your operating system's package manager."
        exit 1
      fi
  fi
else
  echo "Neither Python nor Python3 is installed."
  echo "To install Python, visit https://www.python.org/downloads/ or use your operating system's package manager."
  exit 1
fi

echo "Installing dependencies from requirements.txt using $pip_command..."
$pip_command install -r requirements.txt

if [ $? -eq 0 ]; then
  echo "Successfully installed dependencies."
else
  echo "Failed to install dependencies."
  exit 1
fi

echo "Starting Flask application..."
flask --app run run
