#!/usr/bin/env python3
"""Icon generator for The IR Reading Room.
Pure-python PNG writer (no PIL): white page + old-school blue link bars on navy.
Supersampled 4x for smooth edges."""
import zlib, struct, os

BG = (10, 14, 60, 255)        # deep navy
PAGE = (255, 255, 255, 255)   # paper white
LINK = (0, 0, 238, 255)        # classic hyperlink blue #0000EE
GOLD = (212, 160, 23, 255)     # one warm accent line

def png_write(path, w, h, rgba_rows):
    def chunk(t, d):
        c = struct.pack(">I", len(d)) + t + d
        return c + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0)
    raw = b"".join(b"\x00" + bytes(row) for row in rgba_rows)
    with open(path, "wb") as f:
        f.write(sig + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))

def in_round_rect(px, py, x0, y0, x1, y1, r):
    """Point-in-rounded-rect test on supersampled canvas."""
    if px < x0 or px > x1 or py < y0 or py > y1:
        return False
    cx = min(max(px, x0 + r), x1 - r)
    cy = min(max(py, y0 + r), y1 - r)
    if (px < x0 + r or px > x1 - r) and (py < y0 + r or py > y1 - r):
        return (px - cx) ** 2 + (py - cy) ** 2 <= r * r
    return True

def draw_icon(size, path, maskable=False):
    S = 4
    W = size * S
    if maskable:
        # white page smaller, safe-zone padding for maskable
        page = (0.30 * W, 0.24 * W, 0.70 * W, 0.76 * W)
        bars_x0, bars_x1 = 0.36 * W, 0.64 * W
    else:
        page = (0.22 * W, 0.16 * W, 0.78 * W, 0.84 * W)
        bars_x0, bars_x1 = 0.30 * W, 0.70 * W
    px0, py0, px1, py1 = (int(v) for v in page)
    pr = int(0.04 * W)
    bh = int(0.035 * W)          # bar height
    br = bh // 2
    rows = []
    bar_ys = [py0 + int(0.16 * (py1 - py0)),
              py0 + int(0.34 * (py1 - py0)),
              py0 + int(0.52 * (py1 - py0))]
    short_y = py0 + int(0.70 * (py1 - py0))
    for y in range(W):
        row = bytearray()
        for x in range(W):
            c = BG
            if in_round_rect(x, y, px0, py0, px1, py1, pr):
                c = PAGE
                for by in bar_ys:
                    if in_round_rect(x, y, bars_x0, by, bars_x1, by + bh, br):
                        c = LINK
                        break
                if in_round_rect(x, y, bars_x0, short_y, bars_x0 + (bars_x1 - bars_x0) * 0.55, short_y + bh, br):
                    c = GOLD
            row += bytes(c)
        rows.append(row)
    # downsample Sx by averaging
    out = []
    for y in range(size):
        orow = bytearray()
        for x in range(size):
            r = g = b = a = 0
            for dy in range(S):
                p = rows[y * S + dy]
                for dx in range(S):
                    i = (x * S + dx) * 4
                    r += p[i]; g += p[i + 1]; b += p[i + 2]; a += p[i + 3]
            n = S * S
            orow += bytes((r // n, g // n, b // n, a // n))
        out.append(orow)
    png_write(path, size, size, out)

os.makedirs("icons", exist_ok=True)
draw_icon(512, "icons/icon-512.png")
draw_icon(192, "icons/icon-192.png")
draw_icon(512, "icons/maskable-512.png", maskable=True)
draw_icon(192, "icons/maskable-192.png", maskable=True)
draw_icon(180, "icons/apple-touch-icon.png")
draw_icon(64, "icons/favicon.png")
print("icons written")
