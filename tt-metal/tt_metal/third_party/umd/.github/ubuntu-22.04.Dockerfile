FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

COPY docker_install_common.sh /docker_install_common.sh
RUN chmod +x /docker_install_common.sh && /docker_install_common.sh

