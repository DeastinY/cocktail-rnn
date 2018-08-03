# Cocktail-RNN
With the summer melting away more and more brain cells I decided to employ some artificial help in creating beautiful cocktail recipes.  
This project uses [torch-rnn](https://github.com/jcjohnson/torch-rnn) on data from [The Cocktail DB](https://thecocktaildb.com) to create new drinks!

## Install
The example given below assumes Ubuntu 18.04 and CUDA support. For everything else check out the torch-rnn repository.

1. Install [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)
2. Start the docker container
    ```nvidia-docker run --rm -ti https://hub.docker.com/r/xoryouyou/torch-rnn/ bash```
3. Copy the training data to data/cocktails.txt
3. Preprocess the sample data
    ```
    python scripts/preprocess.py \
    --input_txt data/cocktails.txt \
    --output_h5 data/cocktails.h5 \
    --output_json data/cocktails.json
    ```
4. Train 
    ```
    th train.lua \
    -input_h5 data/cocktails.h5 \
    -input_json data/cocktails.json
    ```
5. Sample
    * `th sample.lua -checkpoint cv/checkpoint_9000.t7 -length 2000`


## Examples

Check the examples.txt file for more cocktails!

## Contribution

Feel free to create bots, apps, websites, spaceships, music, drawings, ... just don't use it for evil!

