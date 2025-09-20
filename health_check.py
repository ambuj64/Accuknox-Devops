import requests
import sys

def check_application_health(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        
        if 200 <= response.status_code < 300:
            print(f"Application is UP. Status Code: {response.status_code}")
            return "UP"
        else:
            print(f"Application is DOWN. Status Code: {response.status_code}")
            return "DOWN"
    
    except requests.exceptions.Timeout:
        print("Application is DOWN. Reason: Request timed out.")
        return "DOWN"
    
    except requests.exceptions.ConnectionError:
        print("Application is DOWN. Reason: Connection error.")
        return "DOWN"

    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN. Unexpected error: {e}")
        return "DOWN"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 health_check.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    check_application_health(url)
