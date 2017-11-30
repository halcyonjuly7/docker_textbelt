Docker_TextBelt



This is a Dockerized version of a standalone Textbelt server.
which allows you easily text any US or Canadian  number for free.
original project is here https://github.com/typpo/textbelt


**Setup:**
1. modify the docker-compose file to add your email address
2. modify .muttrc file located at textbelt/.muttrc to include your email credentials and mutt setup
3. run docker-compose up



**Usage:**
   

     curl -X POST http://your_servers_ip/text \
            -d number=5551234567 \
            -d "message=I sent this message for free with textbelt.com"
