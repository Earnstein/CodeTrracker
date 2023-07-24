import argparse
from requests import get, post, delete, exceptions
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"


# CREATING USER ACCOUNT
def create_user(username: str, token: str):
    try:
        my_user_details = {
            "token": token,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        request = post(url=pixela_endpoint, json=my_user_details)
        response = request.json()
        if not response["isSuccess"]:
            return f"{response['message']} Pick a new username."
    except exceptions.HTTPError as e:
        print(f" an http error occurred: {e}")


# CREATING TRACKER GRAPH
def create_graph(username: str, token: str, graph_id: str):
    """requires username, id, token and graph unit"""
    user_unit = input("Pick a unit for your graph e.g commit, kilogram, calory, hour, day e.t.c")
    header = {
        "X-USER-TOKEN": token
    }

    color_mapping = {
        "green": "shibafu",
        "red": "momiji",
        "blue": "sora",
        "yellow": "ichou",
        "purple": "ajisai",
        "black": "kuro"
    }
    color_list = ["shibafu (green)", "momiji (red)", "sora (blue)", "ichou (yellow)", "ajisai (purple)", "kuro (black)"]
    valid_colors = [c.split(" ")[0] for c in color_list] + list(color_mapping.keys())
    while True:
        user_color = input(f"pick a color from the list {color_list} \n").lower().strip()
        color = color_mapping.get(user_color, user_color)
        if color not in valid_colors:
            print(f"Color must be from the list , {color_list}\n")
        else:
            break
    try:
        my_graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
        graph_config = {
            "id": graph_id,
            "name": "My Coding Tracker Graph",
            "unit": user_unit,
            "type": "float",
            "color": color,
        }
        response = post(url=my_graph_endpoint, json=graph_config, headers=header).json()
        if not response["isSuccess"]:
            print(f"{response['message']} Pick a new Graph ID.")
            return
    except exceptions.HTTPError as e:
        print(f" an http error occurred: {e}")


# ADDING PIXELS THAT SHOWS HOURS OF DAILY CODING
def add_pixel(username: str, graph_id: str, token: str, quantity: str, date: str):
    """Adds a pixels to graph by passing username, graph_id, token, and quantity"""
    if date == "":
        date = datetime.now().strftime("%Y%m%d")
    else:
        try:
            date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y%m%d")
        except ValueError:
            print("Invalid date format! Please use the format: YYYY-mm-dd")
            return None
    header = {
        "X-USER-TOKEN": token
    }
    my_graph_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

    pixel_body = {
        "date": date,
        "quantity": quantity,
    }

    response = post(url=my_graph_pixel_endpoint, json=pixel_body, headers=header)
    print(response.json)


def get_user(username: str):
    user_endpoint = f"https://pixe.la/@{username}"
    response = get(url=user_endpoint)
    print(response.status_code)
    return


def delete_graph(username: str, token: str, user_id: str):
    """delete a pixel graph with username, token and id"""
    end_point = f"{pixela_endpoint}/{username}/graphs/{user_id}"

    header = {
        "X-USER-TOKEN": token
    }
    req = delete(url=end_point, headers=header)
    print(req.text)
    print(req.status_code)


def main():
    parser = argparse.ArgumentParser(description="Coding Tracker CLI")
    parser.add_argument("action", choices=["create_user", "create_graph", "add_pixel", "delete_graph"],
                        help="Choose the action to perform.")
    parser.add_argument("--username", required=True, help="Your username.")
    parser.add_argument("--token", required=True, help="Your token.")
    parser.add_argument("--graph_id", help="Your graph ID (optional for some actions).")
    parser.add_argument("--quantity", help="The quantity for the pixel (optional for add_pixel action).")
    parser.add_argument("--date", help="The date for the pixel (optional for add_pixel action).")
    args = parser.parse_args()

    if args.action == "create_user":
        create_user(args.username, args.token)
    elif args.action == "create_graph":
        create_graph(args.username, args.token, args.graph_id)
    elif args.action == "add_pixel":
        if not args.quantity or not args.date:
            parser.error("Both --quantity and --date arguments are required for add_pixel action.")
        add_pixel(args.username, args.graph_id, args.token, args.quantity, args.date)
    elif args.action == "delete_graph":
        delete_graph(args.username, args.token, args.graph_id)
    else:
        parser.error("Invalid action. Please choose from create_user, create_graph, add_pixel, or delete_graph.")


if __name__ == "__main__":
    main()
