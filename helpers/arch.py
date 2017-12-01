import argparse
import os



textbelt_dockerfile = """
FROM {src}
ARG email
RUN python /root/update_email.py --email $email
WORKDIR /root/textbelt
COPY .muttrc /root
CMD nodejs server/app.js
"""



def init_args():
    parser  = argparse.ArgumentParser()
    parser.add_argument("-a")
    return parser.parse_args()

def get_source(arch):
    return "cyna/textbelt_arm" if "arm" in arch else "cyna/textbelt"


def modify_textbelt(src):
    textbelt_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "textbelt", "Dockerfile")
    with open(textbelt_path, "w") as docker_file:
        docker_file.write(textbelt_dockerfile.format(src=src))

if __name__ == "__main__":
    args = init_args()
    src = get_source(args.a)
    modify_textbelt(src)

