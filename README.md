# flog
## backend class based view
### get from db and new url to access
```
cd /home/cf/program/
source my_pyenv/bin/activate
/home/cf/program/flog/blog/python manage.py runserver 0.0.0.0:9000
```

#### curl for get test
```
curl -s http://150.158.168.151:9000/decoration/cart/
```

#### web for get test
```
http://150.158.168.151:9000/decoration/cart/
```

### post to db
#### only when model table updating, it is required to execute two commands
```
python manage.py makemigrations
python manage.py migrate
```

#### view to post db
```
```

#### curl to post db
```
1. curl -H "Content-Type:application/json" -X POST --data '{"name":"fei"}' http://150.158.168.151:9000/decoration/cart/
2. ➜  
~client request:
curl -H "Content-Type:application/json" -X POST --data '{"payid":5215, "name":"test155", "fee":55, "paydate": "2021-02-19"}' http://150.158.168.151:9001/decoration/cart/
~server response:
{"data": [{"payid": 5215, "name": "test155", "fee": 55, "paydate": "2021-02-19"}], "status": 200, "msg": "new"}% 
```

### put(update) to db
```
~client request:
curl -H "Content-Type:application/json" -X PUT --data '{"payid":555, "name":"test15", "fee":555, "paydate": "2021-02-19"}' http://150.158.168.151:9001/decoration/cart/
~server response:
{"data": [{"payid": 555, "name": "test15", "fee": 555, "paydate": "2021-02-19"}], "msg": "update", "status": 200}%
```

### delete from db
```
~client request:
curl -H "Content-Type:application/json" -X DELETE --data '{"payid":555, "name":"test15", "fee":555, "paydate": "2021-02-19"}' http://150.158.168.151:9001/decoration/cart/
~server response:
{"data": [{"payid": 555, "name": "test15", "fee": 555, "paydate": "2021-02-19"}], "msg": "delete", "status": 200}% 
```
