import os
from configparser import ConfigParser

config = ConfigParser.RawConfigParser("../application.properties")

print(config.get("OpenAiSection","openai_token"))