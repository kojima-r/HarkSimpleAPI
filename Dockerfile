FROM ubuntu:18.04
MAINTAINER Kojima <kojima.ryosuke.8e@kyoto-u.ac.jp>
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y wget bzip2 curl git lsb-release gnupg sudo
RUN mkdir -p ~/usr/hark
WORKDIR /usr/hark

RUN echo "deb http://archive.hark.jp/harkrepos $(lsb_release -cs) non-free\ndeb-src http://archive.hark.jp/harkrepos $(lsb_release -cs) non-free" > /etc/apt/sources.list.d/hark.list
RUN wget -q -O - http://archive.hark.jp/harkrepos/public.gpg | apt-key add -
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && \
    apt-get install -y nodejs hark-base harkmw hark-core hark-designer harktool5 harktool5-gui kaldidecoder-hark python3-pip nginx
ADD docker/default /etc/nginx/sites-available/default
ADD docker/setup.sh /usr/hark/setup.sh

ADD ./docker/anaconda_exp.sh /root/
RUN apt-get install -y expect
RUN cd ~/ && \
    curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh && \
    sh anaconda_exp.sh

ENV PATH /root/anaconda3/bin:$PATH
RUN conda install flask 
RUN apt-get install -y hark-python3 python3-numpy python3-matplotlib
RUN apt-get install -y sox
ENTRYPOINT bash /usr/hark/setup.sh && tail -f /dev/null

