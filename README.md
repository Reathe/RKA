# replit_keep_alive
Keeps your replit alive by calling keep_alive, and having uptimerobot monitor the page it created

In your code:

```python
from keep_alive import keep_alive
keep_alive()
```

Don't forget to add a monitor to the created page, so it gets visited every few minutes. As long it has visitors, it won't die ! 
