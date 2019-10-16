import base64
import random
import string
import os
import sys
import yaml


generateSecret = lambda length: base64.b64encode(''.join(random.sample(string.capwords+string.digits,length))) #32 length
def populateConfig():
    configIn = {
        "kind": "EncryptionConfig",
        "apiVersion": "v1",
        "resources": [
            {
            "resources": [
                "secrets"
            ],
            "providers": [
                {
                "aescbc": {
                    "keys": [
                    {
                        "name": "key1",
                        "secret": "%s" % (generateSecret(32))
                    }
                    ]
                }
                }
            ]
            }
        ]
        }
    
    configOut = yaml.dump(configIn)
    return configOut


configOut = populateConfig()

print(configOut)