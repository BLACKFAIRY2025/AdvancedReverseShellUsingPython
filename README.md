# Reverse Shell To Run Commands

This script sets up a basic reverse shell listener in Python. It's meant for educational and research purposes only — use responsibly.

## What it Does

* Listens for incoming connections from a reverse shell client
* Sends commands from the listener (your system) to the connected target
* Receives and displays the output of those commands from the target
* Gracefully handles connection and communication errors

---

## How to Use

1. **Set up your listener machine:**

   Make sure you're on the same network (e.g., 192.168.x.x) as the target or you have proper port forwarding for external connections.

2. **Edit the IP address:**

   In the `server()` function, change:

   ```python
   s.bind(("192.168.0.1", 4444))
   ```

   Replace `"192.168.0.1"` with your listener machine’s local IP address.

3. **Run the script:**

   ```bash
   python listener.py
   ```

   It’ll start listening for incoming connections on port 4444.

4. **Connect from the client:**

   The target (reverse shell client) should connect back to your IP and port.

5. **Send commands:**

   Once the connection is established, you can type commands and get their output from the target machine.

   Type `q` to quit the shell.

---

## Example Output

```
Listening to incoming connections...
Connection established with: ('192.168.0.8', 51234)
Command: whoami
target_user
Command: ipconfig
Windows IP Configuration ...
Command: q
```

---
