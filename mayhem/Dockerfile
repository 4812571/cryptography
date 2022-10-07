# Copyright 2022 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################

# Use google's oss-fuzz base python imagine with Atheris pre-installed
FROM gcr.io/oss-fuzz-base/base-builder-python

# Copy the current directory into '/cryptography' in the container
COPY . /cryptography

# Delete the contents of the container's '/cryptography/mayhem' folder
RUN rm -rf /cryptography/mayhem

# Install build dependencies
RUN apt-get install build-essential libssl-dev libffi-dev python3-dev cargo -y

# Install pip3
RUN pip3 install --upgrade pip

# Download and run the rustup shell script
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

# Add cargo to the system PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Run rustup
RUN rustup install nightly
RUN rustup default nightly

# Set the working directory to '/cryptography'
WORKDIR /cryptography

# Copy both 'mayhem/build.sh' and 'mayhem/symenc_fuzz.py' into the '$SRC' environment variable path
COPY mayhem/build.sh mayhem/example_fuzz.py $SRC/

# Set the 'FUZZING_LANGUAGE', 'SANITIZER', and 'FUZZING_ENGINE' environment variables
ENV FUZZING_LANGUAGE=python SANITIZER=address FUZZING_ENGINE=libfuzzer

# Compile libFuzzer
RUN compile

# Make '/out/symenc_fuzz.pkg' executable
RUN chmod +x /out/example_fuzz.pkg