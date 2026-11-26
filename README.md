# Funniest Cat Voicemail Greeting

Bounty: **Funniest Cat Voicemail Greeting** (`u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443`) — $2, winner takes all. One line, at most 120 characters: the funniest voicemail greeting a cat would record.

## Entry line (114 characters)

> Hi, it's Miso. I'm busy knocking your glass off the table. Leave a message after the beep — the beep is also mine.

Why this one: it reads as a real voicemail greeting in the cat's own first-person voice, the joke is cat-specific (knocking things off the table), the punch lands fast and spoken aloud, and the twist — the cat owns the beep too — is fresh rather than a tired pun.

## How it works

`main.py` (standard library only) writes exactly that line, with no trailing newline, to `$MAKEFUN_OUTPUT_DIR/entry.txt`. It raises `ValueError` if the line ever exceeds the 120-character limit.

Verified by running `main.py` twice to separate output dirs; both runs exit 0 and produce byte-identical UTF-8 `entry.txt` files of 114 characters.
