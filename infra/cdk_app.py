#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Main AWS CDK entry point for the workshop infrastructure
"""
# Python Built-Ins:
import json
import os

# External Dependencies:
import aws_cdk as cdk

# Local Dependencies:
from cdk_src.cdk_stack import LLMEValWKshpStack
from cdk_src.config_utils import bool_env_var

# Top-level configurations are loaded from environment variables at the point `cdk synth` or
# `cdk deploy` is run (or you can override here):
config = {
    "deploy_prompt_app": bool_env_var("DEPLOY_PROMPT_APP", default=True),
    "deploy_sagemaker_domain": bool_env_var("DEPLOY_SAGEMAKER_DOMAIN", default=True),
    "sagemaker_code_checkout": os.environ.get("SAGEMAKER_CODE_CHECKOUT"),
    "sagemaker_code_repo": os.environ.get(
        "SAGEMAKER_CODE_REPO",
        "https://github.com/aws-samples/llm-evaluation-methodology",
    ),
}

app = cdk.App()
print(f"Preparing stack with configuration:\n{json.dumps(config, indent=2)}")
llm_eval_wkshp_stack = LLMEValWKshpStack(app, "LLMEValWKshpStack", **config)

app.synth()
