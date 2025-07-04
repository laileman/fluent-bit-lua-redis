# a test demo for fluent-bit  lua filter, get data from redis

## run
```bash
docker-compose up -d

docker logs -f fluent-bit
```

## post record
```bash
curl -X POST   localhost:8000 -d '{"name":"leman","city":"shenzhen","ip":"'{"name":"leman","city":"shenzhen","ip":"IP_ADDRESS","age":200,"from_":"sg"}'
{
  "name": "leman",
  "city": "shenzhen",
  "ip": "10.0.0.1",
  "age": 200,
  "from_": "sg"
  
}
```
## log record
```json
[{"date":1751601766.506,"from":"sg","ip":"10.0.0.1","levelname":"INFO","message":"Hello Leman","env":"prod","app":"main-app.py","city":"shenzhen","age":200,"app_name":"app","app_version":"1.0.0","app_env":"dev","app_hostname":"3ff509b48388"}]

```