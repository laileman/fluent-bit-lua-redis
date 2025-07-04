FROM fluent/fluent-bit:latest-debug
RUN apt update && apt install -y  luarocks \
    && luarocks install luasocket

# entrypoint ["/fluent-bit/bin/fluent-bit", "-c", "/fluent-bit/etc/fluent-bit.conf"]