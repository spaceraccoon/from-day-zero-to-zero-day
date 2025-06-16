# From Day Zero to Zero Day

[From Day Zero to Zero Day](https://fromdayzerotozeroday.com) features many working examples that you should test out for your-self. The majority of examples are run on the latest version of Kali Linux at the time of publication or use free and open source software, but a handful include Windows targets, so it’s best to use virtual machines to run the relevant operating systems and targets.

The examples are all based on x86 and x64, so the virtual machines can’t be ARM-based, which means you can’t host them on Apple Silicon devices.

## Getting Started
This repository hosts the source code and scripts used in the book's examples. The repository contains Git submodules, which are copies of specific versions of open source repositories, so you’ll have to run an additional Git command to fetch them after cloning the repository:

```bash
git clone https://github.com/spaceraccoon/from-day-zero-to-zero-day
cd from-day-zero-to-zero-day
git submodule update --init
```

## Contributing

If you face any problems with the examples or have fur-
ther questions, feel free to create an issue on the GitHub repository or reach
out to me on X at https://x.com/spaceraccoonsec.