# CodeAlpha Network Sniffer

## Project Overview

This project is a simple Network Sniffer built using Python and Scapy as part of the CodeAlpha Cyber Security Internship.

The tool captures live network packets and displays important information such as:

- Source IP Address
- Destination IP Address
- Protocol Type (TCP / UDP / ICMP)
- Packet Payload Preview
- Packet Counter
- Dynamic Interface Selection

This helps in understanding how network traffic flows and how packet analysis works in real-world cybersecurity environments.

---

## Features

✔ Capture live network packets  
✔ Display Source IP and Destination IP  
✔ Detect Protocol Type (TCP / UDP / ICMP / Or any other Protocol)  
✔ Show Payload Preview (first 20 bytes)  
✔ Packet Counter  
✔ Dynamic Network Interface Selection  

---

## Technologies Used

- Python
- Scapy Library
- Kali Linux

---

## How to Run the Project

Step 1:
  
   - write this in the terminal >>> sudo python3 sniffer.py
     
       . Just to run the program

Step 2:

   - Select network interface when prompted (eth0 / lo / ... )

Step 3:
  
   - Open other terminal and generate a traffic
        
        . ping google.com 
        . ping facebook.com
        . ping x.com
        . ping (a usable IP)


Packets will appear in real time.

---

## Learning Outcome

Through this project I learned:

- How packet sniffing works
- Basics of network traffic analysis
- How to extract IP layer information
- How to detect protocols
- How cybersecurity analysts monitor network traffic

---

## Author

Mazen Mahmoud Roshdy 

Cyber Security Student

Faculty of computers and data science

Alexandria University , Egypt
