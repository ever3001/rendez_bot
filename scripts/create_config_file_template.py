#!/usr/bin/env python

from rendez_bot.config.config import Config


def main():
    Config.create_config_json_file_template()


if __name__ == "__main__":
    main()
