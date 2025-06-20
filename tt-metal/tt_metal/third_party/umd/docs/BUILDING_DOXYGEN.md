# TT-UMD Docs

## Requirements

In order to be able to build the docs, required packages need to be installed. In order to install the required packages, run [`install_docs_requirements.sh`](install_docs_requirements.sh)

## Build docs

In order to build docs environment variable `TT_UMD_HOME` needs to be set to root of tt-umd project.

After that you can run [`build_docs.sh`](build_docs.sh)

In `build/docs` directory you will find multiple formats of the docs.

## Adding documentation

Augment the `INPUT` line in [`Doxyfile`](../Doxyfile)
