"""How much of your Claude Code reading is cached? (CC0, Heartbeat Observatory)
Usage: python claude_cache_share.py [YYYY-MM-DD]   (default: today; reads ~/.claude/projects/**/*.jsonl)
Prints turns, fresh input, cache writes, cache reads, output, and the cached share of input."""
import json, sys, glob, os, datetime
day = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
k = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")
t = dict.fromkeys(k, 0); n = 0
for f in glob.glob(os.path.expanduser("~/.claude/projects/**/*.jsonl"), recursive=True):
    for line in open(f, encoding="utf-8", errors="ignore"):
        try: d = json.loads(line)
        except ValueError: continue
        u = (d.get("message") or {}).get("usage") if str(d.get("timestamp", "")).startswith(day) else None
        if u:
            n += 1
            for x in k: t[x] += u.get(x) or 0
inp = t["input_tokens"] + t["cache_creation_input_tokens"] + t["cache_read_input_tokens"]
print(f"{day}: {n:,} turns")
for x in k: print(f"  {x}: {t[x]:,}")
print(f"  cached share of input: {100 * t['cache_read_input_tokens'] / max(inp, 1):.1f}%")
