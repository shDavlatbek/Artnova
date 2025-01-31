## Static files setup



```bash
python manage.py collectstatic
```

Setup Nginx proxy to port 8200 (You can change port in docker-compose.yml)

Add alias folders static and media 

## Deployement

```bash
docker compose up --build -d
```


