
print("===============================================================================================================================================")
print("   _____                           _________      .__  _____  _____                     __________                __                      .__")
print("  /  _  \_____________            /   _____/ ____ |__|/ ____\/ ____\___________         \______   \_______  _____/  |_  ____   ____  ____ |  |")
print(" /  /_\  \_  __ \____ \   ______  \_____  \ /    \|  \   __\   __\/ __ \_  __ \  ______ |     ___/\_  __ \ /  _  \   _\/  _ \_/ ___\/  _ \|  |")
print("/    |    \  | \/  |_> > /_____/  /        \   |  \  ||  |   |  | \  ___/|  | \/ /_____/ |    |     |  | \(  <_> )  | (  <_> )  \__(  <_> )  |")
print("\____|__  /__|  |   __/          /_______  /___|  /__||__|   |__|  \___  >__|            |____|     |__|   \____/|__|  \____/ \___  >____/|____/")
print("        \/      |__|                     \/     \/                     \/                                                         \/")
print("================================================================================================================================================")

from scapy.all import ARP, sniff, wrpcap
def sniffer_packet(packet):
    if(packet[ARP].op == 1):
      print("pedido: do endereco {} para o endereco {}".format(
          packet[ARP].psrc, packet[ARP].pdst
      ))
    elif(packet[ARP].op == 2):
      print("resposta: do mac {} para o endereco {}".format(
          packet[ARP].hwsrc,packet[ARP].pdst
      ))
    print(packet.show())
data = sniff(filter='arp', prn=sniffer_packet, count=10)
wrpcap('data_sniffed.pcap', data)
