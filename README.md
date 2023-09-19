# replit_keep_alive
![Tests](https://github.com/Reathe/replit_keep_alive/actions/workflows/tests.yml/badge.svg)

Easy way to keep your replit alive by calling keep_alive, and then having (for example) uptimerobot monitor the page it created

In your code:

```python
from replit_keep_alive import keep_alive
keep_alive.run()
```

Don't forget to add a monitor to the created page, so it gets visited every few minutes. As long it has visitors, it won't die ! 
