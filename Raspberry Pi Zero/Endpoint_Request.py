import sys
import requests

def get_url(option):
    url_options = {
        "option1": "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=807b7c64-2e02-4292-a8b2-e3b303dbccb9&token=2d52cdf7-8e9b-4369-abf6-fffe11969d2e&response=xml",
        "option2": "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=19a96199-f790-4f71-9c8d-c93f464ca150&token=86f6ca0e-31db-4f49-8ae0-f20c1124c1ee&response=xml",
        "option3": "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=65316ded-ee46-44b7-80fa-633b36cb9944&token=74d98bd8-47ea-4d76-86d5-0763f1c57b8c&response=xml",
        "option4": "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=28e4468f-514d-441b-986f-b502306c5618&token=26d27fba-6730-40e4-8c56-2e4cdac91f69&response=xml",
        "option5": "https://example.com/option5",
        "option6": "https://example.com/option6",
        "option7": "https://example.com/option7",
        "option8": "https://example.com/option8",
        "option9": "https://example.com/option9",
        "option10": "https://example.com/option10",
    }
    return url_options.get(option)

def hit_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        if "URLRoutineTrigger" in json_data and "triggerActivationStatus" in json_data["URLRoutineTrigger"]:
            activation_status = json_data["URLRoutineTrigger"]["triggerActivationStatus"]
            if activation_status == "success":
                print("Trigger activation successful")
            else:
                print("Trigger activation failed with status:", activation_status)
        else:
            print("Invalid response format")
    else:
        print("Failed to hit the URL")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <option>")
        sys.exit(1)

    option = sys.argv[1]
    url = get_url(option)
    if url is None:
        print("Invalid option")
        sys.exit(1)

    hit_url(url)