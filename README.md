# From Day Zero to Zero Day

[From Day Zero to Zero Day](https://fromdayzerotozeroday.com) features many working examples that you should test out for yourself. The majority of examples are run on the latest version of Kali Linux at the time of publication or use free and open source software, but a handful include Windows targets, so it's best to use virtual machines to run the relevant operating systems and targets.

The examples are all based on x86 and x64, so the virtual machines can't be ARM-based, which means you can't host them on Apple Silicon devices.

## Getting Started
This repository hosts the source code and scripts used in the book's examples. The repository contains Git submodules, which are copies of specific versions of open source repositories, so you'll have to run an additional Git command to fetch them after cloning the repository:

```bash
git clone https://github.com/spaceraccoon/from-day-zero-to-zero-day
cd from-day-zero-to-zero-day
git submodule update --init
```

## Updates and Errata

Tech changes constantly, especially the tools used in vulnerability research. While I've noted down most of the versions of tools used throughout the book, it's possible that future versions might break, or better tools emerge.

### Chapter 03

* Some versions of Semgrep may error out on the examples with messages like `Syntax error at line expat/lib/xmlparse.c`. You can use the version **1.80.0** to avoid this issue; install it with `python3 -m pip install semgrep==1.80.0` or follow the instructions at https://semgrep.dev/docs/kb/semgrep-code/run-specific-version depending on your installation method. To get the exact same output as that in the book, use version **1.36.0**. Thanks @0xFA7E!

### Chapter 05

* FreshTomato's website no longer hosts older versions used in the examples. As such, a copy of `freshtomato-AC1450-ARM_NG-2022.5-AIO-64K.zip` has been added to [this repo](https://github.com/spaceraccoon/from-day-zero-to-zero-day/blob/main/chapter-05/freshtomato-AC1450-ARM_NG-2022.5-AIO-64K.zip). Thanks @jbmls!
* Later versions of Frida introducing breaking changes to the API that may cause the `hook.py` script to fail with errors such as `frida.ProcessNotRespondingError`. While you may want to adapt your script for newer versions of Frida, you can get the examples to work by downgrading with `pip install frida-tools==10.8.0`. Thanks @pudii!

### Chapter 06

* FreshTomato's website no longer hosts older versions used in the examples. As such, a copy of `freshtomato-RT-N66U_RT-AC6x-2022.5-AIO-64K.zip` has been added to [this repo](https://github.com/spaceraccoon/from-day-zero-to-zero-day/blob/main/chapter-06/freshtomato-RT-N66U_RT-AC6x-2022.5-AIO-64K.zip). Thanks @0xdea!
* A newer Ghidra plugin, [Cartographer](https://github.com/nccgroup/Cartographer), supports the drcov version 3 format and is a decent alternative to Lightkeeper used in the book, which only supports version 2. Always keep your toolbox updated! Thanks @phordiienko!

## Contributing

If you face any problems with the examples or have fur-
ther questions, feel free to create an issue on the GitHub repository or reach
out to me on X at https://x.com/spaceraccoonsec.
