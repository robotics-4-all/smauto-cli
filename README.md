# smauto-cli
CLI for SmartAuto (smauto) DSL

Provides command-line interfaces for:
- Model Validation
- Model Interpretation
- Model transformation to automation graph

## Installation

Fork this repository and install using pip:

```
git clone https://github.com/robotics-4-all/smauto-cli
cd smauto-cli
pip install .
```


## Usage

```
smauto --help

Usage: smauto [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  graph      Automation Graph generator
  interpret  Interpreter
  validate   Validator
```

### Model Validation

To validate an SmAuto model:

```
smauto validate simple_model.smauto
```
Replace `simple_model.smauto` with the path to your model

### Generate Automation Graph from an SmAuto model

To generate the automation graph of an SmAuto model the plantuml package
should first be installed in your environment.

For Arch-based Linux systems simply install via pacman package manager:

```
pacman -Sy plantuml
```

Then use the ``
