## Starsector Mod Template

This is just a personal mod template for my own use.

# Setup
This is using the VSCode extension "Java Project Manager"
Once created from template, it should look something like this once cloned
Something like:
```
starsector
|-mods
  |-Repo Name (Mod name)
    |-.git
    |-.vscode
      |-settings.json
    |-lib
      |-standard libs from Starsector
    |-jars (Will be created on first build with the {name of repo}.jar)
    |-src
      |-org
        |-tuvox
          |-ModPlugin.jar
    |-README.md
```