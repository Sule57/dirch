# Dirch by Sule57

Dirch is a simple python script that will take the provided (or not) wordlist and test if a directory named the same as any of the words in the words inside the provided wordlist exists on the provided website.

The usage is designed to be quite simple (plug and play).
No unnecessary libraries used that require you to install stuff, just clone the repository and run the script as described below.

The project was created to remember python and to have a tool that I can make how I like it, but please if you have any ideas for implementations, don't hesitate.

### Triggers

* **-u | --url** - Specify the target URL
* **-w | --wordlist** - Specify the Wordlist to use (by default common.txt)
* **-d | --delay** - Specify the delay between requests

## How to use

### Without a custom wordlist

```
python3 dirch.py -u https://susic-security.com


-------------------------------------------------------------
Welcome to dirch.py - A directory discovery tool
Created by github.com/sule57
-------------------------------------------------------------
No wordlist passed, using common.txt by Marc Rivero López: 
-------------------------------------------------------------

[Info] Found: https://susic-security.com/  |  200  |  OK  |
```

### With a custom wordlist

```
python3 dirch.py -u https://susic-security.com -w custom.txt


-------------------------------------------------------------
Welcome to dirch.py - A directory discovery tool
Created by github.com/sule57
-------------------------------------------------------------
Using wordlist: custom.txt
-------------------------------------------------------------

[Info] Found: https://susic-security.com/posts  |  200  |  OK  |
```

**Feel free to contribute with ideas or implementations**
