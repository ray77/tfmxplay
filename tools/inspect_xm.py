#!/usr/bin/env python3
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = sys.argv[1]
with open(path, 'rb') as f:
    data = f.read()

print(f'XM file size: {len(data)} bytes')
print(f'Module name: {data[17:37].decode("ascii", errors="replace").rstrip(chr(0))}')
song_len = int.from_bytes(data[64:66], 'little')
print(f'Song length (patterns in order): {song_len}')
restart_pos = int.from_bytes(data[66:68], 'little')
print(f'Restart position: {restart_pos}')
num_chans = int.from_bytes(data[68:70], 'little')
print(f'Channels: {num_chans}')
num_pats = int.from_bytes(data[70:72], 'little')
print(f'Patterns: {num_pats}')
num_insts = int.from_bytes(data[72:74], 'little')
print(f'Instruments: {num_insts}')
print(f'Order table: {list(data[80:80+song_len])}')
