FROM cyna/textbelt
ARG email
RUN python /root/update_email.py --email $email
WORKDIR /root/textbelt
COPY .muttrc /root
CMD nodejs server/app.js
