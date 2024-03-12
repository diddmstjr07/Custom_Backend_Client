import subprocess
import re

def signal_get(URL, PORT):
    if re.match(r'^https://', URL):
        result = subprocess.run(["curl", "-X", "GET", URL + f":{PORT}"], capture_output=True, text=True)
        result = result.stdout
        result = re.sub(r'\s+$', '', result)
        if result == '':
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": None Correction URL")
            raise ConnectionRefusedError
        else:
            return result
    else:
        URL = "https://" + URL + f":{PORT}"
        result = subprocess.run(["curl", "-X", "GET", URL], capture_output=True, text=True)
        result = result.stdout
        result = re.sub(r'\s+$', '', result)
        if result == '':
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": None Correction URL")
            raise ConnectionRefusedError
        else:
            return result

def signal_post(URL):
    if re.match(r'^https://', URL):
        result = subprocess.run(["curl", "-X", "POST", URL], capture_output=True, text=True)
        result = result.stdout
        result = re.sub(r'\s+$', '', result)
        if result == '':
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": None Correction URL")
            raise ConnectionRefusedError
        else:
            return result
    else:
        URL = "https://" + URL
        result = subprocess.run(["curl", "-X", "POST", URL], capture_output=True, text=True)
        result = result.stdout
        result = re.sub(r'\s+$', '', result)
        if result == '':
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": None Correction URL")
            raise ConnectionRefusedError
        else:
            return result

def signal_put(URL, TYPE, JSON):
    if re.match(r'^https://', URL):
        if re.match(r'^\{.*\}$', JSON):
            result = subprocess.run(["curl", "-X", "PUT", "-H", TYPE, "-d", JSON, URL], capture_output=True, text=True)
            result = result.stdout
            result = re.sub(r'\s+$', '', result)
        else:
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": Data Form should be JSON")
            raise ValueError
        if result == '':
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": None Correction URL")
            raise ConnectionRefusedError
        else:
            return result
    else:
        if re.match(r'^\{.*\}$', JSON):
            result = subprocess.run(["curl", "-X", "PUT", "-H", TYPE, "-d", JSON, URL], capture_output=True, text=True)
            result = result.stdout
            result = re.sub(r'\s+$', '', result)
        else:
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": Data Form should be JSON")
            raise ValueError
        if result == '':
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": None Correction URL")
            raise ConnectionRefusedError
        else:
            return result

def signal_delete(URL):
    if re.match(r'^https://', URL):
        result = subprocess.run(["curl", "-X", "DELETE", URL], capture_output=True, text=True)
        result = result.stdout
        result = re.sub(r'\s+$', '', result)
        if result == '':
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": None Correction URL")
            raise ConnectionRefusedError
        else:
            return result
    else:
        result = subprocess.run(["curl", "-X", "DELETE", URL], capture_output=True, text=True)
        result = result.stdout
        result = re.sub(r'\s+$', '', result)
        if result == '':
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": None Correction URL")
            raise ConnectionRefusedError
        else:
            return result

def signal_head(URL):
    if re.match(r'^https://', URL):
        result = subprocess.run(["curl", "-I", URL], capture_output=True, text=True)
        result = result.stdout
        result = re.sub(r'\s+$', '', result)
        if result == '':
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": None Correction URL")
            raise ConnectionRefusedError
        else:
            return result
    else:
        result = subprocess.run(["curl", "-I", URL], capture_output=True, text=True)
        result = result.stdout
        result = re.sub(r'\s+$', '', result)
        if result == '':
            print("\033[1m\033[91m" + "ERROR" + "\033[0m" + ": None Correction URL")
            raise ConnectionRefusedError
        else:
            return result