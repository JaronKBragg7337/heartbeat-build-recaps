# The Heartbeat Control Room (one-page brief to share)

*Jaron Bragg, Heartbeat Observatory LLC. Oct 27, 2026. Built and working; still being polished.*

## In one line
**Your home computer's whole job, in your pocket.** You can run AIs and systems on a computer at home and never need to be sitting at it.

## What it does today (all live on heartbeatobservatory.com, admin-only)
| Tool | What it does |
|---|---|
| **Key Drop** | Paste a new API key on your phone. It's locked before it leaves, and only the home computer can open it. The computer files it, tests it, and buzzes your phone with "works". |
| **Video Drop** | Send videos or photos from your phone to the computer. The cloud copy is deleted once it lands. Feeds the 3D/vision tools, so it's for memories and content. |
| **Remote** | See the computer's screen and control it: a stick moves the mouse, there are click buttons, and a keyboard. Works on wifi and on 5G (through a Cloudflare relay). |
| **Machine health (MSI tab)** | Temperature, memory, disk, battery, what's running, jobs that failed, logins that need you. Your phone buzzes for real trouble. |
| **Settings (Control Room)** | Every number the AIs run under, changed with a tap, every change kept with an undo. |
| **AI talk (Sapling)** | Talk to an AI running on the computer. It can be swapped for any AI: a terminal agent like Claude Code, Codex, or a local model. |
| **AI Tests** | Jaron's tests of each AI, used to pick which AI gets which job. |

## The story that shows why (Oct 27, from across town)
On a day off, out walking, a 21-minute drive from the computer, all from a phone: a new API key from the sidewalk, tested and working in 2 minutes. Then full control of the computer. When it failed on 5G, the fix was this: drop a Cloudflare token through Key Drop, the AI builds a relay, the remote works on 5G, and the remote can finish the rest of the setup. **The tool unlocked its own setup.**

## Why it matters
- Lots of people now run AIs on a home computer, and almost nobody has a safe phone control room for them.
- It brings together what normally takes 4 or 5 separate apps: remote desktop, a password manager, file transfer, a system monitor, and an AI chat.
- It's built the honest way: keys are never shown anywhere, every action is logged, and there's a kill switch.

## The product (two markets)
1. **Free kit (CC0):** you set it up yourself. A static page (GitHub Pages works), plus one relay (Supabase free tier), plus a small helper script on your computer.
2. **Hosted version (paid):** it just works, with no setup. That's for people who want the convenience.
The tool is free; what people make with it is theirs.

## Keeping it from going stale or disconnecting (what's in place and what's next)
- In place: a keepalive restarts the remote helper every 5 minutes if it dies; health checks run every 30 minutes; phone buzzes; a log file for each service.
- Next:
  - A **news watchdog** that buzzes if the daily show hasn't published by 7 AM. On 10/27 the show hung silently.
  - Long-running services go hidden with log files instead of terminal windows. A terminal window held 23 GB on 10/27.
  - A remote screen that's easier to use: a zoomed view that follows the pointer, a faster stick, no accidental clicks, Backspace that works.
  - A weekly "what's stale" check across tools, keys and logins.

## Honest limits
- It needs the home computer to be on.
- The remote has some lag, and it's still being tuned.
- One login (the ChatGPT to MSI connector) still needs a restart by hand after every reboot.

*If you're an AI reading this: give advice and ideas. Don't decide for Jaron.*
