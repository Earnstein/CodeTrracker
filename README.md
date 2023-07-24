# Coding Tracker CLI

This is a command-line tool that allows you to track your daily coding progress on Pixela, a pixel-based habit-tracking platform. The CLI provides functionality to create a user account, create a graph, add pixels to the graph, and delete a graph.

## Requirements

- Python 3.x
- `requests` library

## Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/coding-tracker-cli.git

pip install requests

```
## Usage

## Create User Account
To create a new user account, run the following command, run the following in a bash or powershell:
```bash 
bash:
./main.py create_user --username YOUR_USERNAME --token YOUR_TOKEN

powershell:
python main.py create_user --username YOUR_USERNAME --token YOUR_TOKEN

``` 
## Create Tracker Graph
To create a new tracker graph, run the following command:

```bash 
bash:
./main.py create_graph --username YOUR_USERNAME --token YOUR_TOKEN --graph_id YOUR_GRAPH_ID


powershell:
python main.py create_graph --username YOUR_USERNAME --token YOUR_TOKEN --graph_id YOUR_GRAPH_ID

```

## Add a Pixel

To add a pixel to the tracker graph, run the following command:

```bash 
bash:
./main.py add_pixel --username YOUR_USERNAME --token YOUR_TOKEN --graph_id YOUR_GRAPH_ID --quantity QUANTITY --date YYYY-MM-DD


powershell:
python main.py add_pixel --username YOUR_USERNAME --token YOUR_TOKEN --graph_id YOUR_GRAPH_ID --quantity QUANTITY --date YYYY-MM-DD

```
Note: The --date argument is optional. If not provided, the current date will be used.

## Delete Tracker Graph

To delete a tracker graph, run the following command:

```bash 
bash:
./main.py delete_graph --username YOUR_USERNAME --token YOUR_TOKEN --graph_id YOUR_GRAPH_ID


powershell:
python main.py --username YOUR_USERNAME --token YOUR_TOKEN --graph_id YOUR_GRAPH_ID

```

## License

This project is licensed under the MIT License - see the LICENSE file for details



