from scapy.all import *

def scan_network(ip_range):
    # Create an ICMP Echo Request packet
    packet = IP(dst=ip_range)/ICMP()
    
    # Send the packet and wait for the response
    response = sr1(packet, timeout=2, verbose=0)
    
    if response:
        print(f"Host {ip_range} is up.")
    else:
        print(f"Host {ip_range} is down.")

if __name__ == "__main__":
    # Define the IP range to scan
    # You can replace this with a specific IP or range
    ip_range = "192.168.1.1"  # Replace with your target IP or range
    
    # Run the scan
    scan_network(ip_range)
