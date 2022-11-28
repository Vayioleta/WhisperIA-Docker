FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

RUN apt update
RUN apt install -y python3
RUN apt install -y wget git
RUN apt install sudo
RUN apt install net-tools
RUN apt install -y pip

RUN pip3 install transformers
RUN pip3 install torch torchvision torchaudio
RUN apt-get install ffmpeg libsm6 libxext6 -y

#Install Whisper IA
RUN pip3 install git+https://github.com/openai/whisper.git
RUN pip3 install jiwer


WORKDIR /ia