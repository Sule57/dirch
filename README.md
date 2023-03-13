# Dirch by Sule57

### Triggers

* **-u | --url** - Specify the target URL
* **-w | --wordlist** - Specify the Wordlist to use (by default common.txt)

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
