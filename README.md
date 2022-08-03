# Before Deploy

Update the `key` in `__main__.py` to your sendgrid API key before deploying via doctl CLI

I stripped down what is found here, hoping for the most bare minimum of code to use for a workshop

https://github.com/digitalocean/sample-functions-python-sendgrid-email

The error I keep getting trying to deploy this project is

```
0:"Output of failed build in /tmp/slices/builds/fn-fb1a6d0e-4b58-4009-ab33-7990aac63022/sample_hello/20..."
1:"/bin/bash: ./build.sh: Permission denied"
```
