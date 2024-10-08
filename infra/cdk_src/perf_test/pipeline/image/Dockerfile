# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# Build from Amazon Linux 2023 image:
FROM public.ecr.aws/amazonlinux/amazonlinux:latest

ENV PYTHONUNBUFFERED=1

# Install necessary OS-level packages
RUN yum install -y --skip-broken wget jq aws-cli bzip2 ca-certificates curl git gcc gcc-c++ make openssl-devel libffi-devel zlib-devel && \
    yum clean all

# Install Miniconda
RUN wget --no-verbose https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p /opt/miniconda && \
    rm /tmp/miniconda.sh && \
    /opt/miniconda/bin/conda clean --all --yes

# Set conda environment variables
ENV PATH="/opt/miniconda/bin:$PATH"
ENV CONDA_AUTO_UPDATE_CONDA=false

# Create and activate the conda environment
RUN conda create --name fmbench_python311 -y python=3.11 ipykernel && \
    echo "source activate fmbench_python311" > ~/.bashrc

# Install fmbench
RUN /opt/miniconda/bin/conda run -n fmbench_python311 pip install -U fmbench

# Set working directorys
WORKDIR /app

# Set the entrypoint to run the fmbench command
ENTRYPOINT ["conda", "run", "-n", "fmbench_python311", "sh", "-c"]
CMD ["fmbench", "--help"]
