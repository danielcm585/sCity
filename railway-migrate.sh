pg_dump -U xodttgmosavbzn -h ec2-34-198-198-141.compute-1.amazonaws.com -p 5432 -W -F t dbkbtgldljao1f > heroku_dump

pg_restore --no-privileges --no-owner -U postgres -h containers-us-west-75.railway.app -p 7341 -W -F t -d railway heroku_dump