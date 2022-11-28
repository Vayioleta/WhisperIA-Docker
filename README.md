# Whisper IA in Docker
> Requirements:
> Docker in GPU: https://github.com/Vayioleta/Wiki/blob/main/Run%20Docker%20in%20GPU.md
> NVIDIA CUDA

# Run and Build
> to Build it , Run this in the folder:
`docker build -t whisper .`

> to run it, Run this in the folder:
`docker container run -it -v <LOCAL FOLDER>:/ia/ --gpus=all whisper`

> exemple:
`docker container run -it -v D:\contenedores\Whisper\volumen:/ia/ --gpus=all whisper`


# Commands inside the container terminal
> Transcribe audio:
`whisper "./audio.mp3" --task transcribe --model medium`
> Translate audio:
`whisper "/content/audio.mp3" --task translate --model medium`
