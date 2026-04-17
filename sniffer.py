from scapy.all import sniff, IP, TCP, UDP, ICMP, get_if_list

# show available interfaces
interfaces = get_if_list()

print("Available interfaces:")
for iface in interfaces:
    print("-", iface)

# user selects interface
selected_interface = input("\nEnter interface to sniff on: ")

packet_count = 0


def process_packet(packet):

    global packet_count
    packet_count += 1

    if packet.haslayer(IP):

        ip_layer = packet[IP]

        print("\nPacket Number:", packet_count)
        print("Source IP:", ip_layer.src)
        print("Destination IP:", ip_layer.dst)

        if packet.haslayer(TCP):
            print("Protocol: TCP")

        elif packet.haslayer(UDP):
            print("Protocol: UDP")

        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")

        else:
            print("Protocol: Other")

        payload = bytes(packet.payload)

        print("Payload Preview:", payload[:20])
        print("--------------------------")


sniff(iface=selected_interface, prn=process_packet)
