import numpy as np
import pandas as pd

path = r""

with open(path, 'r') as f:
    lines = f.readlines()

lines = [line.replace(' ', ',') for line in lines]


with open(path, 'w') as f:
    f.write("event,time,from_node,to_node,pkt_type,pkt_size,flags,fid,src_addr,dst_addr,seq,pkt_id \n")
    f.writelines(lines)
    
df = pd.read_csv(path)

total_packet_size = 0
r40_counter = 0
r1040_counter = 0
plus_counter = 0
minus_counter = 0
total_time_taken = df.iloc[-1]['time']

for _ in range(len(df)):
    if df.iloc[_]['event'] == 'r':
        #total_packet_size += df.iloc[_]['pkt_size']
        if df.iloc[_]['pkt_size'] == 40:
            r40_counter += 1
        if df.iloc[_]['pkt_size'] == 1040:
            r1040_counter += 1
            
    if df.iloc[_]['event'] == '+':
        plus_counter += 1
        
    if df.iloc[_]['event'] == '-':
        minus_counter += 1
  

total_packet_size = int(r40_counter)*40 + int(r1040_counter)*1040
throughput = total_packet_size / total_time_taken
delivery_ratio = (r40_counter+r1040_counter) / len(df)
print(f"Throughput: {throughput} Bytes/Second")
print(f"Delivery Ratio: {delivery_ratio}")