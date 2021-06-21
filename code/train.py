from argparse import ArgumentParser

import torch
from utils.log import Logger
from utils.misc import ConfigParser
from models.conv_vq_vae import ConvolutionalVQVAE


def main(opts):
    config = ConfigParser.parse_json_config(opts.config_path)
    device = "cuda" if config["use_cuda"] and torch.cuda.is_available() else "cpu"

    logger = Logger(config["log_dir"], config["verbose"])

    logger.log_config(config)
    if config["decoder_type"] == "deconv":
        model = ConvolutionalVQVAE(config, device).to(device)
    else:
        raise NotImplementedError(
            "Decoder of type {} not implemented.".format(config["decoder_type"])
        )

    print(model)
    # TODO: trainer, dataloader

    return None


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--config_path",
        help="Path to YAML file containing configuration. See config/test.yaml",
        default="../config/test.yaml",
    )
    opts = parser.parse_args()
    evaluation_metrics = main(opts)
